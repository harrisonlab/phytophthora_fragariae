#Aligns P. rubi reads to the BC-16 PacBio sequenced genome for downstream phylogenetic analysis

```bash
Reference=repeat_masked/P.fragariae/Bc16/filtered_contigs_repmask/95m_contigs_unmasked.fa
for StrainPath in $(ls -d /home/groups/harrisonlab/project_files/phytophthora_rubi/qc_dna/paired/P.rubi/*)
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
