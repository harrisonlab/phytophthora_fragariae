#Runs commands from Maria to analyse output from SNP calling

#Create a cut-down vcf that only includes *P. fragariae* strains

```bash
vcftools=/home/sobczm/bin/vcftools/bin
vcflib=/home/sobczm/bin/vcflib/bin
```

##Just *P. fragariae* strains
First argument: unfiltered input VCF file with all SNPs
Subsequent arguments: Sample names of individuals to be removed

```bash
$vcflib/vcfremovesamples 95m_contigs_unmasked.vcf SCRP249 SCRP324 SCRP333 >Pfrag_only_95m_contigs_unmasked.vcf
```

#Filter vcf outputs, only retain biallelic high-quality SNPS with no missing data for genetic analyses.

```bash
for vcf in $(ls SNP_calling/*_contigs_unmasked.vcf)
do
	echo $vcf
	script=/home/adamst/git_repos/scripts/popgen/snp/sub_vcf_parser.sh
	qsub $script $vcf
done
```

#General VCF stats (remember that vcftools needs to have the PERL library exported)

```bash
perl /home/sobczm/bin/vcftools/bin/vcf-stats \
SNP_calling/95m_contigs_unmasked.vcf >SNP_calling/95m_contigs_unmasked.stat
perl /home/sobczm/bin/vcftools/bin/vcf-stats \
SNP_calling/95m_contigs_unmasked_filtered.vcf >SNP_calling/95m_contigs_unmasked_filtered.stat

perl /home/sobczm/bin/vcftools/bin/vcf-stats \
SNP_calling/Pfrag_only_95m_contigs_unmasked.vcf >SNP_calling/Pfrag_only_95m_contigs_unmasked.stat
perl /home/sobczm/bin/vcftools/bin/vcf-stats \
SNP_calling/Pfrag_only_95m_contigs_unmasked_filtered.vcf >SNP_calling/Pfrag_only_95m_contigs_unmasked_filtered.stat
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