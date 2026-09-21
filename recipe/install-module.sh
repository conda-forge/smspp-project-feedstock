set -ex

# SMSPP_MODULES: the directories of the build that this output installs
for module in ${SMSPP_MODULES}; do
    cmake --install build/${module} --config Release
done
