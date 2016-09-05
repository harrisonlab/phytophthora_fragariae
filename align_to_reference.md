Alignment of raw MiSeq reads vs the BC-16 genome

Sequence data for isolates with a data from only the MiSeq was aligned against the BC-16 PacBio sequenced genome

```bash
Reference=repeat_masked/P.fragariae/Bc16/filtered_contigs_repmask/95m_contigs_unmasked.fa
for StrainPath in $(ls -d qc_dna/paired/P.fragariae/* | grep -v '62471' | grep -v 'Bc16')
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

Sequence data for isolates with a data from two sequencing runs was aligned against the Fus2 genome

Reference=$(ls repeat_masked/*/*/*/*_contigs_unmasked.fa | grep -w 'Fus2_canu_new')
for StrainPath in $(ls -d qc_dna/paired/F.*/* | grep -e 'HB6' -e 'Fus2'); do
echo $StrainPath
Strain=$(echo $StrainPath | rev | cut -f1 -d '/' | rev)
Organism=$(echo $StrainPath | rev | cut -f2 -d '/' | rev)
echo "$Organism - $Strain"
F1_Read=$(ls $StrainPath/F/*_trim.fq.gz | head -n1 | tail -n1);
R1_Read=$(ls $StrainPath/R/*_trim.fq.gz | head -n1 | tail -n1);
F2_Read=$(ls $StrainPath/F/*_trim.fq.gz | head -n2 | tail -n1);
R2_Read=$(ls $StrainPath/R/*_trim.fq.gz | head -n2 | tail -n1);
echo $F1_Read
echo $R1_Read
echo $F2_Read
echo $R2_Read
OutDir=analysis/genome_alignment/bowtie/$Organism/$Strain/vs_Fus2_unmasked_max1200
ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/genome_alignment
qsub $ProgDir/bowtie/sub_bowtie_2lib.sh $Reference $F1_Read $R1_Read $F2_Read $R2_Read $OutDir $Strain
done
