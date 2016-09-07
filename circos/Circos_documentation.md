In order to examine the genomic structure of Phytophthora fragariae

Alignment of raw MiSeq reads vs the BC-16 genome

Sequence data for isolates with a data from only the MiSeq was aligned against the BC-16 PacBio sequenced genome

single MiSeq run

```bash
Reference=repeat_masked/P.fragariae/Bc16/filtered_contigs_repmask/95m_contigs_unmasked.fa
for StrainPath in $(ls -d qc_dna/paired/P.fragariae/* | grep -v '62471' | grep -v 'Bc16' | grep -v 'Nov71' | grep -v 'Bc1' | grep -v 'Nov9')
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

two MiSeq runs

```bash
Reference=repeat_masked/P.fragariae/Bc16/filtered_contigs_repmask/95m_contigs_unmasked.fa
for StrainPath in $(ls -d qc_dna/paired/P.*/* | grep -v '62471' | grep -v 'Bc16' | grep -v 'SCRP245_v2' | grep -v 'ONT3' | grep -v 'A4' | grep -v 'Bc23' | grep -v 'Nov27' | grep -v 'Nov5' | grep -v 'Nov77' | grep -v 'Bc1' | grep -v 'Nov9')
do
    echo $StrainPath
    Strain=$(echo $StrainPath | rev | cut -f1 -d '/' | rev)
    Organism=$(echo $StrainPath | rev | cut -f2 -d '/' | rev)
    echo "$Organism - $Strain"
    F1_Read=$(ls $StrainPath/F/*_trim.fq.gz | head -n1 | tail -n1)
    R1_Read=$(ls $StrainPath/R/*_trim.fq.gz | head -n1 | tail -n1)
    F2_Read=$(ls $StrainPath/F/*_trim.fq.gz | head -n2 | tail -n1)
    R2_Read=$(ls $StrainPath/R/*_trim.fq.gz | head -n2 | tail -n1)
    echo $F1_Read
    echo $R1_Read
    echo $F2_Read
    echo $R2_Read
    OutDir=analysis/genome_alignment/bowtie/$Organism/$Strain/vs_Bc16_unmasked_max1200
    ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/genome_alignment
    qsub $ProgDir/bowtie/sub_bowtie_2lib.sh $Reference $F1_Read $R1_Read $F2_Read $R2_Read $OutDir $Strain
done
```

for three MiSeq reads

```bash
Reference=repeat_masked/P.fragariae/Bc16/filtered_contigs_repmask/95m_contigs_unmasked.fa
for StrainPath in $(ls -d qc_dna/paired/P.*/* | grep -v '62471' | grep -v 'Bc16' | grep -v 'SCRP245_v2' | grep -v 'ONT3' | grep -v 'A4' | grep -v 'Bc23' | grep -v 'Nov27' | grep -v 'Nov5' | grep -v 'Nov77' | grep -v 'Nov71')
do
    echo $StrainPath
    Strain=$(echo $StrainPath | rev | cut -f1 -d '/' | rev)
    Organism=$(echo $StrainPath | rev | cut -f2 -d '/' | rev)
    echo "$Organism - $Strain"
    F1_Read=$(ls $StrainPath/F/*_trim.fq.gz | head -n1 | tail -n1)
    R1_Read=$(ls $StrainPath/R/*_trim.fq.gz | head -n1 | tail -n1)
    F2_Read=$(ls $StrainPath/F/*_trim.fq.gz | head -n2 | tail -n1)
    R2_Read=$(ls $StrainPath/R/*_trim.fq.gz | head -n2 | tail -n1)
    F3_Read=$(ls $StrainPath/F/*_trim.fq.gz | head -n3 | tail -n1)
    R3_Read=$(ls $StrainPath/R/*_trim.fq.gz | head -n3 | tail -n1)
    echo $F1_Read
    echo $R1_Read
    echo $F2_Read
    echo $R2_Read
    echo $F3_Read
    echo $R3_Read
    OutDir=analysis/genome_alignment/bowtie/$Organism/$Strain/vs_Bc16_unmasked_max1200
    ProgDir=/home/adamst/git_repos/tools/seq_tools/genome_alignment
    qsub $ProgDir/bowtie/sub_bowtie_3lib.sh $Reference $F1_Read $R1_Read $F2_Read $R2_Read $F3_Read $R3_Read $OutDir $Strain
done
```

100 Kb windows of the genome created as gff features over which coverage can be plotted

```bash
ProgDir=/home/armita/git_repos/emr_repos/scripts/fusarium/pathogen/identify_LS_chromosomes/circos
Genome=assembly/merged_canu_spades/P.fragariae/Bc16/95m/filtered_contigs/Bc16_contigs_renamed.fasta
OutDir=circos
mkdir -p $OutDir
$ProgDir/fasta2gff_windows.py --genome $Genome > $OutDir/100kb_windows.gff
```

Extract read coverage within every 100 kb window

```bash
for AlignDir in $(ls -d analysis/genome_alignment/bowtie/*/*/vs_Bc16_unmasked_max1200)
do
    AlignedReads=$AlignDir/95m_contigs_unmasked.fa_aligned_sorted.bam
    Gff=circos/100kb_windows.gff
    bedtools coverage -abam $AlignedReads -b $Gff > $AlignDir/coverage_over_100kb_windows.bed
    echo finished
done
```

Convert the output .bed file into circos plot format

```bash
for AlignDir in $(ls -d analysis/genome_alignment/bowtie/*/*/vs_Bc16_unmasked_max1200)
do
ProgDir=/home/armita/git_repos/emr_repos/scripts/fusarium/pathogen/identify_LS_chromosomes/circos
BedFile=$AlignDir/coverage_over_100kb_windows.bed
```
