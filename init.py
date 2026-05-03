"""
CRISP-py
========
Comprehensive Robust Integrated SNP Processing (Python)

A Python-native reimplementation of CRISP, the genotype quality control
pipeline for large-scale SNP array data. Supports PLINK, VCF, BCF and
BGEN input formats. Instruction file compatible with CRISP v1.x.

Developed by Igor Pupko
https://github.com/ipupko/CRISP-py

Status
------
CRISP-py is currently in early development. Active work will begin
following the release of CRISP v1.0. For the current pipeline please
visit https://github.com/ipupko/CRISP.

Planned modules
---------------
crisp.steps
    Step-by-step QC pipeline modules.
    Each step mirrors a chunk in the original CRISP pipeline.

    step1_validate   File validation, MD5 generation, input summary
    step2_convert    Format conversion to BED/BIM/FAM
    step3_callrate   Sample call rate filtering
    step4_snprate    Variant call rate, monomorphic and MAF filtering
    step5_sexcheck   Sex check and mismatch detection
    step6_aneuploidy Turner, Klinefelter and triple-X detection
    step7_homozygosity  Heterozygosity and homozygosity outlier detection
    step8_relatedness   IBD and KING relatedness filtering
    step9_variantqc  HWE filtering
    step10_pca       LD pruning, PCA and ancestry visualisation
    step11_amend     Apply all exclusion lists, produce clean dataset
    step12_report    End-to-end QC summary report

crisp.plots
    Plotting modules for each QC step.
    R (ggplot2) available as an optional backend.

    plot_callrate    Sample missingness distribution
    plot_snprate     Variant missingness distribution
    plot_sexcheck    F-statistic and Y-count scatter plots
    plot_homozygosity  Homozygosity Z-score vs ROH
    plot_pca         PCA scatter plots and ancestry visualisation

crisp.io
    Input/output utilities.

    readers          Format-aware genotype file readers
    writers          Exclusion list and report writers
    validators       File signature and parameter validation

crisp.config
    Instruction file parser and default parameter management.

Version history
---------------
0.1.0   Placeholder release. Repository initialised.
1.0.0   First full release (planned, post CRISP v1.0).
"""

__version__     = "0.1.0"
__author__      = "Igor Pupko"
__email__       = ""
__license__     = "MIT"
__status__      = "Placeholder"
__url__         = "https://github.com/ipupko/CRISP-py"
__crisp_url__   = "https://github.com/ipupko/CRISP"

# CRISP-py is not yet importable as a package.
# This file reserves the namespace and documents planned structure.
# Active development begins after CRISP v1.0 release.

__all__ = [
    "__version__",
    "__author__",
    "__license__",
    "__status__",
    "__url__",
]
