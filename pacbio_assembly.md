##Data extraction

for P. fragariae data:

```bash
cd /home/groups/harrisonlab/project_files/phytophthora_fragariae
RawDatDir=/home/harrir/projects/pacbio_test/p_frag
mkdir -p raw_dna/pacbio/P.fragariae/Bc16
cp -r $RawDatDir/C07_1 raw_dna/pacbio/P.fragariae/Bc16/.
cp -r $RawDatDir/D07_1 raw_dna/pacbio/P.fragariae/Bc16/.
cp -r $RawDatDir/E07_1 raw_dna/pacbio/P.fragariae/Bc16/.
cp -r $RawDatDir/F07_1 raw_dna/pacbio/P.fragariae/Bc16/.
OutDir=raw_dna/pacbio/P.fragariae/Bc16/extracted
mkdir -p $OutDir
cat raw_dna/pacbio/P.fragariae/Bc16/*/Analysis_Results/*.subreads.fastq > $OutDir/concatenated_pacbio.fastq
```

#Canu Assembly

Canu assembly - ran both at genome size of 65m and 95m

```bash
Reads=$(ls raw_dna/pacbio/*/*/extracted/concatenated_pacbio.fastq)
GenomeSz="95m"
Strain=$(echo $Reads | rev | cut -f3 -d '/' | rev)
Organism=$(echo $Reads | rev | cut -f4 -d '/' | rev)
Prefix="$Strain"_canu
OutDir="assembly/canu/$Organism/$Strain/95m"
ProgDir=~/git_repos/tools/seq_tools/assemblers/canu
qsub $ProgDir/submit_canu.sh $Reads $GenomeSz $Prefix $OutDir
```

Assemblies were polished using Pilon

First, concatenate trimmed reads as have data from two runs of the same library

```bash
IlluminaDirF=qc_dna/paired/P.fragariae/Bc16/F
IlluminaDirR=qc_dna/paired/P.fragariae/Bc16/R
mkdir -p $IlluminaDirF/concatenated
mkdir -p $IlluminaDirR/concatenated
ConcatenatedF=$IlluminaDirF/concatenated/Bc16_cat_F.fq
ConcatenatedR=$IlluminaDirR/concatenated/Bc16_cat_R.fq
cat $IlluminaDirF/Bc16_S1_L001_R1_001_trim.fq.gz > $ConcatenatedF
cat $IlluminaDirF/Bc16_S2_L001_R1_001_160129_trim.fq.gz >> $ConcatenatedF
cat $IlluminaDirR/Bc16_S1_L001_R2_001_trim.fq.gz > $ConcatenatedR
cat $IlluminaDirR/Bc16_S2_L001_R2_001_160129_trim.fq.gz >> $ConcatenatedR
```

Run pilon

```bash
Assembly=assembly/canu/P.fragariae/Bc16/95m/Bc16_canu.contigs.fasta
Organism=P.fragariae
Strain=Bc16
IlluminaDirF=qc_dna/paired/P.fragariae/Bc16/F
IlluminaDirR=qc_dna/paired/P.fragariae/Bc16/R
TrimF1_Read=$IlluminaDirF/concatenated/Bc16_cat_F.fq
TrimR1_Read=$IlluminaDirR/concatenated/Bc16_cat_R.fq
OutDir=assembly/canu/$Organism/$Strain/95m/polished/
ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/pilon
qsub $ProgDir/sub_pilon.sh $Assembly $TrimF1_Read $TrimR1_Read $OutDir
```

#Spades Assembly

```bash
for PacBioDat in $(ls raw_dna/pacbio/*/*/extracted/concatenated_pacbio.fastq)
do
    Organism=$(echo $PacBioDat | rev | cut -f4 -d '/' | rev)
    Strain=$(echo $PacBioDat | rev | cut -f3 -d '/' | rev)
    IlluminaDir=$(ls -d qc_dna/paired/$Organism/$Strain)
    TrimF1_Read=$(ls $IlluminaDir/F/Bc16_S1_L001_R1_001_trim.fq.gz)
    TrimR1_Read=$(ls $IlluminaDir/R/Bc16_S1_L001_R2_001_trim.fq.gz)
    TrimF2_Read=$(ls $IlluminaDir/F/Bc16_S2_L001_R1_001_160129_trim.fq.gz)
    TrimR2_Read=$(ls $IlluminaDir/R/Bc16_S2_L001_R2_001_160129_trim.fq.gz)
    OutDir=assembly/spades_pacbio/$Organism/"$Strain"
    echo $TrimR1_Read
    echo $TrimR1_Read
    echo $TrimF2_Read
    echo $TrimR2_Read
    ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/assemblers/spades/multiple_libraries
    qsub $ProgDir/subSpades_2lib_pacbio.sh $PacBioDat $TrimF1_Read $TrimR1_Read $TrimF2_Read $TrimR2_Read $OutDir 50
done
```

#Filter out contigs < 500bp

```bash
Contigs=assembly/spades_pacbio/P.fragariae/Bc16/contigs.fasta
AssemblyDir=$(dirname $Contigs)
mkdir $AssemblyDir/filtered_contigs
FilterDir=/home/armita/git_repos/emr_repos/tools/seq_tools/assemblers/abyss
$FilterDir/filter_abyss_contigs.py $Contigs 500 > $AssemblyDir/filtered_contigs/contigs_min_500bp.fasta
```

#QUAST

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/quast
Assembly=assembly/spades_pacbio/P.fragariae/Bc16/filtered_contigs/contigs_min_500bp.fasta
Strain=Bc16
Organism=P.fragariae
OutDir=assembly/spades_pacbio/$Organism/$Strain/filtered_contigs
qsub $ProgDir/sub_quast.sh $Assembly $OutDir
```

**N50:46270
L50:414
Number of contigs:4941**
