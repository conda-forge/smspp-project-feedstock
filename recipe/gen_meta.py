"""Writes the outputs of meta.yaml, one per module and one per tool.

conda-build needs them spelled out, so they are generated from the tables
below: a new module of SMS++ is one line of LIBS, a new tool one of TOOLS.
Run it from anywhere, it rewrites the meta.yaml next to it.
"""
import os

LIBS = [
    ("libsmspp", "SMS++", [],
     ["libboost-devel", "eigen", "netcdf-cxx4", "netcdf-cxx4 * nompi_*",
      "libnetcdf", "libnetcdf * nompi_*", "hdf5", "hdf5 * nompi_*",
      "libaec  # [unix]", "openssl  # [unix]", "libcurl  # [unix]", "zlib"]),
    ("libsmspp-bkb", "BinaryKnapsackBlock", ["libsmspp"],
     ["libgomp  # [linux]", "llvm-openmp  # [osx]"]),
    ("libsmspp-mcf", "MCFBlock", ["libsmspp"], []),
    ("libsmspp-cflb", "CapacitatedFacilityLocationBlock",
     ["libsmspp-bkb", "libsmspp-mcf"], []),
    ("libsmspp-mmcf", "MMCFBlock",
     ["libsmspp-bkb", "libsmspp-mcf"], []),
    ("libsmspp-lukfi", "LukFiBlock", ["libsmspp"], []),
    ("libsmspp-ucblock", "UCBlock", ["libsmspp"], []),
    ("libsmspp-stochastic", "StochasticBlock", ["libsmspp"], []),
    ("libsmspp-tssb", "TwoStageStochasticBlock",
     ["libsmspp-stochastic"], []),
    ("libsmspp-mssb", "MultiStageStochasticBlock",
     ["libsmspp-tssb"], []),
    ("libsmspp-sddp", "SDDPBlock", ["libsmspp-stochastic"],
     ["stopt", "libboost-mpi", "{{ mpi }}",
      "libgomp  # [linux]", "llvm-openmp  # [osx]"]),
    ("libsmspp-investment", "InvestmentBlock",
     ["libsmspp-sddp", "libsmspp-tssb", "libsmspp-ucblock"],
     ["libboost-mpi", "{{ mpi }}"]),
    ("libsmspp-svm", "SVMBlock", ["libsmspp"], ["libsvm"]),
    ("libsmspp-sfdcr", "SingleFlowDCRBlock", ["libsmspp"], []),
    ("libsmspp-milp", "MILPSolver", ["libsmspp"], ["highs"]),
    ("libsmspp-bundle", "BundleSolver", ["libsmspp-milp"],
     ["coin-or-utils", "coin-or-clp", "coin-or-osi", "openblas"]),
    ("libsmspp-lds", "LagrangianDualSolver",
     ["libsmspp-milp"], []),
    ("libsmspp-frankwolfe", "FrankWolfeSolver", ["libsmspp"], []),
    ("libsmspp-bnx", "BranchAndXSolver", ["libsmspp"], []),
    ("libsmspp-bds", "BendersDecompositionSolver",
     ["libsmspp"], []),
    ("libsmspp-mcfclass", "MCFClassSolver", ["libsmspp-mcf"], []),
    ("libsmspp-mcflemon", "MCFLemonSolver", ["libsmspp-mcf"], ["lemon"]),
    ("libsmspp-srs", "ScenarioReductionSolver",
     ["libsmspp-tssb"], []),
]

SOLVERS = ["libsmspp-lds", "libsmspp-bundle",
           "libsmspp-milp"]
EX = "${PREFIX}/share/SMS++_tools"
TOOLS = [
    ("smspp-ucblock", ["ucblock_solver"], ["libsmspp-ucblock"] + SOLVERS,
     [f"ucblock_solver {EX}/ucblock_solver/examples/Bus_Test.nc4"]),
    ("smspp-tssb", ["tssb_solver"],
     ["libsmspp-ucblock", "libsmspp-tssb"] + SOLVERS,
     [f"tssb_solver {EX}/tssb_solver/examples/toy_tssb.nc4"]),
    ("smspp-mssb", ["mssb_solver"],
     ["libsmspp-ucblock", "libsmspp-mssb"] + SOLVERS, []),
    ("smspp-sddp", ["sddp_solver"], ["libsmspp-ucblock", "libsmspp-sddp"] + SOLVERS,
     [f"sddp_solver -p {EX}/sddp_solver/examples/ SDDPBlock.nc4"]),
    ("smspp-investment", ["investmentblock_solver"],
     ["libsmspp-investment", "libsmspp-mssb"] + SOLVERS,
     [f"investmentblock_solver {EX}/investmentblock_solver/examples/InvestmentBlockBus.nc4"]),
    ("smspp-svm", ["svm_solver"], ["libsmspp-svm"] + SOLVERS, []),
    ("smspp-mcf", ["mcfblock_solver"],
     ["libsmspp-mcf", "libsmspp-mcfclass", "libsmspp-mcflemon",
      "libsmspp-milp"],
     [f"mcfblock_solver {EX}/mcfblock_solver/examples/example.dmx"]),
    ("smspp-bkb", ["bkblock_solver"],
     ["libsmspp-bkb", "libsmspp-milp"],
     [f"bkblock_solver {EX}/bkblock_solver/examples/example.txt"]),
    ("smspp-cflb", ["cflblock_solver"],
     ["libsmspp-cflb", "libsmspp-milp"],
     [f"cflblock_solver {EX}/cflblock_solver/examples/example.txt"]),
    ("smspp-mmcf", ["mmcfblock_solver"], ["libsmspp-mmcf"] + SOLVERS,
     [f"mmcfblock_solver {EX}/mmcfblock_solver/examples/small.std"]),
    ("smspp-sfdcr", ["sfdcrblock_solver"],
     ["libsmspp-sfdcr", "libsmspp-milp"], []),
    ("smspp-tools", ["block_solver", "chgcfg"],
     ["libsmspp-investment", "libsmspp-mcf", "libsmspp-mcfclass",
      "libsmspp-mcflemon"] + SOLVERS, []),
]

# the libraries are linked without --as-needed, so every one of them has
# among its DSOs the external libraries of all the modules it needs, which
# its host requirements must then list for their run_exports
REQS = {name: reqs for name, _, _, reqs in LIBS}
NEEDS = {name: needs for name, _, needs, _ in LIBS}


def externals(needs, own=()):
    out, seen, todo = list(own), set(), list(needs)
    while todo:
        n = todo.pop(0)
        if n in seen:
            continue
        seen.add(n)
        out += REQS[n]
        todo += NEEDS[n]
    return list(dict.fromkeys(out))


META = os.path.join(os.path.dirname(os.path.abspath(__file__)), "meta.yaml")
head, tail = open(META).read().split("outputs:\n", 1)
about = tail[tail.index("about:\n"):]

o = []
w = o.append
w("outputs:\n")
w("  # written by gen_meta.py: edit its tables, not these lines\n")
w("  # the library of each module, installed from the build of the umbrella\n")
for name, module, needs, reqs in LIBS:
    w(f"  - name: {name}\n")
    w("    script: install-module.sh  # [unix]\n")
    w("    script: install-module.bat  # [win]\n")
    w("    build:\n")
    w("      script_env:\n")
    w(f"        - SMSPP_MODULES={module}\n")
    w("      run_exports:\n")
    w(f"        - {{{{ pin_subpackage('{name}', max_pin='x.x.x') }}}}\n")
    w("    requirements:\n")
    w("      build:\n")
    w("        - {{ compiler('cxx') }}\n")
    w("        - {{ stdlib('c') }}\n")
    w("        - cmake >=3.21\n")
    w("      host:\n")
    for n in needs:
        w(f"        - {{{{ pin_subpackage('{n}', exact=True) }}}}\n")
    for r in externals(needs, reqs):
        w(f"        - {r}\n")
    if needs:
        w("      run:\n")
        for n in needs:
            w(f"        - {{{{ pin_subpackage('{n}', exact=True) }}}}\n")
    w("    test:\n")
    w("      commands:\n")
    w(f"        - test -f ${{PREFIX}}/lib/cmake/{module}/{module}Config.cmake  # [unix]\n")
    w(f"        - if not exist %LIBRARY_PREFIX%\\lib\\cmake\\{module}\\{module}Config.cmake exit 1  # [win]\n")
    w("\n")
w("  # the command-line tools, each with its configuration and examples\n")
for name, dirs, needs, cmds in TOOLS:
    w(f"  - name: {name}\n")
    w("    script: install-module.sh  # [unix]\n")
    w("    script: install-module.bat  # [win]\n")
    w("    build:\n")
    w("      script_env:\n")
    w(f"        - SMSPP_MODULES={' '.join('tools/' + d for d in dirs)}\n")
    w("    requirements:\n")
    w("      build:\n")
    w("        - {{ compiler('cxx') }}\n")
    w("        - {{ stdlib('c') }}\n")
    w("        - cmake >=3.21\n")
    w("      host:\n")
    for n in needs:
        w(f"        - {{{{ pin_subpackage('{n}', exact=True) }}}}\n")
    for r in externals(needs):
        w(f"        - {r}\n")
    w("      run:\n")
    for n in needs:
        w(f"        - {{{{ pin_subpackage('{n}', exact=True) }}}}\n")
    w("    test:\n")
    w("      commands:\n")
    for d in dirs:
        w(f"        - {d} --help\n")
    for c in cmds:
        w(f"        - {c}  # [unix]\n")
    w("\n")
w("  # everything, the libraries and the tools\n")
w("  - name: smspp-project\n")
w("    requirements:\n")
w("      host:\n")
w("        - {{ mpi }}\n")
w("      run:\n")
for name, *_ in LIBS + TOOLS:
    w(f"        - {{{{ pin_subpackage('{name}', exact=True) }}}}\n")
w("    test:\n")
w("      commands:\n")
w("        - ucblock_solver --help\n")
w("        - investmentblock_solver --help\n")
w("\n")

open(META, "w").write(head + "".join(o) + about)
print(len(LIBS) + len(TOOLS) + 1, "outputs")
