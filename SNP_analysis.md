#Runs commands from Maria to analyse output from SNP calling

#Create a cut-down vcf that only includes *P.fragariae* strains

```bash
vcftools=/home/sobczm/bin/vcftools/bin
vcflib=/home/sobczm/bin/vcflib/bin
```

#All, without A13
#First argument: unfiltered input VCF file with all SNPs
#Subsequent arguments: Sample names of individuals to be removed
$vcflib/vcfremovesamples Fus2_canu_contigs_unmasked.vcf FOCA13 >Fus2_canu_contigs_unmasked_noA13.vcf
#Filter the SNPs
$scripts/snp/vcf_parser_haploid.py --i Fus2_canu_contigs_unmasked_noA13.vcf
#Remove monomorphic sites (minor allele count minimum 1). Argument --vcf is the filtered VCF file, and --out is the suffix to be used for the output file.
$vcftools/vcftools --vcf Fus2_canu_contigs_unmasked_noA13_filtered.vcf --mac 1 --recode --out Fus2_canu_contigs_unmasked_noA13_filtered

#Only pathogens, without A13
$vcflib/vcfremovesamples Fus2_canu_contigs_unmasked.vcf FOCA13 FOCA1-2 FOCD2 FOCA28 FOCCB3 FOCHB6 FOCPG >Fus2_canu_contigs_unmasked_patho.vcf
$scripts/snp/vcf_parser_haploid.py --i Fus2_canu_contigs_unmasked_patho.vcf
$vcftools/vcftools --vcf Fus2_canu_contigs_unmasked_patho_filtered.vcf --mac 1 --recode --out Fus2_canu_contigs_unmasked_patho_filtered

#Filter inital vcf output, only retain biallelic high-quality SNPS with no missing data for genetic analyses.

```bash
vcf=SNP_calling/95m_contigs_unmasked.vcf
script=/home/adamst/git_repos/scripts/popgen/snp/sub_vcf_parser.sh
qsub $script $vcf
```

#General VCF stats (remember that vcftools needs to have the PERL library exported)

```bash
perl /home/sobczm/bin/vcftools/bin/vcf-stats \
SNP_calling/95m_contigs_unmasked.vcf >95m_contigs_unmasked.stat
perl /home/sobczm/bin/vcftools/bin/vcf-stats \
95m_contigs_unmasked_filtered.vcf >95m_contigs_unmasked_filtered.stat
```

#Calculate the index for percentage of shared SNP alleles between the individs.
$scripts/similarity_percentage.py Fus2_canu_contigs_unmasked_filtered.vcf
#Visualise the output as heatmap and clustering dendrogram
Rscript --vanilla $scripts/distance_matrix.R Fus2_canu_contigs_unmasked_filtered_distance.log
#Carry out PCA and plot the results
Rscript --vanilla $scripts/pca.R Fus2_canu_contigs_unmasked_filtered.vcf
#Calculate an NJ tree based on all the SNPs. Outputs a basic diplay of the tree, plus a Newick file to be used
#for displaying the tree in FigTree and beautifying it.
$scripts/nj_tree.sh Fus2_canu_contigs_unmasked_filtered.vcf