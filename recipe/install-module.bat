:: SMSPP_MODULES: the directories of the build that this output installs
for %%m in (%SMSPP_MODULES%) do (
    cmake --install build/%%m --config Release
    if errorlevel 1 exit 1
)
