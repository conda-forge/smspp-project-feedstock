:: the whole umbrella is built once, and every output installs its part
mkdir build
cd build
cmake %CMAKE_ARGS% ^
    -DOpenMP_RUNTIME_MSVC="llvm" ^
    -DBUILD_tests=OFF ^
    -DBUILD_SHARED_LIBS=OFF ^
    -DCMAKE_INSTALL_PREFIX=%LIBRARY_PREFIX% ^
    -DCMAKE_PREFIX_PATH=%LIBRARY_PREFIX% ^
    -DFETCHCONTENT_SOURCE_DIR_FASTFLOW=%SRC_DIR%\fastflow ^
    -DCMAKE_DISABLE_FIND_PACKAGE_CPLEX=ON ^
    -DCMAKE_DISABLE_FIND_PACKAGE_GUROBI=ON ^
    -DCMAKE_DISABLE_FIND_PACKAGE_SCIP=ON ^
    -DCMAKE_DISABLE_FIND_PACKAGE_PIPS=ON ^
    -DCMAKE_DISABLE_FIND_PACKAGE_Torch=ON ^
    -DHiGHS_ROOT=%LIBRARY_PREFIX% ^
    -DStOpt_ROOT=%LIBRARY_PREFIX% ^
    -DCoinUtils_ROOT=%LIBRARY_PREFIX% ^
    -DOsi_ROOT=%LIBRARY_PREFIX% ^
    -DClp_ROOT=%LIBRARY_PREFIX% ^
    ..
if %ERRORLEVEL% neq 0 (type CMakeError.log && exit 1)

cmake --build . --config Release -j%CPU_COUNT%
if %ERRORLEVEL% neq 0 exit %ERRORLEVEL%
