#Begins the analysis of the summary stats section from Maria's github

##Copy input for the analysis into a new directory

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats
snpeff=/home/sobczm/bin/snpEff
scripts=/home/adamst/git_repos/scripts/popgen
```

##All individuals

```bash
mkdir -p $input
cp /home/groups/harrisonlab/project_files/phytophthora_fragariae/SNP_calling/95m_contigs_unmasked.vcf $input
cp /home/groups/harrisonlab/project_files/phytophthora_fragariae/SNP_calling/95m_contigs_unmasked_filtered.vcf $input
cp /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/P.fragariae/Bc16/filtered_contigs_repmask/95m_contigs_unmasked.fa $input
cp gene_pred/codingquary/P.fragariae/Bc16/final/final_genes_appended.gff3 $input
cd $input
```

##Create additional subsets of VCF files with reduced number of individuals

```bash
vcftools=/home/sobczm/bin/vcftools/bin
vcflib=/home/sobczm/bin/vcflib/bin
```

##Cutting down vcf to just closely related strains of UK1, 2 and 3
First argument: unfiltered input VCF file with all SNPs
Subsequent arguments: Sample names of individuals to be removed

```bash
$vcflib/vcfremovesamples 95m_contigs_unmasked.vcf SCRP245_v2 Bc23 ONT3 Nov77 >95m_contigs_unmasked_UK123.vcf
```

##Filter the SNPs

```bash
cd SNP_calling/
for vcf in $(ls *_contigs_unmasked_UK123.vcf)
do
    echo $vcf
    script=/home/adamst/git_repos/scripts/popgen/snp/sub_vcf_parser.sh
    qsub $script $vcf
done
```

#Remove monomorphic sites (minor allele count minimum 1). Argument --vcf is the filtered VCF file, and --out is the suffix to be used for the output file.
$vcftools/vcftools --vcf Fus2_canu_contigs_unmasked_noA13_filtered.vcf --mac 1 --recode --out Fus2_canu_contigs_unmasked_noA13_filtered
```

#Only pathogens, without A13
$vcflib/vcfremovesamples Fus2_canu_contigs_unmasked.vcf FOCA13 FOCA1-2 FOCD2 FOCA28 FOCCB3 FOCHB6 FOCPG >Fus2_canu_contigs_unmasked_patho.vcf
$scripts/snp/vcf_parser_haploid.py --i Fus2_canu_contigs_unmasked_patho.vcf
$vcftools/vcftools --vcf Fus2_canu_contigs_unmasked_patho_filtered.vcf --mac 1 --recode --out Fus2_canu_contigs_unmasked_patho_filtered

#Only pathogens, without A13 and 55
$vcflib/vcfremovesamples Fus2_canu_contigs_unmasked.vcf FOCA13 FOCA1-2 FOCD2 FOCA28 FOCCB3 FOCHB6 FOCPG FOC55 >Fus2_canu_contigs_unmasked_patho_no55.vcf
$scripts/snp/vcf_parser_haploid.py --i Fus2_canu_contigs_unmasked_patho_no55.vcf
$vcftools/vcftools --vcf Fus2_canu_contigs_unmasked_patho_no55_filtered.vcf --mac 1 --recode --out Fus2_canu_contigs_unmasked_patho_no55_filtered

#Only non-pathogens, without A13
$vcflib/vcfremovesamples Fus2_canu_contigs_unmasked.vcf FOCA13 FOC55 FOCFus2 FOCA23 FOC125 >Fus2_canu_contigs_unmasked_non-patho.vcf
$scripts/snp/vcf_parser_haploid.py --i Fus2_canu_contigs_unmasked_non-patho.vcf
$vcftools/vcftools --vcf Fus2_canu_contigs_unmasked_non-patho_filtered.vcf --mac 1 --recode --out Fus2_canu_contigs_unmasked_non-patho_filtered

##Create custom SnpEff genome database
$scripts/summary_stats/build_genome_database.sh Fus2_canu_contigs_unmasked.fa Fus2_final_genes_appended.gff3 Fus2

#Annotate VCF files
cd $input
for a in *recode.vcf
do
$scripts/summary_stats/annotate_snps_genome.sh $a Fus2v1.0
done

###Create FASTA alignment files containing only select subsets of SNPs. Required
### for analyses in the fus_popgenome_analysis.sh script.
### From now onwards, analysing the dataset without A13.
cd $input/noA13
ref_genome=/home/sobczm/popgen/summary_stats/Fus2_canu_contigs_unmasked.fa
##all
python $scripts/summary_stats/vcf_to_fasta.py Fus2_canu_contigs_unmasked_noA13_filtered.recode_annotated.vcf $ref_genome 1
#Moving each subset of FASTA files into a separate dir.
mkdir all
mv *.fasta ./all
##coding
python $scripts/summary_stats/vcf_to_fasta.py Fus2_canu_contigs_unmasked_noA13_filtered.recode_annotated_coding.vcf $ref_genome 1
mkdir coding
mv *.fasta ./coding
##silent(four-fold degenerate)
python $scripts/summary_stats/vcf_to_fasta.py Fus2_canu_contigs_unmasked_noA13_filtered.recode_annotated_syn_silent.vcf $ref_genome 1
mkdir silent
mv *.fasta ./silent

###Split the GFF file into one contig --> one GFF file. Required
### for analyses in the fus_popgenome_analysis.sh script.

cd $input
mkdir gff
sh $scripts/summary_stats/split_gff_contigs.sh Fus2_final_genes_appended.gff3
mv *.gff ./gff
