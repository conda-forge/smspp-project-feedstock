set -ex
export LDFLAGS=${LDFLAGS//-Wl,--as-needed/}
export LDFLAGS=${LDFLAGS//-Wl,-dead_strip_dylibs/}

# the whole umbrella is built once, and every output installs its part
mkdir build
cd build
cmake ${CMAKE_ARGS} \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_tests=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_INSTALL_PREFIX=${PREFIX} \
    -DCMAKE_PREFIX_PATH=${PREFIX} \
    -DFETCHCONTENT_SOURCE_DIR_FASTFLOW=${SRC_DIR}/fastflow \
    -DCMAKE_DISABLE_FIND_PACKAGE_CPLEX=ON \
    -DCMAKE_DISABLE_FIND_PACKAGE_GUROBI=ON \
    -DCMAKE_DISABLE_FIND_PACKAGE_SCIP=ON \
    -DCMAKE_DISABLE_FIND_PACKAGE_PIPS=ON \
    -DCMAKE_DISABLE_FIND_PACKAGE_Torch=ON \
    -DHiGHS_ROOT=${PREFIX} \
    -DStOpt_ROOT=${PREFIX} \
    -DCoinUtils_ROOT=${PREFIX} \
    -DOsi_ROOT=${PREFIX} \
    -DClp_ROOT=${PREFIX} \
    ..
cmake --build . --config Release -j ${CPU_COUNT}
