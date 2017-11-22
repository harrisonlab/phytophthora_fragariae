# *Phytophthora fragariae*
Commands used in the analysis of P. fragariae genomes
A4, BC-1, BC-16, BC-23, NOV-27, NOV-5, NOV-71, NOV-77, NOV-9, ONT-3, SCRP245_v2
====================

Commands used during analysis of Phytophthora fragariae genomes. Note - all this work was performed in the directory: /home/groups/harrisonlab/project_files/phytophthora_fragariae

The following is a summary of the work presented in this Readme:
Data organisation:
  * Preparing data  
Draft Genome assembly
  * Data qc
  * Genome assembly
  * Repeatmasking
  * Gene prediction
  * Functional annotation
Genome analysis
  * Homology between predicted genes & published effectors


#Data organisation

Data was copied from the raw_data repository to a local directory for assembly
and annotation.

```bash
mkdir -p /home/groups/harrisonlab/project_files/phytophthora_fragariae
cd /home/groups/harrisonlab/project_files/phytophthora_fragariae
Species=P.fragariae
mkdir -p raw_dna/paired/P.fragariae/A4/F
mkdir -p raw_dna/paired/P.fragariae/A4/R
mkdir -p raw_dna/paired/P.fragariae/SCRP245_v2/F
mkdir -p raw_dna/paired/P.fragariae/SCRP245_v2/R
mkdir -p raw_dna/paired/P.fragariae/Bc23/F
mkdir -p raw_dna/paired/P.fragariae/Bc23/R
mkdir -p raw_dna/paired/P.fragariae/Nov5/F
mkdir -p raw_dna/paired/P.fragariae/Nov5/R
mkdir -p raw_dna/paired/P.fragariae/Nov77/F
mkdir -p raw_dna/paired/P.fragariae/Nov77/R
mkdir -p raw_dna/paired/P.fragariae/ONT3/F
mkdir -p raw_dna/paired/P.fragariae/ONT3/R
RawDat=/home/groups/harrisonlab/raw_data/raw_seq/raw_reads/150716_M01678_0023_AB0YF
cp $RawDat/PfragariaeA4_S3_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/A4/F/.
cp $RawDat/PfragariaeA4_S3_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/A4/R/.
RawDat=/home/groups/harrisonlab/raw_data/raw_seq/raw_reads/150925_M01678_0029_AC669
cp $RawDat/Pfrag-SCRP245_S3_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/SCRP245_v2/F/.
cp $RawDat/Pfrag-SCRP245_S3_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/SCRP245_v2/R/.
cp $RawDat/Pfrag-Bc23_S2_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/Bc23/F/.
cp $RawDat/Pfrag-Bc23_S2_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/Bc23/R/.
RawDat=/home/groups/harrisonlab/raw_data/raw_seq/raw_reads/150918_M01678_0028_AC60K
cp $RawDat/Pfrag-Nov-5_S2_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/Nov5/F/.
cp $RawDat/Pfrag-Nov-5_S2_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/Nov5/R/.
cp $RawDat/Pfrag-Nov-77_S3_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/Nov77/F/.
cp $RawDat/Pfrag-Nov-77_S3_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/Nov77/R/.
cp $RawDat/Pfrag-ONT-3_S1_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/ONT3/F/.
cp $RawDat/Pfrag-ONT-3_S1_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/ONT3/R/.
RawDatDir=/home/groups/harrisonlab/raw_data/raw_seq/raw_reads/160108_M01678_0039_AEMMF
mkdir -p raw_dna/paired/P.fragariae/Bc16/F
mkdir -p raw_dna/paired/P.fragariae/Bc16/R
cp $RawDatDir/Bc16_S1_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/Bc16/F/.
cp $RawDatDir/Bc16_S1_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/Bc16/R/.
mkdir -p raw_dna/paired/P.fragariae/62471/F/.
mkdir -p raw_dna/paired/P.fragariae/62471/R/.
cp $RawDatDir/62471_S3_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/62471/F/.
cp $RawDatDir/62471_S3_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/62471/R/.
mkdir -p raw_dna/paired/P.fragariae/Nov27/F/.
mkdir -p raw_dna/paired/P.fragariae/Nov27/R/.
cp $RawDatDir/Nov27_S2_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/Nov27/F/.
cp $RawDatDir/Nov27_S2_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/Nov27/R/.
```

```bash
RawDatDir=/home/groups/harrisonlab/raw_data/raw_seq/raw_reads/160108_M01678_0039_AEMMF
mkdir -p raw_dna/paired/P.fragariae/Bc16/F
mkdir -p raw_dna/paired/P.fragariae/Bc16/R
cp $RawDatDir/Bc16_S1_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/Bc16/F/.
cp $RawDatDir/Bc16_S1_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/Bc16/R/.
mkdir -p raw_dna/paired/P.fragariae/62471/F/.
mkdir -p raw_dna/paired/P.fragariae/62471/R/.
cp $RawDatDir/62471_S3_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/62471/F/.
cp $RawDatDir/62471_S3_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/62471/R/.
mkdir -p raw_dna/paired/P.fragariae/Nov27/F/.
mkdir -p raw_dna/paired/P.fragariae/Nov27/R/.
cp $RawDatDir/Nov27_S2_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/Nov27/F/.
cp $RawDatDir/Nov27_S2_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/Nov27/R/.
```

```bash
ReadDir=/home/groups/harrisonlab/raw_data/raw_seq/raw_reads
mkdir -p raw_dna/paired/P.fragariae/Nov9/F
mkdir -p raw_dna/paired/P.fragariae/Nov9/R
cp $ReadDir/151113_M01678_0031_000000000-ACUNP/PfragNov9_S3_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/Nov9/F/.
cp $ReadDir/151113_M01678_0031_000000000-ACUNP/PfragNov9_S3_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/Nov9/R/.
cp $ReadDir/151127_M01678_0032_000000000-ACUUN/Pfrag-Nov9_S1_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/Nov9/F/.
cp $ReadDir/151127_M01678_0032_000000000-ACUUN/Pfrag-Nov9_S1_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/Nov9/R/.

mkdir -p raw_dna/paired/P.fragariae/Nov71/F
mkdir -p raw_dna/paired/P.fragariae/Nov71/R
cp $ReadDir/151113_M01678_0031_000000000-ACUNP/PfragNov71_S2_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/Nov71/F/.
cp $ReadDir/151113_M01678_0031_000000000-ACUNP/PfragNov71_S2_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/Nov71/R/.
cp $ReadDir/151127_M01678_0032_000000000-ACUUN/Pfrag-Nov71_S2_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/Nov71/F/.
cp $ReadDir/151127_M01678_0032_000000000-ACUUN/Pfrag-Nov71_S2_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/Nov71/R/.

mkdir -p raw_dna/paired/P.fragariae/Bc1/F
mkdir -p raw_dna/paired/P.fragariae/Bc1/R
cp $ReadDir/151113_M01678_0031_000000000-ACUNP/PfragBc1_S1_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/Bc1/F/.
cp $ReadDir/151113_M01678_0031_000000000-ACUNP/PfragBc1_S1_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/Bc1/R/.
cp $ReadDir/151127_M01678_0032_000000000-ACUUN/Pfrag-Bc1_S3_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/Bc1/F/.
cp $ReadDir/151127_M01678_0032_000000000-ACUUN/Pfrag-Bc1_S3_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/Bc1/R/.
```

```bash
RawDatDir=/home/groups/harrisonlab/raw_data/raw_seq/raw_reads/160129_M04465_0001-AHMT4
mkdir -p raw_dna/paired/P.fragariae/Bc1/F
mkdir -p raw_dna/paired/P.fragariae/Bc1/R
cp $RawDatDir/Bc1_S1_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/Bc1/F/Bc1_S1_L001_R1_001_160129.fastq.gz
cp $RawDatDir/Bc1_S1_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/Bc1/R/Bc1_S1_L001_R2_001_160129.fastq.gz

mkdir -p raw_dna/paired/P.fragariae/Bc16/F
mkdir -p raw_dna/paired/P.fragariae/Bc16/R
cp $RawDatDir/Bc16_S2_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/Bc16/F/Bc16_S2_L001_R1_001_160129.fastq.gz
cp $RawDatDir/Bc16_S2_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/Bc16/R/Bc16_S2_L001_R2_001_160129.fastq.gz

mkdir -p raw_dna/paired/P.fragariae/Nov9/F
mkdir -p raw_dna/paired/P.fragariae/Nov9/R
cp $RawDatDir/Nov9_S3_L001_R1_001.fastq.gz raw_dna/paired/P.fragariae/Nov9/F/Nov9_S3_L001_R1_001_160129.fastq.gz
cp $RawDatDir/Nov9_S3_L001_R2_001.fastq.gz raw_dna/paired/P.fragariae/Nov9/R/Nov9_S3_L001_R2_001_160129.fastq.gz
```


#Data qc

programs: fastqc fastq-mcf kmc

Data quality was visualised using fastqc:


```bash
for Strain in Bc1 Bc16 Nov9; do
    for RawData in $(ls raw_dna/paired/P.fragariae/$Strain/*/*.fastq.gz | grep '_160129'); do
        echo $RawData;
        ProgDir=/home/adamst/git_repos/tools/seq_tools/dna_qc;
        qsub $ProgDir/run_fastqc.sh $RawData;
    done
done
```

Trimming was performed on data to trim adapters from sequences and remove poor quality data.
This was done with fastq-mcf


```bash
for Strain in Bc1 Bc16 Nov9; do
    echo $Strain
    Read_F=$(ls raw_dna/paired/P.fragariae/$Strain/F/*.fastq.gz | grep '_160129')
    Read_R=$(ls raw_dna/paired/P.fragariae/$Strain/R/*.fastq.gz | grep '_160129')
    IluminaAdapters=/home/adamst/git_repos/tools/seq_tools/ncbi_adapters.fa
    ProgDir=/home/adamst/git_repos/tools/seq_tools/rna_qc
    echo $Read_F
    echo $Read_R
    qsub $ProgDir/rna_qc_fastq-mcf.sh $Read_F $Read_R $IluminaAdapters DNA
done
```

Data quality was visualised once again following trimming:

```bash
for Strain in Bc1 Bc16 Nov9; do
    for RawData in $(ls qc_dna/paired/P.fragariae/$Strain/*/*.fq.gz | grep '_160129'); do
        echo $RawData;
        ProgDir=/home/adamst/git_repos/tools/seq_tools/dna_qc;
        qsub $ProgDir/run_fastqc.sh $RawData;
    done
done
```


kmer counting was performed using kmc.
This allowed estimation of sequencing depth and total genome size:

```bash  
for Strain in Nov9; do
    echo $Strain;
    Trim_F1=$(ls qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz | grep 'S1');
    Trim_R1=$(ls qc_dna/paired/P.fragariae/$Strain/R/*.fq.gz | grep 'S1');
    Trim_F2=$(ls qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz | grep 'PfragNov9');
    Trim_R2=$(ls qc_dna/paired/P.fragariae/$Strain/R/*.fq.gz | grep 'PfragNov9');
    Trim_F3=$(ls qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz | grep '_160129');
    Trim_R3=$(ls qc_dna/paired/P.fragariae/$Strain/R/*.fq.gz | grep '_160129');
    ProgDir=/home/adamst/git_repos/tools/seq_tools/dna_qc;
    qsub $ProgDir/kmc_kmer_counting.sh $Trim_F1 $Trim_R1 $Trim_F2 $Trim_R2 $Trim_F3 $Trim_$R3
done
```

```
Estimated Genome Size is:
A4: 93,413,554
SCRP245_v2: 127,550,025
Bc23: 103,251,773
Nov5: 95,350,039
Nov77: 92,399,813
ONT3: 103,869,049
Bc16: 90,864,210
Nov27: 93,851,233
Bc1: 1,196,301,136
Nov9: 959,591,302
Nov71: 810,779,109
```

##Calculate coverage using the count_nucl.pl script

###For one library

```bash
for DataDir in $(ls -d qc_dna/paired/P.fragariae/* | grep -v 'Nov71' | grep -v 'Bc1' | grep -v 'Nov9' | grep -v 'Bc16' | grep -v '62471')
do
    F_Read=$(ls $DataDir/F/*.gz)
    R_Read=$(ls $DataDir/R/*.gz)
    Strain=$(echo $DataDir | rev | cut -f1 -d '/' | rev)
    Organism=$(echo $DataDir | rev | cut -f2 -d '/' | rev)
    WorkDir=tmp_dir/$Strain
    mkdir -p $WorkDir
    cp -r $F_Read $WorkDir
    cp -r $R_Read $WorkDir
    cd $WorkDir
    Read1=*R1*
    Read2=*R2*
    gunzip $Read1
    gunzip $Read2
    Sub1=*R1*.fq
    Sub2=*R2*.fq
    echo "$Organism - $Strain"
    count_nucl.pl -i $Sub1 -i $Sub2 -g 96
    cd /home/groups/harrisonlab/project_files/phytophthora_fragariae
done
```

###For two libraries

```bash
for DataDir in $(ls -d qc_dna/paired/P.fragariae/* | grep -e 'Nov71')
do
    F_Read1=$(ls $DataDir/F/Pfrag-Nov71*.gz)
    R_Read1=$(ls $DataDir/R/Pfrag-Nov71*.gz)
    F_Read2=$(ls $DataDir/F/PfragNov71*.gz)
    R_Read2=$(ls $DataDir/R/PfragNov71*.gz)
    Strain=$(echo $DataDir | rev | cut -f1 -d '/' | rev)
    Organism=$(echo $DataDir | rev | cut -f2 -d '/' | rev)
    WorkDir=tmp_dir/$Strain
    mkdir -p $WorkDir
    cp -r $F_Read1 $WorkDir
    cp -r $R_Read1 $WorkDir
    cp -r $F_Read2 $WorkDir
    cp -r $R_Read2 $WorkDir
    cd $WorkDir
    Read1=PfragN*R1*
    Read2=PfragN*R2*
    Read3=Pfrag-*R1*
    Read4=Pfrag-*R2*
    gunzip $Read1
    gunzip $Read2
    gunzip $Read3
    gunzip $Read4
    Sub1=PfragN*R1*.fq
    Sub2=PfragN*R2*.fq
    Sub3=Pfrag-*R1*.fq
    Sub4=Pfrag-*R2*.fq
    cat $Sub1 $Sub3 > Forward.fq
    cat $Sub2 $Sub4 > Reverse.fq
    echo "$Organism - $Strain"
    count_nucl.pl -i Forward.fq -i Reverse.fq -g 96
    cd /home/groups/harrisonlab/project_files/phytophthora_fragariae
done
```

###For three libraries - NOV-9

```bash
for DataDir in $(ls -d qc_dna/paired/P.fragariae/* | grep -e 'Nov9')
do
    F_Read1=$(ls $DataDir/F/Nov9_S3*.gz)
    R_Read1=$(ls $DataDir/R/Nov9_S3*.gz)
    F_Read2=$(ls $DataDir/F/*S1*.gz)
    R_Read2=$(ls $DataDir/R/*S1*.gz)
    F_Read3=$(ls $DataDir/F/PfragNov9*.gz)
    R_Read3=$(ls $DataDir/R/PfragNov9*.gz)
    Strain=$(echo $DataDir | rev | cut -f1 -d '/' | rev)
    Organism=$(echo $DataDir | rev | cut -f2 -d '/' | rev)
    WorkDir=tmp_dir/$Strain
    mkdir -p $WorkDir
    cp -r $F_Read1 $WorkDir
    cp -r $R_Read1 $WorkDir
    cp -r $F_Read2 $WorkDir
    cp -r $R_Read2 $WorkDir
    cp -r $F_Read3 $WorkDir
    cp -r $R_Read3 $WorkDir
    cd $WorkDir
    Read1=Nov9_S3*R1*
    Read2=Nov9_S3*R2*
    Read3=Pfrag-*R1*
    Read4=Pfrag-*R2*
    Read5=PfragN*R1*
    Read6=PfragN*R2*
    gunzip $Read1
    gunzip $Read2
    gunzip $Read3
    gunzip $Read4
    gunzip $Read5
    gunzip $Read6
    Sub1=Nov9_S3*R1*.fq
    Sub2=Nov9_S3*R2*.fq
    Sub3=Pfrag-*R1*.fq
    Sub4=Pfrag-*R2*.fq
    Sub5=PfragN*R1*.fq
    Sub6=PfragN*R2*.fq
    cat $Sub1 $Sub3 $Sub5 > Forward.fq
    cat $Sub2 $Sub4 $Sub6 > Reverse.fq
    echo "$Organism - $Strain"
    count_nucl.pl -i Forward.fq -i Reverse.fq -g 96
    cd /home/groups/harrisonlab/project_files/phytophthora_fragariae
done
```

###For three libraries - BC-1

```bash
for DataDir in $(ls -d qc_dna/paired/P.fragariae/* | grep -e 'Bc1')
do
    F_Read1=$(ls $DataDir/F/Bc1*.gz)
    R_Read1=$(ls $DataDir/R/Bc1*.gz)
    F_Read2=$(ls $DataDir/F/Pfrag*S1*.gz)
    R_Read2=$(ls $DataDir/R/Pfrag*S1*.gz)
    F_Read3=$(ls $DataDir/F/*S3*.gz)
    R_Read3=$(ls $DataDir/R/*S3*.gz)
    Strain=$(echo $DataDir | rev | cut -f1 -d '/' | rev)
    Organism=$(echo $DataDir | rev | cut -f2 -d '/' | rev)
    WorkDir=tmp_dir/$Strain
    mkdir -p $WorkDir
    cp -r $F_Read1 $WorkDir
    cp -r $R_Read1 $WorkDir
    cp -r $F_Read2 $WorkDir
    cp -r $R_Read2 $WorkDir
    cp -r $F_Read3 $WorkDir
    cp -r $R_Read3 $WorkDir
    cd $WorkDir
    Read1=Bc1*R1*
    Read2=Bc1*R2*
    Read3=Pfrag*S1*R1*
    Read4=Pfrag*S1*R2*
    Read5=*S3*R1*
    Read6=*S3*R2*
    gunzip $Read1
    gunzip $Read2
    gunzip $Read3
    gunzip $Read4
    gunzip $Read5
    gunzip $Read6
    Sub1=Bc1*R1*.fq
    Sub2=Bc1*R2*.fq
    Sub3=Pfrag*S1*R1*.fq
    Sub4=Pfrag*S1*R2*.fq
    Sub5=*S3*R1*.fq
    Sub6=*S3*R2*.fq
    cat $Sub1 $Sub3 $Sub5 > Forward.fq
    cat $Sub2 $Sub4 $Sub6 > Reverse.fq
    echo "$Organism - $Strain"
    count_nucl.pl -i Forward.fq -i Reverse.fq -g 96
    cd /home/groups/harrisonlab/project_files/phytophthora_fragariae
done
```

###For PacBio data

```bash
gunzip -fc raw_dna/pacbio/P.fragariae/Bc16/extracted/concatenated_pacbio_1.fastq.gz
gunzip -fc raw_dna/pacbio/P.fragariae/Bc16/extracted/concatenated_pacbio_2.fastq.gz
cat raw_dna/pacbio/P.fragariae/Bc16/extracted/concatenated_pacbio_1.fastq | paste - - - - | cut -f3 | tr -d '\n' | wc -c
cat raw_dna/pacbio/P.fragariae/Bc16/extracted/concatenated_pacbio_2.fastq | paste - - - - | cut -f3 | tr -d '\n' | wc -c
```

```
Estimated Coverage is:
A4: 35.91
SCRP245_v2: 51.47
Bc23: 49.33
Nov5: 40.21
Nov77: 46.29
ONT3: 45.18
Bc16: 61.29
Nov27: 52.27
Bc1: 116.25
Nov9: 103.23
Nov71: 79.92
```
Target coverage is 20.
The ones at value 5 are errors from filtering of error kmers, estimate from plots follow in ().

# Assembly
Assembly was performed using: Spades
hybrid canu and spades assembly for Bc16 detailed in pacbio_assembly.md

## Spades Assembly

For single runs

```bash
for Strain in SCRP245_v2
do
    F_Read=$(ls qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz)
    R_Read=$(ls qc_dna/paired/P.fragariae/$Strain/R/*.fq.gz)
    CovCutoff='10'
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/spades
    Species=$(echo $F_Read | rev | cut -f4 -d '/' | rev)
    OutDir=assembly/spades/$Species/$Strain
    echo $Species
    echo $Strain
    qsub $ProgDir/submit_SPAdes_HiMem.sh $F_Read $R_Read $OutDir correct $CovCutoff
done
```

For two runs

```bash
for Strain in Nov71
do
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/spades/multiple_libraries
    F_Read1=$(ls qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz | grep 'Pfrag-Nov71')
    R_Read1=$(ls qc_dna/paired/P.fragariae/$Strain/R/*.fq.gz | grep 'Pfrag-Nov71')
    F_Read2=$(ls qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz | grep 'PfragNov71')
    R_Read2=$(ls qc_dna/paired/P.fragariae/$Strain/R/*.fq.gz | grep 'PfragNov71')
    echo $F_Read1
    echo $R_Read1
    echo $F_Read2
    echo $R_Read2
    Species=$(echo $F_Read1 | rev | cut -f4 -d '/' | rev)
    echo $Strain
    echo $Species
    OutDir=assembly/spades/$Species/$Strain
    qsub $ProgDir/subSpades_2lib_HiMem.sh $F_Read1 $R_Read1 $F_Read2 $R_Read2 $OutDir correct 10
done
```

For three runs

```bash
for Strain in Bc1
do
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/spades/multiple_libraries
    F_Read1=$(ls qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz | grep 'S3')
    R_Read1=$(ls qc_dna/paired/P.fragariae/$Strain/R/*.fq.gz | grep 'S3')
    F_Read2=$(ls qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz | grep 'PfragBc1')
    R_Read2=$(ls qc_dna/paired/P.fragariae/$Strain/R/*.fq.gz | grep 'PfragBc1')
    F_Read3=$(ls qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz | grep '_160129')
    R_Read3=$(ls qc_dna/paired/P.fragariae/$Strain/R/*.fq.gz | grep '_160129')
    echo $F_Read1
    echo $R_Read1
    echo $F_Read2
    echo $R_Read2
    echo $F_Read3
    echo $R_Read3
    Species=$(echo $F_Read1 | rev | cut -f4 -d '/' | rev)
    echo $Strain
    echo $Species
    OutDir=assembly/spades/$Species/$Strain
    qsub $ProgDir/subSpades_3lib_HiMem.sh $F_Read1 $R_Read1 $F_Read2 $R_Read2 $F_Read3 $R_Read3 $OutDir correct 10
done
```

###Quast

```bash
for Strain in A4 Bc1 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/remove_contaminants
    OutDir=$(ls -d assembly/spades/*/$Strain/filtered_contigs)
    AssFiltered=$OutDir/contigs_min_500bp.fasta
    AssRenamed=$OutDir/contigs_min_500bp_renamed.fasta
    echo $AssFiltered
    printf '.\t.\t.\t.\n' > editfile.tab
    $ProgDir/remove_contaminants.py --inp $AssFiltered --out $AssRenamed --coord_file editfile.tab
    rm editfile.tab
done
```

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/remove_contaminants
touch tmp.csv
for Assembly in $(ls assembly/FALCON_Trial/quiver_results/polished/pilon_1.fasta)
do
    Strain=Bc16
    OutDir=assembly/FALCON_Trial/quiver_results/polished/filtered_contigs
    mkdir -p $OutDir
    $ProgDir/remove_contaminants.py --inp $Assembly --out $OutDir/"$Strain"_contigs_renamed.fasta --coord_file tmp.csv
done
rm tmp.csv
```

###QUAST used to summarise assembly statistics

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/quast
for Strain in A4 Bc1 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for Assembly in $(ls assembly/spades/*/$Strain/filtered_contigs/*_500bp_renamed.fasta)
    do
        Strain=$(echo $Assembly | rev | cut -d '/' -f3 | rev)
        Organism=$(echo $Assembly | rev | cut -d '/' -f4 | rev)
        OutDir=assembly/spades/$Organism/$Strain/filtered_contigs
        qsub $ProgDir/sub_quast.sh $Assembly $OutDir
    done
done
```

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/quast
Assembly=assembly/FALCON_Trial/quiver_results/polished/filtered_contigs/Bc16_contigs_renamed.fasta
OutDir=assembly/FALCON_Trial/quiver_results/polished/
qsub $ProgDir/sub_quast.sh $Assembly $OutDir
```

```
N50:
A4: 18,245
BC-16: 923,458
BC-23: 18,227
NOV-27: 19,406
NOV-5: 17,887
NOV-77: 18,909
ONT-3: 22,074
SCRP245_v2: 20,105
NOV-71: 20,226
NOV-9: 21,522
BC-1: 21,834

L50:
A4: 1,116
BC-16: 33
BC-23: 1,119
NOV-27: 1,046
NOV-5: 1,134
NOV-77: 1,102
ONT-3: 917
SCRP245_v2: 994
NOV-71: 1,016
NOV-9: 978
BC-1: 954

Number of contigs > 1kb:
A4: 8,660
BC-16: 180
BC-23: 8,556
NOV-27: 8,040
NOV-5: 8,760
NOV-77: 8,500
ONT-3: 8,540
SCRP245_v2: 8,584
NOV-71: 7,885
NOV-9: 7,655
BC-1: 7,504
```

##Run Deconseq to identify potential contaminents in the assembly

###SPAdes assemblies

Contigs were identified that had BLAST hits to non-phytophthora genomes

```bash
for Assembly in $(ls assembly/spades/*/*/filtered_contigs/contigs_min_500bp_renamed.fasta | grep -v 'Bc16')
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    echo "$Organism - $Strain"
    # Exclude_db="bact,virus,hsref"
    Exclude_db="paenibacillus"
    Good_db="phytoph"
    AssemblyDir=$(dirname $Assembly)
    # OutDir=$AssemblyDir/../deconseq
    OutDir=$AssemblyDir/../deconseq_Paen
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/remove_contaminants
    qsub $ProgDir/sub_deconseq.sh $Assembly $Exclude_db $Good_db $OutDir
done
```

Results were summarised using the following commands

```bash
# for File in $(ls assembly/spades/P.*/*/deconseq/log.txt); do
for File in $(ls assembly/spades/P.*/*/deconseq_Paen/log.txt)
do
    Name=$(echo $File | rev | cut -f3 -d '/' | rev)
    Good=$(cat $File |cut -f2 | head -n1 | tail -n1)
    Both=$(cat $File |cut -f2 | head -n2 | tail -n1)
    Bad=$(cat $File |cut -f2 | head -n3 | tail -n1)
    printf "$Name\t$Good\t$Both\t$Bad\n"
done
```

```
A4	13445	1	1
Bc1	11555	1	1
Bc23	13189	2	1
Nov27	12487	2	1
Nov5	13526	2	1
Nov71	12211	2	1
Nov77	13319	2	1
Nov9	11801	1	1
ONT3	13290	2	54
SCRP245_v2	13247	2	10
```

Contaminent organisms identified by NCBI BLAST

```bash
A4:
PhiX

BC-1:
PhiX

BC-23:
PhiX

NOV-27:
PhiX

NOV-5:
PhiX

NOV-71:
PhiX

NOV-77:
PhiX

NOV-9:
PhiX

ONT-3:
Paenibacillus
Thermobacillus compostii
Brevibacillus brevis
Bacillus simplex (poor hit)
PhiX

SCRP245_v2:
PhiX
Bacillus oceanisediminis
Staphylococcus spp
```

Assembly stats were collected on filtered assemblies

```bash
for Assembly in $(ls assembly/spades/P.*/*/deconseq_Paen/contigs_min_500bp_filtered_renamed.fasta)
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    OutDir=$(dirname $Assembly)
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/quast
    qsub $ProgDir/sub_quast.sh $Assembly $OutDir
done
```

Assembly size was summarised and compared to previous assembly results

```bash
for Assembly in $(ls assembly/spades/P.*/*/deconseq_Paen/report.tsv)
do  
    Strain=$(echo $Assembly | rev | cut -f3 -d '/'| rev)
    Size=$(cat $Assembly | grep 'Total length' | head -n1 | cut -f2)
    OldAssembly=$(ls assembly/spades/P.*/$Strain/filtered_contigs*/report.tsv)
    OldSize=$(cat $OldAssembly | grep 'Total length' | head -n1 | cut -f2)
    printf "$Strain\t$Size\t$OldSize\n"
done
```

```
A4	79079019	79084532
Bc1	79098893	79104406
Bc23	78255805	78261318
Nov27	78749363	78754876
Nov5	78992821	78998334
Nov71	78371685	78377198
Nov77	78804247	78809760
Nov9	79429452	79434965
ONT3	84322417	88587983
SCRP245_v2	83127441	83317162
```

###FALCON assembly

Contigs were identified that had BLAST hits to non-phytophthora genomes

```bash
Assembly=assembly/FALCON_Trial/quiver_results/polished/filtered_contigs/Bc16_contigs_renamed.fasta
Strain=Bc16
Organism=P.fragariae
echo "$Organism - $Strain"
# Exclude_db="bact,virus,hsref"
Exclude_db="paenibacillus"
Good_db="phytoph"
AssemblyDir=$(dirname $Assembly)
# OutDir=$AssemblyDir/../deconseq
OutDir=$AssemblyDir/../deconseq_Paen
ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/remove_contaminants
qsub $ProgDir/sub_deconseq.sh $Assembly $Exclude_db $Good_db $OutDir
```

Results were summarised using the following commands

```bash
# for File in $(ls assembly/spades/P.*/*/deconseq/log.txt); do
File=assembly/FALCON_Trial/quiver_results/polished/deconseq_Paen/log.txt
Name=Bc16
Good=$(cat $File |cut -f2 | head -n1 | tail -n1)
Both=$(cat $File |cut -f2 | head -n2 | tail -n1)
Bad=$(cat $File |cut -f2 | head -n3 | tail -n1)
printf "$Name\t$Good\t$Both\t$Bad\n"
```

```
Bc16	180	0	0
```

Assembly stats were collected on filtered assemblies

```bash
Assembly=assembly/FALCON_Trial/quiver_results/polished/deconseq_Paen/contigs_min_500bp_filtered_renamed.fasta
Strain=Bc16
Organism=P.fragariae
OutDir=$(dirname $Assembly)
ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/quast
qsub $ProgDir/sub_quast.sh $Assembly $OutDir
```

Assembly stats were summarised and compared to previous assembly results

```bash
Assembly=assembly/FALCON_Trial/quiver_results/polished/deconseq_Paen/report.tsv
Strain=Bc16
Size=$(cat $Assembly | grep 'Total length' | head -n1 | cut -f2)
OldAssembly=assembly/FALCON_Trial/quiver_results/polished/report.tsv
OldSize=$(cat $OldAssembly | grep 'Total length' | head -n1 | cut -f2)
printf "$Strain\t$Size\t$OldSize\n"
```

```
Bc16	90967989	90967989
```

Final Assembly statistics

```
N50:
A4: 18,245
BC-16: 923,458
BC-23: 18,227
NOV-27: 19,406
NOV-5: 17,887
NOV-77: 18,925
ONT-3: 20,565
SCRP245_v2: 20,056
NOV-71: 20,226
NOV-9: 21,522
BC-1: 21,842

L50:
A4: 1,116
BC-16: 33
BC-23: 1,119
NOV-27: 1,046
NOV-5: 1,134
NOV-77: 1,101
ONT-3: 988
SCRP245_v2: 995
NOV-71: 1,016
NOV-9: 978
BC-1: 953

Number of contigs > 1kb:
A4: 8,659
BC-16: 180
BC-23: 8,555
NOV-27: 8,039
NOV-5: 8,759
NOV-77: 8,499
ONT-3: 8,492
SCRP245_v2: 8,576
NOV-71: 7,884
NOV-9: 7,654
BC-1: 7,503
```

Extra corrections for submitting to genbank performed in Genbank_corrections.md

#Repeatmasking

Repeat masking was performed and used the following programs: Repeatmasker Repeatmodeler

The best assemblies were used to perform repeatmasking

for BC-16 FALCON assembly:

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/repeat_masking
for BestAss in $(ls assembly/FALCON_Trial/quiver_results/polished/filtered_contigs/*_contigs_renamed.fasta)
do
    qsub $ProgDir/rep_modeling.sh $BestAss
    qsub $ProgDir/transposonPSI.sh $BestAss
done
```

for other isolates Illumina data:

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/repeat_masking
for Strain in A4 Bc1 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for BestAss in $(ls assembly/spades/*/$Strain/deconseq_Paen/*_500bp_filtered_renamed.fasta)
    do
        qsub $ProgDir/rep_modeling.sh $BestAss
        qsub $ProgDir/transposonPSI.sh $BestAss
    done
done   
```

For assemblies cleaned after NCBI detection of contaminants

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/repeat_masking
for Strain in A4 Bc1 Nov5 Nov71 Nov9 SCRP245_v2
do
    for BestAss in $(ls assembly/spades/*/$Strain/ncbi_edits/contigs_min_500bp_renamed.fasta)
    do
        qsub $ProgDir/rep_modeling.sh $BestAss
        qsub $ProgDir/transposonPSI.sh $BestAss
    done
done   
```

The number of bases masked by transposonPSI and Repeatmasker were summarised using the following commands:

```bash
for RepDir in $(ls -d repeat_masked/P.fragariae/*/deconseq_Paen_repmask)
do
    Strain=$(echo $RepDir | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $RepDir | rev | cut -f3 -d '/' | rev)  
    RepMaskGff=$(ls $RepDir/"$Strain"_contigs_hardmasked.gff)
    TransPSIGff=$(ls $RepDir/"$Strain"_contigs_unmasked.fa.TPSI.allHits.chains.gff3)
    printf "$Organism\t$Strain\n"
    printf "The number of bases masked by RepeatMasker:\t"
    sortBed -i $RepMaskGff | bedtools merge | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
    printf "The number of bases masked by TransposonPSI:\t"
    sortBed -i $TransPSIGff | bedtools merge | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
    printf "The total number of masked bases are:\t"
    cat $RepMaskGff $TransPSIGff | sortBed | bedtools merge | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
done
```

For FALCON assembly

```bash
for RepDir in $(ls -d repeat_masked/quiver_results/*/*)
do
    Strain=$(echo $RepDir | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $RepDir | rev | cut -f3 -d '/' | rev)  
    RepMaskGff=$(ls $RepDir/polished_contigs_hardmasked.gff)
    TransPSIGff=$(ls $RepDir/polished_contigs_unmasked.fa.TPSI.allHits.chains.gff3)
    printf "$Organism\t$Strain\n"
    printf "The number of bases masked by RepeatMasker:\t"
    sortBed -i $RepMaskGff | bedtools merge | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
    printf "The number of bases masked by TransposonPSI:\t"
    sortBed -i $TransPSIGff | bedtools merge | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
    printf "The total number of masked bases are:\t"
    cat $RepMaskGff $TransPSIGff | sortBed | bedtools merge | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
done
```

For assemblies corrected by NCBI

```bash
for RepDir in $(ls -d repeat_masked/P.fragariae/*/ncbi_edits_repmask)
do
    Strain=$(echo $RepDir | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $RepDir | rev | cut -f3 -d '/' | rev)  
    RepMaskGff=$(ls $RepDir/"$Strain"_contigs_hardmasked.gff)
    TransPSIGff=$(ls $RepDir/"$Strain"_contigs_unmasked.fa.TPSI.allHits.chains.gff3)
    printf "$Organism\t$Strain\n"
    printf "The number of bases masked by RepeatMasker:\t"
    sortBed -i $RepMaskGff | bedtools merge | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
    printf "The number of bases masked by TransposonPSI:\t"
    sortBed -i $TransPSIGff | bedtools merge | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
    printf "The total number of masked bases are:\t"
    cat $RepMaskGff $TransPSIGff | sortBed | bedtools merge | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
done
```

```
P.fragariae	A4
The number of bases masked by RepeatMasker:	24,225,474
The number of bases masked by TransposonPSI:	6,237,528
The total number of masked bases are:	25,918,245
P.fragariae	Bc1
The number of bases masked by RepeatMasker:	24,762,347
The number of bases masked by TransposonPSI:	6,219,359
The total number of masked bases are:	26,468,865
P.fragariae	Bc16
The number of bases masked by RepeatMasker:	34,585,513
The number of bases masked by TransposonPSI:	8,335,020
The total number of masked bases are:	36,352,455
P.fragariae	Bc23
The number of bases masked by RepeatMasker:	24,253,140
The number of bases masked by TransposonPSI:	6,101,880
The total number of masked bases are:	25,855,136
P.fragariae	Nov27
The number of bases masked by RepeatMasker:	24,280,526
The number of bases masked by TransposonPSI:	6,209,723
The total number of masked bases are:	26,042,750
P.fragariae	Nov5
The number of bases masked by RepeatMasker:	24,217,567
The number of bases masked by TransposonPSI:	6,242,472
The total number of masked bases are:	25,921,835
P.fragariae	Nov71
The number of bases masked by RepeatMasker:	24,035,545
The number of bases masked by TransposonPSI:	6,080,704
The total number of masked bases are:	25,789,456
P.fragariae	Nov77
The number of bases masked by RepeatMasker:	24,578,287
The number of bases masked by TransposonPSI:	6,250,930
The total number of masked bases are:	26,395,760
P.fragariae	Nov9
The number of bases masked by RepeatMasker:	24,970,270
The number of bases masked by TransposonPSI:	6,289,715
The total number of masked bases are:	26,760,322
P.fragariae	ONT3
The number of bases masked by RepeatMasker:	24,798,551
The number of bases masked by TransposonPSI:	6,234,855
The total number of masked bases are:	26,544,846
P.fragariae	SCRP245_v2
The number of bases masked by RepeatMasker:	23,766,590
The number of bases masked by TransposonPSI:	6,037,588
The total number of masked bases are:	25,543,462
```

#Merging RepeatMasker and TransposonPSI outputs

```bash
for File in $(ls -d repeat_masked/*/*/*/*_contigs_softmasked.fa)
do
    OutDir=$(dirname $File)
    TPSI=$(ls $OutDir/*_contigs_unmasked.fa.TPSI.allHits.chains.gff3)
    OutFile=$(echo $File | sed 's/_contigs_softmasked.fa/_contigs_softmasked_repeatmasker_TPSI_appended.fa/g')
    bedtools maskfasta -soft -fi $File -bed $TPSI -fo $OutFile
    echo "$OutFile"
    echo "Number of masked bases:"
    cat $OutFile | grep -v '>' | tr -d '\n' | awk '{print $0, gsub("[a-z]", ".")}' | cut -f2 -d ' '
done
```

#Gene Prediction
Gene prediction followed three steps: Pre-gene prediction - Quality of genome assemblies were assessed using Cegma to see how many core eukaryotic genes can be identified. Gene model training - Gene models were trained using assembled RNAseq data as part of the Braker1 pipeline Gene prediction - Gene models were used to predict genes in genomes as part of the the Braker1 pipeline. This used RNAseq data as hints for gene models.

##Pre-gene prediction

Quality of genome assemblies was assessed by looking for the gene space in the assemblies.

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    Organism=P.fragariae
    if [ -f repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    elif [ -f repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    else
        Assembly=$(ls repeat_masked/quiver_results/polished/filtered_contigs_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    fi
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/busco
    BuscoDB=Eukaryotic
    OutDir=assembly/spades/P.fragariae/$Strain/Busco
    mkdir -p $OutDir
    qsub $ProgDir/sub_busco3.sh $Assembly $BuscoDB $OutDir
done
```

```
A4
Complete and single copy genes: 274
Complete and duplicated genes: 6
Fragmented genes: 6
Missing genes: 17

Bc16
Complete and single copy genes: 266
Complete and duplicated genes: 9
Fragmented genes: 5
Missing genes: 23

Bc1
Complete and single copy genes: 274
Complete and duplicated genes: 6
Fragmented genes: 6
Missing genes: 17

Bc23
Complete and single copy genes: 275
Complete and duplicated genes: 5
Fragmented genes: 7
Missing genes: 16

Nov27
Complete and single copy genes: 273
Complete and duplicated genes: 6
Fragmented genes: 7
Missing genes: 17

Nov5
Complete and single copy genes: 273
Complete and duplicated genes: 7
Fragmented genes: 6
Missing genes: 17

Nov71
Complete and single copy genes: 274
Complete and duplicated genes: 6
Fragmented genes: 6
Missing genes: 17

Nov77
Complete and single copy genes: 272
Complete and duplicated genes: 8
Fragmented genes: 6
Missing genes: 17

Nov9
Complete and single copy genes: 273
Complete and duplicated genes: 6
Fragmented genes: 7
Missing genes: 17

ONT3
Complete and single copy genes: 277
Complete and duplicated genes: 7
Fragmented genes: 4
Missing genes: 15

SCRP245_v2
Complete and single copy genes: 273
Complete and duplicated genes: 7
Fragmented genes: 7
Missing genes: 16
```

#Gene prediction
Gene prediction was performed for the P. fragariae genomes. Two gene prediction approaches were used:

Gene prediction using Braker1 and Prediction of all putative ORFs in the genome using the ORF finder (atg.pl) approach.

##Gene prediction 1 - Braker1 gene model training and prediction

Gene prediction was performed using Braker1.

First, RNAseq data was aligned to P. fragariae genomes.

RNASeq data was acquired from the phytophthora sequencing consortium, hosted at: http://files.cgrb.oregonstate.edu/Tyler_Lab/Phytophthora_sequence

It looks like P. rubi and P. fragariae data has been mixed up, align both to see if this is the case

First perform qc of all RNA using fastqc_mcf

qc of novogene RNA is detailed in RNA-Seq_analysis.md

```bash
for Species in P.rubi P.frag
do
    RNADir=raw_rna/consortium/$Species
    FileF1=$RNADir/F/4*1.fq.gz
    FileR1=$RNADir/R/4*2.fq.gz
    FileF2=$RNADir/F/P*1.fq.gz
    FileR2=$RNADir/R/P*2.fq.gz
    IlluminaAdapters=/home/armita/git_repos/emr_repos/tools/seq_tools/ncbi_adapters.fa
    ProgDir=/home/adamst/git_repos/tools/seq_tools/rna_qc
    qsub $ProgDir/rna_qc_fastq-mcf.sh $FileF1 $FileR1 $IlluminaAdapters RNA
    qsub $ProgDir/rna_qc_fastq-mcf.sh $FileF2 $FileR2 $IlluminaAdapters RNA
done
```

Data quality was visualised using fastqc:

```bash
for Species in P.rubi P.frag
do
    RNADir=qc_rna/raw_rna/consortium/$Species
    FileF1=$RNADir/F/4*1_trim.fq.gz
    FileR1=$RNADir/R/4*2_trim.fq.gz
    FileF2=$RNADir/F/P*1_trim.fq.gz
    FileR2=$RNADir/R/P*2_trim.fq.gz
    ProgDir=/home/adamst/git_repos/tools/seq_tools/dna_qc
    qsub $ProgDir/run_fastqc.sh $FileF1
    qsub $ProgDir/run_fastqc.sh $FileR1
    qsub $ProgDir/run_fastqc.sh $FileF2
    qsub $ProgDir/run_fastqc.sh $FileR2
done
```

#Aligning

<!-- Insert sizes of the RNA seq library were unknown until a draft alignment could be made. To do this tophat and cufflinks were run, aligning the reads against a single genome. The fragment length and stdev were printed to stdout while cufflinks was running.

```bash
for Assembly in $(ls repeat_masked/*/Bc16/*/*_contigs_softmasked_repeatmasker_TPSI_appended.fa)
do
    Strain=$(echo $Assembly| rev | cut -d '/' -f3 | rev)
    Organism=$(echo $Assembly | rev | cut -d '/' -f4 | rev)
    echo "$Organism - $Strain"
    for RNADir in $(ls -d qc_rna/raw_rna/consortium/*)
    do
        Species=$(echo $RNADir | rev | cut -f1 -d '/' | rev)
        echo "$Species"
        FileF1=$(ls $RNADir/F/4*_trim.fq.gz)
        FileR1=$(ls $RNADir/R/4*_trim.fq.gz)
        FileF2=$(ls $RNADir/F/P*_trim.fq.gz)
        FileR2=$(ls $RNADir/R/P*_trim.fq.gz)
        OutDir1=alignment/$Organism/$Strain/$Species/1
        OutDir2=alignment/$Organism/$Strain/$Species/2
        ProgDir=/home/adamst/git_repos/tools/seq_tools/RNAseq
        qsub $ProgDir/tophat_alignment.sh $Assembly $FileF1 $FileR1 $OutDir1
        qsub $ProgDir/tophat_alignment.sh $Assembly $FileF2 $FileR2 $OutDir2
    done
done
```

```
P.frag 4954V8:

Overall read mapping rate = 83.7%
Concordant pair alignment rate = 74.3%

P.frag Pf4954PB:

Overall read mapping rate = 96.4%
Concordant pair alignment rate = 91.6%

P.rubi 4671V8:

Overall read mapping rate = 85.9%
Concordant read mapping rate = 77.7%

P.rubi Pr4671PB:

Overall read mapping rate = 85.1%
Concordant read mapping rate = 76.4%
```

Cufflinks was run to produce the fragment length and stdev statistics

```bash
for Assembly in $(ls repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_softmasked_repeatmasker_TPSI_appended.fa)
do
    Strain=Bc16
    Organism=P.fragariae
    echo "$Organism - $Strain"
    for AcceptedHits in $(ls -d alignment/P.fragariae/Bc16/novogene/*/accepted_hits.bam)
    do
        Species=$(echo $AcceptedHits| rev | cut -d '/' -f3 | rev)
        Num=$(echo $AcceptedHits | rev | cut -d '/' -f2 | rev)
        echo $AcceptedHits
        OutDir=gene_pred/cufflinks/$Organism/$Strain/$Species/$Num
        mkdir -p $OutDir
        ProgDir=/home/adamst/git_repos/tools/seq_tools/RNAseq
        touch $OutDir/cufflinks.log
        cufflinks -o $OutDir/cufflinks -p 8 --max-intron-length 4000 $AcceptedHits 2>&1 | tee $OutDir/cufflinks.log
    done
done
```

```
P.frag 4954V8:

Estimated mean = 196.65
Estimated Std Dev = 28.22

P.frag Pf4954PB:

Estimated mean = 198.88
Estimated Std Dev = 29.12

P.rubi 4671V8:

Estimated mean = 198.30
Estimated Std Dev = 27.77

P.rubi Pr4671PB:

Estimated mean = 188.54
Estimated Std Dev = 26.86
```

These estimated mean values allowed us to calculate the mean insert size. Read length was estimated from fast_qc output. The equation used was: insert gap = mean length - (2 * read length)

```
P.frag 4954V8:

Estimated mean = 196.65
Estimated read length = 87
Estimated insert gap = 22.65

P.frag Pf4954PB:

Estimated mean = 198.88
Estimated read length = 87
Estimated insert gap = 24.88

P.rubi 4671V8:

Estimated mean = 198.30
Estimated read length = 87
Estimated insert gap = 24.3

P.rubi Pr4671PB:

Estimated mean = 188.54
Estimated read length = 87
Estimated insert gap = 14.54
```

The RNASeq data was aligned to each genome Assembly, commands for each pair of reads are run as separate commands from within separate screen sessions

First pair

```bash
for Assembly in $(ls repeat_masked/P.fragariae/*/filtered_contigs_repmask/*_contigs_softmasked_repeatmasker_TPSI_appended.fa)
do
    Strain=$(echo $Assembly| rev | cut -d '/' -f3 | rev)
    Organism=$(echo $Assembly | rev | cut -d '/' -f4 | rev)
    echo "$Organism - $Strain"
    for RNADir in $(ls -d qc_rna/raw_rna/consortium/P.frag)
    do
        Species=$(echo $RNADir | rev | cut -f1 -d '/' | rev)
        echo "$Species"
        FileF=$(ls $RNADir/F/4*_trim.fq.gz)
        FileR=$(ls $RNADir/R/4*_trim.fq.gz)
        OutDir=alignment/$Organism/$Strain/$Species/1
        InsertGap='25'
        InsertStdDev='28'
        Jobs=$(qstat | grep 'tophat' | grep 'qw' | wc -l)
        while [ $Jobs -gt 1 ]
        do
            sleep 10
            printf "."
            Jobs=$(qstat | grep 'tophat' | grep 'qw' | wc -l)
        done
        printf "\n"
        ProgDir=/home/adamst/git_repos/tools/seq_tools/RNAseq
        qsub $ProgDir/tophat_alignment.sh $Assembly $FileF $FileR $OutDir $InsertGap $InsertStdDev
    done
done
```

Second pair

```bash
for Assembly in $(ls repeat_masked/P.fragariae/*/filtered_contigs_repmask/*_contigs_softmasked_repeatmasker_TPSI_appended.fa)
do
    Strain=$(echo $Assembly| rev | cut -d '/' -f3 | rev)
    Organism=$(echo $Assembly | rev | cut -d '/' -f4 | rev)
    echo "$Organism - $Strain"
    for RNADir in $(ls -d qc_rna/raw_rna/consortium/P.frag)
    do
        Species=$(echo $RNADir | rev | cut -f1 -d '/' | rev)
        echo "$Species"
        FileF=$(ls $RNADir/F/P*_trim.fq.gz)
        FileR=$(ls $RNADir/R/P*_trim.fq.gz)
        OutDir=alignment/$Organism/$Strain/$Species/2
        InsertGap='23'
        InsertStdDev='29'
        Jobs=$(qstat | grep 'tophat' | grep 'qw' | wc -l)
        while [ $Jobs -gt 1 ]
        do
            sleep 10
            printf "."
            Jobs=$(qstat | grep 'tophat' | grep 'qw' | wc -l)
        done
        printf "\n"
        ProgDir=/home/adamst/git_repos/tools/seq_tools/RNAseq
        qsub $ProgDir/tophat_alignment.sh $Assembly $FileF $FileR $OutDir $InsertGap $InsertStdDev
    done
done
```

Third pair

```bash
for Assembly in $(ls repeat_masked/P.fragariae/*/filtered_contigs_repmask/*_contigs_softmasked_repeatmasker_TPSI_appended.fa)
do
    Strain=$(echo $Assembly| rev | cut -d '/' -f3 | rev)
    Organism=$(echo $Assembly | rev | cut -d '/' -f4 | rev)
    echo "$Organism - $Strain"
    for RNADir in $(ls -d qc_rna/raw_rna/consortium/P.rubi)
    do
        Species=$(echo $RNADir | rev | cut -f1 -d '/' | rev)
        echo "$Species"
        FileF=$(ls $RNADir/F/4*_trim.fq.gz)
        FileR=$(ls $RNADir/R/4*_trim.fq.gz)
        OutDir=alignment/$Organism/$Strain/$Species/1
        InsertGap='24'
        InsertStdDev='28'
        Jobs=$(qstat | grep 'tophat' | grep 'qw' | wc -l)
        while [ $Jobs -gt 1 ]
        do
            sleep 10
            printf "."
            Jobs=$(qstat | grep 'tophat' | grep 'qw' | wc -l)
        done
        printf "\n"
        ProgDir=/home/adamst/git_repos/tools/seq_tools/RNAseq
        qsub $ProgDir/tophat_alignment.sh $Assembly $FileF $FileR $OutDir $InsertGap $InsertStdDev
    done
done
```

Fourth pair

```bash
for Assembly in $(ls repeat_masked/P.fragariae/*/filtered_contigs_repmask/*_contigs_softmasked_repeatmasker_TPSI_appended.fa)
do
    Strain=$(echo $Assembly| rev | cut -d '/' -f3 | rev)
    Organism=$(echo $Assembly | rev | cut -d '/' -f4 | rev)
    echo "$Organism - $Strain"
    for RNADir in $(ls -d qc_rna/raw_rna/consortium/P.rubi)
    do
        Species=$(echo $RNADir | rev | cut -f1 -d '/' | rev)
        echo "$Species"
        FileF=$(ls $RNADir/F/P*_trim.fq.gz)
        FileR=$(ls $RNADir/R/P*_trim.fq.gz)
        OutDir=alignment/$Organism/$Strain/$Species/2
        InsertGap='15'
        InsertStdDev='27'
        Jobs=$(qstat | grep 'tophat' | grep 'qw' | wc -l)
        while [ $Jobs -gt 1 ]
        do
            sleep 10
            printf "."
            Jobs=$(qstat | grep 'tophat' | grep 'qw' | wc -l)
        done
        printf "\n"
        ProgDir=/home/adamst/git_repos/tools/seq_tools/RNAseq
        qsub $ProgDir/tophat_alignment.sh $Assembly $FileF $FileR $OutDir $InsertGap $InsertStdDev
    done
done
```

Maria created a script using stampy, which apparently maps better

```bash
for Assembly in $(ls repeat_masked/*/*/filtered_contigs_repmask/*_contigs_unmasked.fa)
do
    Strain=$(echo $Assembly| rev | cut -d '/' -f3 | rev)
    Organism=$(echo $Assembly | rev | cut -d '/' -f4 | rev)
    echo "$Organism - $Strain"
    RNA_Dir=qc_rna/genbank/P.cactorum/10300
    RNA_F=$RNA_Dir/F/*
    RNA_R=$RNA_Dir/R/*
    OutDir=alignment/stampy/$Organism/$Strain
    ProgDir=/home/adamst/git_repos/scripts/stampy
    qsub $ProgDir/sub_stampy.sh $Assembly $RNA_F $RNA_R
done
```

This has had issues running -->

##Use STAR

FALCON and Illumina assemblies aligning shown in RNA-Seq_analysis.md

#Braker prediction

##Alignment outputs were concatenated and Braker1 prediction was run

###Concatenation

```bash
for Strain in Bc1 Bc16 Nov5 A4 Nov27 Nov71 ONT3 Bc23 Nov77 SCRP245_v2 Nov9
do
    Organism=P.fragariae
    echo "$Organism - $Strain"
    Assembly=repeat_masked/*/$Strain/deconseq_Paen_repmask/*_contigs_softmasked_repeatmasker_TPSI_appended.fa
    mkdir -p alignment/$Organism/$Strain/concatenated
    samtools merge -f alignment/$Organism/$Strain/concatenated/concatenated.bam \
    alignment/star/$Organism/$Strain/24hr/TA-07/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/24hr/TA-08/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/24hr/TA-09/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/48hr/TA-12/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/48hr/TA-13/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/48hr/TA-14/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/96hr/TA-18/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/96hr/TA-19/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/96hr/TA-20/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/mycelium/TA-32/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/mycelium/TA-34/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/mycelium/TA-35/star_aligmentAligned.sortedByCoord.out.bam
done
```

For assemblies cleaned for NCBI

```bash
for Strain in Bc1 Nov5 A4 Nov71 SCRP245_v2 Nov9
do
    Organism=P.fragariae
    echo "$Organism - $Strain"
    Assembly=repeat_masked/*/$Strain/ncbi_edits_repmask/*_contigs_softmasked_repeatmasker_TPSI_appended.fa
    mkdir -p alignment/$Organism/$Strain/concatenated
    samtools merge -f alignment/$Organism/$Strain/concatenated/concatenated.bam \
    alignment/star/$Organism/$Strain/24hr/TA-07/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/24hr/TA-08/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/24hr/TA-09/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/48hr/TA-12/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/48hr/TA-13/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/48hr/TA-14/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/96hr/TA-18/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/96hr/TA-19/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/96hr/TA-20/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/mycelium/TA-32/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/mycelium/TA-34/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/mycelium/TA-35/star_aligmentAligned.sortedByCoord.out.bam
done
```

For FALCON assembly

```bash
for Strain in Bc16
do
    Organism=P.fragariae
    echo "$Organism - $Strain"
    Assembly=repeat_masked/*/polished/filtered_contigs_repmask/*_contigs_softmasked_repeatmasker_TPSI_appended.fa
    mkdir -p alignment/$Organism/$Strain/concatenated
    samtools merge -f alignment/$Organism/$Strain/concatenated/concatenated.bam \
    alignment/star/$Organism/$Strain/24hr/TA-07/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/24hr/TA-08/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/24hr/TA-09/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/48hr/TA-12/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/48hr/TA-13/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/48hr/TA-14/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/96hr/TA-18/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/96hr/TA-19/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/96hr/TA-20/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/mycelium/TA-32/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/mycelium/TA-34/star_aligmentAligned.sortedByCoord.out.bam \
    alignment/star/$Organism/$Strain/mycelium/TA-35/star_aligmentAligned.sortedByCoord.out.bam
done
```

###Run Braker1

```bash
for Strain in Nov27 ONT3 Bc23 Nov77
do
    Organism=P.fragariae
    echo "$Organism - $Strain"
    Assembly=repeat_masked/*/$Strain/*/*_contigs_softmasked_repeatmasker_TPSI_appended.fa
    OutDir=gene_pred/braker/$Organism/"$Strain"_braker
    AcceptedHits=alignment/$Organism/$Strain/concatenated/concatenated.bam
    GeneModelName="$Organism"_"$Strain"_braker
    rm -r /home/armita/prog/augustus-3.1/config/species/"$Organism"_"$Strain"_braker
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/braker1
    qsub $ProgDir/sub_braker_fungi.sh $Assembly $OutDir $AcceptedHits $GeneModelName
done
```

For FALCON assembly

```bash
Strain=Bc16
Organism=P.fragariae
Assembly=repeat_masked/*/polished/*/*_contigs_softmasked_repeatmasker_TPSI_appended.fa
OutDir=gene_pred/braker/$Organism/"$Strain"_braker
AcceptedHits=alignment/$Organism/$Strain/concatenated/concatenated.bam
GeneModelName="$Organism"_"$Strain"_braker
rm -r /home/armita/prog/augustus-3.1/config/species/"$Organism"_"$Strain"_braker
ProgDir=/home/adamst/git_repos/tools/gene_prediction/braker1
qsub $ProgDir/sub_braker_fungi.sh $Assembly $OutDir $AcceptedHits $GeneModelName
```

Repeat for assemblies cleaned for ncbi

```bash
for Strain in Bc1 Nov5 A4 Nov71 SCRP245_v2 Nov9
do
    Organism=P.fragariae
    echo "$Organism - $Strain"
    Assembly=repeat_masked/*/$Strain/ncbi_edits_repmask/*_contigs_softmasked_repeatmasker_TPSI_appended.fa
    OutDir=gene_pred/braker/$Organism/"$Strain"_braker
    AcceptedHits=alignment/$Organism/$Strain/concatenated/concatenated.bam
    GeneModelName="$Organism"_"$Strain"_braker
    rm -r /home/armita/prog/augustus-3.1/config/species/"$Organism"_"$Strain"_braker
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/braker1
    qsub $ProgDir/sub_braker_fungi.sh $Assembly $OutDir $AcceptedHits $GeneModelName
done
```

#Supplementing Braker gene models with CodingQuarry genes

Additional genes were added to Braker gene predictions, using CodingQuarry in pathogen mode to predict additional regions.

Firstly, aligned RNAseq data was assembled into transcripts using Cufflinks.

Note - cufflinks doesn't always predict direction of a transcript and therefore features can not be restricted by strand when they are intersected.

```bash
for Strain in Bc1 Nov5 A4 Nov27 Nov71 ONT3 Bc23 Nov77 SCRP245_v2 Nov9
do
    Organism=P.fragariae
    echo "$Organism - $Strain"
    Assembly=repeat_masked/*/$Strain/*/*_contigs_unmasked.fa
    OutDir=gene_pred/star/cufflinks/$Organism/$Strain/concatenated
    mkdir -p $OutDir
    AcceptedHits=alignment/$Organism/$Strain/concatenated/concatenated.bam
    ProgDir=/home/adamst/git_repos/tools/seq_tools/RNAseq
    qsub $ProgDir/sub_cufflinks.sh $AcceptedHits $OutDir
done
```

For FALCON assembly

```bash
Strain=Bc16
Organism=P.fragariae
Assembly=repeat_masked/*/polished/*/*_contigs_unmasked.fa
OutDir=gene_pred/star/cufflinks/$Organism/$Strain/concatenated
mkdir -p $OutDir
AcceptedHits=alignment/$Organism/$Strain/concatenated/concatenated.bam
ProgDir=/home/adamst/git_repos/tools/seq_tools/RNAseq
qsub $ProgDir/sub_cufflinks.sh $AcceptedHits $OutDir
```

Repeat for assemblies cleaned for NCBI

```bash
for Strain in Bc1 Nov5 A4 Nov71 SCRP245_v2 Nov9
do
    Organism=P.fragariae
    echo "$Organism - $Strain"
    Assembly=repeat_masked/*/$Strain/ncbi_edits_repmask/*_contigs_unmasked.fa
    OutDir=gene_pred/star/cufflinks/$Organism/$Strain/concatenated
    mkdir -p $OutDir
    AcceptedHits=alignment/$Organism/$Strain/concatenated/concatenated.bam
    ProgDir=/home/adamst/git_repos/tools/seq_tools/RNAseq
    qsub $ProgDir/sub_cufflinks.sh $AcceptedHits $OutDir
done
```

Secondly, genes were predicted using CodingQuarry:

```bash
for Strain in Nov27 ONT3 Bc23 Nov77
do
    Organism=P.fragariae
    echo "$Organism - $Strain"
    Assembly=repeat_masked/*/$Strain/deconseq_Paen_repmask/*_contigs_softmasked_repeatmasker_TPSI_appended.fa
    OutDir=gene_pred/codingquarry/$Organism/$Strain
    CufflinksGTF=gene_pred/star/cufflinks/$Organism/$Strain/concatenated/transcripts.gtf
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/codingquary
    qsub $ProgDir/sub_CodingQuary.sh $Assembly $CufflinksGTF $OutDir
done
```

Repeat for assemblies cleaned for NCBI

```bash
for Strain in Bc1 Nov5 A4 Nov71 SCRP245_v2 Nov9
do
    Organism=P.fragariae
    echo "$Organism - $Strain"
    Assembly=repeat_masked/*/$Strain/ncbi_edits_repmask/*_contigs_softmasked_repeatmasker_TPSI_appended.fa
    OutDir=gene_pred/codingquarry/$Organism/$Strain
    CufflinksGTF=gene_pred/star/cufflinks/$Organism/$Strain/concatenated/transcripts.gtf
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/codingquary
    qsub $ProgDir/sub_CodingQuary.sh $Assembly $CufflinksGTF $OutDir
done
```

For FALCON assembly

```bash
Strain=Bc16
Organism=P.fragariae
echo "$Organism - $Strain"
Assembly=repeat_masked/*/polished/*/*_contigs_softmasked_repeatmasker_TPSI_appended.fa
OutDir=gene_pred/codingquarry/$Organism/$Strain
CufflinksGTF=gene_pred/star/cufflinks/$Organism/$Strain/concatenated/transcripts.gtf
ProgDir=/home/adamst/git_repos/tools/gene_prediction/codingquary
qsub $ProgDir/sub_CodingQuary.sh $Assembly $CufflinksGTF $OutDir
```

Then, additional transcripts were added to Braker1 gene models, when CodingQuarry genes were predicted in regions of the genome, not containing Braker1 gene models. This had a bug that Andy corrected:

For set of assemblies not cleaned for NCBI:

```bash
for BrakerGff in $(ls gene_pred/braker/*/*_braker/*/augustus.gff3)
do
    Strain=$(echo $BrakerGff| rev | cut -d '/' -f3 | rev | sed 's/_braker//g')
    Organism=$(echo $BrakerGff | rev | cut -d '/' -f4 | rev)
    echo "$Organism - $Strain"
    if [ -f repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    elif [ -f repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    else
        Assembly=$(ls repeat_masked/quiver_results/Bc16/filtered_contigs_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    fi
    CodingQuarryGff=gene_pred/codingquarry/$Organism/$Strain/out/PredictedPass.gff3
    PGNGff=gene_pred/codingquarry/$Organism/$Strain/out/PGN_predictedPass.gff3
    AddDir=gene_pred/codingquarry/$Organism/$Strain/additional
    FinalDir=gene_pred/final/$Organism/$Strain/final
    AddGenesList=$AddDir/additional_genes.txt
    AddGenesGff=$AddDir/additional_genes.gff
    FinalGff=$AddDir/combined_genes.gff
    mkdir -p $AddDir
    mkdir -p $FinalDir

    bedtools intersect -v -a $CodingQuarryGff -b $BrakerGff | grep 'gene'| cut -f2 -d'=' | cut -f1 -d';' > $AddGenesList
    bedtools intersect -v -a $PGNGff -b $BrakerGff | grep 'gene'| cut -f2 -d'=' | cut -f1 -d';' >> $AddGenesList
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
    $ProgDir/gene_list_to_gff.pl $AddGenesList $CodingQuarryGff CodingQuarry_v2.0 ID CodingQuary > $AddGenesGff
    $ProgDir/gene_list_to_gff.pl $AddGenesList $PGNGff PGNCodingQuarry_v2.0 ID CodingQuary >> $AddGenesGff
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/codingquary
    # -
    # This section is edited
    $ProgDir/add_CodingQuary_features.pl $AddGenesGff $Assembly > $AddDir/add_genes_CodingQuarry_unspliced.gff3
    $ProgDir/correct_CodingQuary_splicing.py --inp_gff $AddDir/add_genes_CodingQuarry_unspliced.gff3 > $FinalDir/final_genes_CodingQuarry.gff3
    # -
    $ProgDir/gff2fasta.pl $Assembly $FinalDir/final_genes_CodingQuarry.gff3 $FinalDir/final_genes_CodingQuarry
    cp $BrakerGff $FinalDir/final_genes_Braker.gff3
    $ProgDir/gff2fasta.pl $Assembly $FinalDir/final_genes_Braker.gff3 $FinalDir/final_genes_Braker
    cat $FinalDir/final_genes_Braker.pep.fasta $FinalDir/final_genes_CodingQuarry.pep.fasta | sed -r 's/\*/X/g' > $FinalDir/final_genes_combined.pep.fasta
    cat $FinalDir/final_genes_Braker.cdna.fasta $FinalDir/final_genes_CodingQuarry.cdna.fasta > $FinalDir/final_genes_combined.cdna.fasta
    cat $FinalDir/final_genes_Braker.gene.fasta $FinalDir/final_genes_CodingQuarry.gene.fasta > $FinalDir/final_genes_combined.gene.fasta
    cat $FinalDir/final_genes_Braker.upstream3000.fasta $FinalDir/final_genes_CodingQuarry.upstream3000.fasta > $FinalDir/final_genes_combined.upstream3000.fasta


    GffBraker=$FinalDir/final_genes_Braker.gff3
    GffQuarry=$FinalDir/final_genes_CodingQuarry.gff3
    GffAppended=$FinalDir/final_genes_appended.gff3
    cat $GffBraker $GffQuarry > $GffAppended
done
```

Then, remove duplicated transcripts

```bash
for GffAppended in $(ls gene_pred/final/*/*/final/final_genes_appended.gff3)
do
    Strain=$(echo $GffAppended | rev | cut -d '/' -f3 | rev)
    Organism=$(echo $GffAppended | rev | cut -d '/' -f4 | rev)
    echo "$Organism - $Strain"
    FinalDir=gene_pred/final/$Organism/$Strain/final
    GffFiltered=$FinalDir/filtered_duplicates.gff
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/codingquary
    $ProgDir/remove_dup_features.py --inp_gff $GffAppended --out_gff $GffFiltered
    GffRenamed=$FinalDir/final_genes_appended_renamed.gff3
    LogFile=$FinalDir/final_genes_appended_renamed.log
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/codingquary
    $ProgDir/gff_rename_genes.py --inp_gff $GffFiltered --conversion_log $LogFile > $GffRenamed
    rm $GffFiltered
    if [ -f repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    elif [ -f repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    else
        Assembly=$(ls repeat_masked/quiver_results/Bc16/filtered_contigs_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    fi
    $ProgDir/gff2fasta.pl $Assembly $GffRenamed gene_pred/final/$Organism/$Strain/final/final_genes_appended_renamed
    # The proteins fasta file contains * instead of Xs for stop codons, these should
    # be changed
    sed -i 's/\*/X/g' gene_pred/final/$Organism/$Strain/final/final_genes_appended_renamed.pep.fasta
done
```

The final number of genes per isolate was observed using:

```bash
for DirPath in $(ls -d gene_pred/final/P.*/*/final)
do
    echo $DirPath
    echo Braker:
    cat $DirPath/final_genes_Braker.pep.fasta | grep '>' | wc -l
    echo CodingQuarry:
    cat $DirPath/final_genes_CodingQuarry.pep.fasta | grep '>' | wc -l
    echo Total:
    cat $DirPath/final_genes_combined.pep.fasta | grep '>' | wc -l
    echo ""
done
```

```
A4
Braker:
31,329
CodingQuarry:
2,365
Total:
33,964

Bc16
Braker:
31,846
CodingQuarry:
4,752
Total:
36,598

Bc1
Braker:
30,365
CodingQuarry:
2,784
Total:
33,149

Bc23
Braker:
30,561
CodingQuarry:
2,556
Total:
33,117

Nov27
Braker:
30,547
CodingQuarry:
2,748
Total:
33,295

Nov5
Braker:
30,781
CodingQuarry:
2,497
Total:
33,278

Nov71
Braker:
30,341
CodingQuarry:
2,508
Total:
32,849

Nov77
Braker:
30,485
CodingQuarry:
2,653
Total:
33,138

Nov9
Braker:
30,367
CodingQuarry:
2,561
Total:
32,928

ONT3
Braker:
33,982
CodingQuarry:
2,872
Total:
36,854

SCRP245_v2
Braker:
34,774
CodingQuarry:
2,564
Total:
37,338
```

##Predicted gene set assessed using BUSCO to assess completeness

```bash
for Transcriptome in $(ls gene_pred/final/*/*/final/final_genes_combined.gene.fasta)
do
    Strain=$(echo $Transcriptome| rev | cut -d '/' -f3 | rev)
    Organism=$(echo $Transcriptome | rev | cut -d '/' -f4 | rev)
    echo "$Organism - $Strain"
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/busco
    BuscoDB=Eukaryotic
    OutDir=gene_pred/busco/$Organism/$Strain/
    qsub $ProgDir/sub_busco3.sh $Transcriptome $BuscoDB $OutDir
done
```

```
A4
Complete and single copy genes: 271
Complete and duplicated genes: 7
Fragmented genes: 10
Missing genes: 15

Bc16
Complete and single copy genes: 263
Complete and duplicated genes: 9
Fragmented genes: 10
Missing genes: 21

Bc1
Complete and single copy genes: 273
Complete and duplicated genes: 7
Fragmented genes: 8
Missing genes: 15

Bc23
Complete and single copy genes: 273
Complete and duplicated genes: 7
Fragmented genes: 8
Missing genes: 15

Nov27
Complete and single copy genes: 273
Complete and duplicated genes: 7
Fragmented genes: 8
Missing genes: 15

Nov5
Complete and single copy genes: 273
Complete and duplicated genes: 7
Fragmented genes: 8
Missing genes: 15

Nov71
Complete and single copy genes: 271
Complete and duplicated genes: 7
Fragmented genes: 10
Missing genes: 15

Nov77
Complete and single copy genes: 272
Complete and duplicated genes: 7
Fragmented genes: 9
Missing genes: 15

Nov9
Complete and single copy genes: 273
Complete and duplicated genes: 7
Fragmented genes: 8
Missing genes: 15

ONT3
Complete and single copy genes: 275
Complete and duplicated genes: 8
Fragmented genes: 7
Missing genes: 13

SCRP245_v2
Complete and single copy genes: 273
Complete and duplicated genes: 7
Fragmented genes: 8
Missing genes: 15
```

Changes with respect to genome sequence

```
A4
Complete and single copy genes: -3
Complete and duplicated genes: +1
Fragmented genes: +4
Missing genes: -2

Bc16
Complete and single copy genes: -3
Complete and duplicated genes: 0
Fragmented genes: +5
Missing genes: -2

Bc1
Complete and single copy genes: -1
Complete and duplicated genes: +1
Fragmented genes: +2
Missing genes: -2

Bc23
Complete and single copy genes: -2
Complete and duplicated genes: +2
Fragmented genes: +1
Missing genes: -1

Nov27
Complete and single copy genes: 0
Complete and duplicated genes: +1
Fragmented genes: +1
Missing genes: -2

Nov5
Complete and single copy genes: 0
Complete and duplicated genes: 0
Fragmented genes: +2
Missing genes: -2

Nov71
Complete and single copy genes: -3
Complete and duplicated genes: +1
Fragmented genes: +4
Missing genes: -2

Nov77
Complete and single copy genes: 0
Complete and duplicated genes: -1
Fragmented genes: +3
Missing genes: -2

Nov9
Complete and single copy genes: 0
Complete and duplicated genes: +1
Fragmented genes: +1
Missing genes: -2

ONT3
Complete and single copy genes: -2
Complete and duplicated genes: +1
Fragmented genes: +3
Missing genes: -2

SCRP245_v2
Complete and single copy genes: 0
Complete and duplicated genes: 0
Fragmented genes: +1
Missing genes: -1
```

#Gene prediction 2 - atg.pl prediction of ORFs

Open reading frame predictions were made using the atg.pl script as part of the path_pipe.sh pipeline. This pipeline also identifies open reading frames containing Signal peptide sequences and RxLRs. This pipeline was run with the following commands:

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    Organism=P.fragariae
    if [ -f repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_unmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_unmasked.fa)
        echo $Assembly
    elif [ -f repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_unmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_unmasked.fa)
        echo $Assembly
    else
        Assembly=$(ls repeat_masked/quiver_results/polished/filtered_contigs_repmask/*_unmasked.fa)
        echo $Assembly
    fi
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    qsub $ProgDir/run_ORF_finder.sh $Assembly
done
```

The Gff files from the the ORF finder are not in true Gff3 format. These were corrected using the following commands:

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
for OrfGff in $(ls gene_pred/ORF_finder/*/*/*_ORF.gff | grep -v 'atg')
do
    echo "$OrfGff"
    OrfGffMod=$(echo $OrfGff | sed 's/.gff/.gff3/g')
    $ProgDir/gff_corrector.pl $OrfGff > $OrfGffMod
done
```

The final number of genes per isolate was observed using:

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov9 Nov71 Nov77 ONT3 SCRP245_v2
do
    for DirPath in $(ls -d gene_pred/ORF_finder/*/$Strain)
    do
        echo $DirPath
        cat $DirPath/*aa_cat.fa | grep '>' | wc -l
        echo ""
    done
done
```

```
ORF_finder - A4
654,457

ORF_finder - Bc1
657,394

ORF_finder - Bc16
776,126

ORF_finder - Bc23
648,130

ORF_finder - Nov27
653,798

ORF_finder - Nov5
654,072

ORF_finder - Nov9
660,249

ORF_finder - Nov71
649,542

ORF_finder - Nov77
653,276

ORF_finder - ONT3
722,865

ORF_finder - SCRP245_v2
689,938
```

#Genomic analysis

##RxLR genes

Putative RxLR genes were identified within Augustus gene models using a number of approaches:

A) From Augustus gene models - Signal peptide & RxLR motif
B) From Augustus gene models - Hmm evidence of WY domains
C) From Augustus gene models - Hmm evidence of RxLR effectors
D) From Augustus gene models - Hmm evidence of CRN effectors
E) From ORF fragments - Signal peptide & RxLR motif
F) From ORF fragments - Hmm evidence of WY domains
G) From ORF fragments - Hmm evidence of RxLR effectors
H) From ORF fragments - Hmm evidence of CRN effectors

##A) From Augustus gene models - Signal peptide & RxLR motif

Required programs:

SigP
biopython

####A.1) Signal peptide prediction using SignalP 2.0, 3.0 & 4.1

Proteins that were predicted to contain signal peptides were identified using the following commands:

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for Proteome in $(ls gene_pred/final/*/$Strain/final/final_genes_combined.pep.fasta)
    do
        SplitfileDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
        ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
        Organism=P.fragariae
        SplitDir=gene_pred/final_split/$Organism/$Strain
        mkdir -p $SplitDir
        BaseName="$Organism""_$Strain"
        $SplitfileDir/splitfile_500.py --inp_fasta $Proteome --out_dir $SplitDir --out_base $BaseName
        for File in $(ls $SplitDir/*_"$Strain"_*)
        do
            Jobs=$(qstat | grep 'pred_sigP' | wc -l)
            while [ $Jobs -gt 20 ]
            do
                sleep 1
                printf "."
                Jobs=$(qstat | grep 'pred_sigP' | wc -l)
            done  
            printf "\n"
            echo $File
            qsub $ProgDir/pred_sigP.sh $File
            qsub $ProgDir/pred_sigP.sh $File signalp-3.0
            qsub $ProgDir/pred_sigP.sh $File signalp-4.1
        done
    done
done
```

The batch files of predicted secreted proteins needed to be combined into a single file for each strain. This was done with the following commands:

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for SplitDir in $(ls -d gene_pred/final_split/P.*/$Strain)
    do
        Organism=P.fragariae
        echo "$Organism - $Strain"
        for SigpDir in $(ls -d gene_pred/final_sig* | cut -f2 -d'/')
        do
            InStringAA=''
            InStringNeg=''
            InStringTab=''
            InStringTxt=''
            for GRP in $(ls -l $SplitDir/*_"$Strain"_*.fa | rev | cut -d '_' -f1 | rev | sort -n)
            do  
                InStringAA="$InStringAA gene_pred/$SigpDir/$Organism/$Strain/split/"$Organism"_"$Strain"_"$GRP"_sp.aa"
                InStringNeg="$InStringNeg gene_pred/$SigpDir/$Organism/$Strain/split/"$Organism"_"$Strain"_"$GRP"_sp_neg.aa"
                InStringTab="$InStringTab gene_pred/$SigpDir/$Organism/$Strain/split/"$Organism"_"$Strain"_"$GRP"_sp.tab"
                InStringTxt="$InStringTxt gene_pred/$SigpDir/$Organism/$Strain/split/"$Organism"_"$Strain"_"$GRP"_sp.txt"
            done
            cat $InStringAA > gene_pred/$SigpDir/$Organism/$Strain/"$Strain"_aug_sp.aa
            cat $InStringNeg > gene_pred/$SigpDir/$Organism/$Strain/"$Strain"_aug_neg_sp.aa
            tail -n +2 -q $InStringTab > gene_pred/$SigpDir/$Organism/$Strain/"$Strain"_aug_sp.tab
            cat $InStringTxt > gene_pred/$SigpDir/$Organism/$Strain/"$Strain"_aug_sp.txt
        done
    done
done
```

####B.2) Prediction using Phobius

Secreted proteins were also predicted using Phobius

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for Proteome in $(ls gene_pred/final/*/$Strain/final/final_genes_combined.pep.fasta)
    do
        Organism=P.fragariae
        echo "$Organism - $Strain"
        OutDir=analysis/phobius_CQ/$Organism/$Strain
        mkdir -p $OutDir
        phobius.pl $Proteome > $OutDir/"$Strain"_phobius.txt
        ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
        $ProgDir/phobius_parser.py --inp_fasta $Proteome --phobius_txt $OutDir/"$Strain"_phobius.txt --out_fasta $OutDir/"$Strain"_phobius.fa
    done
done
```

Secreted proteins from different sources were combined into a single file:

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for Proteome in $(ls gene_pred/final/*/$Strain/final/final_genes_combined.pep.fasta)
    do
        Organism=$(echo $Proteome | rev | cut -f4 -d '/' | rev)
        echo "$Organism - $Strain"
        OutDir=gene_pred/combined_sigP_CQ/$Organism/$Strain
        mkdir -p $OutDir
        echo "The following number of sequences were predicted as secreted:"
        cat gene_pred/final_sig*/$Organism/$Strain/*_aug_sp.aa analysis/phobius_CQ/$Organism/$Strain/"$Strain"_phobius.fa > $OutDir/"$Strain"_all_secreted.fa
        cat $OutDir/"$Strain"_all_secreted.fa | grep '>' | wc -l
        echo "This represented the following number of unique genes:"
        cat gene_pred/final_sig*/$Organism/$Strain/*_aug_sp.aa analysis/phobius_CQ/$Organism/$Strain/"$Strain"_phobius.fa | grep '>' | cut -f1 | tr -d ' >' | sort -g | uniq > $OutDir/"$Strain"_secreted.txt
        ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
        $ProgDir/extract_from_fasta.py --fasta $Proteome --headers $OutDir/"$Strain"_secreted.txt > $OutDir/"$Strain"_secreted.fa
        cat $OutDir/"$Strain"_secreted.fa | grep '>' | wc -l
    done
done
```

```
P.fragariae - A4
The following number of sequences were predicted as secreted:
11,042
This represented the following number of unique genes:
3,751
P.fragariae - Bc1
The following number of sequences were predicted as secreted:
11,152
This represented the following number of unique genes:
3,765
P.fragariae - Bc16
The following number of sequences were predicted as secreted:
12,785
This represented the following number of unique genes:
4,300
P.fragariae - Bc23
The following number of sequences were predicted as secreted:
11,043
This represented the following number of unique genes:
3,731
P.fragariae - Nov27
The following number of sequences were predicted as secreted:
11,113
This represented the following number of unique genes:
3,772
P.fragariae - Nov5
The following number of sequences were predicted as secreted:
11,110
This represented the following number of unique genes:
3,762
P.fragariae - Nov71
The following number of sequences were predicted as secreted:
11,135
This represented the following number of unique genes:
3,763
P.fragariae - Nov77
The following number of sequences were predicted as secreted:
11,085
This represented the following number of unique genes:
3,750
P.fragariae - Nov9
The following number of sequences were predicted as secreted:
11,302
This represented the following number of unique genes:
3,809
P.fragariae - ONT3
The following number of sequences were predicted as secreted:
12,473
This represented the following number of unique genes:
4,297
P.fragariae - SCRP245_v2
The following number of sequences were predicted as secreted:
11,935
This represented the following number of unique genes:
4,078
```

The regular expression R.LR.{,40}[ED][ED][KR] has previously been used to identify RxLR effectors. The addition of an EER motif is significant as it has been shown as required for host uptake of the protein.

The RxLR_EER_regex_finder.py script was used to search for this regular expression and annotate the EER domain where present.

```bash
for Secretome in $(ls gene_pred/combined_sigP_CQ/*/*/*_all_secreted.fa)
do
    Strain=$(echo $Secretome | rev | cut -d '/' -f2 | rev)
    Organism=$(echo $Secretome | rev |  cut -d '/' -f3 | rev)
    Proteome=$(ls gene_pred/final/$Organism/$Strain/final/final_genes_combined.pep.fasta)
    Gff=$(ls gene_pred/final/$Organism/$Strain/final/final_genes_appended.gff3)
    OutDir=analysis/RxLR_effectors/RxLR_EER_regex_finder/"$Organism"/"$Strain"
    mkdir -p $OutDir
    printf "\nstrain: $Strain\tspecies: $Organism\n"
    printf "the total number of SigP gene is:\t"
    cat $Secretome | grep '>' | wc -l
    printf "the number of unique SigP gene is:\t"
    cat $Secretome | grep '>' | cut -f1 | tr -d ' '| sort | uniq | wc -l
    printf "the number of SigP-RxLR genes are:\t"
    ProgDir=/home/adamst/git_repos/tools/pathogen/RxLR_effectors
    $ProgDir/RxLR_EER_regex_finder.py $Secretome > $OutDir/"$Strain"_all_secreted_RxLR_regex.fa
    cat $OutDir/"$Strain"_all_secreted_RxLR_regex.fa | grep '>' | cut -f1 | tr -d '>' | tr -d ' ' | sort -g | uniq > $OutDir/"$Strain"_RxLR_regex.txt
    cat $OutDir/"$Strain"_RxLR_regex.txt | wc -l
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    $ProgDir/extract_from_fasta.py --fasta $Proteome --headers $OutDir/"$Strain"_RxLR_regex.txt > $OutDir/"$Strain"_RxLR_EER_regex.fa
    printf "the number of SigP-RxLR-EER genes are:\t"
    cat $OutDir/"$Strain"_all_secreted_RxLR_regex.fa | grep '>' | grep 'EER_motif_start' | cut -f1 | tr -d '>' | tr -d ' ' | sort -g | uniq > $OutDir/"$Strain"_RxLR_EER_regex.txt
    cat $OutDir/"$Strain"_RxLR_EER_regex.txt | wc -l
    $ProgDir/extract_from_fasta.py --fasta $Proteome --headers $OutDir/"$Strain"_RxLR_EER_regex.txt > $OutDir/"$Strain"_RxLR_EER_regex.fa
    printf "\n"
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
    sed -i -r 's/\.t.*//' $OutDir/"$Strain"_RxLR_regex.txt
    sed -i -r 's/\.t.*//' $OutDir/"$Strain"_RxLR_EER_regex.txt
    cat $Gff | grep -w -f $OutDir/"$Strain"_RxLR_regex.txt> $OutDir/"$Strain"_RxLR_regex.gff3
    cat $Gff | grep -w -f $OutDir/"$Strain"_RxLR_EER_regex.txt > $OutDir/"$Strain"_RxLR_EER_regex.gff3
    echo "$Strain complete"
done
```

```
strain: A4      species: P.fragariae
the total number of SigP gene is:       11,042
the number of unique SigP gene is:      3,751
the number of SigP-RxLR genes are:      379
the number of SigP-RxLR-EER genes are:  189


strain: Bc16    species: P.fragariae
the total number of SigP gene is:       12,785
the number of unique SigP gene is:      4,300
the number of SigP-RxLR genes are:      449
the number of SigP-RxLR-EER genes are:  207


strain: Bc1     species: P.fragariae
the total number of SigP gene is:       11,152
the number of unique SigP gene is:      3,765
the number of SigP-RxLR genes are:      382
the number of SigP-RxLR-EER genes are:  192


strain: Bc23    species: P.fragariae
the total number of SigP gene is:       11,043
the number of unique SigP gene is:      3,731
the number of SigP-RxLR genes are:      372
the number of SigP-RxLR-EER genes are:  191


strain: Nov27   species: P.fragariae
the total number of SigP gene is:       11,113
the number of unique SigP gene is:      3,772
the number of SigP-RxLR genes are:      375
the number of SigP-RxLR-EER genes are:  187


strain: Nov5    species: P.fragariae
the total number of SigP gene is:       11,110
the number of unique SigP gene is:      3,762
the number of SigP-RxLR genes are:      388
the number of SigP-RxLR-EER genes are:  194


strain: Nov71   species: P.fragariae
the total number of SigP gene is:       11,135
the number of unique SigP gene is:      3,763
the number of SigP-RxLR genes are:      389
the number of SigP-RxLR-EER genes are:  190


strain: Nov77   species: P.fragariae
the total number of SigP gene is:       11,085
the number of unique SigP gene is:      3,750
the number of SigP-RxLR genes are:      357
the number of SigP-RxLR-EER genes are:  170


strain: Nov9    species: P.fragariae
the total number of SigP gene is:       11,302
the number of unique SigP gene is:      3,809
the number of SigP-RxLR genes are:      375
the number of SigP-RxLR-EER genes are:  191


strain: ONT3    species: P.fragariae
the total number of SigP gene is:       12,473
the number of unique SigP gene is:      4,297
the number of SigP-RxLR genes are:      395
the number of SigP-RxLR-EER genes are:  191


strain: SCRP245_v2      species: P.fragariae
the total number of SigP gene is:       11,935
the number of unique SigP gene is:      4,078
the number of SigP-RxLR genes are:      383
the number of SigP-RxLR-EER genes are:  189
```

####F) From Secreted gene models - Hmm evidence of RxLR effectors

```bash
for Strain in A4 Bc16 Bc1 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for Proteome in $(ls gene_pred/final/*/$Strain/final/final_genes_combined.pep.fasta)
    do
        ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer
        HmmModel=/home/armita/git_repos/emr_repos/SI_Whisson_et_al_2007/cropped.hmm
        Organism=$(echo $Proteome | rev | cut -f4 -d '/' | rev)
        OutDir=analysis/RxLR_effectors/hmmer_RxLR/$Organism/$Strain
        mkdir -p $OutDir
        HmmResults="$Strain"_RxLR_hmmer.txt
        hmmsearch -T 0 $HmmModel $Proteome > $OutDir/$HmmResults
        echo "$Organism $Strain"
        cat $OutDir/$HmmResults | grep 'Initial search space'
        cat $OutDir/$HmmResults | grep 'number of targets reported over threshold'
        HmmFasta="$Strain"_RxLR_hmmer.fa
        $ProgDir/hmmer2fasta.pl $OutDir/$HmmResults $Proteome > $OutDir/$HmmFasta
        Headers="$Strain"_RxLR_hmmer_headers.txt
        cat $OutDir/$HmmFasta | grep '>' | cut -f1 | tr -d '>' | sed -r 's/\.t.*//' | tr -d ' ' | sort | uniq > $OutDir/$Headers
        Gff=$(ls gene_pred/final/$Organism/$Strain/final/final_genes_appended.gff3)
        cat $Gff | grep -w -f $OutDir/$Headers > $OutDir/"$Strain"_Aug_RxLR_regex.gff3
        echo "$Strain complete"
    done
done
```

```
P.fragariae A4
Initial search space (Z):             33,586  [actual number of targets]
Domain search space  (domZ):             186  [number of targets reported over threshold]
P.fragariae Bc16
Initial search space (Z):             36,598  [actual number of targets]
Domain search space  (domZ):             217  [number of targets reported over threshold]
P.fragariae Bc1
Initial search space (Z):             33,063  [actual number of targets]
Domain search space  (domZ):             190  [number of targets reported over threshold]
P.fragariae Bc23
Initial search space (Z):             33,039  [actual number of targets]
Domain search space  (domZ):             196  [number of targets reported over threshold]
P.fragariae Nov27
Initial search space (Z):             33,171  [actual number of targets]
Domain search space  (domZ):             189  [number of targets reported over threshold]
P.fragariae Nov5
Initial search space (Z):             33,278  [actual number of targets]
Domain search space  (domZ):             193  [number of targets reported over threshold]
P.fragariae Nov71
Initial search space (Z):             32,775  [actual number of targets]
Domain search space  (domZ):             190  [number of targets reported over threshold]
P.fragariae Nov77
Initial search space (Z):             33,068  [actual number of targets]
Domain search space  (domZ):             180  [number of targets reported over threshold]
P.fragariae Nov9
Initial search space (Z):             32,815  [actual number of targets]
Domain search space  (domZ):             193  [number of targets reported over threshold]
P.fragariae ONT3
Initial search space (Z):             36,913  [actual number of targets]
Domain search space  (domZ):             189  [number of targets reported over threshold]
P.fragariae SCRP245_v2
Initial search space (Z):             36,817  [actual number of targets]
Domain search space  (domZ):             193  [number of targets reported over threshold]
```

####G) Combining RxLRs from Regex and hmm searches

The total RxLRs are found by combining different sources:

```bash
echo "Without EER"
for RegexRxLR in $(ls analysis/RxLR_effectors/RxLR_EER_regex_finder/*/*/*_RxLR_regex.txt)
do
    Organism=$(echo $RegexRxLR | rev |  cut -d '/' -f3 | rev)
    Strain=$(echo $RegexRxLR | rev | cut -d '/' -f2 | rev)
    Gff=$(ls gene_pred/final/$Organism/$Strain/final/final_genes_appended.gff3)
    Proteome=$(ls gene_pred/final/$Organism/$Strain/final/final_genes_combined.pep.fasta)
    HmmRxLR=analysis/RxLR_effectors/hmmer_RxLR/$Organism/$Strain/*_RxLR_hmmer_headers.txt
    echo "$Organism - $Strain"
    echo "Number of RxLRs identified by Regex:"
    cat $RegexRxLR | sort | uniq | wc -l
    echo "Number of RxLRs identified by Hmm:"
    cat $HmmRxLR | sort | uniq | wc -l
    echo "Number of RxLRs in combined dataset:"
    cat $RegexRxLR $HmmRxLR | sort | uniq | wc -l
    # echo "Number of RxLRs in both datasets:"
    # cat $RegexRxLR $HmmRxLR | sort | uniq -d | wc -l
    echo ""
    # echo "Extracting RxLRs from datasets"
    OutDir=analysis/RxLR_effectors/combined_evidence/$Organism/$Strain
    mkdir -p $OutDir
    cat $RegexRxLR $HmmRxLR | sort | uniq > $OutDir/"$Strain"_total_RxLR_headers.txt
    Gff=$(ls gene_pred/final/$Organism/$Strain/final/final_genes_appended.gff3)
    cat $Gff | grep -w -f $OutDir/"$Strain"_total_RxLR_headers.txt > $OutDir/"$Strain"_total_RxLR.gff
    echo "Number of genes in the extracted gff file:"
    cat $OutDir/"$Strain"_total_RxLR.gff | grep -w 'gene' | wc -l
    echo "$Strain complete without EER"
done

echo "With EER"
for RegexRxLR in $(ls analysis/RxLR_effectors/RxLR_EER_regex_finder/*/*/*_RxLR_EER_regex.txt)
do
    Organism=$(echo $RegexRxLR | rev |  cut -d '/' -f3 | rev)
    Strain=$(echo $RegexRxLR | rev | cut -d '/' -f2 | rev)
    Gff=$(ls gene_pred/final/$Organism/$Strain/final/final_genes_appended.gff3)
    Proteome=$(ls gene_pred/final/$Organism/$Strain/final/final_genes_combined.pep.fasta)
    HmmRxLR=analysis/RxLR_effectors/hmmer_RxLR/$Organism/$Strain/*_RxLR_hmmer_headers.txt
    echo "$Organism - $Strain"
    echo "Number of RxLRs identified by Regex:"
    cat $RegexRxLR | sort | uniq | wc -l
    echo "Number of RxLRs identified by Hmm:"
    cat $HmmRxLR | sort | uniq | wc -l
    echo "Number of RxLRs in combined dataset:"
    cat $RegexRxLR $HmmRxLR | sort | uniq | wc -l
    # echo "Number of RxLRs in both datasets:"
    # cat $RegexRxLR $HmmRxLR | sort | uniq -d | wc -l
    echo ""
    # echo "Extracting RxLRs from datasets"
    OutDir=analysis/RxLR_effectors/combined_evidence/$Organism/$Strain
    mkdir -p $OutDir
    cat $RegexRxLR $HmmRxLR | sort | uniq > $OutDir/"$Strain"_total_RxLR_EER_headers.txt
    Gff=$(ls gene_pred/final/$Organism/$Strain/final/final_genes_appended.gff3)
    cat $Gff | grep -w -f $OutDir/"$Strain"_total_RxLR_EER_headers.txt > $OutDir/"$Strain"_total_RxLR_EER.gff
    echo "Number of genes in the extracted gff file:"
    cat $OutDir/"$Strain"_total_RxLR_EER.gff | grep -w 'gene' | wc -l
    echo "$Strain complete with EER"
done
```

```
With EER:
P.fragariae - A4
Number of RxLRs identified by Regex:
189
Number of RxLRs identified by Hmm:
186
Number of RxLRs in combined dataset:
228
Number of genes in the extracted gff file:
228
P.fragariae - Bc16
Number of RxLRs identified by Regex:
205
Number of RxLRs identified by Hmm:
215
Number of RxLRs in combined dataset:
259
Number of genes in the extracted gff file:
259
P.fragariae - Bc1
Number of RxLRs identified by Regex:
190
Number of RxLRs identified by Hmm:
188
Number of RxLRs in combined dataset:
230
Number of genes in the extracted gff file:
230
P.fragariae - Bc23
Number of RxLRs identified by Regex:
191
Number of RxLRs identified by Hmm:
196
Number of RxLRs in combined dataset:
238
Number of genes in the extracted gff file:
238
P.fragariae - Nov27
Number of RxLRs identified by Regex:
187
Number of RxLRs identified by Hmm:
189
Number of RxLRs in combined dataset:
230
Number of genes in the extracted gff file:
230
P.fragariae - Nov5
Number of RxLRs identified by Regex:
194
Number of RxLRs identified by Hmm:
193
Number of RxLRs in combined dataset:
235
Number of genes in the extracted gff file:
235
P.fragariae - Nov71
Number of RxLRs identified by Regex:
190
Number of RxLRs identified by Hmm:
190
Number of RxLRs in combined dataset:
230
Number of genes in the extracted gff file:
230
P.fragariae - Nov77
Number of RxLRs identified by Regex:
170
Number of RxLRs identified by Hmm:
180
Number of RxLRs in combined dataset:
215
Number of genes in the extracted gff file:
215
P.fragariae - Nov9
Number of RxLRs identified by Regex:
191
Number of RxLRs identified by Hmm:
193
Number of RxLRs in combined dataset:
233
Number of genes in the extracted gff file:
233
P.fragariae - ONT3
Number of RxLRs identified by Regex:
191
Number of RxLRs identified by Hmm:
189
Number of RxLRs in combined dataset:
231
Number of genes in the extracted gff file:
231
P.fragariae - SCRP245_v2
Number of RxLRs identified by Regex:
188
Number of RxLRs identified by Hmm:
191
Number of RxLRs in combined dataset:
231
Number of genes in the extracted gff file:
231

Without EER:
P.fragariae - A4
Number of RxLRs identified by Regex:
379
Number of RxLRs identified by Hmm:
186
Number of RxLRs in combined dataset:
409
Number of genes in the extracted gff file:
409
P.fragariae - Bc16
Number of RxLRs identified by Regex:
447
Number of RxLRs identified by Hmm:
215
Number of RxLRs in combined dataset:
489
Number of genes in the extracted gff file:
489
P.fragariae - Bc1
Number of RxLRs identified by Regex:
378
Number of RxLRs identified by Hmm:
188
Number of RxLRs in combined dataset:
409
Number of genes in the extracted gff file:
409
P.fragariae - Bc23
Number of RxLRs identified by Regex:
372
Number of RxLRs identified by Hmm:
196
Number of RxLRs in combined dataset:
410
Number of genes in the extracted gff file:
410
P.fragariae - Nov27
Number of RxLRs identified by Regex:
375
Number of RxLRs identified by Hmm:
189
Number of RxLRs in combined dataset:
408
Number of genes in the extracted gff file:
408
P.fragariae - Nov5
Number of RxLRs identified by Regex:
387
Number of RxLRs identified by Hmm:
193
Number of RxLRs in combined dataset:
419
Number of genes in the extracted gff file:
419
P.fragariae - Nov71
Number of RxLRs identified by Regex:
388
Number of RxLRs identified by Hmm:
190
Number of RxLRs in combined dataset:
419
Number of genes in the extracted gff file:
419
P.fragariae - Nov77
Number of RxLRs identified by Regex:
357
Number of RxLRs identified by Hmm:
180
Number of RxLRs in combined dataset:
395
Number of genes in the extracted gff file:
395
P.fragariae - Nov9
Number of RxLRs identified by Regex:
374
Number of RxLRs identified by Hmm:
193
Number of RxLRs in combined dataset:
407
Number of genes in the extracted gff file:
407
P.fragariae - ONT3
Number of RxLRs identified by Regex:
392
Number of RxLRs identified by Hmm:
189
Number of RxLRs in combined dataset:
422
Number of genes in the extracted gff file:
422
P.fragariae - SCRP245_v2
Number of RxLRs identified by Regex:
381
Number of RxLRs identified by Hmm:
191
Number of RxLRs in combined dataset:
414
Number of genes in the extracted gff file:
414
```

####D) From Augustus gene models - Hmm evidence of CRN effectors

A hmm model relating to crinkler domains was used to identify putative crinklers in Augustus gene models. This was done with the following commands:

```bash
HmmDir=/home/groups/harrisonlab/project_files/idris/analysis/CRN_effectors/hmmer_models
LFLAK_hmm=$(ls $HmmDir/Pinf_Pram_Psoj_Pcap_LFLAK.hmm)
DWL_hmm=$(ls $HmmDir/Pinf_Pram_Psoj_Pcap_DWL.hmm)
for Proteome in $(ls gene_pred/final/*/*/final/final_genes_combined.pep.fasta)
do
    Strain=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Proteome | rev | cut -f4 -d '/' | rev)
    OutDir=analysis/CRN_effectors/hmmer_CRN/$Organism/$Strain
    mkdir -p $OutDir
    echo "$Organism - $Strain"
    # Run hmm searches LFLAK domains
    CrinklerProts_LFLAK=$OutDir/"$Strain"_pub_CRN_LFLAK_hmm.txt
    hmmsearch -T0 $LFLAK_hmm $Proteome > $CrinklerProts_LFLAK
    cat $CrinklerProts_LFLAK | grep 'Initial search space'
    cat $CrinklerProts_LFLAK | grep 'number of targets reported over threshold'
    ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer
    $ProgDir/hmmer2fasta.pl $CrinklerProts_LFLAK $Proteome > $OutDir/"$Strain"_pub_CRN_LFLAK_hmm.fa
    # Run hmm searches DWL domains
    CrinklerProts_DWL=$OutDir/"$Strain"_pub_CRN_DWL_hmm.txt
    hmmsearch -T0 $DWL_hmm $Proteome > $CrinklerProts_DWL
    cat $CrinklerProts_DWL | grep 'Initial search space'
    cat $CrinklerProts_DWL | grep 'number of targets reported over threshold'
    ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer
    $ProgDir/hmmer2fasta.pl $CrinklerProts_DWL $Proteome > $OutDir/"$Strain"_pub_CRN_DWL_hmm.fa
    # Identify the genes detected in both models
    cat $OutDir/"$Strain"_pub_CRN_LFLAK_hmm.fa $OutDir/"$Strain"_pub_CRN_DWL_hmm.fa | grep '>' | cut -f1 | tr -d '>' | sort | uniq -d > $OutDir/"$Strain"_pub_CRN_LFLAK_DWL.txt
    echo "Total number of CRNs from both models"
    cat $OutDir/"$Strain"_pub_CRN_LFLAK_DWL.txt | wc -l
    echo "$Strain done"
done
```

```
P.fragariae - A4
Initial search space (Z):             33,586  [actual number of targets]
Domain search space  (domZ):             141  [number of targets reported over threshold]
Initial search space (Z):             33,586  [actual number of targets]
Domain search space  (domZ):             117  [number of targets reported over threshold]
Total number of CRNs from both models
106
P.fragariae - Bc16
Initial search space (Z):             36,598  [actual number of targets]
Domain search space  (domZ):             151  [number of targets reported over threshold]
Initial search space (Z):             36,598  [actual number of targets]
Domain search space  (domZ):             132  [number of targets reported over threshold]
Total number of CRNs from both models
122
P.fragariae - Bc1
Initial search space (Z):             33,063  [actual number of targets]
Domain search space  (domZ):             142  [number of targets reported over threshold]
Initial search space (Z):             33,063  [actual number of targets]
Domain search space  (domZ):             117  [number of targets reported over threshold]
Total number of CRNs from both models
108
P.fragariae - Bc23
Initial search space (Z):             33,039  [actual number of targets]
Domain search space  (domZ):             141  [number of targets reported over threshold]
Initial search space (Z):             33,039  [actual number of targets]
Domain search space  (domZ):             120  [number of targets reported over threshold]
Total number of CRNs from both models
109
P.fragariae - Nov27
Initial search space (Z):             33,171  [actual number of targets]
Domain search space  (domZ):             144  [number of targets reported over threshold]
Initial search space (Z):             33,171  [actual number of targets]
Domain search space  (domZ):             121  [number of targets reported over threshold]
Total number of CRNs from both models
110
P.fragariae - Nov5
Initial search space (Z):             33,278  [actual number of targets]
Domain search space  (domZ):             143  [number of targets reported over threshold]
Initial search space (Z):             33,278  [actual number of targets]
Domain search space  (domZ):             118  [number of targets reported over threshold]
Total number of CRNs from both models
108
P.fragariae - Nov71
Initial search space (Z):             32,775  [actual number of targets]
Domain search space  (domZ):             141  [number of targets reported over threshold]
Initial search space (Z):             32,775  [actual number of targets]
Domain search space  (domZ):             118  [number of targets reported over threshold]
Total number of CRNs from both models
105
P.fragariae - Nov77
Initial search space (Z):             33,068  [actual number of targets]
Domain search space  (domZ):             134  [number of targets reported over threshold]
Initial search space (Z):             33,068  [actual number of targets]
Domain search space  (domZ):             119  [number of targets reported over threshold]
Total number of CRNs from both models
105
P.fragariae - Nov9
Initial search space (Z):             32,815  [actual number of targets]
Domain search space  (domZ):             145  [number of targets reported over threshold]
Initial search space (Z):             32,815  [actual number of targets]
Domain search space  (domZ):             118  [number of targets reported over threshold]
Total number of CRNs from both models
108
P.fragariae - ONT3
Initial search space (Z):             36,913  [actual number of targets]
Domain search space  (domZ):             138  [number of targets reported over threshold]
Initial search space (Z):             36,913  [actual number of targets]
Domain search space  (domZ):             117  [number of targets reported over threshold]
Total number of CRNs from both models
103
P.fragariae - SCRP245_v2
Initial search space (Z):             36,817  [actual number of targets]
Domain search space  (domZ):             142  [number of targets reported over threshold]
Initial search space (Z):             36,817  [actual number of targets]
Domain search space  (domZ):             119  [number of targets reported over threshold]
Total number of CRNs from both models
109
```

Extract gff annotations for Crinklers:

```bash
for CRNlist in $(ls analysis/CRN_effectors/hmmer_CRN/*/*/*_pub_CRN_LFLAK_DWL.txt)
do
    Strain=$(echo $CRNlist | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $CRNlist | rev | cut -f3 -d '/' | rev)
    OutName=$(echo $CRNlist | sed 's/.txt/.gff/g')
    echo "$Organism - $Strain"
    Gff=$(ls gene_pred/final/$Organism/$Strain/final/final_genes_appended.gff3)
    cat $CRNlist | sed -r 's/\.t.$//g' > tmp.txt
    cat $Gff | grep -w -f tmp.txt > $OutName
    rm tmp.txt
done
```

####E) From ORF gene models - Signal peptide & RxLR motif

Required programs:

SigP
Phobius
biopython

#####E.1) Prediction using SignalP

Proteins that were predicted to contain signal peptides were identified using the following commands:

```bash
for Proteome in $(ls gene_pred/ORF_finder/*/*/*.aa_cat.fa)
do
    SplitfileDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
    Strain=$(echo $Proteome | rev | cut -f2 -d '/' | rev)
    Organism=P.fragariae
    SplitDir=gene_pred/ORF_split/$Organism/$Strain
    mkdir -p $SplitDir
    BaseName="$Organism""_$Strain"_ORF_preds
    $SplitfileDir/splitfile_500.py --inp_fasta $Proteome --out_dir $SplitDir --out_base $BaseName
    for File in $(ls $SplitDir/*_ORF_preds_*)
    do
        Jobs=$(qstat | grep 'pred_sigP' | wc -l)
        while [ $Jobs -gt 20 ]
        do
            sleep 1
            printf "."
            Jobs=$(qstat | grep 'pred_sigP' | wc -l)
        done        
        printf "\n"
        echo $File
        qsub $ProgDir/pred_sigP.sh $File
        qsub $ProgDir/pred_sigP.sh $File signalp-3.0
        qsub $ProgDir/pred_sigP.sh $File signalp-4.1
    done
done
```

The batch files of predicted secreted proteins needed to be combined into a single file for each strain. This was done with the following commands:

```bash
for SplitDir in $(ls -d gene_pred/ORF_split/*/*)
do
    Strain=$(echo $SplitDir | cut -d '/' -f4)
    Organism=$(echo $SplitDir | cut -d '/' -f3)
    echo "$Organism - $Strain"
    for SigpDir in $(ls -d gene_pred/ORF_sig* | cut -f2 -d'/')
    do
        InStringAA=''
        InStringNeg=''
        InStringTab=''
        InStringTxt=''
        for GRP in $(ls -l $SplitDir/*_ORF_*.fa | rev | cut -d '_' -f1 | rev | sort -n)
        do  
            InStringAA="$InStringAA gene_pred/$SigpDir/$Organism/$Strain/split/"$Organism"_"$Strain"_ORF_preds_$GRP""_sp.aa"
            InStringNeg="$InStringNeg gene_pred/$SigpDir/$Organism/$Strain/split/"$Organism"_"$Strain"_ORF_preds_$GRP""_sp_neg.aa"
            InStringTab="$InStringTab gene_pred/$SigpDir/$Organism/$Strain/split/"$Organism"_"$Strain"_ORF_preds_$GRP""_sp.tab"
            InStringTxt="$InStringTxt gene_pred/$SigpDir/$Organism/$Strain/split/"$Organism"_"$Strain"_ORF_preds_$GRP""_sp.txt"
        done
        cat $InStringAA > gene_pred/$SigpDir/$Organism/$Strain/"$Strain"_aug_sp.aa
        cat $InStringNeg > gene_pred/$SigpDir/$Organism/$Strain/"$Strain"_aug_neg_sp.aa
        tail -n +2 -q $InStringTab > gene_pred/$SigpDir/$Organism/$Strain/"$Strain"_aug_sp.tab
        cat $InStringTxt > gene_pred/$SigpDir/$Organism/$Strain/"$Strain"_aug_sp.txt
    done
done
```

E.2) Prediction using Phobius

Secreted proteins were also predicted using Phobius

```bash
for Proteome in $(ls gene_pred/ORF_finder/*/*/*.aa_cat.fa)
do
    Strain=$(echo $Proteome | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
    echo "$Organism - $Strain"
    OutDir=analysis/phobius_ORF/$Organism/$Strain
    mkdir -p $OutDir
    phobius.pl $Proteome > $OutDir/"$Strain"_phobius.txt
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
    $ProgDir/phobius_parser.py --inp_fasta $Proteome --phobius_txt $OutDir/"$Strain"_phobius.txt --out_fasta $OutDir/"$Strain"_phobius.fa
done
```

Because of the way ORF_finder predicts proteins, phobius predictions cannot be used downstream as there is no way to remove overlapping features.

Secreted proteins from different sources were combined into a single file:

```bash
for Proteome in $(ls gene_pred/ORF_finder/*/*/*.aa_cat.fa)
do
    Strain=$(echo $Proteome | rev | cut -f2 -d '/' | rev)
    Organism=P.fragariae
    echo "$Organism - $Strain"
    OutDir=gene_pred/combined_sigP_ORF/$Organism/$Strain
    mkdir -p $OutDir
    echo "The following number of sequences were predicted as secreted:"
    # cat gene_pred/ORF_sig*/$Organism/$Strain/*_aug_sp.aa analysis/phobius_ORF/$Organism/$Strain/"$Strain"_phobius.fa > $OutDir/"$Strain"_all_secreted.fa
    cat gene_pred/ORF_sig*/$Organism/$Strain/*_aug_sp.aa > $OutDir/"$Strain"_all_secreted.fa
    cat $OutDir/"$Strain"_all_secreted.fa | grep '>' | tr -d '>' | tr -d ' ' | sed "s/HMM_score\t/HMM_score=\t/g" > $OutDir/"$Strain"_all_secreted_headers.txt
    cat $OutDir/"$Strain"_all_secreted_headers.txt | wc -l
    echo "This represented the following number of unique genes:"
    # cat gene_pred/final_sig*/$Organism/$Strain/*_aug_sp.aa analysis/phobius/$Organism/$Strain/"$Strain"_phobius.fa | grep '>' | cut -f1 | tr -d ' >' | sort -g | uniq > $OutDir/"$Strain"_secreted.txt
    cat gene_pred/ORF_sig*/$Organism/$Strain/*_aug_sp.aa | grep '>' | cut -f1 | tr -d ' >' | sort -g | uniq > $OutDir/"$Strain"_secreted.txt
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    $ProgDir/extract_from_fasta.py --fasta $Proteome --headers $OutDir/"$Strain"_secreted.txt > $OutDir/"$Strain"_secreted.fa
    cat $OutDir/"$Strain"_secreted.fa | grep '>' | wc -l
done
```

```
P.fragariae - A4
The following number of sequences were predicted as secreted:
81,964
This represented the following number of unique genes:
40,784
P.fragariae - Bc16
The following number of sequences were predicted as secreted:
97,133
This represented the following number of unique genes:
48,486
P.fragariae - Bc1
The following number of sequences were predicted as secreted:
82,683
This represented the following number of unique genes:
41,080
P.fragariae - Bc23
The following number of sequences were predicted as secreted:
81,405
This represented the following number of unique genes:
40,484
P.fragariae - Nov27
The following number of sequences were predicted as secreted:
81,986
This represented the following number of unique genes:
40,789
P.fragariae - Nov5
The following number of sequences were predicted as secreted:
81,962
This represented the following number of unique genes:
40,803
P.fragariae - Nov71
The following number of sequences were predicted as secreted:
81,981
This represented the following number of unique genes:
40,711
P.fragariae - Nov77
The following number of sequences were predicted as secreted:
82,170
This represented the following number of unique genes:
40,933
P.fragariae - Nov9
The following number of sequences were predicted as secreted:
82,839
This represented the following number of unique genes:
41,177
P.fragariae - ONT3
The following number of sequences were predicted as secreted:
89,185
This represented the following number of unique genes:
44,318
P.fragariae - SCRP245_v2
The following number of sequences were predicted as secreted:
85,884
This represented the following number of unique genes:
42,759
```

E.3) Prediction of RxLRs

Names of ORFs containing signal peptides were extracted from fasta files. This included information on the position and hmm score of RxLRs.

```bash
for FastaFile in $(ls gene_pred/combined_sigP_ORF/*/*/*_all_secreted.fa)
do
    Strain=$(echo $FastaFile | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $FastaFile | rev | cut -f3 -d '/' | rev)
    SigP_headers=gene_pred/ORF_sigP/$Organism/$Strain/"$Strain"_ORF_sp_names.txt
    cat $FastaFile | grep '>' | sed -r 's/>//g' | sed -r 's/\s+/\t/g'| sed 's/=\t/=/g' | sed 's/--//g' > $SigP_headers
    echo "$Strain done"
done
```

Due to the nature of predicting ORFs, some features overlapped with one another. A single ORF was selected from each set of overlapped ORFs. This was was selected on the basis of its SignalP Hmm score. Biopython was used to identify overlaps and identify the ORF with the best signalP score.

```bash
for Strain in A4 Bc16 Bc1 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for ORF_Gff in $(ls gene_pred/ORF_finder/*/$Strain/"$Strain"_ORF.gff3)
    do
        Organism=P.fragariae
        OutDir=$(ls -d gene_pred/combined_sigP_ORF/$Organism/$Strain)
        echo "$Organism - $Strain"
        SigP_fasta=$(ls $OutDir/"$Strain"_all_secreted.fa)
        SigP_headers=$(ls $OutDir/"$Strain"_all_secreted_headers.txt)
        ORF_fasta=$(ls gene_pred/ORF_finder/*/$Strain/"$Strain".aa_cat.fa)

        SigP_Gff=$OutDir/"$Strain"_all_secreted_unmerged.gff
        SigP_Merged_Gff=$OutDir/"$Strain"_all_secreted_merged.gff
        SigP_Merged_txt=$OutDir/"$Strain"_all_secreted_merged.txt
        SigP_Merged_AA=$OutDir/"$Strain"_all_secreted_merged.aa

        ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
        $ProgDir/extract_gff_for_sigP_hits.pl $SigP_headers $ORF_Gff SigP Name > $SigP_Gff
        echo "Extracting Gff done"
        ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/merge_gff
        $ProgDir/make_gff_database.py --inp $SigP_Gff --db sigP_ORF.db
        echo "Gff database made"
        ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
        $ProgDir/merge_sigP_ORFs.py --inp sigP_ORF.db --id sigP_ORF --out sigP_ORF_merged.db --gff > $SigP_Merged_Gff
        echo "Merging complete"
        cat $SigP_Merged_Gff | grep 'transcript' | rev | cut -f1 -d'=' | rev > $SigP_Merged_txt
        $ProgDir/extract_from_fasta.py --fasta $SigP_fasta --headers $SigP_Merged_txt > $SigP_Merged_AA
        echo "$Strain complete"
        # $ProgDir/extract_from_fasta.py --fasta $ORF_fasta --headers $SigP_Merged_txt > $SigP_Merged_AA
    done
done
```

The regular expression R.LR.{,40}[ED][ED][KR] has previously been used to identify RxLR effectors. The addition of an EER motif is significant as it has been shown as required for host uptake of the protein.

The RxLR_EER_regex_finder.py script was used to search for this regular expression and annotate the EER domain where present.

```bash
for Secretome in $(ls gene_pred/combined_sigP_ORF/*/*/*_all_secreted.fa)
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/RxLR_effectors
    Strain=$(echo $Secretome | rev | cut -d '/' -f2 | rev)
    Organism=$(echo $Secretome | rev |  cut -d '/' -f3 | rev)
    OutDir=analysis/RxLR_effectors/RxLR_EER_regex_finder/"$Organism"/"$Strain"
    mkdir -p $OutDir
    printf "\nstrain: $Strain\tspecies: $Organism\n"
    printf "the number of SigP gene is:\t"
    cat $Secretome | grep '>' | wc -l
    printf "the number of SigP-RxLR genes are:\t"
    $ProgDir/RxLR_EER_regex_finder.py $Secretome > $OutDir/"$Strain"_ORF_RxLR_EER_regex_unmerged.fa
    cat $OutDir/"$Strain"_ORF_RxLR_EER_regex_unmerged.fa | grep '>' | cut -f1 | tr -d '>' | sed -r 's/\.t.*//' | tr -d ' ' > $OutDir/"$Strain"_ORF_RxLR_regex_unmerged.txt
    cat $OutDir/"$Strain"_ORF_RxLR_regex_unmerged.txt | tr -d ' ' | sort | uniq | wc -l
    printf "the number of SigP-RxLR-EER genes are:\t"
    cat $OutDir/"$Strain"_ORF_RxLR_EER_regex_unmerged.fa | grep '>' | grep 'EER_motif_start' | cut -f1 | tr -d '>' | sed -r 's/\.t.*//' | tr -d ' '> $OutDir/"$Strain"_ORF_RxLR_EER_regex_unmerged.txt
    cat $OutDir/"$Strain"_ORF_RxLR_EER_regex_unmerged.txt | tr -d ' ' | sort | uniq | wc -l
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
    SigP_Gff=gene_pred/combined_sigP_ORF/$Organism/$Strain/"$Strain"_all_secreted_unmerged.gff
    ORF_fasta=$(ls gene_pred/ORF_finder/*/$Strain/"$Strain".aa_cat.fa)
    # $ProgDir/gene_list_to_gff.pl $OutDir/"$Strain"_ORF_RxLR_EER_regex_unmerged.txt  $SigP_Gff   RxLR_EER_regex_finder.py Name Augustus > $OutDir/"$Strain"_ORF_RxLR_regex_unmerged.gff
    $ProgDir/gene_list_to_gff.pl $OutDir/"$Strain"_ORF_RxLR_regex_unmerged.txt  $SigP_Gff   RxLR_regex_finder.py Name Augustus > $OutDir/"$Strain"_ORF_RxLR_regex_unmerged.gff
    RxLR_Merged_Gff=$OutDir/"$Strain"_ORF_RxLR_regex_merged.gff
    RxLR_Merged_txt=$OutDir/"$Strain"_ORF_RxLR_regex_merged.txt
    RxLR_Merged_AA=$OutDir/"$Strain"_ORF_RxLR_regex_merged.aa
    ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/merge_gff
    $ProgDir/make_gff_database.py --inp $OutDir/"$Strain"_ORF_RxLR_regex_unmerged.gff --db sigP_ORF_RxLR.db
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    $ProgDir/merge_sigP_ORFs.py --inp sigP_ORF_RxLR.db --id sigP_ORF_RxLR --out sigP_ORF_RxLR_merged.db --gff > $RxLR_Merged_Gff
    cat $RxLR_Merged_Gff | grep 'transcript' | rev | cut -f1 -d '=' | rev > $RxLR_Merged_txt
    $ProgDir/extract_from_fasta.py --fasta $ORF_fasta --headers $RxLR_Merged_txt > $RxLR_Merged_AA
    printf "Merged RxLR regex proteins:\t"
    cat $RxLR_Merged_AA | grep '>' | wc -l
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
    $ProgDir/gene_list_to_gff.pl $OutDir/"$Strain"_ORF_RxLR_EER_regex_unmerged.txt  $SigP_Gff   RxLR_regex_finder.py Name Augustus > $OutDir/"$Strain"_ORF_RxLR_EER_regex_unmerged.gff
    RxLR_Merged_Gff=$OutDir/"$Strain"_ORF_RxLR_EER_regex_merged.gff
    RxLR_Merged_txt=$OutDir/"$Strain"_ORF_RxLR_EER_regex_merged.txt
    RxLR_Merged_AA=$OutDir/"$Strain"_ORF_RxLR_EER_regex_merged.aa
    ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/merge_gff
    $ProgDir/make_gff_database.py --inp $OutDir/"$Strain"_ORF_RxLR_EER_regex_unmerged.gff --db sigP_ORF_RxLR.db
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    $ProgDir/merge_sigP_ORFs.py --inp sigP_ORF_RxLR.db --id sigP_ORF_RxLR --out sigP_ORF_RxLR_merged.db --gff > $RxLR_Merged_Gff
    cat $RxLR_Merged_Gff | grep 'transcript' | rev | cut -f1 -d '=' | rev > $RxLR_Merged_txt
    $ProgDir/extract_from_fasta.py --fasta $ORF_fasta --headers $RxLR_Merged_txt > $RxLR_Merged_AA
    printf "Merged RxLR-EER regex proteins:\t"
    cat $RxLR_Merged_AA | grep '>' | wc -l
    printf "\n"
    echo "$Strain done"
done
```

```
strain: A4      species: P.fragariae
the number of SigP gene is:     81,964
the number of SigP-RxLR genes are:      2,675
the number of SigP-RxLR-EER genes are:  298
Merged RxLR regex proteins: 2,176
Merged RxLR-EER regex proteins: 269


strain: Bc16    species: P.fragariae
the number of SigP gene is:     97,133
the number of SigP-RxLR genes are:      2,969
the number of SigP-RxLR-EER genes are:  327
Merged RxLR regex proteins: 2,450
Merged RxLR-EER regex proteins: 297


strain: Bc1     species: P.fragariae
the number of SigP gene is:     82,683
the number of SigP-RxLR genes are:      2,691
the number of SigP-RxLR-EER genes are:  299
Merged RxLR regex proteins: 2,189
Merged RxLR-EER regex proteins: 270


strain: Bc23    species: P.fragariae
the number of SigP gene is:     81,405
the number of SigP-RxLR genes are:      2,695
the number of SigP-RxLR-EER genes are:  304
Merged RxLR regex proteins: 2,191
Merged RxLR-EER regex proteins: 273


strain: Nov27   species: P.fragariae
the number of SigP gene is:     81,986
the number of SigP-RxLR genes are:      2,660
the number of SigP-RxLR-EER genes are:  299
Merged RxLR regex proteins: 2,163
Merged RxLR-EER regex proteins: 270


strain: Nov5    species: P.fragariae
the number of SigP gene is:     81,962
the number of SigP-RxLR genes are:      2,660
the number of SigP-RxLR-EER genes are:  298
Merged RxLR regex proteins: 2,161
Merged RxLR-EER regex proteins: 269


strain: Nov71   species: P.fragariae
the number of SigP gene is:     81,981
the number of SigP-RxLR genes are:      2,658
the number of SigP-RxLR-EER genes are:  298
Merged RxLR regex proteins: 2,159
Merged RxLR-EER regex proteins: 269


strain: Nov77   species: P.fragariae
the number of SigP gene is:     82,170
the number of SigP-RxLR genes are:      2,647
the number of SigP-RxLR-EER genes are:  288
Merged RxLR regex proteins: 2,158
Merged RxLR-EER regex proteins: 258


strain: Nov9    species: P.fragariae
the number of SigP gene is:     82,839
the number of SigP-RxLR genes are:      2,698
the number of SigP-RxLR-EER genes are:  297
Merged RxLR regex proteins: 2,203
Merged RxLR-EER regex proteins: 268


strain: ONT3    species: P.fragariae
the number of SigP gene is:     89,185
the number of SigP-RxLR genes are:      2,803
the number of SigP-RxLR-EER genes are:  306
Merged RxLR regex proteins: 2,268
Merged RxLR-EER regex proteins: 274


strain: SCRP245_v2      species: P.fragariae
the number of SigP gene is:     85,884
the number of SigP-RxLR genes are:      2,660
the number of SigP-RxLR-EER genes are:  302
Merged RxLR regex proteins: 2,167
Merged RxLR-EER regex proteins: 273
```

E5) From ORF gene models - Hmm evidence of WY domains

Hmm models for the WY domain contained in many RxLRs were used to search ORFs predicted with atg.pl. These were run with the following commands:

```bash
for Secretome in $(ls gene_pred/combined_sigP_ORF/*/*/*_all_secreted.fa)
do
    ProgDir=/home/armita/git_repos/emr_repos/scripts/phytophthora/pathogen/hmmer
    HmmModel=/home/armita/git_repos/emr_repos/scripts/phytophthora/pathogen/hmmer/WY_motif.hmm
    Strain=$(echo $Secretome | rev | cut -f2 -d '/' | rev)
    Organism=P.fragariae
    OutDir=analysis/RxLR_effectors/hmmer_WY/$Organism/$Strain
    mkdir -p $OutDir
    HmmResults="$Strain"_ORF_WY_hmmer.txt
    hmmsearch -T 0 $HmmModel $Secretome > $OutDir/$HmmResults
    echo "$Organism $Strain"
    cat $OutDir/$HmmResults | grep 'Initial search space'
    cat $OutDir/$HmmResults | grep 'number of targets reported over threshold'
    HmmFasta="$Strain"_ORF_WY_hmmer.fa
    $ProgDir/hmmer2fasta.pl $OutDir/$HmmResults $Secretome > $OutDir/$HmmFasta
    Headers="$Strain"_ORF_WY_hmmer_headers.txt
    cat $OutDir/$HmmFasta | grep '>' | cut -f1 | tr -d '>' | sed -r 's/\.t.*//' | tr -d ' ' > $OutDir/$Headers
    SigP_Merged_Gff=gene_pred/combined_sigP_ORF/$Organism/$Strain/"$Strain"_all_secreted_merged.gff
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
    $ProgDir/gene_list_to_gff.pl $OutDir/$Headers $SigP_Merged_Gff $HmmModel Name Augustus > $OutDir/"$Strain"_ORF_WY_hmmer.gff
    echo "$Strain done"
done
```

```
P.fragariae A4
Initial search space (Z):             81,964  [actual number of targets]
Domain search space  (domZ):             390  [number of targets reported over threshold]
P.fragariae Bc16
Initial search space (Z):             97,133  [actual number of targets]
Domain search space  (domZ):             397  [number of targets reported over threshold]
P.fragariae Bc1
Initial search space (Z):             82,683  [actual number of targets]
Domain search space  (domZ):             387  [number of targets reported over threshold]
P.fragariae Bc23
Initial search space (Z):             81,405  [actual number of targets]
Domain search space  (domZ):             396  [number of targets reported over threshold]
P.fragariae Nov27
Initial search space (Z):             81,986  [actual number of targets]
Domain search space  (domZ):             388  [number of targets reported over threshold]
P.fragariae Nov5
Initial search space (Z):             81,962  [actual number of targets]
Domain search space  (domZ):             387  [number of targets reported over threshold]
P.fragariae Nov71
Initial search space (Z):             81,981  [actual number of targets]
Domain search space  (domZ):             390  [number of targets reported over threshold]
P.fragariae Nov77
Initial search space (Z):             82,170  [actual number of targets]
Domain search space  (domZ):             363  [number of targets reported over threshold]
P.fragariae Nov9
Initial search space (Z):             82,839  [actual number of targets]
Domain search space  (domZ):             390  [number of targets reported over threshold]
P.fragariae ONT3
Initial search space (Z):             89,185  [actual number of targets]
Domain search space  (domZ):             396  [number of targets reported over threshold]
P.fragariae SCRP245_v2
Initial search space (Z):             85,884  [actual number of targets]
Domain search space  (domZ):             378  [number of targets reported over threshold]
```

E6) From ORF gene models - Hmm evidence of RxLR effectors

```bash
for Secretome in $(ls gene_pred/combined_sigP_ORF/*/*/*_all_secreted.fa)
do
    ProgDir=/home/armita/git_repos/emr_repos/scripts/phytophthora/pathogen/hmmer
    HmmModel=/home/armita/git_repos/emr_repos/SI_Whisson_et_al_2007/cropped.hmm
    Strain=$(echo $Secretome | rev | cut -f2 -d '/' | rev)
    Organism=P.fragariae
    OutDir=analysis/RxLR_effectors/hmmer_RxLR/$Organism/$Strain
    mkdir -p $OutDir
    HmmResults="$Strain"_ORF_RxLR_hmmer_unmerged.txt
    hmmsearch -T 0 $HmmModel $Secretome > $OutDir/$HmmResults
    echo "$Organism $Strain"
    cat $OutDir/$HmmResults | grep 'Initial search space'
    cat $OutDir/$HmmResults | grep 'number of targets reported over threshold'
    HmmFasta="$Strain"_ORF_RxLR_hmmer.fa
    $ProgDir/hmmer2fasta.pl $OutDir/$HmmResults $Secretome > $OutDir/$HmmFasta
    Headers="$Strain"_ORF_RxLR_hmmer_headers_unmerged.txt
    cat $OutDir/$HmmFasta | grep '>' | cut -f1 | tr -d '>' | sed -r 's/\.t.*//' | tr -d ' ' > $OutDir/$Headers
    SigP_Gff=gene_pred/combined_sigP_ORF/$Organism/$Strain/"$Strain"_all_secreted_unmerged.gff
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
    $ProgDir/gene_list_to_gff.pl $OutDir/$Headers $SigP_Gff $HmmModel Name Augustus > $OutDir/"$Strain"_ORF_RxLR_hmmer_unmerged.gff3
    RxLR_Merged_Gff=$OutDir/"$Strain"_ORF_RxLR_hmm_merged.gff
    RxLR_Merged_txt=$OutDir/"$Strain"_ORF_RxLR_hmm_merged.txt
    RxLR_Merged_AA=$OutDir/"$Strain"_ORF_RxLR_hmm_merged.aa
    ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/merge_gff
    $ProgDir/make_gff_database.py --inp $OutDir/"$Strain"_ORF_RxLR_hmmer_unmerged.gff3 --db sigP_ORF_RxLR_hmm.db
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    $ProgDir/merge_sigP_ORFs.py --inp sigP_ORF_RxLR_hmm.db --id sigP_ORF_RxLR_hmm --out sigP_ORF_RxLR_hmm_merged.db --gff > $RxLR_Merged_Gff
    cat $RxLR_Merged_Gff | grep 'transcript' | rev | cut -f1 -d '=' | rev > $RxLR_Merged_txt
    ORF_fasta=$(ls gene_pred/ORF_finder/*/$Strain/"$Strain".aa_cat.fa)
    $ProgDir/extract_from_fasta.py --fasta $ORF_fasta --headers $RxLR_Merged_txt > $RxLR_Merged_AA
    printf "Merged RxLR-EER Hmm proteins:\t"
    cat $RxLR_Merged_AA | grep '>' | wc -l
    echo "$Strain done"
done
```

```
P.fragariae A4
Initial search space (Z):             81,964  [actual number of targets]
Domain search space  (domZ):             654  [number of targets reported over threshold]
Merged RxLR-EER Hmm proteins:   199
P.fragariae Bc16
Initial search space (Z):             97,133  [actual number of targets]
Domain search space  (domZ):             708  [number of targets reported over threshold]
Merged RxLR-EER Hmm proteins:   218
P.fragariae Bc1
Initial search space (Z):             82,683  [actual number of targets]
Domain search space  (domZ):             654  [number of targets reported over threshold]
Merged RxLR-EER Hmm proteins:   199
P.fragariae Bc23
Initial search space (Z):             81,405  [actual number of targets]
Domain search space  (domZ):             671  [number of targets reported over threshold]
Merged RxLR-EER Hmm proteins:   204
P.fragariae Nov27
Initial search space (Z):             81,986  [actual number of targets]
Domain search space  (domZ):             653  [number of targets reported over threshold]
Merged RxLR-EER Hmm proteins:   199
P.fragariae Nov5
Initial search space (Z):             81,962  [actual number of targets]
Domain search space  (domZ):             654  [number of targets reported over threshold]
Merged RxLR-EER Hmm proteins:   199
P.fragariae Nov71
Initial search space (Z):             81,981   [actual number of targets]
Domain search space  (domZ):             654  [number of targets reported over threshold]
Merged RxLR-EER Hmm proteins:   199
P.fragariae Nov77
Initial search space (Z):             82,170  [actual number of targets]
Domain search space  (domZ):             643  [number of targets reported over threshold]
Merged RxLR-EER Hmm proteins:   195
P.fragariae Nov9
Initial search space (Z):             82,839  [actual number of targets]
Domain search space  (domZ):             657  [number of targets reported over threshold]
Merged RxLR-EER Hmm proteins:   200
P.fragariae ONT3
Initial search space (Z):             89,185  [actual number of targets]
Domain search space  (domZ):             677  [number of targets reported over threshold]
Merged RxLR-EER Hmm proteins:   206
P.fragariae SCRP245_v2
Initial search space (Z):             85,884  [actual number of targets]
Domain search space  (domZ):             666  [number of targets reported over threshold]
Merged RxLR-EER Hmm proteins:   203
```

E7) Combining RxLRs from Regex and hmm searches

The total RxLRs are

```bash
echo "Without EER"
for RegexRxLR in $(ls analysis/RxLR_effectors/RxLR_EER_regex_finder/*/*/*_ORF_RxLR_regex_merged.txt)
do
    Organism=$(echo $RegexRxLR | rev |  cut -d '/' -f3 | rev)
    Strain=$(echo $RegexRxLR | rev | cut -d '/' -f2 | rev)
    Gff=$(ls gene_pred/ORF_finder/*/$Strain/"$Strain"_ORF.gff3)
    Proteome=$(ls gene_pred/ORF_finder/*/$Strain/"$Strain".aa_cat.fa)
    HmmRxLR=$(ls analysis/RxLR_effectors/hmmer_RxLR/$Organism/$Strain/"$Strain"_ORF_RxLR_hmm_merged.txt)
    echo "$Organism - $Strain"
    echo "Number of RxLRs identified by Regex:"
    cat $RegexRxLR | sort | uniq | wc -l
    echo "Number of RxLRs identified by Hmm:"
    cat $HmmRxLR | sort | uniq | wc -l
    echo "Number of RxLRs in combined dataset:"
    cat $RegexRxLR $HmmRxLR | sort | uniq | wc -l
    OutDir=analysis/RxLR_effectors/combined_evidence/$Organism/$Strain
    mkdir -p $OutDir
    cat $RegexRxLR $HmmRxLR | sort | uniq > $OutDir/"$Strain"_total_ORF_RxLR_headers.txt
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
    $ProgDir/gene_list_to_gff.pl $OutDir/"$Strain"_total_ORF_RxLR_headers.txt $Gff ORF_RxLR Name Augustus > $OutDir/"$Strain"_total_ORF_RxLR.gff
    echo "Number of genes in the extracted gff file:"
    cat $OutDir/"$Strain"_total_ORF_RxLR.gff | grep -w 'gene' | wc -l
    echo ""
    echo "$Strain done without EER"
done

echo "With EER"
for RegexRxLR in $(ls analysis/RxLR_effectors/RxLR_EER_regex_finder/*/*/*_ORF_RxLR_EER_regex_merged.txt)
do
    Organism=$(echo $RegexRxLR | rev |  cut -d '/' -f3 | rev)
    Strain=$(echo $RegexRxLR | rev | cut -d '/' -f2 | rev)
    Gff=$(ls gene_pred/ORF_finder/*/$Strain/"$Strain"_ORF.gff3)
    Proteome=$(ls gene_pred/ORF_finder/*/$Strain/"$Strain".aa_cat.fa)
    HmmRxLR=$(ls analysis/RxLR_effectors/hmmer_RxLR/$Organism/$Strain/"$Strain"_ORF_RxLR_hmm_merged.txt)
    echo "$Organism - $Strain"
    echo "Number of RxLRs identified by Regex:"
    cat $RegexRxLR | sort | uniq | wc -l
    echo "Number of RxLRs identified by Hmm:"
    cat $HmmRxLR | sort | uniq | wc -l
    echo "Number of RxLRs in combined dataset:"
    cat $RegexRxLR $HmmRxLR | sort | uniq | wc -l
    OutDir=analysis/RxLR_effectors/combined_evidence/$Organism/$Strain
    mkdir -p $OutDir
    cat $RegexRxLR $HmmRxLR | sort | uniq > $OutDir/"$Strain"_total_ORF_RxLR_EER_headers.txt
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
    $ProgDir/gene_list_to_gff.pl $OutDir/"$Strain"_total_ORF_RxLR_EER_headers.txt $Gff ORF_RxLR Name Augustus > $OutDir/"$Strain"_total_ORF_RxLR_EER.gff
    echo "Number of genes in the extracted gff file:"
    cat $OutDir/"$Strain"_total_ORF_RxLR_EER.gff | grep -w 'gene' | wc -l
    echo ""
    echo "$Strain done with EER"
done
```

```
With EER:
P.fragariae - A4
Number of RxLRs identified by Regex:
269
Number of RxLRs identified by Hmm:
199
Number of RxLRs in combined dataset:
297
Number of genes in the extracted gff file:
297

P.fragariae - Bc16
Number of RxLRs identified by Regex:
297
Number of RxLRs identified by Hmm:
218
Number of RxLRs in combined dataset:
326
Number of genes in the extracted gff file:
326

P.fragariae - Bc1
Number of RxLRs identified by Regex:
270
Number of RxLRs identified by Hmm:
199
Number of RxLRs in combined dataset:
297
Number of genes in the extracted gff file:
297

P.fragariae - Bc23
Number of RxLRs identified by Regex:
273
Number of RxLRs identified by Hmm:
204
Number of RxLRs in combined dataset:
302
Number of genes in the extracted gff file:
302

P.fragariae - Nov27
Number of RxLRs identified by Regex:
270
Number of RxLRs identified by Hmm:
199
Number of RxLRs in combined dataset:
297
Number of genes in the extracted gff file:
297

P.fragariae - Nov5
Number of RxLRs identified by Regex:
269
Number of RxLRs identified by Hmm:
199
Number of RxLRs in combined dataset:
296
Number of genes in the extracted gff file:
296

P.fragariae - Nov71
Number of RxLRs identified by Regex:
269
Number of RxLRs identified by Hmm:
199
Number of RxLRs in combined dataset:
296
Number of genes in the extracted gff file:
296

P.fragariae - Nov77
Number of RxLRs identified by Regex:
258
Number of RxLRs identified by Hmm:
195
Number of RxLRs in combined dataset:
282
Number of genes in the extracted gff file:
282

P.fragariae - Nov9
Number of RxLRs identified by Regex:
268
Number of RxLRs identified by Hmm:
200
Number of RxLRs in combined dataset:
296
Number of genes in the extracted gff file:
296

P.fragariae - ONT3
Number of RxLRs identified by Regex:
274
Number of RxLRs identified by Hmm:
206
Number of RxLRs in combined dataset:
304
Number of genes in the extracted gff file:
304

P.fragariae - SCRP245_v2
Number of RxLRs identified by Regex:
273
Number of RxLRs identified by Hmm:
203
Number of RxLRs in combined dataset:
300
Number of genes in the extracted gff file:
300

Without EER:
P.fragariae - A4
Number of RxLRs identified by Regex:
2,176
Number of RxLRs identified by Hmm:
199
Number of RxLRs in combined dataset:
2,187
Number of genes in the extracted gff file:
2,187

P.fragariae - Bc16
Number of RxLRs identified by Regex:
2,450
Number of RxLRs identified by Hmm:
218
Number of RxLRs in combined dataset:
2,462
Number of genes in the extracted gff file:
2,462

P.fragariae - Bc1
Number of RxLRs identified by Regex:
2,189
Number of RxLRs identified by Hmm:
199
Number of RxLRs in combined dataset:
2,200
Number of genes in the extracted gff file:
2,200

P.fragariae - Bc23
Number of RxLRs identified by Regex:
2,191
Number of RxLRs identified by Hmm:
204
Number of RxLRs in combined dataset:
2,204
Number of genes in the extracted gff file:
2,204

P.fragariae - Nov27
Number of RxLRs identified by Regex:
2,164
Number of RxLRs identified by Hmm:
199
Number of RxLRs in combined dataset:
2,174
Number of genes in the extracted gff file:
2,174

P.fragariae - Nov5
Number of RxLRs identified by Regex:
2,161
Number of RxLRs identified by Hmm:
199
Number of RxLRs in combined dataset:
2,172
Number of genes in the extracted gff file:
2,172

P.fragariae - Nov71
Number of RxLRs identified by Regex:
2,159
Number of RxLRs identified by Hmm:
199
Number of RxLRs in combined dataset:
2,170
Number of genes in the extracted gff file:
2,170

P.fragariae - Nov77
Number of RxLRs identified by Regex:
2,158
Number of RxLRs identified by Hmm:
195
Number of RxLRs in combined dataset:
2,167
Number of genes in the extracted gff file:
2,167

P.fragariae - Nov9
Number of RxLRs identified by Regex:
2,203
Number of RxLRs identified by Hmm:
200
Number of RxLRs in combined dataset:
2,214
Number of genes in the extracted gff file:
2,214

P.fragariae - ONT3
Number of RxLRs identified by Regex:
2,268
Number of RxLRs identified by Hmm:
206
Number of RxLRs in combined dataset:
2,279
Number of genes in the extracted gff file:
2,279

P.fragariae - SCRP245_v2
Number of RxLRs identified by Regex:
2,167
Number of RxLRs identified by Hmm:
203
Number of RxLRs in combined dataset:
2,178
Number of genes in the extracted gff file:
2,178
```

4.2.c Analysis of RxLR effectors - merger of Augustus / published genes with ORFs

Intersection between the coodinates of putative RxLRs from gene models and ORFs were identified to determine the total number of RxLRs predicted in these genomes.

The RxLR effectors from both Gene models and ORF finding approaches were combined into a single file.

```bash
echo "Without EER"
for MergeDir in $(ls -d analysis/RxLR_effectors/combined_evidence/*/*)
do
    Strain=$(echo "$MergeDir" | rev | cut -f1 -d '/' | rev)
    Species=$(echo "$MergeDir" | rev | cut -f2 -d '/' | rev)
    AugGff=$MergeDir/"$Strain"_total_RxLR.gff
    AugTxt=$MergeDir/"$Strain"_total_RxLR_headers.txt
    AugFa=$(ls gene_pred/final/"$Species"/"$Strain"/final/final_genes_combined.pep.fasta)

    ORFGff=$(ls $MergeDir/"$Strain"_total_ORF_RxLR.gff)
    ORFsFa=$(ls gene_pred/ORF_finder/*/"$Strain"/"$Strain".aa_cat.fa)
    ORFsTxt=$(ls $MergeDir/"$Strain"_total_ORF_RxLR_headers.txt)

    ORFsInAug=$MergeDir/"$Strain"_ORFsInAug_RxLR_motif_hmm.gff
    AugInORFs=$MergeDir/"$Strain"_AugInORFs_RxLR_motif_hmm.gff
    ORFsUniq=$MergeDir/"$Strain"_ORFsUniq_RxLR_motif_hmm.gff
    AugUniq=$MergeDir/"$Strain"_Aug_Uniq_RxLR_motif_hmm.gff
    TotalRxLRsTxt=$MergeDir/"$Strain"_Total_RxLR_motif_hmm.txt
    TotalRxLRsGff=$MergeDir/"$Strain"_Total_RxLR_motif_hmm.gff

    bedtools intersect -wa -u -a $ORFGff -b $AugGff > $ORFsInAug
    bedtools intersect -wa -u -a $AugGff -b $ORFGff > $AugInORFs
    bedtools intersect -v -wa -a $ORFGff -b $AugGff > $ORFsUniq
    bedtools intersect -v -wa -a $AugGff -b $ORFGff > $AugUniq

    echo "$Species - $Strain"
    echo "The number of ORF RxLRs overlapping Augustus RxLRs:"
    cat $ORFsInAug | grep -w 'gene' | wc -l
    echo "The number of Augustus RxLRs overlapping ORF RxLRs:"
    cat $AugInORFs | grep -w 'gene' | wc -l
    echo "The number of RxLRs unique to ORF models:"
    cat $ORFsUniq | grep -w 'transcript' | cut -f9 | cut -f1 -d ';' | cut -f2 -d '=' | wc -l
    echo "The number of RxLRs unique to Augustus models:"
    cat $AugUniq | grep -w -e 'transcript' -e 'mRNA' | wc -l
    echo "The total number of putative RxLRs are:"
    cat $AugInORFs | grep -w -e 'transcript' -e 'mRNA'  | cut -f9 | cut -f1 -d ';' | cut -f2 -d '=' > $TotalRxLRsTxt
    cat $AugUniq | grep -w -e 'transcript' -e 'mRNA'  | cut -f9 | cut -f1 -d ';' | cut -f2 -d '=' >> $TotalRxLRsTxt
    cat $ORFsUniq | grep -w -e 'transcript' -e 'mRNA'  | cut -f9 | cut -f3 -d ';' | cut -f2 -d '=' >> $TotalRxLRsTxt
    cat $TotalRxLRsTxt | wc -l
    cat $AugInORFs $AugUniq $ORFsUniq | grep -w -f $TotalRxLRsTxt > $TotalRxLRsGff

    RxLRsFa=$MergeDir/"$Strain"_final_RxLR.fa
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    $ProgDir/extract_from_fasta.py --fasta $AugFa --headers $TotalRxLRsTxt > $RxLRsFa
    $ProgDir/extract_from_fasta.py --fasta $ORFsFa --headers $TotalRxLRsTxt >> $RxLRsFa
    echo "The number of sequences extracted is"
    cat $RxLRsFa | grep '>' | wc -l
    echo "$Strain done without EER"
done

echo "With EER"
for MergeDir in $(ls -d analysis/RxLR_effectors/combined_evidence/*/*)
do
    Strain=$(echo "$MergeDir" | rev | cut -f1 -d '/' | rev)
    Species=$(echo "$MergeDir" | rev | cut -f2 -d '/' | rev)
    AugGff=$MergeDir/"$Strain"_total_RxLR_EER.gff
    AugTxt=$MergeDir/"$Strain"_total_RxLR_EER_headers.txt
    AugFa=$(ls gene_pred/final/"$Species"/"$Strain"/final/final_genes_combined.pep.fasta)

    ORFGff=$(ls $MergeDir/"$Strain"_total_ORF_RxLR_EER.gff)
    ORFsFa=$(ls gene_pred/ORF_finder/*/"$Strain"/"$Strain".aa_cat.fa)
    ORFsTxt=$(ls $MergeDir/"$Strain"_total_ORF_RxLR_EER_headers.txt)

    ORFsInAug=$MergeDir/"$Strain"_ORFsInAug_RxLR_EER_motif_hmm.gff
    AugInORFs=$MergeDir/"$Strain"_AugInORFs_RxLR_EER_motif_hmm.gff
    ORFsUniq=$MergeDir/"$Strain"_ORFsUniq_RxLR_EER_motif_hmm.gff
    AugUniq=$MergeDir/"$Strain"_Aug_Uniq_RxLR_EER_motif_hmm.gff
    TotalRxLRsTxt=$MergeDir/"$Strain"_Total_RxLR_EER_motif_hmm.txt
    TotalRxLRsGff=$MergeDir/"$Strain"_Total_RxLR_EER_motif_hmm.gff

    bedtools intersect -wa -u -a $ORFGff -b $AugGff > $ORFsInAug
    bedtools intersect -wa -u -a $AugGff -b $ORFGff > $AugInORFs
    bedtools intersect -v -wa -a $ORFGff -b $AugGff > $ORFsUniq
    bedtools intersect -v -wa -a $AugGff -b $ORFGff > $AugUniq

    echo "$Species - $Strain"
    echo "The number of ORF RxLRs overlapping Augustus RxLRs:"
    cat $ORFsInAug | grep -w 'gene' | wc -l
    echo "The number of Augustus RxLRs overlapping ORF RxLRs:"
    cat $AugInORFs | grep -w 'gene' | wc -l
    echo "The number of RxLRs unique to ORF models:"
    cat $ORFsUniq | grep -w 'transcript' | cut -f9 | cut -f1 -d ';' | cut -f2 -d '=' | wc -l
    echo "The number of RxLRs unique to Augustus models:"
    cat $AugUniq | grep -w -e 'transcript' -e 'mRNA' | wc -l
    echo "The total number of putative RxLRs are:"
    cat $AugInORFs | grep -w -e 'transcript' -e 'mRNA'  | cut -f9 | cut -f1 -d ';' | cut -f2 -d '=' > $TotalRxLRsTxt
    cat $AugUniq | grep -w -e 'transcript' -e 'mRNA'  | cut -f9 | cut -f1 -d ';' | cut -f2 -d '=' >> $TotalRxLRsTxt
    cat $ORFsUniq | grep -w -e 'transcript' -e 'mRNA'  | cut -f9 | cut -f3 -d ';' | cut -f2 -d '=' >> $TotalRxLRsTxt
    cat $TotalRxLRsTxt | wc -l
    cat $AugInORFs $AugUniq $ORFsUniq | grep -w -f $TotalRxLRsTxt > $TotalRxLRsGff

    RxLRsFa=$MergeDir/"$Strain"_final_RxLR_EER.fa
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    $ProgDir/extract_from_fasta.py --fasta $AugFa --headers $TotalRxLRsTxt > $RxLRsFa
    $ProgDir/extract_from_fasta.py --fasta $ORFsFa --headers $TotalRxLRsTxt >> $RxLRsFa
    echo "The number of sequences extracted is"
    cat $RxLRsFa | grep '>' | wc -l
    echo "$Strain done with EER"
done
```

```
With EER:
P.fragariae - A4
The number of ORF RxLRs overlapping Augustus RxLRs:
202
The number of Augustus RxLRs overlapping ORF RxLRs:
202
The number of RxLRs unique to ORF models:
95
The number of RxLRs unique to Augustus models:
26
The total number of putative RxLRs are:
326
The number of sequences extracted is
326
P.fragariae - Bc1
The number of ORF RxLRs overlapping Augustus RxLRs:
204
The number of Augustus RxLRs overlapping ORF RxLRs:
204
The number of RxLRs unique to ORF models:
93
The number of RxLRs unique to Augustus models:
27
The total number of putative RxLRs are:
328
The number of sequences extracted is
328
P.fragariae - Bc16
The number of ORF RxLRs overlapping Augustus RxLRs:
221
The number of Augustus RxLRs overlapping ORF RxLRs:
221
The number of RxLRs unique to ORF models:
105
The number of RxLRs unique to Augustus models:
38
The total number of putative RxLRs are:
367
The number of sequences extracted is
367
P.fragariae - Bc23
The number of ORF RxLRs overlapping Augustus RxLRs:
208
The number of Augustus RxLRs overlapping ORF RxLRs:
208
The number of RxLRs unique to ORF models:
94
The number of RxLRs unique to Augustus models:
30
The total number of putative RxLRs are:
335
The number of sequences extracted is
335
P.fragariae - Nov27
The number of ORF RxLRs overlapping Augustus RxLRs:
205
The number of Augustus RxLRs overlapping ORF RxLRs:
205
The number of RxLRs unique to ORF models:
92
The number of RxLRs unique to Augustus models:
26
The total number of putative RxLRs are:
325
The number of sequences extracted is
325
P.fragariae - Nov5
The number of ORF RxLRs overlapping Augustus RxLRs:
206
The number of Augustus RxLRs overlapping ORF RxLRs:
206
The number of RxLRs unique to ORF models:
90
The number of RxLRs unique to Augustus models:
30
The total number of putative RxLRs are:
328
The number of sequences extracted is
328
P.fragariae - Nov71
The number of ORF RxLRs overlapping Augustus RxLRs:
205
The number of Augustus RxLRs overlapping ORF RxLRs:
205
The number of RxLRs unique to ORF models:
91
The number of RxLRs unique to Augustus models:
25
The total number of putative RxLRs are:
323
The number of sequences extracted is
323
P.fragariae - Nov77
The number of ORF RxLRs overlapping Augustus RxLRs:
184
The number of Augustus RxLRs overlapping ORF RxLRs:
184
The number of RxLRs unique to ORF models:
98
The number of RxLRs unique to Augustus models:
31
The total number of putative RxLRs are:
315
The number of sequences extracted is
315
P.fragariae - Nov9
The number of ORF RxLRs overlapping Augustus RxLRs:
206
The number of Augustus RxLRs overlapping ORF RxLRs:
206
The number of RxLRs unique to ORF models:
90
The number of RxLRs unique to Augustus models:
27
The total number of putative RxLRs are:
324
The number of sequences extracted is
324
P.fragariae - ONT3
The number of ORF RxLRs overlapping Augustus RxLRs:
203
The number of Augustus RxLRs overlapping ORF RxLRs:
203
The number of RxLRs unique to ORF models:
101
The number of RxLRs unique to Augustus models:
28
The total number of putative RxLRs are:
334
The number of sequences extracted is
334
P.fragariae - SCRP245_v2
The number of ORF RxLRs overlapping Augustus RxLRs:
203
The number of Augustus RxLRs overlapping ORF RxLRs:
202
The number of RxLRs unique to ORF models:
97
The number of RxLRs unique to Augustus models:
30
The total number of putative RxLRs are:
333
The number of sequences extracted is
333

Without EER:
P.fragariae - A4
The number of ORF RxLRs overlapping Augustus RxLRs:
327
The number of Augustus RxLRs overlapping ORF RxLRs:
324
The number of RxLRs unique to ORF models:
1,860
The number of RxLRs unique to Augustus models:
87
The total number of putative RxLRs are:
2,278
The number of sequences extracted is
2,278
P.fragariae - Bc1
The number of ORF RxLRs overlapping Augustus RxLRs:
329
The number of Augustus RxLRs overlapping ORF RxLRs:
325
The number of RxLRs unique to ORF models:
1,871
The number of RxLRs unique to Augustus models:
87
The total number of putative RxLRs are:
2,293
The number of sequences extracted is
2,293
P.fragariae - Bc16
The number of ORF RxLRs overlapping Augustus RxLRs:
385
The number of Augustus RxLRs overlapping ORF RxLRs:
378
The number of RxLRs unique to ORF models:
2,077
The number of RxLRs unique to Augustus models:
111
The total number of putative RxLRs are:
2,569
The number of sequences extracted is
2,569
P.fragariae - Bc23
The number of ORF RxLRs overlapping Augustus RxLRs:
325
The number of Augustus RxLRs overlapping ORF RxLRs:
322
The number of RxLRs unique to ORF models:
1,879
The number of RxLRs unique to Augustus models:
92
The total number of putative RxLRs are:
2,301
The number of sequences extracted is
2,301
P.fragariae - Nov27
The number of ORF RxLRs overlapping Augustus RxLRs:
327
The number of Augustus RxLRs overlapping ORF RxLRs:
323
The number of RxLRs unique to ORF models:
1,847
The number of RxLRs unique to Augustus models:
89
The total number of putative RxLRs are:
2,263
The number of sequences extracted is
2,263
P.fragariae - Nov5
The number of ORF RxLRs overlapping Augustus RxLRs:
327
The number of Augustus RxLRs overlapping ORF RxLRs:
324
The number of RxLRs unique to ORF models:
1,845
The number of RxLRs unique to Augustus models:
98
The total number of putative RxLRs are:
2,272
The number of sequences extracted is
2,272
P.fragariae - Nov71
The number of ORF RxLRs overlapping Augustus RxLRs:
335
The number of Augustus RxLRs overlapping ORF RxLRs:
331
The number of RxLRs unique to ORF models:
1,835
The number of RxLRs unique to Augustus models:
92
The total number of putative RxLRs are:
2,265
The number of sequences extracted is
2,265
P.fragariae - Nov77
The number of ORF RxLRs overlapping Augustus RxLRs:
307
The number of Augustus RxLRs overlapping ORF RxLRs:
304
The number of RxLRs unique to ORF models:
1,860
The number of RxLRs unique to Augustus models:
93
The total number of putative RxLRs are:
2,263
The number of sequences extracted is
2,263
P.fragariae - Nov9
The number of ORF RxLRs overlapping Augustus RxLRs:
326
The number of Augustus RxLRs overlapping ORF RxLRs:
322
The number of RxLRs unique to ORF models:
1,888
The number of RxLRs unique to Augustus models:
87
The total number of putative RxLRs are:
2,301
The number of sequences extracted is
2,301
P.fragariae - ONT3
The number of ORF RxLRs overlapping Augustus RxLRs:
337
The number of Augustus RxLRs overlapping ORF RxLRs:
333
The number of RxLRs unique to ORF models:
1,942
The number of RxLRs unique to Augustus models:
92
The total number of putative RxLRs are:
2,377
The number of sequences extracted is
2,377
P.fragariae - SCRP245_v2
The number of ORF RxLRs overlapping Augustus RxLRs:
329
The number of Augustus RxLRs overlapping ORF RxLRs:
323
The number of RxLRs unique to ORF models:
1,849
The number of RxLRs unique to Augustus models:
95
The total number of putative RxLRs are:
2,277
The number of sequences extracted is
2,277
```

H) From ORF gene models - Hmm evidence of CRN effectors

A hmm model relating to crinkler domains was used to identify putative crinklers in ORF gene models. This was done with the following commands:

```bash
for Proteome in $(ls gene_pred/ORF_finder/*/*/*.aa_cat.fa)
do
    # Setting variables
    Strain=$(echo $Proteome | rev | cut -f2 -d '/' | rev)
    Organism=P.fragariae
    OutDir=analysis/CRN_effectors/hmmer_CRN/$Organism/$Strain
    mkdir -p $OutDir
    # Hmmer variables
    ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer
    HmmDir=/home/groups/harrisonlab/project_files/idris/analysis/CRN_effectors/hmmer_models
    # Searches for LFLAK domain
    LFLAK_hmm=$HmmDir/Pinf_Pram_Psoj_Pcap_LFLAK.hmm
    HmmResultsLFLAK="$Strain"_ORF_CRN_LFLAK_unmerged_hmmer.txt
    hmmsearch -T 0 $LFLAK_hmm $Proteome > $OutDir/$HmmResultsLFLAK
    echo "Searching for LFLAK domains in: $Organism $Strain"
    cat $OutDir/$HmmResultsLFLAK | grep 'Initial search space'
    cat $OutDir/$HmmResultsLFLAK | grep 'number of targets reported over threshold'
    HmmFastaLFLAK="$Strain"_ORF_CRN_LFLAK_unmerged_hmmer.fa
    $ProgDir/hmmer2fasta.pl $OutDir/$HmmResultsLFLAK $Proteome > $OutDir/$HmmFastaLFLAK
    # Searches for DWL domain
    DWL_hmm=$HmmDir/Pinf_Pram_Psoj_Pcap_DWL.hmm
    HmmResultsDWL="$Strain"_ORF_CRN_DWL_unmerged_hmmer.txt
    hmmsearch -T 0 $DWL_hmm $Proteome > $OutDir/$HmmResultsDWL
    echo "Searching for DWL domains in: $Organism $Strain"
    cat $OutDir/$HmmResultsDWL | grep 'Initial search space'
    cat $OutDir/$HmmResultsDWL | grep 'number of targets reported over threshold'
    HmmFastaDWL="$Strain"_ORF_CRN_DWL_unmerged_hmmer.fa
    $ProgDir/hmmer2fasta.pl $OutDir/$HmmResultsDWL $Proteome > $OutDir/$HmmFastaDWL
    # Identify ORFs found by both models
    CommonHeaders=$OutDir/"$Strain"_ORF_CRN_DWL_LFLAK_unmerged_headers.txt
    cat $OutDir/$HmmFastaLFLAK $OutDir/$HmmFastaDWL | grep '>' | cut -f1 | tr -d '>' | sort | uniq -d > $CommonHeaders
    echo "The number of CRNs common to both models are:"
    cat $CommonHeaders | wc -l
    # The sequences will be merged based upon the strength of their DWL domain score
    # For this reason headers as they appear in the DWL fasta file were extracted
    Headers=$OutDir/"$Strain"_CRN_hmmer_unmerged_headers.txt
    cat $OutDir/$HmmFastaDWL | grep '>' | grep -w -f $CommonHeaders | tr -d '>' | sed -r 's/\s+/\t/g'| sed 's/=\t/=/g' | tr -d '-' | sed 's/hmm_score/HMM_score/g' > $Headers
    # As we are dealing with JGI and Broad sequences, some features need formatting:
    ORF_Gff=$(ls gene_pred/ORF_finder/*/$Strain/*_ORF.gff3)
    # Gff features were extracted for each header
    CRN_unmerged_Gff=$OutDir/"$Strain"_CRN_unmerged_hmmer.gff3
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    $ProgDir/extract_gff_for_sigP_hits.pl $Headers $ORF_Gff CRN_HMM Name > $CRN_unmerged_Gff
    # Gff features were merged based upon the DWL hmm score
    DbDir=analysis/databases/$Organism/$Strain
    mkdir -p $DbDir
    ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/merge_gff
    $ProgDir/make_gff_database.py --inp $CRN_unmerged_Gff --db $DbDir/CRN_ORF.db
    CRN_Merged_Gff=$OutDir/"$Strain"_CRN_merged_hmmer.gff3
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    $ProgDir/merge_sigP_ORFs.py --inp $DbDir/CRN_ORF.db --id LFLAK_DWL_CRN --out $DbDir/CRN_ORF_merged.db --gff > $CRN_Merged_Gff
    # Final results are reported:
    echo "Number of CRN ORFs after merging:"
    cat $CRN_Merged_Gff | grep 'gene' | wc -l
    echo "$Strain done"
done
```

```
Searching for LFLAK domains in: P.fragariae A4
Initial search space (Z):            654,457  [actual number of targets]
Domain search space  (domZ):             243  [number of targets reported over threshold]
Searching for DWL domains in: P.fragariae A4
Initial search space (Z):            654,457  [actual number of targets]
Domain search space  (domZ):             380  [number of targets reported over threshold]
The number of CRNs common to both models are:
169
Number of CRN ORFs after merging:
106
Searching for LFLAK domains in: P.fragariae Bc16
Initial search space (Z):            776,140  [actual number of targets]
Domain search space  (domZ):             276  [number of targets reported over threshold]
Searching for DWL domains in: P.fragariae Bc16
Initial search space (Z):            776,140  [actual number of targets]
Domain search space  (domZ):             425  [number of targets reported over threshold]
The number of CRNs common to both models are:
192
Number of CRN ORFs after merging:
118
Searching for LFLAK domains in: P.fragariae Bc1
Initial search space (Z):            657,394  [actual number of targets]
Domain search space  (domZ):             243  [number of targets reported over threshold]
Searching for DWL domains in: P.fragariae Bc1
Initial search space (Z):            657,394  [actual number of targets]
Domain search space  (domZ):             380  [number of targets reported over threshold]
The number of CRNs common to both models are:
169
Number of CRN ORFs after merging:
106
Searching for LFLAK domains in: P.fragariae Bc23
Initial search space (Z):            648,130  [actual number of targets]
Domain search space  (domZ):             244  [number of targets reported over threshold]
Searching for DWL domains in: P.fragariae Bc23
Initial search space (Z):            648,130  [actual number of targets]
Domain search space  (domZ):             367  [number of targets reported over threshold]
The number of CRNs common to both models are:
169
Number of CRN ORFs after merging:
106
Searching for LFLAK domains in: P.fragariae Nov27
Initial search space (Z):            653,798  [actual number of targets]
Domain search space  (domZ):             246  [number of targets reported over threshold]
Searching for DWL domains in: P.fragariae Nov27
Initial search space (Z):            653,798  [actual number of targets]
Domain search space  (domZ):             371  [number of targets reported over threshold]
The number of CRNs common to both models are:
171
Number of CRN ORFs after merging:
106
Searching for LFLAK domains in: P.fragariae Nov5
Initial search space (Z):            654,072  [actual number of targets]
Domain search space  (domZ):             245  [number of targets reported over threshold]
Searching for DWL domains in: P.fragariae Nov5
Initial search space (Z):            654,072  [actual number of targets]
Domain search space  (domZ):             378  [number of targets reported over threshold]
The number of CRNs common to both models are:
171
Number of CRN ORFs after merging:
106
Searching for LFLAK domains in: P.fragariae Nov71
Initial search space (Z):            649,542  [actual number of targets]
Domain search space  (domZ):             247  [number of targets reported over threshold]
Searching for DWL domains in: P.fragariae Nov71
Initial search space (Z):            649,542  [actual number of targets]
Domain search space  (domZ):             377  [number of targets reported over threshold]
The number of CRNs common to both models are:
170
Number of CRN ORFs after merging:
105
Searching for LFLAK domains in: P.fragariae Nov77
Initial search space (Z):            653,276  [actual number of targets]
Domain search space  (domZ):             230  [number of targets reported over threshold]
Searching for DWL domains in: P.fragariae Nov77
Initial search space (Z):            653,276  [actual number of targets]
Domain search space  (domZ):             371  [number of targets reported over threshold]
The number of CRNs common to both models are:
167
Number of CRN ORFs after merging:
104
Searching for LFLAK domains in: P.fragariae Nov9
Initial search space (Z):            660,249  [actual number of targets]
Domain search space  (domZ):             243  [number of targets reported over threshold]
Searching for DWL domains in: P.fragariae Nov9
Initial search space (Z):            660,249  [actual number of targets]
Domain search space  (domZ):             377  [number of targets reported over threshold]
The number of CRNs common to both models are:
167
Number of CRN ORFs after merging:
105
Searching for LFLAK domains in: P.fragariae ONT3
Initial search space (Z):            722,865  [actual number of targets]
Domain search space  (domZ):             241  [number of targets reported over threshold]
Searching for DWL domains in: P.fragariae ONT3
Initial search space (Z):            722,865  [actual number of targets]
Domain search space  (domZ):             361  [number of targets reported over threshold]
The number of CRNs common to both models are:
166
Number of CRN ORFs after merging:
103
Searching for LFLAK domains in: P.fragariae SCRP245_v2
Initial search space (Z):            689,938  [actual number of targets]
Domain search space  (domZ):             241  [number of targets reported over threshold]
Searching for DWL domains in: P.fragariae SCRP245_v2
Initial search space (Z):            689,938  [actual number of targets]
Domain search space  (domZ):             363  [number of targets reported over threshold]
The number of CRNs common to both models are:
167
Number of CRN ORFs after merging:
105
```

Merge CRNs from augustus models and ORF fragments

```bash
for MergeDir in $(ls -d analysis/CRN_effectors/hmmer_CRN/*/*)
do
    Strain=$(echo "$MergeDir" | rev | cut -f1 -d '/' | rev)
    Species=$(echo "$MergeDir" | rev | cut -f2 -d '/' | rev)
    AugGff=$(ls $MergeDir/"$Strain"_pub_CRN_LFLAK_DWL.gff)
    AugFa=$(ls gene_pred/final/"$Species"/"$Strain"/final/final_genes_combined.pep.fasta)
    ORFsFa=$(ls gene_pred/ORF_finder/*/"$Strain"/"$Strain".aa_cat.fa)
    ORFGff=$MergeDir/"$Strain"_CRN_merged_hmmer.gff3
    ORFsInAug=$MergeDir/"$Strain"_ORFsInAug_CRN_hmmer.bed
    AugInORFs=$MergeDir/"$Strain"_AugInORFs_CRN_hmmer.bed
    ORFsUniq=$MergeDir/"$Strain"_ORFsUniq_CRN_hmmer.bed
    AugUniq=$MergeDir/"$Strain"_Aug_Uniq_CRN_hmmer.bed
    TotalCRNsTxt=$MergeDir/"$Strain"_final_CRN.txt
    TotalCRNsGff=$MergeDir/"$Strain"_final_CRN.gff
    TotalCRNsHeaders=$MergeDir/"$Strain"_Total_CRN_headers.txt
    bedtools intersect -wa -u -a $ORFGff -b $AugGff > $ORFsInAug
    bedtools intersect -wa -u -a $AugGff -b $ORFGff > $AugInORFs
    bedtools intersect -v -wa -a $ORFGff -b $AugGff > $ORFsUniq
    bedtools intersect -v -wa -a $AugGff -b $ORFGff > $AugUniq
    echo "$Species - $Strain"

    echo "The number of ORF CRNs overlapping Augustus CRNs:"
    cat $ORFsInAug | grep -w -e 'transcript' -e 'mRNA' | wc -l
    echo "The number of Augustus CRNs overlapping ORF CRNs:"
    cat $AugInORFs | grep -w -e 'transcript' -e 'mRNA' | wc -l
    cat $AugInORFs | grep -w -e 'transcript' -e 'mRNA'  | cut -f9 | cut -f1 -d ';' | cut -f2 -d '=' > $TotalCRNsTxt
    echo "The number of CRNs unique to ORF models:"
    cat $ORFsUniq | grep -w 'transcript'| grep -w -e 'transcript' -e 'mRNA'  | cut -f9 | cut -f4 -d ';' | cut -f2 -d '=' | wc -l
    cat $ORFsUniq | grep -w 'transcript'| grep -w -e 'transcript' -e 'mRNA'  | cut -f9 | cut -f4 -d ';' | cut -f2 -d '=' >> $TotalCRNsTxt
    echo "The number of CRNs unique to Augustus models:"
    cat $AugUniq | grep -w -e 'transcript' -e 'mRNA' | wc -l
    cat $AugUniq | grep -w -e 'transcript' -e 'mRNA'  | cut -f9 | cut -f1 -d ';' | cut -f2 -d '=' >> $TotalCRNsTxt

    cat $AugInORFs $AugUniq $ORFsUniq | grep -w -f $TotalCRNsTxt > $TotalCRNsGff

    CRNsFa=$MergeDir/"$Strain"_final_CRN.fa
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    $ProgDir/extract_from_fasta.py --fasta $AugFa --headers $TotalCRNsTxt > $CRNsFa
    $ProgDir/extract_from_fasta.py --fasta $ORFsFa --headers $TotalCRNsTxt >> $CRNsFa
    echo "The number of sequences extracted is"
    cat $CRNsFa | grep '>' | wc -l
    echo "$Strain done"
done
```

```
P.fragariae - A4
The number of ORF CRNs overlapping Augustus CRNs:
100
The number of Augustus CRNs overlapping ORF CRNs:
105
The number of CRNs unique to ORF models:
6
The number of CRNs unique to Augustus models:
4
The number of sequences extracted is
115
P.fragariae - Bc1
The number of ORF CRNs overlapping Augustus CRNs:
100
The number of Augustus CRNs overlapping ORF CRNs:
107
The number of CRNs unique to ORF models:
6
The number of CRNs unique to Augustus models:
4
The number of sequences extracted is
117
P.fragariae - Bc16
The number of ORF CRNs overlapping Augustus CRNs:
111
The number of Augustus CRNs overlapping ORF CRNs:
117
The number of CRNs unique to ORF models:
7
The number of CRNs unique to Augustus models:
5
The number of sequences extracted is
129
P.fragariae - Bc23
The number of ORF CRNs overlapping Augustus CRNs:
101
The number of Augustus CRNs overlapping ORF CRNs:
107
The number of CRNs unique to ORF models:
5
The number of CRNs unique to Augustus models:
6
The number of sequences extracted is
118
P.fragariae - Nov27
The number of ORF CRNs overlapping Augustus CRNs:
101
The number of Augustus CRNs overlapping ORF CRNs:
109
The number of CRNs unique to ORF models:
5
The number of CRNs unique to Augustus models:
5
The number of sequences extracted is
119
P.fragariae - Nov5
The number of ORF CRNs overlapping Augustus CRNs:
101
The number of Augustus CRNs overlapping ORF CRNs:
107
The number of CRNs unique to ORF models:
5
The number of CRNs unique to Augustus models:
4
The number of sequences extracted is
116
P.fragariae - Nov71
The number of ORF CRNs overlapping Augustus CRNs:
99
The number of Augustus CRNs overlapping ORF CRNs:
107
The number of CRNs unique to ORF models:
6
The number of CRNs unique to Augustus models:
5
The number of sequences extracted is
118
P.fragariae - Nov77
The number of ORF CRNs overlapping Augustus CRNs:
99
The number of Augustus CRNs overlapping ORF CRNs:
107
The number of CRNs unique to ORF models:
5
The number of CRNs unique to Augustus models:
4
The number of sequences extracted is
116
P.fragariae - Nov9
The number of ORF CRNs overlapping Augustus CRNs:
100
The number of Augustus CRNs overlapping ORF CRNs:
108
The number of CRNs unique to ORF models:
5
The number of CRNs unique to Augustus models:
4
The number of sequences extracted is
117
P.fragariae - ONT3
The number of ORF CRNs overlapping Augustus CRNs:
97
The number of Augustus CRNs overlapping ORF CRNs:
104
The number of CRNs unique to ORF models:
6
The number of CRNs unique to Augustus models:
4
The number of sequences extracted is
114
P.fragariae - SCRP245_v2
The number of ORF CRNs overlapping Augustus CRNs:
100
The number of Augustus CRNs overlapping ORF CRNs:
108
The number of CRNs unique to ORF models:
5
The number of CRNs unique to Augustus models:
6
The number of sequences extracted is
119
```

#Making a combined file of Braker and CodingQuary genes with additional ORF effector candidates

```bash
#Without EER discrimination
for GeneGff in $(ls gene_pred/final/*/*/final/final_genes_appended.gff3)
do
    Strain=$(echo $GeneGff | rev | cut -d '/' -f3 | rev)
    Organism=$(echo $GeneGff | rev | cut -d '/' -f4 | rev)
    echo "$Strain - $Organism"
    GffOrfRxLR=$(ls analysis/RxLR_effectors/combined_evidence/P.fragariae/$Strain/"$Strain"_ORFsUniq_RxLR_motif_hmm.gff)
    GffOrfCRN=$(ls analysis/CRN_effectors/hmmer_CRN/P.fragariae/$Strain/"$Strain"_ORFsUniq_CRN_hmmer.bed)
    if [ -f repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked.fa)
        echo $Assembly
    elif [ -f repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked.fa)
        echo $Assembly
    else
        Assembly=$(ls repeat_masked/quiver_results/Bc16/filtered_contigs_repmask/*_softmasked.fa)
        echo $Assembly
    fi
    OutDir=gene_pred/annotation/P.fragariae/$Strain
    mkdir -p $OutDir
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/augustus
    $ProgDir/aug_gff_add_exon.py --inp_gff $GeneGff  \
    	| sed 's/\(\tCDS\t.*\)transcript_id "\(.*\)"; gene_id.*/\1ID=\2.CDS; Parent=\2/g' \
    	| sed 's/\(\exon\t.*\)transcript_id "\(.*\)"; gene_id.*/\1ID=\2.exon; Parent=\2/g' \
    	| sed 's/transcript_id "/ID=/g' | sed 's/";/;/g' | sed 's/ gene_id "/Parent=/g' \
    	| sed -r "s/\tg/\tID=g/g" | sed 's/ID=gene/gene/g' | sed -r "s/;$//g" \
    	| sed "s/\ttranscript\t.*ID=\(.*\).t.*$/\0;Parent=\1/" \
    	> $OutDir/"$Strain"_genes_incl_ORFeffectors.gff3
    # cat $GeneGff > $OutDir/10300_genes_incl_ORFeffectors.gff3
    ProgDir=/home/adamst/git_repos/scripts/phytophthora/10300_analysis
    $ProgDir/gff_name2id.py --gff $GffOrfRxLR > $OutDir/ORF_RxLR_parsed.gff3
    $ProgDir/gff_name2id.py --gff $GffOrfCRN > $OutDir/ORF_CRN_parsed.gff3

    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    $ProgDir/add_ORF_features.pl $OutDir/ORF_RxLR_parsed.gff3 $Assembly >> $OutDir/"$Strain"_genes_incl_ORFeffectors.gff3
    $ProgDir/add_ORF_features.pl $OutDir/ORF_CRN_parsed.gff3 $Assembly >> $OutDir/"$Strain"_genes_incl_ORFeffectors.gff3
    # Make gene models from gff files.
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/codingquary
    $ProgDir/gff2fasta.pl $Assembly $OutDir/"$Strain"_genes_incl_ORFeffectors.gff3 $OutDir/"$Strain"_genes_incl_ORFeffectors
    # Note - these fasta files have not been validated - do not use
done

#With EER discrimination
for GeneGff in $(ls gene_pred/final/*/*/final/final_genes_appended.gff3)
do
    Strain=$(echo $GeneGff | rev | cut -d '/' -f3 | rev)
    Organism=$(echo $GeneGff | rev | cut -d '/' -f4 | rev)
    echo "$Strain - $Organism"
    GffOrfRxLR=$(ls analysis/RxLR_effectors/combined_evidence/P.fragariae/$Strain/"$Strain"_ORFsUniq_RxLR_EER_motif_hmm.gff)
    GffOrfCRN=$(ls analysis/CRN_effectors/hmmer_CRN/P.fragariae/$Strain/"$Strain"_ORFsUniq_CRN_hmmer.bed)
    if [ -f repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked.fa)
        echo $Assembly
    elif [ -f repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked.fa)
        echo $Assembly
    else
        Assembly=$(ls repeat_masked/quiver_results/Bc16/filtered_contigs_repmask/*_softmasked.fa)
        echo $Assembly
    fi
    OutDir=gene_pred/annotation/P.fragariae/$Strain
    mkdir -p $OutDir
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/augustus
    $ProgDir/aug_gff_add_exon.py --inp_gff $GeneGff  \
    	| sed 's/\(\tCDS\t.*\)transcript_id "\(.*\)"; gene_id.*/\1ID=\2.CDS; Parent=\2/g' \
    	| sed 's/\(\exon\t.*\)transcript_id "\(.*\)"; gene_id.*/\1ID=\2.exon; Parent=\2/g' \
    	| sed 's/transcript_id "/ID=/g' | sed 's/";/;/g' | sed 's/ gene_id "/Parent=/g' \
    	| sed -r "s/\tg/\tID=g/g" | sed 's/ID=gene/gene/g' | sed -r "s/;$//g" \
    	| sed "s/\ttranscript\t.*ID=\(.*\).t.*$/\0;Parent=\1/" \
    	> $OutDir/"$Strain"_genes_incl_ORFeffectors_conservative.gff3
    # cat $GeneGff > $OutDir/10300_genes_incl_ORFeffectors.gff3
    ProgDir=/home/adamst/git_repos/scripts/phytophthora/10300_analysis
    $ProgDir/gff_name2id.py --gff $GffOrfRxLR > $OutDir/ORF_RxLR_EER_parsed.gff3
    $ProgDir/gff_name2id.py --gff $GffOrfCRN > $OutDir/ORF_CRN_parsed.gff3

    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    $ProgDir/add_ORF_features.pl $OutDir/ORF_RxLR_EER_parsed.gff3 $Assembly >> $OutDir/"$Strain"_genes_incl_ORFeffectors_conservative.gff3
    $ProgDir/add_ORF_features.pl $OutDir/ORF_CRN_parsed.gff3 $Assembly >> $OutDir/"$Strain"_genes_incl_ORFeffectors_conservative.gff3
    # Make gene models from gff files.
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/codingquary
    $ProgDir/gff2fasta.pl $Assembly $OutDir/"$Strain"_genes_incl_ORFeffectors_conservative.gff3 $OutDir/"$Strain"_genes_incl_ORFeffectors_conservative
    # Note - these fasta files have not been validated - do not use
done
```

#Functional annotation

##A)Interproscan
Interproscan was used to give gene models functional annotations. These scripts are modified to take into account different directory structures

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/interproscan/
for Genes in $(ls gene_pred/annotation/P.fragariae/*/*_genes_incl_ORFeffectors.pep.fasta)
do
    $ProgDir/sub_interproscan.sh $Genes
done

ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/interproscan/
for Genes in $(ls gene_pred/annotation/P.fragariae/*/*_genes_incl_ORFeffectors_conservative.pep.fasta)
do
    $ProgDir/sub_interproscan2.sh $Genes
done
```

Following this, split files were combined as follows:

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/interproscan
for Proteome in $(ls gene_pred/annotation/P.fragariae/*/*_genes_incl_ORFeffectors.pep.fasta)
do
    Strain=$(echo $Proteome | rev | cut -d '/' -f2 | rev)
    Organism=$(echo $Proteome | rev | cut -d '/' -f3 | rev)
    echo "$Organism - $Strain"
    echo $Strain
    InterProRaw=gene_pred/interproscan/$Organism/$Strain/greedy/raw
    $ProgDir/append_interpro.sh $Proteome $InterProRaw
done

ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/interproscan
for Proteome in $(ls gene_pred/annotation/P.fragariae/*/*_genes_incl_ORFeffectors_conservative.pep.fasta)
do
    Strain=$(echo $Proteome | rev | cut -d '/' -f2 | rev)
    Organism=$(echo $Proteome | rev | cut -d '/' -f3 | rev)
    echo "$Organism - $Strain"
    echo $Strain
    InterProRaw=gene_pred/interproscan/$Organism/$Strain/conservative/raw
    $ProgDir/append_interpro_2.sh $Proteome $InterProRaw
done
```

##B)Swissprot

```bash
for Proteome in $(ls gene_pred/annotation/P.fragariae/*/*_genes_incl_ORFeffectors.pep.fasta)
do
    Strain=$(echo $Proteome | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
    OutDir=gene_pred/swissprot/$Organism/$Strain/greedy
    SwissDbDir=../../uniprot/swissprot
    SwissDbName=uniprot_sprot
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/swissprot
    qsub $ProgDir/sub_swissprot.sh $Proteome $OutDir $SwissDbDir $SwissDbName
done

for Proteome in $(ls gene_pred/annotation/P.fragariae/*/*_genes_incl_ORFeffectors_conservative.pep.fasta)
do
    Strain=$(echo $Proteome | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
    OutDir=gene_pred/swissprot/$Organism/$Strain/conservative
    SwissDbDir=../../uniprot/swissprot
    SwissDbName=uniprot_sprot
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/swissprot
    qsub $ProgDir/sub_swissprot.sh $Proteome $OutDir $SwissDbDir $SwissDbName
done
```

##C)Identify genes with transmembrane domains
WARNING: This has a high false positive rate - modified from the base script to allow greedy/conservative

```bash
for Proteome in $(ls gene_pred/annotation/P.fragariae/*/*_genes_incl_ORFeffectors.pep.fasta)
do
    Strain=$(echo $Proteome | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/transmembrane_helices
    qsub $ProgDir/submit_TMHMM.sh $Proteome
done

for Proteome in $(ls gene_pred/annotation/P.fragariae/*/*_genes_incl_ORFeffectors_conservative.pep.fasta)
do
    Strain=$(echo $Proteome | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/transmembrane_helices
    qsub $ProgDir/submit_TMHMM2.sh $Proteome
done
```

Summarise numbers of TM Proteins

```bash
for TM in $(ls gene_pred/trans_mem/P.fragariae/*/*/*_TM_genes_pos.txt)
do
    Strain=$(echo $TM | rev | cut -f3 -d '/' | rev)
    Type=$(echo $TM | rev | cut -f2 -d '/' | rev)
    echo "$Strain - $Type"
    echo "The number of proteins scoring positive for a transmembrane helix is:"
    cat $TM | wc -l
    echo ""
done
```

```
A4 - conservative
The number of proteins scoring positive for a transmembrane helix is:
4,268

A4 - greedy
The number of proteins scoring positive for a transmembrane helix is:
4,600

Bc16 - conservative
The number of proteins scoring positive for a transmembrane helix is:
4,281

Bc16 - greedy
The number of proteins scoring positive for a transmembrane helix is:
4,634

Bc1 - conservative
The number of proteins scoring positive for a transmembrane helix is:
4,233

Bc1 - greedy
The number of proteins scoring positive for a transmembrane helix is:
4,564

Bc23 - conservative
The number of proteins scoring positive for a transmembrane helix is:
4,241

Bc23 - greedy
The number of proteins scoring positive for a transmembrane helix is:
4,567

Nov27 - conservative
The number of proteins scoring positive for a transmembrane helix is:
4,263

Nov27 - greedy
The number of proteins scoring positive for a transmembrane helix is:
4,585

Nov5 - conservative
The number of proteins scoring positive for a transmembrane helix is:
4,288

Nov5 - greedy
The number of proteins scoring positive for a transmembrane helix is:
4,616

Nov71 - conservative
The number of proteins scoring positive for a transmembrane helix is:
4,276

Nov71 - greedy
The number of proteins scoring positive for a transmembrane helix is:
4,596

Nov77 - conservative
The number of proteins scoring positive for a transmembrane helix is:
4,280

Nov77 - greedy
The number of proteins scoring positive for a transmembrane helix is:
4,597

Nov9 - conservative
The number of proteins scoring positive for a transmembrane helix is:
4,251

Nov9 - greedy
The number of proteins scoring positive for a transmembrane helix is:
4,586

ONT3 - conservative
The number of proteins scoring positive for a transmembrane helix is:
5,216

ONT3 - greedy
The number of proteins scoring positive for a transmembrane helix is:
5,569

SCRP245_v2 - conservative
The number of proteins scoring positive for a transmembrane helix is:
5,159

SCRP245_v2 - greedy
The number of proteins scoring positive for a transmembrane helix is:
5,487
```

Create a headers file

```bash
for PosFile in $(ls gene_pred/trans_mem/*/*/*/*_TM_genes_pos.txt)
do
    TmHeaders=$(echo $PosFile | sed 's/.txt/_headers.txt/g')
    cat $PosFile | cut -f1 > $TmHeaders
done
```

##D)Identify genes with GPI anchors

Proteins were identified by submitting the combined protein file to webserver at http://gpi.unibe.ch

Output directory made

This crashed before running ONT-3_conservative, SCRP245_v2_greedy and SCRP245_v2_conservative - have sent an email requesting a reboot, but it's not strictly crucial

```bash
for Proteome in $(ls gene_pred/annotation/P.fragariae/*/*_genes_incl_ORFeffectors.pep.fasta)
do
    Strain=$(echo $Proteome | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
    echo "$Organism - $Strain"
    OutDir=gene_pred/GPIsom/$Organism/$Strain/greedy
    mkdir -p $OutDir
done

for Proteome in $(ls gene_pred/annotation/P.fragariae/*/*_genes_incl_ORFeffectors_conservative.pep.fasta)
do
    Strain=$(echo $Proteome | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
    echo "$Organism - $Strain"
    OutDir=gene_pred/GPIsom/$Organism/$Strain/conservative
    mkdir -p $OutDir
done
```

Results were parsed to the file

```bash
nano gene_pred/GPIsom/P.fragariae/A4/greedy/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/Bc1/greedy/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/Bc16/greedy/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/Bc23/greedy/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/Nov27/greedy/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/Nov5/greedy/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/Nov71/greedy/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/Nov77/greedy/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/Nov9/greedy/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/ONT3/greedy/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/SCRP245_v2/greedy/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/A4/conservative/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/Bc1/conservative/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/Bc16/conservative/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/Bc23/conservative/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/Nov27/conservative/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/Nov5/conservative/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/Nov71/conservative/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/Nov77/conservative/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/Nov9/conservative/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/ONT3/conservative/GPI_pos.fa
nano gene_pred/GPIsom/P.fragariae/SCRP245_v2/conservative/GPI_pos.fa
```

Create a file just listing gene names

```bash
for PosFile in $(ls gene_pred/GPIsom/*/*/*/GPI_pos.fa)
do
    GPIHeaders=$(echo $PosFile | sed 's/.fa/.txt/g')
    cat $PosFile | grep -e ">" | cut -f1 -d ' ' | sed 's/>//g' > $GPIHeaders
done
```

Summarise numbers of GPI Proteins

```bash
for GPI in $(ls gene_pred/GPIsom/P.fragariae/*/*/*.txt)
do
    Strain=$(echo $GPI | rev | cut -f3 -d '/' | rev)
    Type=$(echo $GPI | rev | cut -f2 -d '/' | rev)
    echo "$Strain - $Type"
    echo "The number of proteins scoring positive for being GPI anchored is:"
    cat $GPI | wc -l
    echo ""
done
```

```
A4 - conservative
The number of proteins scoring positive for being GPI anchored is:
576

A4 - greedy
The number of proteins scoring positive for being GPI anchored is:
829

Bc16 - conservative
The number of proteins scoring positive for being GPI anchored is:
647

Bc16 - greedy
The number of proteins scoring positive for being GPI anchored is:
925

Bc1 - conservative
The number of proteins scoring positive for being GPI anchored is:
570

Bc1 - greedy
The number of proteins scoring positive for being GPI anchored is:
827

Bc23 - conservative
The number of proteins scoring positive for being GPI anchored is:
581

Bc23 - greedy
The number of proteins scoring positive for being GPI anchored is:
839

Nov27 - conservative
The number of proteins scoring positive for being GPI anchored is:
561

Nov27 - greedy
The number of proteins scoring positive for being GPI anchored is:
813

Nov5 - conservative
The number of proteins scoring positive for being GPI anchored is:
574

Nov5 - greedy
The number of proteins scoring positive for being GPI anchored is:
827

Nov71 - conservative
The number of proteins scoring positive for being GPI anchored is:
579

Nov71 - greedy
The number of proteins scoring positive for being GPI anchored is:
832

Nov77 - conservative
The number of proteins scoring positive for being GPI anchored is:
565

Nov77 - greedy
The number of proteins scoring positive for being GPI anchored is:
816

Nov9 - conservative
The number of proteins scoring positive for being GPI anchored is:
569

Nov9 - greedy
The number of proteins scoring positive for being GPI anchored is:
829

ONT3 - conservative
The number of proteins scoring positive for being GPI anchored is:
649

ONT3 - greedy
The number of proteins scoring positive for being GPI anchored is:
915

SCRP245_v2 - conservative
The number of proteins scoring positive for being GPI anchored is:
585

SCRP245_v2 - greedy
The number of proteins scoring positive for being GPI anchored is:
841
```

Further downstream analysis done in Whole_Genome_Orthology.md, RNA-Seq_analysis.md and SNP_analysis.md
