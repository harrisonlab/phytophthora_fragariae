#Commands to run analysis of linkage disequilibrium, also phases diploid genomes

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats
scripts=/home/adamst/git_repos/scripts/popgen
vcftools=/home/sobczm/bin/vcftools/bin
```

#Carry out phasing of diploid genomes

```bash
cd summary_stats
inputvcf=95m_contigs_unmasked_UK123_filtered.recode.vcf
qsub $scripts/snp/sub_beagle.sh $inputvcf
```

#Calculate D, D' and r^2 for SNPs separated by between 1 and 100 kbp in non-pathogens (program calculates the stats using only the individuals listed after "--indv" switch)

```bash
gunzip 95m_contigs_unmasked_UK123_filtered.recode_haplo.vcf.gz
$vcftools/vcftools --vcf 95m_contigs_unmasked_UK123_filtered.recode_haplo.vcf \
--hap-r2 --ld-window-bp-min 1000 --ld-window-bp 100000 \
--indv Bc1 --indv Bc16 --indv A4 --indv Nov27 --indv Nov9 --indv Nov5 --indv Nov71
mv out.hap.ld ld.UK123

qsub $scripts/sub_plot_ld.sh ld.UK123
```

#Calculate D, D' and r^2 for SNPs separated by between 1 and 100 kbp
#in pathogens (program calculates the stats using only the individuals
#listed after "--indv" switch)

$vcftools/vcftools --vcf Fus2_canu_contigs_unmasked_noA13_filtered.recode.vcf \
--hap-r2 --ld-window-bp-min 1000 --ld-window-bp 100000 \
--indv FOC55 --indv FOCA23 --indv FOC125 --indv FOCFus2

mv out.hap.ld ld.patho

qsub $scripts/sub_plot_ld.sh ld.patho
