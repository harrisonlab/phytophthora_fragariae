#README for popgen analyses


Maria has put together a series of tools for population genetics analyses. This file explains the order in which the various scripts in this directory were run in order to allow for easier replication.

1. pre_SNP_calling_cleanup.md - Inital set up commands before running SNP calling
2. SNP_calling_multithreaded.md - Runs the core SNP calling pipeline
3. sub_SNP_calling_multithreaded.md - Script that is qsubbed for core SNP calling
4. SNP_analysis.md - Inital sets of analysis on resulting .vcf file
5. structural_variants.md - Uses bwa-mem and lumpy to ID and assess structural variants between isolates
