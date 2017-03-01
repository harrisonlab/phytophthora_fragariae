#Data extraction

for first set of P. fragariae data:

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
for code in C07_1 D07_1 E07_1 F07_1
do
    cat raw_dna/pacbio/P.fragariae/Bc16/$code/Analysis_Results/*.subreads.fastq > $OutDir/concatenated_pacbio_1.fastq
done
```

for second set of *P. fragariae* data:

```bash
cd /home/groups/harrisonlab/project_files/phytophthora_fragariae
RawDatDir=/home/groups/harrisonlab/raw_data/raw_seq/pacbio/
cp -r $RawDatDir/Richard_Harrison_NEMR.RH.ENQ-933.C.02_extra_coverage.tar.gz raw_dna/pacbio/P.fragariae/Bc16/.
cd raw_dna/pacbio/P.fragariae/Bc16/
gunzip Richard_Harrison_NEMR.RH.ENQ-933.C.02_extra_coverage.tar.gz
cp -r Richard_Harrison_NEMR.RH.ENQ-933.C.02_extra_coverage/*_1 .
rm -r Richard_Harrison_NEMR.RH.ENQ-933.C.02_extra_coverage
OutDir=extracted
mkdir -p $OutDir
for code in A04_1 E02_1 F02_1 G02_1 G03_1 H03_1
do
cat $code/Analysis_Results/*.subreads.fastq > $OutDir/concatenated_pacbio_2.fastq
done
```

#Canu Assembly

Canu assembly - ran at genome size of 95m

```bash
cd /home/groups/harrisonlab/project_files/phytophthora_fragariae
Reads1=$(ls raw_dna/pacbio/*/*/extracted/concatenated_pacbio_1.fastq)
Reads2=$(ls raw_dna/pacbio/*/*/extracted/concatenated_pacbio_2.fastq)
GenomeSz="95m"
Strain=$(echo $Reads | rev | cut -f3 -d '/' | rev)
Organism=$(echo $Reads | rev | cut -f4 -d '/' | rev)
Prefix="$Strain"_canu
OutDir="assembly/canu/$Organism/$Strain"
ProgDir=~/git_repos/tools/seq_tools/assemblers/canu
qsub $ProgDir/submit_canu_2lib.sh $Reads1 $Reads2 $GenomeSz $Prefix $OutDir
```

#Assemblies were polished using Pilon

```bash
Assembly=assembly/canu/P.fragariae/Bc16/Bc16_canu.contigs.fasta
Organism=P.fragariae
Strain=Bc16
IlluminaDirF=qc_dna/paired/P.fragariae/Bc16/F
IlluminaDirR=qc_dna/paired/P.fragariae/Bc16/R
TrimF1_Read=$IlluminaDirF/Bc16_S1_L001_R1_001_trim.fq.gz
TrimR1_Read=$IlluminaDirR/Bc16_S1_L001_R2_001_trim.fq.gz
TrimF2_Read=$IlluminaDirF/Bc16_S2_L001_R1_001_160129_trim.fq.gz
TrimR2_Read=$IlluminaDirR/Bc16_S2_L001_R2_001_160129_trim.fq.gz
OutDir=assembly/canu/$Organism/$Strain/polished
ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/pilon
qsub $ProgDir/sub_pilon_2_libs.sh $Assembly $TrimF1_Read $TrimR1_Read $TrimF2_Read $TrimR2_Read $OutDir
```

#Spades Assembly

```bash
for PacBioDat1 in $(ls raw_dna/pacbio/*/*/extracted/concatenated_pacbio_1.fastq)
do
    PacBioDat2=raw_dna/pacbio/*/*/extracted/concatenated_pacbio_2.fastq
    Organism=$(echo $PacBioDat1 | rev | cut -f4 -d '/' | rev)
    Strain=$(echo $PacBioDat1 | rev | cut -f3 -d '/' | rev)
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
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/spades/multiple_libraries
    qsub $ProgDir/subSPAdes_2lib_pacbio_2lib.sh $PacBioDat1 $PacBioDat2 $TrimF1_Read $TrimR1_Read $TrimF2_Read $TrimR2_Read $OutDir 50
done
```

--progress here--

##Filter out contigs < 500bp

```bash
Contigs=assembly/spades_pacbio/P.fragariae/Bc16/contigs.fasta
AssemblyDir=$(dirname $Contigs)
mkdir $AssemblyDir/filtered_contigs
FilterDir=/home/armita/git_repos/emr_repos/tools/seq_tools/assemblers/abyss
$FilterDir/filter_abyss_contigs.py $Contigs 500 > $AssemblyDir/filtered_contigs/contigs_min_500bp.fasta
```

##Merging pacbio and hybrid assemblies

```bash
for PacBioAssembly in $(ls assembly/canu/*/*/polished/pilon.fasta)
do
    Organism=P.fragariae
    Strain=Bc16
    HybridAssembly=$(ls assembly/spades_pacbio/$Organism/$Strain/contigs.fasta)
    OutDir=assembly/merged_canu_spades/$Organism/$Strain
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/quickmerge
    echo $HybridAssembly
    qsub $ProgDir/sub_quickmerge.sh $PacBioAssembly $HybridAssembly $OutDir
done
```

###This merged assembly was polished using Pilon

```bash
for Assembly in $(ls assembly/merged_canu_spades/P.fragariae/Bc16/merged.fasta)
do
    Organism=P.fragariae
    Strain=Bc16
    Reads=$(echo $Assembly | rev | cut -f2 -d '/' | rev)
    IlluminaDirF=qc_dna/paired/P.fragariae/Bc16/F
    IlluminaDirR=qc_dna/paired/P.fragariae/Bc16/R
    TrimF1_Read=$IlluminaDirF/Bc16_S1_L001_R1_001_trim.fq.gz
    TrimR1_Read=$IlluminaDirR/Bc16_S1_L001_R2_001_trim.fq.gz
    TrimF2_Read=$IlluminaDirF/Bc16_S2_L001_R1_001_160129_trim.fq.gz
    TrimR2_Read=$IlluminaDirR/Bc16_S2_L001_R2_001_160129_trim.fq.gz
    OutDir=assembly/merged_canu_spades/$Organism/$Strain/polished
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/pilon
    qsub $ProgDir/sub_pilon_2_libs.sh $Assembly $TrimF1_Read $TrimR1_Read $TrimF2_Read $TrimR2_Read $OutDir
done
```

####Contigs were renamed in accordance with ncbi recomendations.

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/remove_contaminants
touch tmp.csv
for Assembly in $(ls assembly/merged_canu_spades/P.fragariae/Bc16/polished/pilon.fasta)
do
    Organism=P.fragariae
    Strain=Bc16
    OutDir=assembly/merged_canu_spades/$Organism/$Strain/filtered_contigs
    mkdir -p $OutDir
    $ProgDir/remove_contaminants.py --inp $Assembly --out $OutDir/"$Strain"_contigs_renamed.fasta --coord_file tmp.csv
done
rm tmp.csv
```

###Assembly stats were collected using quast

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/quast
for Assembly in $(ls assembly/merged_canu_spades/P.fragariae/Bc16/polished/pilon.fasta)
do
    Organism=P.fragariae
    Strain=Bc16
    OutDir=$(dirname $Assembly)
    qsub $ProgDir/sub_quast.sh $Assembly $OutDir
done
```

** Results from quast:

Number of contigs: 406
N50: 437436
L50: 59 **

#Checking PacBio coverage against BC-16 contigs

The accuracy of PacBio assembly pipelines is currently unknown. To help identify regions that may have been missassembled the pacbio reads were aligned back to the assembled genome. Coverage was determined using bedtools genomecov and regions with low coverage flagged using a python script flag_low_coverage.py. These low coverage regions were visually inspected using IGV.

```bash
Assembly=assembly/merged_canu_spades/P.fragariae/Bc16/filtered_contigs/Bc16_contigs_renamed.fasta
Reads=raw_dna/pacbio/P.fragariae/Bc16/extracted/concatenated_pacbio_1.fastq raw_dna/pacbio/P.fragariae/Bc16/extracted/concatenated_pacbio_2.fastq
OutDir=analysis/genome_alignment/bwa/P.fragariae/Bc16/vs_Bc16
ProgDir=/home/adamst/git_repos/tools/seq_tools/genome_alignment/bwa
qsub $ProgDir/sub_bwa_pacbio.sh $Assembly $Reads $OutDir
```
