# Runs commands from Maria to analyse output from SNP calling

## Create a cut-down vcf that only includes *P. fragariae* strains

```bash
vcftools=/home/sobczm/bin/vcftools/bin
vcflib=/home/sobczm/bin/vcflib/bin
```

### Just *P. fragariae* strains
First argument: unfiltered input VCF file with all SNPs
Subsequent arguments: Sample names of individuals to be removed

```bash
cd SNP_calling
$vcflib/vcfremovesamples polished_contigs_unmasked.vcf SCRP249 SCRP324 SCRP333 > Pfrag_only_polished_contigs_unmasked.vcf
```

## Filter vcf outputs, only retain biallelic high-quality SNPS with no missing data for genetic analyses.

```bash
for vcf in $(ls *_contigs_unmasked.vcf)
do
    echo $vcf
    script=/home/adamst/git_repos/scripts/popgen/snp/sub_vcf_parser.sh
    qsub $script $vcf
done
```

Only one of these can be run at a time!

#General VCF stats (remember that vcftools needs to have the PERL library exported)

```bash
cd ../
perl /home/sobczm/bin/vcftools/bin/vcf-stats \
SNP_calling/polished_contigs_unmasked.vcf > SNP_calling/polished_contigs_unmasked.stat
perl /home/sobczm/bin/vcftools/bin/vcf-stats \
SNP_calling/polished_contigs_unmasked_filtered.vcf > SNP_calling/polished_contigs_unmasked_filtered.stat

perl /home/sobczm/bin/vcftools/bin/vcf-stats \
SNP_calling/Pfrag_only_polished_contigs_unmasked.vcf > SNP_calling/Pfrag_only_polished_contigs_unmasked.stat
perl /home/sobczm/bin/vcftools/bin/vcf-stats \
SNP_calling/Pfrag_only_polished_contigs_unmasked_filtered.vcf > SNP_calling/Pfrag_only_polished_contigs_unmasked_filtered.stat
```

#Calculate the index for percentage of shared SNP alleles between the individuals.

```bash
for vcf in $(ls SNP_calling/*_filtered.vcf)
do
    scripts=/home/adamst/git_repos/scripts/popgen/snp
    echo $vcf
    $scripts/similarity_percentage.py $vcf
done
```

#Remove monomorphic sites (minor allele count minimum 1). Argument --vcf is the filtered VCF file, and --out is the suffix to be used for the output file.

```bash
for vcf in $(ls SNP_calling/*_filtered.vcf)
do
    echo $vcf
    out=$(basename $vcf .vcf)
    echo $out
    $vcftools/vcftools --vcf $vcf --mac 1 --recode --out SNP_calling/$out
done
```

#Create custom SnpEff genome database

```bash
snpeff=/home/adamst/prog/snpEff
nano $snpeff/snpEff.config
```

##Add the following lines to the section with databases:

```
#---
# EMR Databases
#----
# Bc16 genome
Bc16v1.0.genome: BC-16
```

#Collect input files

```bash
mkdir -p $snpeff/data/Bc16v1.0
cp repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa $snpeff/data/Bc16v1.0
cp gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors_renamed.gff3 $snpeff/data/Bc16v1.0
```

#Rename input files

```bash
cd $snpeff/data/Bc16v1.0
mv Bc16_genes_incl_ORFeffectors_renamed.gff3 genes.gff
mv polished_contigs_unmasked.fa sequences.fa
```

#Build database using GFF3 annotation

```bash
java -jar $snpeff/snpEff.jar build -gff3 -v Bc16v1.0
```

#Annotate VCF files

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae
cd $input
for a in SNP_calling/*recode.vcf
do
    echo $a
    filename=$(basename "$a")
    java -Xmx4g -jar $snpeff/snpEff.jar -v -ud 0 Bc16v1.0 $a > ${filename%.vcf}_annotated.vcf
    mv snpEff_genes.txt SNP_calling/snpEff_genes_${filename%.vcf}.txt
    mv snpEff_summary.html  SNP_calling/snpEff_summary__${filename%.vcf}.html
done
```

#Visualise the output as heatmap and clustering dendrogram

```bash
for log in $(ls SNP_calling/*distance.log)
do
    scripts=/home/adamst/git_repos/scripts/popgen/snp
    Rscript --vanilla $scripts/distance_matrix.R $log
done
```

#Carry out PCA and plot the results

```bash
for vcf in $(ls SNP_calling/*filtered.vcf)
do
    echo $vcf
    scripts=/home/adamst/git_repos/scripts/popgen/snp
    out=$(basename $vcf contigs_unmasked_filtered.vcf)
    echo $out
    /home/adamst/prog/R/R-3.2.5/bin/Rscript --vanilla $scripts/pca.R $vcf $out
done
```

#Calculate an NJ tree based on all the SNPs. Outputs a basic diplay of the tree, plus a Newick file to be used for displaying the tree in FigTree and beautifying it.

```bash
cd SNP_calling
for vcf in $(ls *filtered.vcf)
do
    echo $vcf
    scripts=/home/adamst/git_repos/scripts/popgen/snp
    $scripts/nj_tree.sh $vcf 2
done
```

This script isn't happy with the low levels of variation I have.
TODO: Investigate other tree methods - Michelle mentioned some possibilities
