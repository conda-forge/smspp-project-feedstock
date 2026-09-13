About smspp-project-feedstock
=============================

Feedstock license: [BSD-3-Clause](https://github.com/conda-forge/ctrl-feedstock/blob/main/LICENSE.txt)

Home: https://gitlab.com/smspp/smspp-project

Package license: LGPL-3.0-only

Summary: A powerful tool to model and solve optimization problems.

Development: https://gitlab.com/smspp/smspp-project

Documentation: https://smspp.gitlab.io/

SMS++ project provides a system for modeling complex, block-structured mathematical models, and solving them via sophisticated, structure-exploiting algorithms.
It is split into the libsmspp library of the core, a libsmspp-<module> library for each of its Blocks and Solvers, a package for each of its command-line tools (e.g. smspp-ucblock for ucblock_solver), and smspp-project, which installs them all.


Current build status
====================


<table><tr>
    <td>GitHub Actions</td>
    <td>
      <a href="https://github.com/conda-forge/ctrl-feedstock/actions/workflows/conda-build.yml">
        <img src="https://github.com/conda-forge/ctrl-feedstock/actions/workflows/conda-build.yml/badge.svg?event=push&branch=main">
      </a>
    </td>
  </tr>
    
  <tr>
    <td>Azure</td>
    <td>
      <details>
        <summary>
          <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=None&branchName=main">
            <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/ctrl-feedstock?branchName=main">
          </a>
        </summary>
        <table>
          <thead><tr><th>Variant</th><th>Status</th></tr></thead>
          <tbody><tr>
              <td>osx_64_hdf51.14.6libnetcdf4.9.3</td>
              <td>
                <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=None&branchName=main">
                  <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/ctrl-feedstock?branchName=main&jobName=osx&configuration=osx%20osx_64_hdf51.14.6libnetcdf4.9.3" alt="variant">
                </a>
              </td>
            </tr><tr>
              <td>osx_64_hdf52libnetcdf4.10.1</td>
              <td>
                <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=None&branchName=main">
                  <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/ctrl-feedstock?branchName=main&jobName=osx&configuration=osx%20osx_64_hdf52libnetcdf4.10.1" alt="variant">
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </details>
    </td>
  </tr>
</table>

Current release info
====================

| Name | Downloads | Version | Platforms |
| --- | --- | --- | --- |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp-green.svg)](https://anaconda.org/conda-forge/libsmspp) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp.svg)](https://anaconda.org/conda-forge/libsmspp) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp.svg)](https://anaconda.org/conda-forge/libsmspp) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp.svg)](https://anaconda.org/conda-forge/libsmspp) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--bds-green.svg)](https://anaconda.org/conda-forge/libsmspp-bds) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-bds.svg)](https://anaconda.org/conda-forge/libsmspp-bds) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-bds.svg)](https://anaconda.org/conda-forge/libsmspp-bds) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-bds.svg)](https://anaconda.org/conda-forge/libsmspp-bds) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--bkb-green.svg)](https://anaconda.org/conda-forge/libsmspp-bkb) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-bkb.svg)](https://anaconda.org/conda-forge/libsmspp-bkb) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-bkb.svg)](https://anaconda.org/conda-forge/libsmspp-bkb) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-bkb.svg)](https://anaconda.org/conda-forge/libsmspp-bkb) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--bnx-green.svg)](https://anaconda.org/conda-forge/libsmspp-bnx) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-bnx.svg)](https://anaconda.org/conda-forge/libsmspp-bnx) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-bnx.svg)](https://anaconda.org/conda-forge/libsmspp-bnx) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-bnx.svg)](https://anaconda.org/conda-forge/libsmspp-bnx) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--bundle-green.svg)](https://anaconda.org/conda-forge/libsmspp-bundle) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-bundle.svg)](https://anaconda.org/conda-forge/libsmspp-bundle) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-bundle.svg)](https://anaconda.org/conda-forge/libsmspp-bundle) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-bundle.svg)](https://anaconda.org/conda-forge/libsmspp-bundle) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--cflb-green.svg)](https://anaconda.org/conda-forge/libsmspp-cflb) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-cflb.svg)](https://anaconda.org/conda-forge/libsmspp-cflb) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-cflb.svg)](https://anaconda.org/conda-forge/libsmspp-cflb) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-cflb.svg)](https://anaconda.org/conda-forge/libsmspp-cflb) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--frankwolfe-green.svg)](https://anaconda.org/conda-forge/libsmspp-frankwolfe) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-frankwolfe.svg)](https://anaconda.org/conda-forge/libsmspp-frankwolfe) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-frankwolfe.svg)](https://anaconda.org/conda-forge/libsmspp-frankwolfe) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-frankwolfe.svg)](https://anaconda.org/conda-forge/libsmspp-frankwolfe) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--investment-green.svg)](https://anaconda.org/conda-forge/libsmspp-investment) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-investment.svg)](https://anaconda.org/conda-forge/libsmspp-investment) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-investment.svg)](https://anaconda.org/conda-forge/libsmspp-investment) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-investment.svg)](https://anaconda.org/conda-forge/libsmspp-investment) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--lds-green.svg)](https://anaconda.org/conda-forge/libsmspp-lds) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-lds.svg)](https://anaconda.org/conda-forge/libsmspp-lds) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-lds.svg)](https://anaconda.org/conda-forge/libsmspp-lds) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-lds.svg)](https://anaconda.org/conda-forge/libsmspp-lds) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--lukfi-green.svg)](https://anaconda.org/conda-forge/libsmspp-lukfi) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-lukfi.svg)](https://anaconda.org/conda-forge/libsmspp-lukfi) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-lukfi.svg)](https://anaconda.org/conda-forge/libsmspp-lukfi) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-lukfi.svg)](https://anaconda.org/conda-forge/libsmspp-lukfi) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--mcf-green.svg)](https://anaconda.org/conda-forge/libsmspp-mcf) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-mcf.svg)](https://anaconda.org/conda-forge/libsmspp-mcf) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-mcf.svg)](https://anaconda.org/conda-forge/libsmspp-mcf) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-mcf.svg)](https://anaconda.org/conda-forge/libsmspp-mcf) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--mcfclass-green.svg)](https://anaconda.org/conda-forge/libsmspp-mcfclass) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-mcfclass.svg)](https://anaconda.org/conda-forge/libsmspp-mcfclass) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-mcfclass.svg)](https://anaconda.org/conda-forge/libsmspp-mcfclass) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-mcfclass.svg)](https://anaconda.org/conda-forge/libsmspp-mcfclass) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--mcflemon-green.svg)](https://anaconda.org/conda-forge/libsmspp-mcflemon) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-mcflemon.svg)](https://anaconda.org/conda-forge/libsmspp-mcflemon) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-mcflemon.svg)](https://anaconda.org/conda-forge/libsmspp-mcflemon) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-mcflemon.svg)](https://anaconda.org/conda-forge/libsmspp-mcflemon) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--milp-green.svg)](https://anaconda.org/conda-forge/libsmspp-milp) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-milp.svg)](https://anaconda.org/conda-forge/libsmspp-milp) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-milp.svg)](https://anaconda.org/conda-forge/libsmspp-milp) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-milp.svg)](https://anaconda.org/conda-forge/libsmspp-milp) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--mmcf-green.svg)](https://anaconda.org/conda-forge/libsmspp-mmcf) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-mmcf.svg)](https://anaconda.org/conda-forge/libsmspp-mmcf) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-mmcf.svg)](https://anaconda.org/conda-forge/libsmspp-mmcf) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-mmcf.svg)](https://anaconda.org/conda-forge/libsmspp-mmcf) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--mssb-green.svg)](https://anaconda.org/conda-forge/libsmspp-mssb) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-mssb.svg)](https://anaconda.org/conda-forge/libsmspp-mssb) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-mssb.svg)](https://anaconda.org/conda-forge/libsmspp-mssb) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-mssb.svg)](https://anaconda.org/conda-forge/libsmspp-mssb) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--sddp-green.svg)](https://anaconda.org/conda-forge/libsmspp-sddp) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-sddp.svg)](https://anaconda.org/conda-forge/libsmspp-sddp) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-sddp.svg)](https://anaconda.org/conda-forge/libsmspp-sddp) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-sddp.svg)](https://anaconda.org/conda-forge/libsmspp-sddp) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--sfdcr-green.svg)](https://anaconda.org/conda-forge/libsmspp-sfdcr) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-sfdcr.svg)](https://anaconda.org/conda-forge/libsmspp-sfdcr) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-sfdcr.svg)](https://anaconda.org/conda-forge/libsmspp-sfdcr) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-sfdcr.svg)](https://anaconda.org/conda-forge/libsmspp-sfdcr) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--srs-green.svg)](https://anaconda.org/conda-forge/libsmspp-srs) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-srs.svg)](https://anaconda.org/conda-forge/libsmspp-srs) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-srs.svg)](https://anaconda.org/conda-forge/libsmspp-srs) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-srs.svg)](https://anaconda.org/conda-forge/libsmspp-srs) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--stochastic-green.svg)](https://anaconda.org/conda-forge/libsmspp-stochastic) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-stochastic.svg)](https://anaconda.org/conda-forge/libsmspp-stochastic) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-stochastic.svg)](https://anaconda.org/conda-forge/libsmspp-stochastic) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-stochastic.svg)](https://anaconda.org/conda-forge/libsmspp-stochastic) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--svm-green.svg)](https://anaconda.org/conda-forge/libsmspp-svm) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-svm.svg)](https://anaconda.org/conda-forge/libsmspp-svm) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-svm.svg)](https://anaconda.org/conda-forge/libsmspp-svm) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-svm.svg)](https://anaconda.org/conda-forge/libsmspp-svm) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--tssb-green.svg)](https://anaconda.org/conda-forge/libsmspp-tssb) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-tssb.svg)](https://anaconda.org/conda-forge/libsmspp-tssb) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-tssb.svg)](https://anaconda.org/conda-forge/libsmspp-tssb) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-tssb.svg)](https://anaconda.org/conda-forge/libsmspp-tssb) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libsmspp--ucblock-green.svg)](https://anaconda.org/conda-forge/libsmspp-ucblock) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libsmspp-ucblock.svg)](https://anaconda.org/conda-forge/libsmspp-ucblock) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libsmspp-ucblock.svg)](https://anaconda.org/conda-forge/libsmspp-ucblock) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libsmspp-ucblock.svg)](https://anaconda.org/conda-forge/libsmspp-ucblock) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-smspp--bkb-green.svg)](https://anaconda.org/conda-forge/smspp-bkb) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/smspp-bkb.svg)](https://anaconda.org/conda-forge/smspp-bkb) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/smspp-bkb.svg)](https://anaconda.org/conda-forge/smspp-bkb) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/smspp-bkb.svg)](https://anaconda.org/conda-forge/smspp-bkb) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-smspp--cflb-green.svg)](https://anaconda.org/conda-forge/smspp-cflb) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/smspp-cflb.svg)](https://anaconda.org/conda-forge/smspp-cflb) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/smspp-cflb.svg)](https://anaconda.org/conda-forge/smspp-cflb) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/smspp-cflb.svg)](https://anaconda.org/conda-forge/smspp-cflb) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-smspp--investment-green.svg)](https://anaconda.org/conda-forge/smspp-investment) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/smspp-investment.svg)](https://anaconda.org/conda-forge/smspp-investment) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/smspp-investment.svg)](https://anaconda.org/conda-forge/smspp-investment) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/smspp-investment.svg)](https://anaconda.org/conda-forge/smspp-investment) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-smspp--mcf-green.svg)](https://anaconda.org/conda-forge/smspp-mcf) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/smspp-mcf.svg)](https://anaconda.org/conda-forge/smspp-mcf) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/smspp-mcf.svg)](https://anaconda.org/conda-forge/smspp-mcf) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/smspp-mcf.svg)](https://anaconda.org/conda-forge/smspp-mcf) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-smspp--mmcf-green.svg)](https://anaconda.org/conda-forge/smspp-mmcf) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/smspp-mmcf.svg)](https://anaconda.org/conda-forge/smspp-mmcf) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/smspp-mmcf.svg)](https://anaconda.org/conda-forge/smspp-mmcf) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/smspp-mmcf.svg)](https://anaconda.org/conda-forge/smspp-mmcf) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-smspp--mssb-green.svg)](https://anaconda.org/conda-forge/smspp-mssb) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/smspp-mssb.svg)](https://anaconda.org/conda-forge/smspp-mssb) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/smspp-mssb.svg)](https://anaconda.org/conda-forge/smspp-mssb) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/smspp-mssb.svg)](https://anaconda.org/conda-forge/smspp-mssb) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-smspp--project-green.svg)](https://anaconda.org/conda-forge/smspp-project) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/smspp-project.svg)](https://anaconda.org/conda-forge/smspp-project) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/smspp-project.svg)](https://anaconda.org/conda-forge/smspp-project) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/smspp-project.svg)](https://anaconda.org/conda-forge/smspp-project) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-smspp--sddp-green.svg)](https://anaconda.org/conda-forge/smspp-sddp) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/smspp-sddp.svg)](https://anaconda.org/conda-forge/smspp-sddp) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/smspp-sddp.svg)](https://anaconda.org/conda-forge/smspp-sddp) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/smspp-sddp.svg)](https://anaconda.org/conda-forge/smspp-sddp) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-smspp--sfdcr-green.svg)](https://anaconda.org/conda-forge/smspp-sfdcr) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/smspp-sfdcr.svg)](https://anaconda.org/conda-forge/smspp-sfdcr) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/smspp-sfdcr.svg)](https://anaconda.org/conda-forge/smspp-sfdcr) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/smspp-sfdcr.svg)](https://anaconda.org/conda-forge/smspp-sfdcr) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-smspp--svm-green.svg)](https://anaconda.org/conda-forge/smspp-svm) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/smspp-svm.svg)](https://anaconda.org/conda-forge/smspp-svm) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/smspp-svm.svg)](https://anaconda.org/conda-forge/smspp-svm) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/smspp-svm.svg)](https://anaconda.org/conda-forge/smspp-svm) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-smspp--tools-green.svg)](https://anaconda.org/conda-forge/smspp-tools) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/smspp-tools.svg)](https://anaconda.org/conda-forge/smspp-tools) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/smspp-tools.svg)](https://anaconda.org/conda-forge/smspp-tools) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/smspp-tools.svg)](https://anaconda.org/conda-forge/smspp-tools) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-smspp--tssb-green.svg)](https://anaconda.org/conda-forge/smspp-tssb) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/smspp-tssb.svg)](https://anaconda.org/conda-forge/smspp-tssb) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/smspp-tssb.svg)](https://anaconda.org/conda-forge/smspp-tssb) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/smspp-tssb.svg)](https://anaconda.org/conda-forge/smspp-tssb) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-smspp--ucblock-green.svg)](https://anaconda.org/conda-forge/smspp-ucblock) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/smspp-ucblock.svg)](https://anaconda.org/conda-forge/smspp-ucblock) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/smspp-ucblock.svg)](https://anaconda.org/conda-forge/smspp-ucblock) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/smspp-ucblock.svg)](https://anaconda.org/conda-forge/smspp-ucblock) |

Installing smspp-project
========================

Installing `smspp-project` from the `conda-forge` channel can be achieved by adding `conda-forge` to your channels with:

```
conda config --add channels conda-forge
conda config --set channel_priority strict
```

How to use
----------

<details>
<summary>With conda</summary>

```
conda install libsmspp libsmspp-bds libsmspp-bkb libsmspp-bnx libsmspp-bundle libsmspp-cflb libsmspp-frankwolfe libsmspp-investment libsmspp-lds libsmspp-lukfi libsmspp-mcf libsmspp-mcfclass libsmspp-mcflemon libsmspp-milp libsmspp-mmcf libsmspp-mssb libsmspp-sddp libsmspp-sfdcr libsmspp-srs libsmspp-stochastic libsmspp-svm libsmspp-tssb libsmspp-ucblock smspp-bkb smspp-cflb smspp-investment smspp-mcf smspp-mmcf smspp-mssb smspp-project smspp-sddp smspp-sfdcr smspp-svm smspp-tools smspp-tssb smspp-ucblock
```

</details>

<details>
<summary>With mamba</summary>

```
mamba install libsmspp libsmspp-bds libsmspp-bkb libsmspp-bnx libsmspp-bundle libsmspp-cflb libsmspp-frankwolfe libsmspp-investment libsmspp-lds libsmspp-lukfi libsmspp-mcf libsmspp-mcfclass libsmspp-mcflemon libsmspp-milp libsmspp-mmcf libsmspp-mssb libsmspp-sddp libsmspp-sfdcr libsmspp-srs libsmspp-stochastic libsmspp-svm libsmspp-tssb libsmspp-ucblock smspp-bkb smspp-cflb smspp-investment smspp-mcf smspp-mmcf smspp-mssb smspp-project smspp-sddp smspp-sfdcr smspp-svm smspp-tools smspp-tssb smspp-ucblock
```

</details>

<details>
<summary>With pixi</summary>

```
# for adding to your local project
pixi add libsmspp libsmspp-bds libsmspp-bkb libsmspp-bnx libsmspp-bundle libsmspp-cflb libsmspp-frankwolfe libsmspp-investment libsmspp-lds libsmspp-lukfi libsmspp-mcf libsmspp-mcfclass libsmspp-mcflemon libsmspp-milp libsmspp-mmcf libsmspp-mssb libsmspp-sddp libsmspp-sfdcr libsmspp-srs libsmspp-stochastic libsmspp-svm libsmspp-tssb libsmspp-ucblock smspp-bkb smspp-cflb smspp-investment smspp-mcf smspp-mmcf smspp-mssb smspp-project smspp-sddp smspp-sfdcr smspp-svm smspp-tools smspp-tssb smspp-ucblock
# for installing globally
pixi global install libsmspp libsmspp-bds libsmspp-bkb libsmspp-bnx libsmspp-bundle libsmspp-cflb libsmspp-frankwolfe libsmspp-investment libsmspp-lds libsmspp-lukfi libsmspp-mcf libsmspp-mcfclass libsmspp-mcflemon libsmspp-milp libsmspp-mmcf libsmspp-mssb libsmspp-sddp libsmspp-sfdcr libsmspp-srs libsmspp-stochastic libsmspp-svm libsmspp-tssb libsmspp-ucblock smspp-bkb smspp-cflb smspp-investment smspp-mcf smspp-mmcf smspp-mssb smspp-project smspp-sddp smspp-sfdcr smspp-svm smspp-tools smspp-tssb smspp-ucblock
```

</details>

Search package versions
-----------------------

It is possible to list all of the versions of `libsmspp` available on your platform:

<details>
<summary>With conda</summary>

```
conda search libsmspp --channel conda-forge
```

</details>

<details>
<summary>With mamba</summary>

```
mamba search libsmspp --channel conda-forge
```

</details>

<details>
<summary>With pixi</summary>

```
pixi search libsmspp --channel conda-forge
```

</details>

<details>
<summary>With mamba repoquery, which may provide more information</summary>

```
# Search all versions available on your platform:
mamba repoquery search libsmspp --channel conda-forge

# List packages depending on `libsmspp`:
mamba repoquery whoneeds libsmspp --channel conda-forge

# List dependencies of `libsmspp`:
mamba repoquery depends libsmspp --channel conda-forge
```

</details>


About conda-forge
=================

[![Powered by
NumFOCUS](https://img.shields.io/badge/powered%20by-NumFOCUS-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://numfocus.org)

conda-forge is a community-led conda channel of installable packages.
In order to provide high-quality builds, the process has been automated into the
conda-forge GitHub organization. The conda-forge organization contains one repository
for each of the installable packages. Such a repository is known as a *feedstock*.

A feedstock is made up of a conda recipe (the instructions on what and how to build
the package) and the necessary configurations for automatic building using freely
available continuous integration services. Thanks to the awesome service provided by
[Azure](https://azure.microsoft.com/en-us/services/devops/), [GitHub](https://github.com/),
[CircleCI](https://circleci.com/), [AppVeyor](https://www.appveyor.com/),
[Drone](https://cloud.drone.io/welcome), and [TravisCI](https://travis-ci.com/)
it is possible to build and upload installable packages to the
[conda-forge](https://anaconda.org/conda-forge) [anaconda.org](https://anaconda.org/)
channel for Linux, Windows and OSX respectively.

To manage the continuous integration and simplify feedstock maintenance,
[conda-smithy](https://github.com/conda-forge/conda-smithy) has been developed.
Using the ``conda-forge.yml`` within this repository, it is possible to re-render all of
this feedstock's supporting files (e.g. the CI configuration files) with ``conda smithy rerender``.

For more information, please check the [conda-forge documentation](https://conda-forge.org/docs/).

Terminology
===========

**feedstock** - the conda recipe (raw material), supporting scripts and CI configuration.

**conda-smithy** - the tool which helps orchestrate the feedstock.
                   Its primary use is in the construction of the CI ``.yml`` files
                   and simplify the management of *many* feedstocks.

**conda-forge** - the place where the feedstock and smithy live and work to
                  produce the finished article (built conda distributions)


Updating smspp-project-feedstock
================================

If you would like to improve the smspp-project recipe or build a new
package version, please fork this repository and submit a PR. Upon submission,
your changes will be run on the appropriate platforms to give the reviewer an
opportunity to confirm that the changes result in a successful build. Once
merged, the recipe will be re-built and uploaded automatically to the
`conda-forge` channel, whereupon the built conda packages will be available for
everybody to install and use from the `conda-forge` channel.
Note that all branches in the conda-forge/smspp-project-feedstock are
immediately built and any created packages are uploaded, so PRs should be based
on branches in forks, and branches in the main repository should only be used to
build distinct package versions.

In order to produce a uniquely identifiable distribution:
 * If the version of a package **is not** being increased, please add or increase
   the [``build/number``](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#build-number-and-string).
 * If the version of a package **is** being increased, please remember to return
   the [``build/number``](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#build-number-and-string)
   back to 0.

Feedstock Maintainers
=====================

* [@davide-f](https://github.com/davide-f/)
* [@dmeoli](https://github.com/dmeoli/)
* [@frangio68](https://github.com/frangio68/)

