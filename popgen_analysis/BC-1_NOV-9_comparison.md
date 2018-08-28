# Create a cut-down vcf that only includes BC-1 and NOV-9, commands run from phytophthora_fragariae/SNP_calling

```bash
vcftools=/home/sobczm/bin/vcftools/bin
vcflib=/home/sobczm/bin/vcflib/bin
```

### Just BC-1 and NOV-9
First argument: unfiltered input VCF file with all SNPs
Subsequent arguments: Sample names of individuals to be removed

```bash
cd SNP_calling
$vcflib/vcfremovesamples polished_contigs_unmasked.vcf Nov71 Nov5 Nov27 A4 Bc16 SCRP245_v2 Bc23 ONT3 Nov77 SCRP249 SCRP324 SCRP333 > BC1_NOV9_only_polished_contigs_unmasked.vcf
```

## Filter vcf outputs, only retain biallelic high-quality SNPS with no missing data for genetic analyses.

```bash
for vcf in $(ls *_contigs_unmasked.vcf | grep -e "BC1")
do
    echo $vcf
    script=/home/adamst/git_repos/scripts/popgen/snp/sub_vcf_parser.sh
    qsub $script $vcf
done
```

#General VCF stats (remember that vcftools needs to have the PERL library exported)

```bash
perl /home/sobczm/bin/vcftools/bin/vcf-stats \
BC1_NOV9_only_polished_contigs_unmasked.vcf > BC1_NOV9_only_polished_contigs_unmasked.stat
perl /home/sobczm/bin/vcftools/bin/vcf-stats \
BC1_NOV9_only_polished_contigs_unmasked_filtered.vcf > BC1_NOV9_only_polished_contigs_unmasked_filtered.stat
```

#Calculate the index for percentage of shared SNP alleles between the individuals.

```bash
for vcf in $(ls *_filtered.vcf | grep -e "BC1")
do
    scripts=/home/adamst/git_repos/scripts/popgen/snp
    $scripts/similarity_percentage.py $vcf
done
```

#Remove monomorphic sites (minor allele count minimum 1). Argument --vcf is the filtered VCF file, and --out is the suffix to be used for the output file.

```bash
for vcf in $(ls *_filtered.vcf | grep -e "BC1")
do
    echo $vcf
    out=$(basename $vcf .vcf)
    echo $out
    $vcftools/vcftools --vcf $vcf --mac 1 --recode --out $out
done
```

<!-- #Create custom SnpEff genome database

```bash
snpeff=/home/sobczm/bin/snpEff
nano $snpeff/snpEff.config
```

##Add the following lines to the section with databases:

```
#---
# EMR Databases
#----
# Fus2 genome
Fus2v1.0.genome : Fus2
# Bc16 genome
Bc16v1.0.genome: BC-16
```

#Collect input files

```bash
mkdir $snpeff/data/Bc16v1.0
cp repeat_masked/P.fragariae/Bc16/filtered_contigs_repmask/95m_contigs_unmasked.fa $snpeff/data/Bc16v1.0
cp gene_pred/codingquary/P.fragariae/Bc16/final/final_genes_appended.gff3 $snpeff/data/Bc16v1.0
```

#Rename input files

```bash
cd $snpeff/data/Bc16v1.0
mv final_genes_appended.gff3 genes.gff
mv 95m_contigs_unmasked.fa sequences.fa
```

#Build database using GFF3 annotation

```bash
java -jar $snpeff/snpEff.jar build -gff3 -v Bc16v1.0
``` -->

#Annotate VCF files

```bash
snpeff=/home/adamst/prog/snpEff
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/SNP_calling
cd $input
for a in *recode.vcf
do
    echo $a
    filename=$(basename "$a")
    java -Xmx4g -jar $snpeff/snpEff.jar -v -ud 0 Bc16v1.0 $a > ${filename%.vcf}_annotated.vcf
    mv snpEff_genes.txt snpEff_genes_${filename%.vcf}.txt
    mv snpEff_summary.html  snpEff_summary__${filename%.vcf}.html
done
```

#Visualise the output as heatmap and clustering dendrogram

```bash
for log in $(ls *distance.log | grep -e "BC1")
do
    scripts=/home/adamst/git_repos/scripts/popgen/snp
    Rscript --vanilla $scripts/distance_matrix.R $log
done
```

#Carry out PCA and plot the results

```bash
for vcf in $(ls *filtered.vcf | grep -e "BC1")
do
    echo $vcf
    scripts=/home/adamst/git_repos/scripts/popgen/snp
    out=$(basename $vcf contigs_unmasked_filtered.vcf)
    echo $out
    Rscript --vanilla $scripts/pca.R $vcf $out
done
```

#Calculate an NJ tree based on all the SNPs. Outputs a basic diplay of the tree, plus a Newick file to be used for displaying the tree in FigTree and beautifying it.

```bash
for vcf in $(ls *filtered.vcf | grep -e "BC1")
do
    echo $vcf
    scripts=/home/adamst/git_repos/scripts/popgen/snp
    $scripts/nj_tree.sh $vcf
done
```
