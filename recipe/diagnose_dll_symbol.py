#!/usr/bin/env python3
"""
Diagnose Windows DLL entry-point errors.

Example:
  python diagnose_dll_symbol.py investmentblock_solver.exe clock_gettime64 libgfortran-5.dll

The script does not execute the target program. It inspects PE import/export
tables, lists matching DLL candidates in the current process PATH, and reports:
  - which DLL/EXE files import the requested symbol;
  - which candidate provider DLLs export the requested symbol;
  - which second-level provider DLL is requested by an importing DLL;
  - the first provider DLL that Windows is likely to find for the target.
"""

from __future__ import annotations

import argparse
import os
import struct
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


IMAGE_DIRECTORY_ENTRY_EXPORT = 0
IMAGE_DIRECTORY_ENTRY_IMPORT = 1


@dataclass(frozen=True)
class Section:
    name: str
    virtual_address: int
    virtual_size: int
    raw_data_ptr: int
    raw_data_size: int


class PEError(Exception):
    pass


class PEFile:
    def __init__(self, path: Path):
        self.path = path
        self.data = path.read_bytes()
        self.sections: list[Section] = []
        self.is_pe64 = False
        self.data_directories: list[tuple[int, int]] = []
        self._parse_headers()

    def _u16(self, off: int) -> int:
        return struct.unpack_from("<H", self.data, off)[0]

    def _u32(self, off: int) -> int:
        return struct.unpack_from("<I", self.data, off)[0]

    def _u64(self, off: int) -> int:
        return struct.unpack_from("<Q", self.data, off)[0]

    def _parse_headers(self) -> None:
        if len(self.data) < 0x40 or self.data[:2] != b"MZ":
            raise PEError("not an MZ executable")

        pe_off = self._u32(0x3C)
        if self.data[pe_off : pe_off + 4] != b"PE\0\0":
            raise PEError("not a PE executable")

        coff = pe_off + 4
        number_of_sections = self._u16(coff + 2)
        size_of_optional_header = self._u16(coff + 16)
        opt = coff + 20
        magic = self._u16(opt)

        if magic == 0x10B:
            self.is_pe64 = False
            data_dir_off = opt + 96
        elif magic == 0x20B:
            self.is_pe64 = True
            data_dir_off = opt + 112
        else:
            raise PEError(f"unknown optional-header magic 0x{magic:x}")

        number_of_rva_and_sizes = self._u32(data_dir_off - 4)
        directories_to_read = min(number_of_rva_and_sizes, 16)
        self.data_directories = [
            (self._u32(data_dir_off + i * 8), self._u32(data_dir_off + i * 8 + 4))
            for i in range(directories_to_read)
        ]

        section_off = opt + size_of_optional_header
        for i in range(number_of_sections):
            off = section_off + i * 40
            raw_name = self.data[off : off + 8].split(b"\0", 1)[0]
            name = raw_name.decode("ascii", errors="replace")
            virtual_size = self._u32(off + 8)
            virtual_address = self._u32(off + 12)
            raw_data_size = self._u32(off + 16)
            raw_data_ptr = self._u32(off + 20)
            self.sections.append(
                Section(name, virtual_address, virtual_size, raw_data_ptr, raw_data_size)
            )

    def rva_to_offset(self, rva: int) -> int:
        for sec in self.sections:
            span = max(sec.virtual_size, sec.raw_data_size)
            if sec.virtual_address <= rva < sec.virtual_address + span:
                return sec.raw_data_ptr + (rva - sec.virtual_address)
        if 0 <= rva < len(self.data):
            return rva
        raise PEError(f"RVA 0x{rva:x} is outside file sections")

    def c_string(self, off: int) -> str:
        end = self.data.find(b"\0", off)
        if end < 0:
            raise PEError("unterminated string")
        return self.data[off:end].decode("utf-8", errors="replace")

    def directory(self, index: int) -> tuple[int, int]:
        if index >= len(self.data_directories):
            return 0, 0
        return self.data_directories[index]

    def imports(self) -> dict[str, list[str]]:
        rva, _size = self.directory(IMAGE_DIRECTORY_ENTRY_IMPORT)
        if not rva:
            return {}

        imports: dict[str, list[str]] = {}
        desc = self.rva_to_offset(rva)
        thunk_step = 8 if self.is_pe64 else 4
        ordinal_flag = 0x8000000000000000 if self.is_pe64 else 0x80000000

        while True:
            original_first_thunk = self._u32(desc)
            name_rva = self._u32(desc + 12)
            first_thunk = self._u32(desc + 16)
            if original_first_thunk == 0 and name_rva == 0 and first_thunk == 0:
                break

            dll_name = self.c_string(self.rva_to_offset(name_rva)).lower()
            thunk_rva = original_first_thunk or first_thunk
            thunk = self.rva_to_offset(thunk_rva)
            imported_names: list[str] = []

            while True:
                value = self._u64(thunk) if self.is_pe64 else self._u32(thunk)
                if value == 0:
                    break
                if value & ordinal_flag:
                    imported_names.append(f"#{value & 0xFFFF}")
                else:
                    hint_name_off = self.rva_to_offset(value)
                    imported_names.append(self.c_string(hint_name_off + 2))
                thunk += thunk_step

            imports[dll_name] = imported_names
            desc += 20

        return imports

    def exports(self) -> list[str]:
        rva, _size = self.directory(IMAGE_DIRECTORY_ENTRY_EXPORT)
        if not rva:
            return []

        off = self.rva_to_offset(rva)
        number_of_names = self._u32(off + 24)
        address_of_names_rva = self._u32(off + 32)
        if number_of_names == 0 or address_of_names_rva == 0:
            return []

        names_off = self.rva_to_offset(address_of_names_rva)
        names: list[str] = []
        for i in range(number_of_names):
            name_rva = self._u32(names_off + i * 4)
            names.append(self.c_string(self.rva_to_offset(name_rva)))
        return names


def unique_existing_dirs(paths: Iterable[Path]) -> list[Path]:
    seen: set[str] = set()
    result: list[Path] = []
    for path in paths:
        try:
            resolved = path.resolve()
        except OSError:
            continue
        key = str(resolved).lower()
        if key not in seen and resolved.is_dir():
            seen.add(key)
            result.append(resolved)
    return result


def safe_resolve(path: Path) -> Path | None:
    try:
        return path.resolve()
    except OSError:
        return None


def default_windows_search_dirs(exe: Path) -> list[Path]:
    windir = Path(os.environ.get("WINDIR", r"C:\Windows"))
    path_dirs = [Path(p) for p in os.environ.get("PATH", "").split(os.pathsep) if p]
    return unique_existing_dirs(
        [
            exe.resolve().parent,
            Path.cwd(),
            windir / "System32",
            windir / "System",
            windir,
            *path_dirs,
        ]
    )


def files_to_scan(dirs: list[Path], extra_files: Iterable[Path]) -> list[Path]:
    seen: set[str] = set()
    result: list[Path] = []

    for file in extra_files:
        resolved = safe_resolve(file)
        if resolved and resolved.is_file():
            key = str(resolved).lower()
            if key not in seen:
                seen.add(key)
                result.append(resolved)

    for directory in dirs:
        try:
            entries = list(directory.iterdir())
        except OSError:
            continue
        for file in entries:
            if file.suffix.lower() not in {".exe", ".dll"}:
                continue
            resolved = safe_resolve(file)
            if not resolved:
                continue
            key = str(resolved).lower()
            if key not in seen:
                seen.add(key)
                result.append(resolved)
    return result


def candidate_providers(search_dirs: list[Path], provider_name: str) -> list[Path]:
    candidates: list[Path] = []
    seen: set[str] = set()
    for directory in search_dirs:
        candidate = directory / provider_name
        if candidate.is_file():
            key = str(candidate.resolve()).lower()
            if key not in seen:
                seen.add(key)
                candidates.append(candidate.resolve())
    return candidates


def inspect_exports(path: Path, symbol: str) -> tuple[bool, str | None]:
    try:
        exports = PEFile(path).exports()
    except Exception as exc:
        return False, f"{type(exc).__name__}: {exc}"
    return symbol in exports, None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Find PE importers/providers for a missing Windows DLL entry point."
    )
    parser.add_argument("exe", nargs="?", default="investmentblock_solver.exe")
    parser.add_argument("symbol", nargs="?", default="clock_gettime64")
    parser.add_argument("provider", nargs="?", default="libgfortran-5.dll")
    parser.add_argument(
        "--dir",
        action="append",
        default=[],
        help="Extra directory to scan/search. May be passed more than once.",
    )
    parser.add_argument(
        "--path-file",
        help=(
            "Optional text file containing a PATH value captured from another environment. "
            "Useful for comparing Explorer and command-prompt PATH values."
        ),
    )
    parser.add_argument(
        "--full-scan",
        action="store_true",
        help="Scan every DLL/EXE in every search directory. This can be slow on large PATHs.",
    )
    args = parser.parse_args()

    exe = Path(args.exe)
    if not exe.is_file():
        print(f"ERROR: executable not found: {exe}", file=sys.stderr)
        return 2

    search_dirs = default_windows_search_dirs(exe)
    search_dirs.extend(Path(d) for d in args.dir)

    if args.path_file:
        path_value = Path(args.path_file).read_text(encoding="utf-8").strip()
        search_dirs.extend(Path(p) for p in path_value.split(os.pathsep) if p)

    search_dirs = unique_existing_dirs(search_dirs)
    reported_dll_name = args.provider.lower()
    symbol = args.symbol

    print(f"Target executable: {exe.resolve()}")
    print(f"Missing symbol:    {symbol}")
    print(f"Reported DLL:      {args.provider}")
    print()

    candidates = candidate_providers(search_dirs, args.provider)
    printed_provider_names: set[str] = set()

    def print_provider_candidates(provider: str) -> None:
        provider_key = provider.lower()
        if provider_key in printed_provider_names:
            return
        printed_provider_names.add(provider_key)
        provider_candidates = candidate_providers(search_dirs, provider)
        print(f"Candidate DLLs for {provider} in Windows search order:")
        if not provider_candidates:
            print(f"  NOT FOUND: {provider}")
        for i, candidate in enumerate(provider_candidates, 1):
            has_symbol, error = inspect_exports(candidate, symbol)
            status = "exports symbol" if has_symbol else "DOES NOT export symbol"
            if error:
                status = f"could not inspect exports ({error})"
            marker = " <- first match Windows is likely to load" if i == 1 else ""
            print(f"  {i:2}. {candidate} [{status}]{marker}")
        print()

    print_provider_candidates(args.provider)

    if args.full_scan:
        scan_dirs = search_dirs
    else:
        scan_dirs = unique_existing_dirs(
            [
                exe.resolve().parent,
                Path.cwd(),
                *(candidate.parent for candidate in candidates),
                *(Path(d) for d in args.dir),
            ]
        )

    scan_files = files_to_scan(scan_dirs, [exe.resolve(), *candidates])
    importer_hits: list[tuple[Path, str]] = []
    provider_import_hits: list[Path] = []

    for file in scan_files:
        try:
            imports = PEFile(file).imports()
        except Exception:
            continue

        for dll_name, names in imports.items():
            if symbol in names:
                importer_hits.append((file, dll_name))
            if dll_name == reported_dll_name:
                provider_import_hits.append(file)

    print(f"Files that import symbol '{symbol}':")
    if not importer_hits:
        print("  none found in scanned directories")
    else:
        for file, dll_name in importer_hits:
            print(f"  {file} imports {symbol} from {dll_name}")
    print()

    imported_provider_names = sorted({dll_name for _file, dll_name in importer_hits})
    for dll_name in imported_provider_names:
        print_provider_candidates(dll_name)

    print(f"Files that directly import {args.provider}:")
    if not provider_import_hits:
        print("  none found in scanned directories")
    else:
        for file in provider_import_hits:
            print(f"  {file}")
    print()

    print("Search directories:")
    for directory in search_dirs:
        print(f"  {directory}")
    print()

    print("Scanned directories:")
    for directory in scan_dirs:
        print(f"  {directory}")

    providers_to_check = imported_provider_names or [reported_dll_name]
    first_bad_candidates: list[tuple[str, Path, Path | None]] = []
    first_exporting_candidates: dict[str, Path] = {}
    importers_by_provider = {provider: file for file, provider in importer_hits}

    for provider in providers_to_check:
        provider_candidates = candidate_providers(search_dirs, provider)
        for candidate in provider_candidates:
            if inspect_exports(candidate, symbol)[0]:
                first_exporting_candidates[provider] = candidate
                break
        if provider_candidates and not inspect_exports(provider_candidates[0], symbol)[0]:
            first_bad_candidates.append(
                (provider, provider_candidates[0], importers_by_provider.get(provider))
            )

    if first_bad_candidates:
        print()
        print("LIKELY CAUSE:")
        for provider, candidate, importer in first_bad_candidates:
            if importer:
                print(f"  {importer} imports {symbol} from {provider}.")
            print(f"  Windows is finding {candidate} first for {provider},")
            print(f"  but that DLL does not export {symbol}.")
            exporting_candidate = first_exporting_candidates.get(provider)
            if exporting_candidate:
                print(f"  A later candidate does export it: {exporting_candidate}")
        print("  Put the exporting DLL earlier in PATH, or copy the matching runtime DLLs")
        print("  next to the executable so they win the Windows DLL search order.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
