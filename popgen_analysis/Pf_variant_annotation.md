# Begins the analysis of the summary stats section from Maria's github

## Copy input for the analysis into a new directory

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats
snpeff=/home/adamst/prog/snpEff
scripts=/home/adamst/git_repos/scripts/popgen
```

## All individuals

```bash
mkdir -p $input
cp /home/groups/harrisonlab/project_files/phytophthora_fragariae/SNP_calling/polished_contigs_unmasked.vcf $input
cp /home/groups/harrisonlab/project_files/phytophthora_fragariae/SNP_calling/polished_contigs_unmasked_filtered.vcf $input
cp /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa $input
cp gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors_renamed.gff3 $input
cd $input
```

## Create additional subsets of VCF files with reduced number of individuals

```bash
vcftools=/home/sobczm/bin/vcftools/bin
vcflib=/home/sobczm/bin/vcflib/bin
```

## Cutting down vcf to just closely related strains of UK1,2,3 population

First argument: unfiltered input VCF file with all SNPs
Subsequent arguments: Sample names of individuals to be removed

```bash
$vcflib/vcfremovesamples polished_contigs_unmasked.vcf SCRP245_v2 Nov77 SCRP249 SCRP324 SCRP333 > polished_contigs_unmasked_two_pops.vcf
```

##Filter the SNPs

```bash
for vcf in $(ls polished_contigs_unmasked_two_pops.vcf)
do
    echo $vcf
    script=/home/adamst/git_repos/scripts/popgen/snp/sub_vcf_parser.sh
    qsub $script $vcf
done
```

vcf parser can only be run one at a time

##Remove monomorphic sites (minor allele count minimum 1). Argument --vcf is the filtered VCF file, and --out is the suffix to be used for the output file.

```bash
$vcftools/vcftools --vcf polished_contigs_unmasked_filtered.vcf --mac 1 --recode --out polished_contigs_unmasked_filtered
$vcftools/vcftools --vcf polished_contigs_unmasked_two_pops_filtered.vcf --mac 1 --recode --out polished_contigs_unmasked_two_pops_filtered
```

##Create custom SnpEff genome database

```bash
$scripts/summary_stats/build_genome_database.sh polished_contigs_unmasked.fa Bc16_genes_incl_ORFeffectors_renamed.gff3 Bc16
```

##Annotate VCF files

```bash
cd $input
for a in polished_contigs_unmasked_filtered.recode.vcf polished_contigs_unmasked_two_pops_filtered.recode.vcf
do
    $scripts/summary_stats/annotate_snps_genome.sh $a Bc16
done
```

##Create FASTA alignment files containing only select subsets of SNPs. Required for analyses in Pf_popgenome_analysis.md. From now onwards, analysing only UK123.

```bash
cd $input
ref_genome=$input/polished_contigs_unmasked.fa
```

###all

```bash
python $scripts/summary_stats/vcf_to_fasta.py polished_contigs_unmasked_UK123_filtered.recode_annotated.vcf $ref_genome 2
```

###Moving each subset of FASTA files into a separate dir.

```bash
mkdir all
mv *.fasta ./all
```

##coding

```bash
python $scripts/summary_stats/vcf_to_fasta.py polished_contigs_unmasked_UK123_filtered.recode_coding.vcf $ref_genome 2
mkdir coding
mv *.fasta ./coding
```

##silent(four-fold degenerate)

```bash
python $scripts/summary_stats/vcf_to_fasta.py polished_contigs_unmasked_UK123_filtered.recode_syn_4fd.vcf $ref_genome 2
mkdir silent
mv *.fasta ./silent
```

###Split the GFF file into one contig --> one GFF file. Required for analyses in Pf_popgenome_analysis.md

```bash
cd $input
mkdir -p gff
$scripts/summary_stats/split_gff_contig.sh Bc16_genes_incl_ORFeffectors_renamed.gff3
mv *.gff ./gff
```

##Create FASTA alignment files containing only select subsets of SNPs. Required for analyses in Pf_popgenome_analysis.md From now onwards, analysing only Pf.

```bash
cd $input
ref_genome=$input/polished_contigs_unmasked.fa
```

###all

```bash
python $scripts/summary_stats/vcf_to_fasta.py polished_contigs_unmasked_Pf_filtered.recode_annotated.vcf $ref_genome 2
```

###Moving each subset of FASTA files into a separate dir.

```bash
mkdir all_Pf
mv *.fasta ./all_Pf
```

##coding

```bash
python $scripts/summary_stats/vcf_to_fasta.py polished_contigs_unmasked_Pf_filtered.recode_coding.vcf $ref_genome 2
mkdir coding_Pf
mv *.fasta ./coding_Pf
```

##silent(four-fold degenerate)

```bash
python $scripts/summary_stats/vcf_to_fasta.py polished_contigs_unmasked_Pf_filtered.recode_syn_4fd.vcf $ref_genome 2
mkdir silent_Pf
mv *.fasta ./silent_Pf
```
