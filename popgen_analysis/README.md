#README for popgen analyses


Maria has put together a series of tools for population genetics analyses. This file explains the order in which the various scripts in this directory were run in order to allow for easier replication.

1. pre_SNP_calling_cleanup.md - Inital set up commands before running SNP calling
2. SNP_calling_multithreaded.md - Runs the core SNP calling pipeline
3. sub_SNP_calling_multithreaded.md - Script that is qsubbed for core SNP calling
4. SNP_analysis.md - Inital sets of analysis on resulting .vcf file
5. Pf_variant_annotation.md - Begins analysis for the summary statistics of popgen analyses
6. BC-1_NOV-9_comparison.md - Similar to variant annotation but only for BC-1 and NOV-9
7. polarising_SNPs.md - Incorrectly named file that identifies private SNPs.
8. structural_variants.md - Uses bwa-mem and lumpy to ID and assess structural variants between isolates
9. Pf_linkage_disequilibrium.md - This phases diploid genomes and run linkage disequilibrium analyses
10. MKT_analysis.md - Commands to test ancestral variants and run some popgen tests such as MKT and Fay & Wu's H - also uses sub_calculate_mkt.sh and calculate_outgroup_mktest.R
11. Pf_popgenome_analysis.md - Extra summary stats analysis using popgenome R tools
