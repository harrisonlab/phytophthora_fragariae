#$ -S /bin/bash
#$ -cwd
#$ -pe smp 6
#$ -l h_vmem=4G
#$ -l h=blacklace01.blacklace|blacklace02.blacklace|blacklace04.blacklace|blacklace05.blacklace|blacklace06.blacklace|blacklace07.blacklace|blacklace08.blacklace|blacklace09.blacklace|blacklace10.blacklace|blacklace12.blacklace

# Testing parallelisation of GATk HaplotypeCaller - may crash. (It did not! Resulted in 2x speedup)
# NOTE: this is a haploid organism. For diploid organism, change "ploidy" argument to 2.
# Changes required in the script:
# VARIABLES
# Reference - the genome reference used in read mapping.
# INSIDE THE GATK command:
# To specify which BAM mapping files (output from pre_SNP_calling_cleanup.sh, filename ending with "_rg" -> that is, with
# read group added) are to be used in SNP calling, use the -I argument with full path to each file following after that.
# Each new BAM file has to be specified after a separate -I

input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/analysis/genome_alignment/bowtie
reference=/home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa

filename=$(basename "$reference")
output="${filename%.*}_temp.vcf"
output2="${filename%.*}.vcf"

gatk=/home/sobczm/bin/GenomeAnalysisTK-3.6

java -jar $gatk/GenomeAnalysisTK.jar \
     -R $reference \
     -T HaplotypeCaller \
     -ploidy 2 \
     -nct 6 \
     --allow_potentially_misencoded_quality_scores \
     -I $input/*/A4/*/A4_polished_contigs_unmasked.fa_aligned_nomulti_proper_sorted_nodup_rg.bam \
     -I $input/*/Bc1/*/Bc1_polished_contigs_unmasked.fa_aligned_nomulti_proper_sorted_nodup_rg.bam \
     -I $input/*/Bc16/*/Bc16_polished_contigs_unmasked.fa_aligned_nomulti_proper_sorted_nodup_rg.bam \
     -I $input/*/Bc23/*/Bc23_polished_contigs_unmasked.fa_aligned_nomulti_proper_sorted_nodup_rg.bam \
     -I $input/*/Nov27/*/Nov27_polished_contigs_unmasked.fa_aligned_nomulti_proper_sorted_nodup_rg.bam \
     -I $input/*/Nov5/*/Nov5_polished_contigs_unmasked.fa_aligned_nomulti_proper_sorted_nodup_rg.bam \
     -I $input/*/Nov71/*/Nov71_polished_contigs_unmasked.fa_aligned_nomulti_proper_sorted_nodup_rg.bam \
     -I $input/*/Nov77/*/Nov77_polished_contigs_unmasked.fa_aligned_nomulti_proper_sorted_nodup_rg.bam \
     -I $input/*/Nov9/*/Nov9_polished_contigs_unmasked.fa_aligned_nomulti_proper_sorted_nodup_rg.bam \
     -I $input/*/ONT3/*/ONT3_polished_contigs_unmasked.fa_aligned_nomulti_proper_sorted_nodup_rg.bam \
     -I $input/*/SCRP245_v2/*/SCRP245_v2_polished_contigs_unmasked.fa_aligned_nomulti_proper_sorted_nodup_rg.bam \
     -I $input/*/SCRP249/*/SCRP249_polished_contigs_unmasked.fa_aligned_nomulti_proper_sorted_nodup_rg.bam \
     -I $input/*/SCRP324/*/SCRP324_polished_contigs_unmasked.fa_aligned_nomulti_proper_sorted_nodup_rg.bam \
     -I $input/*/SCRP333/*/SCRP333_polished_contigs_unmasked.fa_aligned_nomulti_proper_sorted_nodup_rg.bam \
     -o $output

#Break down complex SNPs into primitive ones with VariantsToAllelicPrimitives
#This tool will take an MNP (e.g. ACCCA -> TCCCG) and break it up into separate records for each component part (A-T and A->G).
#This tool modifies only bi-allelic variants.

java -jar $gatk/GenomeAnalysisTK.jar \
   -T VariantsToAllelicPrimitives \
   -R $reference \
   -V $output \
   -o $output2 \


#####################################
# Notes on GATK parallelisation
#####################################
# http://gatkforums.broadinstitute.org/gatk/discussion/1975/how-can-i-use-parallelism-to-make-gatk-tools-run-faster
