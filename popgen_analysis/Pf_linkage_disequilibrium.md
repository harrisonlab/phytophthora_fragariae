# Commands to run analysis of linkage disequilibrium, also phases diploid genomes

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats
scripts=/home/adamst/git_repos/scripts/popgen
vcftools=/home/sobczm/bin/vcftools/bin
```

## Analysis restricted to UK races 1, 2 and 3, based on fastStructure results

### Carry out phasing of diploid genomes

```bash
cd summary_stats
inputvcf=polished_contigs_unmasked_UK123_filtered.recode.vcf
qsub $scripts/snp/sub_beagle.sh $inputvcf
```

### Calculate D, D' and r^2 for variants separated by 1 - 100 kbp in UK123

program calculates the stats using only the individuals listed after "--indv" switch

```bash
gunzip polished_contigs_unmasked_UK123_filtered.recode_haplo.vcf.gz
$vcftools/vcftools --vcf polished_contigs_unmasked_UK123_filtered.recode_haplo.vcf \
--hap-r2 --ld-window-bp-min 1000 --ld-window-bp 100000 \
--indv Bc1 --indv Bc16 --indv A4 --indv Nov27 --indv Nov9 --indv Nov5 --indv Nov71
mv out.hap.ld ld.UK123

# Run on head due to version of R required
$scripts/summary_stats/sub_plot_ld.sh ld.UK123

mkdir -p UK123
mv ld* UK123/.
```

## Analysis on all *P. fragariae* isolates less NOV-77

based on fastStructure results

### Carry out phasing of diploid genomes

```bash
inputvcf=polished_contigs_unmasked_Pf_filtered.recode_annotated.vcf
qsub $scripts/snp/sub_beagle.sh $inputvcf
```

### Calculate D, D' and r^2 for SNPs separated by 1 - 100 kbp in Pf

program calculates the stats using only the individuals listed after "--indv" switch

```bash
gunzip polished_contigs_unmasked_Pf_filtered.recode_annotated_haplo.vcf.gz
$vcftools/vcftools --vcf polished_contigs_unmasked_Pf_filtered.recode_annotated_haplo.vcf \
--hap-r2 --ld-window-bp-min 1000 --ld-window-bp 100000 \
--indv Bc1 --indv Bc16 --indv A4 --indv Nov27 --indv Nov9 --indv Nov5 --indv Nov71 --indv Bc23 --indv ONT3 --indv SCRP245_v2
mv out.hap.ld ld.Pf

$scripts/summary_stats/sub_plot_ld.sh ld.Pf

mkdir -p Pf
mv ld* Pf/.
```

## Analysis of BC-23 and ONT-3

based on fastStructure results - they group separately

### Carry out phasing of diploid genomes

```bash
fullvcf=../SNP_calling/polished_contigs_unmasked_filtered.recode.vcf
inputvcf=polished_contigs_unmasked_Bc23ONT3_filtered.recode_annotated.vcf
vcflib=/home/sobczm/bin/vcflib/bin
$vcflib/vcfremovesamples $fullvcf A4 Bc1 Bc16 Nov5 Nov9 Nov27 Nov71 Nov77 SCRP245_v2 SCRP249 SCRP324 SCRP333 > $inputvcf
vcftools=/home/sobczm/bin/vcftools/bin
input_vcf_cleaned=polished_contigs_unmasked_Bc23ONT3_filtered.recode_annotated_nomissing.recode.vcf
$vcftools/vcftools --vcf $inputvcf --out polished_contigs_unmasked_Bc23ONT3_filtered.recode_annotated_nomissing --max-missing 1 --recode
qsub $scripts/snp/sub_beagle.sh $input_vcf_cleaned
```

### Calculate D, D' and r^2 for SNPs separated by 1 - 100 kbp in Pf

program calculates the stats using only the individuals listed after "--indv" switch

```bash
gunzip polished_contigs_unmasked_Bc23ONT3_filtered.recode_annotated_nomissing.recode_haplo.vcf.gz
$vcftools/vcftools --vcf polished_contigs_unmasked_Bc23ONT3_filtered.recode_annotated_nomissing.recode_haplo.vcf \
--hap-r2 --ld-window-bp-min 1000 --ld-window-bp 100000 \
--indv Bc23 --indv ONT3
mv out.hap.ld ld.Bc23_ONT3

# Run in qlogin session due to high memory usage
/home/adamst/prog/R/R-3.2.5/bin/Rscript --vanilla $scripts/summary_stats/plot_ld.R ld.Bc23_ONT3

mkdir -p Bc23_ONT3
mv ld* Bc23_ONT3/.
```

## Analysis of LD decay in UK123 isolates

### Recalculate LD statistics without a minimum window size

```bash
$vcftools/vcftools --vcf polished_contigs_unmasked_UK123_filtered.recode_haplo.vcf \
--hap-r2 --ld-window-bp 100000 \
--indv Bc1 --indv Bc16 --indv A4 --indv Nov27 --indv Nov9 --indv Nov5 --indv Nov71
mv out.hap.ld ld.UK123_no_min
mv ld* UK123/.
```

### Calculate LD decay and plot curve

```
Size is:
The number of individuals sampled * number of chromosomes sequenced * ploidy
I have three as Pf n = 10 - 12 (https://doi.org/10.1073/pnas.96.10.5878)
```

```bash
for Size in 560 616 672
do
    Out_File_Fitted=UK123/r^2_decay_"$Size"_fitted.pdf
    Out_File_Unfitted=UK123/r^2_decay_"$Size"_unfitted.pdf
    LD_file=UK123/ld.UK123_no_min
    units=bp
    window_size=100000
    bin_size=1000
    Cstart=0.1
    ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae/popgen_analysis
    echo "Sample size of $Size:"
    Rscript --vanilla $ProgDir/plot_LD_decay.R --out_file_fitted $Out_File_Fitted --out_file_unfitted $Out_File_Unfitted --Chromosome_number $Size --LD_statistics $LD_file --units $units --window_size $window_size --bin_size $bin_size --Cstart $Cstart
    printf "\n"
done
```
