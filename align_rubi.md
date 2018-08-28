# Aligns P. rubi reads to the BC-16 PacBio genome for phylogenetic analysis

```bash
cp -r /home/groups/harrisonlab/project_files/phytophthora_rubi/qc_dna rubi_reads
Reference=repeat_masked/P.fragariae/Bc16/filtered_contigs_repmask/95m_contigs_unmasked.fa
for StrainPath in $(ls -d rubi_reads/paired/P.rubi/*)
do
    Organism=$(echo $StrainPath | rev | cut -f2 -d '/' | rev)
    Strain=$(echo $StrainPath | rev | cut -f1 -d '/' | rev)
    echo "$Organism - $Strain"
    F_Read=$(ls $StrainPath/F/*.fq.gz)
    R_Read=$(ls $StrainPath/R/*.fq.gz)
    echo $F_Read
    echo $R_Read
    OutDir=analysis/genome_alignment/bowtie/$Organism/$Strain/vs_Bc16_unmasked_max1200
    ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/genome_alignment
    qsub $ProgDir/bowtie/sub_bowtie.sh $Reference $F_Read $R_Read $OutDir $Strain
done
```

## After jobs are completed remove rubi reads

```bash
rm -r rubi_reads
```

# Also align BC-16 MiSeq reads back to PacBio assembled genome

```bash
Reference=repeat_masked/P.fragariae/Bc16/filtered_contigs_repmask/95m_contigs_unmasked.fa
for StrainPath in $(ls -d qc_dna/paired/P.fragariae/Bc16)
do
    Organism=$(echo $StrainPath | rev | cut -f2 -d '/' | rev)
    Strain=$(echo $StrainPath | rev | cut -f1 -d '/' | rev)
    echo "$Organism - $Strain"
    F_Read1=$(ls $StrainPath/F/*S1*.gz)
    R_Read1=$(ls $StrainPath/R/*S1*.gz)
    F_Read2=$(ls $StrainPath/F/*S2*.gz)
    R_Read2=$(ls $StrainPath/R/*S2*.gz)
    echo $F_Read1
    echo $R_Read1
    echo $F_Read2
    echo $R_Read2
    OutDir=analysis/genome_alignment/bowtie/$Organism/$Strain/vs_Bc16_unmasked_max1200_SNP
    ProgDir=/home/adamst/git_repos/tools/seq_tools/genome_alignment
    qsub $ProgDir/bowtie/sub_bowtie_2lib.sh $Reference $F_Read1 \
    $R_Read1 $F_Read2 $R_Read2 $OutDir $Strain
done
```
