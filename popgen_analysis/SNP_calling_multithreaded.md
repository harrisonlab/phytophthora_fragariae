# Runs a SNP calling script from Maria in order to be able to draw up a phylogeny
To change in each analysis:

```bash
input=repeat_masked/quiver_results/polished/filtered_contigs_repmask
reference=repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa

filename=$(basename "$reference")
output="${filename%.*}.dict"
```

## Prepare genome reference indexes required by GATK

```bash
java -jar /home/sobczm/bin/picard-tools-2.5.0/picard.jar CreateSequenceDictionary R=$reference O=$input/$output
samtools faidx $reference
```

### Copy index file to same folder as BAM alignments

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov5 Nov27 Nov71 Nov77 Nov9 ONT3 SCRP245_v2 SCRP249 SCRP324 SCRP333
do
    Index=repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa.fai
    Directory=analysis/genome_alignment/bowtie/*/$Strain/vs_Bc16_FALCON/
    cp $Index $Directory
done
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
scripts=/home/adamst/git_repos/scripts/phytophthora_fragariae/popgen_analysis
qsub $scripts/sub_SNP_calling_multithreaded.sh
```
