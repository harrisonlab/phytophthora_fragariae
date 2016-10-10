#Runs a SNP calling script from Maria in order to be able to draw up a phylogeny
To change in each analysis:

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/analysis/genome_alignment/bowtie
reference=repeat_masked/P.fragariae/Bc16/filtered_contigs_repmask/95m_contigs_unmasked.fa

filename=$(basename "$reference")
output="${filename%.*}.dict"
```

##Prepare genome reference indexes required by GATK

```bash
java -jar /home/sobczm/bin/picard-tools-2.5.0/picard.jar CreateSequenceDictionary R=$reference O=$input/$output
samtools faidx $reference
```

##Move to the directory where the output of SNP calling should be placed

```bash
mkdir -p /home/groups/harrisonlab/project_files/phytophthora_fragariae/SNP_calling
cd /home/groups/harrisonlab/project_files/phytophthora_fragariae/SNP_calling
```

##Start SNP calling with GATK
The submission script required need to be custom-prepared for each analysis, depending on what samples are being analysed.
See inside the submission script below:

```bash
scripts=/home/adamst/git_repos/scripts/phytophthora_fragariae
qsub $scripts/sub_SNP_calling_multithreaded.sh
```
