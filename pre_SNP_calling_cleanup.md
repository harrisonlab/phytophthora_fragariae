#Sets up correct formatting for SNP calling analysis

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/analysis/genome_alignment/bowtie
scripts=/home/adamst/git_repos/scripts/popgen
```

## Rename input mapping files in each folder by prefixing with the strain ID

```bash
cd $input/*/A4/vs_Bc16_unmasked_max1200
for filename in 95m_contigs_unmasked.fa_aligned_sorted.bam
do
    mv "$filename" "A4_$filename"
done

cd $input/*/Bc1/vs_Bc16_unmasked_max1200
for filename in 95m_contigs_unmasked.fa_aligned_sorted.bam
do
    mv "$filename" "Bc1_$filename"
done

cd $input/*/Bc16/vs_Bc16_unmasked_max1200
for filename in 95m_contigs_unmasked.fa_aligned_sorted.bam
do
    mv "$filename" "Bc16_$filename"
done

cd $input/*/Bc23/vs_Bc16_unmasked_max1200
for filename in 95m_contigs_unmasked.fa_aligned_sorted.bam
do
    mv "$filename" "Bc23_$filename"
done

cd $input/*/Nov27/vs_Bc16_unmasked_max1200
for filename in 95m_contigs_unmasked.fa_aligned_sorted.bam
do
    mv "$filename" "Nov27_$filename"
done

cd $input/*/Nov5/vs_Bc16_unmasked_max1200
for filename in 95m_contigs_unmasked.fa_aligned_sorted.bam
do
    mv "$filename" "Nov5_$filename"
done

cd $input/*/Nov71/vs_Bc16_unmasked_max1200
for filename in 95m_contigs_unmasked.fa_aligned_sorted.bam
do
    mv "$filename" "Nov71_$filename"
done

cd $input/*/Nov77/vs_Bc16_unmasked_max1200
for filename in 95m_contigs_unmasked.fa_aligned_sorted.bam
do
    mv "$filename" "Nov77_$filename"
done

cd $input/*/Nov9/vs_Bc16_unmasked_max1200
for filename in 95m_contigs_unmasked.fa_aligned_sorted.bam
do
    mv "$filename" "Nov9_$filename"
done

cd $input/*/ONT3/vs_Bc16_unmasked_max1200
for filename in 95m_contigs_unmasked.fa_aligned_sorted.bam
do
    mv "$filename" "ONT3_$filename"
done

cd $input/*/SCRP245_v2/vs_Bc16_unmasked_max1200
for filename in 95m_contigs_unmasked.fa_aligned_sorted.bam
do
    mv "$filename" "SCRP245_v2_$filename"
done

cd $input/*/SCRP249/vs_Bc16_unmasked_max1200
for filename in 95m_contigs_unmasked.fa_aligned_sorted.bam
do
    mv "$filename" "SCRP249_$filename"
done

cd $input/*/SCRP324/vs_Bc16_unmasked_max1200
for filename in 95m_contigs_unmasked.fa_aligned_sorted.bam
do
    mv "$filename" "SCRP324_$filename"
done

cd $input/*/SCRP333/vs_Bc16_unmasked_max1200
for filename in 95m_contigs_unmasked.fa_aligned_sorted.bam
do
    mv "$filename" "SCRP333_$filename"
done
```

## Remove multimapping reads, discordant reads. PCR and optical duplicates, and add read group and sample name to each mapped read (preferably, the shortest ID possible)
Convention used:
qsub $scripts/sub_pre_snp_calling.sh <INPUT SAM FILE> <SAMPLE_ID>

```bash
qsub $scripts/sub_pre_snp_calling.sh $input/125/125_Fus2_canu_contigs_unmasked.fa_aligned.sam FOC125
qsub $scripts/sub_pre_snp_calling.sh $input/55/55_Fus2_canu_contigs_unmasked.fa_aligned.sam FOC55
qsub $scripts/sub_pre_snp_calling.sh $input/A1-2/A1-2_Fus2_canu_contigs_unmasked.fa_aligned.sam FOCA1-2
qsub $scripts/sub_pre_snp_calling.sh $input/A13/A13_Fus2_canu_contigs_unmasked.fa_aligned.sam FOCA13
qsub $scripts/sub_pre_snp_calling.sh $input/A23/A23_Fus2_canu_contigs_unmasked.fa_aligned.sam FOCA23
qsub $scripts/sub_pre_snp_calling.sh $input/A28/A28_Fus2_canu_contigs_unmasked.fa_aligned.sam FOCA28
qsub $scripts/sub_pre_snp_calling.sh $input/CB3/CB3_Fus2_canu_contigs_unmasked.fa_aligned.sam FOCCB3
qsub $scripts/sub_pre_snp_calling.sh $input/D2/D2_Fus2_canu_contigs_unmasked.fa_aligned.sam FOCD2
qsub $scripts/sub_pre_snp_calling.sh $input/Fus2/Fus2_Fus2_canu_contigs_unmasked.fa_aligned.sam FOCFus2
qsub $scripts/sub_pre_snp_calling.sh $input/HB6/HB6_Fus2_canu_contigs_unmasked.fa_aligned.sam FOCHB6
qsub $scripts/sub_pre_snp_calling.sh $input/PG/PG_Fus2_canu_contigs_unmasked.fa_aligned.sam FOCPG
```
