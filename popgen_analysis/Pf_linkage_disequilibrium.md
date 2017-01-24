input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats
scripts=/home/adamst/git_repos/scripts/phytophthora_fragariae/popgen_analysis
vcftools=/home/sobczm/bin/vcftools/bin

#Calculate D, D' and r^2 for SNPs separated by between 1 and 100 kbp
#in non-pathogens (program calculates the stats using only the individuals
#listed after "--indv" switch)
$vcftools/vcftools --vcf Fus2_canu_contigs_unmasked_noA13_filtered.recode.vcf \
--hap-r2 --ld-window-bp-min 1000 --ld-window-bp 100000 \
--indv FOCPG --indv FOCHB6 --indv FOCCB3 --indv FOCA28 --indv FOCD2 --indv FOCA1-2
mv out.hap.ld ld.nonpatho

qsub $scripts/sub_plot_ld.sh ld.nonpatho

#Calculate D, D' and r^2 for SNPs separated by between 1 and 100 kbp
#in pathogens (program calculates the stats using only the individuals
#listed after "--indv" switch)

$vcftools/vcftools --vcf Fus2_canu_contigs_unmasked_noA13_filtered.recode.vcf \
--hap-r2 --ld-window-bp-min 1000 --ld-window-bp 100000 \
--indv FOC55 --indv FOCA23 --indv FOC125 --indv FOCFus2

mv out.hap.ld ld.patho

qsub $scripts/sub_plot_ld.sh ld.patho
