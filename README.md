# *Phytophthora fragariae*
Commands used in the analysis of P. fragariae genomes
A4, Bc23, Nov5, Nov77, ONT3, SCRP245_v2, Bc16, 62471 and Nov27
62471 is P. cactorum
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

** Estimated Genome Size is:
A4: 93,413,554
SCRP245_v2: 127,550,025
Bc23: 103,251,773
Nov5: 95,350,039
Nov77: 92,399,813
ONT3: 103,869,049
Bc16: 90,864,210
62471: 548,976,060
Nov27: 93,851,233
Bc1: 1,196,301,136
Nov9: 959,591,302
Nov71: 810,779,109 **

** Esimated Coverage is:
A4: 23
SCRP245_v2: 23
Bc23: 24
Nov5: 25
Nov77: 30
ONT3: 26
Bc16: 41
62471: 5 (38)
Nov27: 31
Bc1: 5 (70)
Nov9: 5 (55)
Nov71: 5 (41) **

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

**N50:
A4: 18245
BC-16: 437436
BC-23: 18227
NOV-27: 19406
NOV-5: 17887
NOV-77: 18909
ONT-3: 22074
SCRP245_v2: 20105
NOV-71: 20226
NOV-9: 21522
BC-1: 21834**

**L50:
A4: 1116
BC-16: 59
BC-23: 1119
NOV-27: 1046
NOV-5: 1134
NOV-77: 1102
ONT-3: 917
SCRP245_v2: 994
NOV-71: 1016
NOV-9: 978
BC-1: 954**

**Number of contigs > 1kb:
A4: 8660
BC-16: 406
BC-23: 8556
NOV-27: 8040
NOV-5: 8760
NOV-77: 8500
ONT-3: 8540
SCRP245_v2: 8584
NOV-71: 7885
NOV-9: 7655
BC-1: 7504**

#Repeatmasking

Repeat masking was performed and used the following programs: Repeatmasker Repeatmodeler

The best assemblies were used to perform repeatmasking

for BC-16 pacbio data:

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/repeat_masking
for BestAss in $(ls assembly/merged_canu_spades/*/*/95m/filtered_contigs/Bc16_contigs_renamed.fasta)
do
    qsub $ProgDir/rep_modeling.sh $BestAss
    qsub $ProgDir/transposonPSI.sh $BestAss
done
```

for other isolates Illumina data:

```bash
for Strain in A4 Bc1 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for BestAss in $(ls assembly/spades/*/$Strain/filtered_contigs/*_500bp_renamed.fasta)
    do
        qsub $ProgDir/rep_modeling.sh $BestAss
        qsub $ProgDir/transposonPSI.sh $BestAss
    done
done   
```

The number of bases masked by transposonPSI and Repeatmasker were summarised using the following commands:

```bash
for RepDir in $(ls -d repeat_masked/P.*/*/filtered_contigs_repmask)
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

** A4
The number of bases masked by RepeatMasker:	24836372
The number of bases masked by TransposonPSI:	6237528
The total number of masked bases are:	26598776
Bc16
The number of bases masked by RepeatMasker:	37871080
The number of bases masked by TransposonPSI:	8820517
The total number of masked bases are:	39592894
Bc1
The number of bases masked by RepeatMasker:	24254593
The number of bases masked by TransposonPSI:	6219671
The total number of masked bases are:	26154357
Bc23
The number of bases masked by RepeatMasker:	23771588
The number of bases masked by TransposonPSI:	6101880
The total number of masked bases are:	25516134
Nov27
The number of bases masked by RepeatMasker:	24653573
The number of bases masked by TransposonPSI:	6209723
The total number of masked bases are:	26343538
Nov5
The number of bases masked by RepeatMasker:	24011096
The number of bases masked by TransposonPSI:	6242538
The total number of masked bases are:	25856769
Nov71
The number of bases masked by RepeatMasker:	24200190
The number of bases masked by TransposonPSI:	6080704
The total number of masked bases are:	25824977
Nov77
The number of bases masked by RepeatMasker:	24253868
The number of bases masked by TransposonPSI:	6250930
The total number of masked bases are:	26117699
Nov9
The number of bases masked by RepeatMasker:	24774161
The number of bases masked by TransposonPSI:	6290033
The total number of masked bases are:	26664169
ONT3
The number of bases masked by RepeatMasker:	25224812
The number of bases masked by TransposonPSI:	6238377
The total number of masked bases are:	26981713
SCRP245_v2
The number of bases masked by RepeatMasker:	23381847
The number of bases masked by TransposonPSI:	6037837
The total number of masked bases are:	25248164 **

#Gene Prediction
Gene prediction followed three steps: Pre-gene prediction - Quality of genome assemblies were assessed using Cegma to see how many core eukaryotic genes can be identified. Gene model training - Gene models were trained using assembled RNAseq data as part of the Braker1 pipeline Gene prediction - Gene models were used to predict genes in genomes as part of the the Braker1 pipeline. This used RNAseq data as hints for gene models.

##Pre-gene prediction

Quality of genome assemblies was assessed by looking for the gene space in the assemblies.

```bash
ProgDir=/home/adamst/git_repos/tools/gene_prediction/cegma
for Genome in $(ls repeat_masked/P.*/*/filtered_contigs_repmask/*_contigs_unmasked.fa)
do
    echo $Genome
    qsub $ProgDir/sub_cegma.sh $Genome dna
done
```

Outputs were summarised using the commands:

```bash
for File in $(ls gene_pred/cegma/*/*/*_dna_cegma.completeness_report)
do
    Strain=$(echo $File | rev | cut -f2 -d '/' | rev)
    Species=$(echo $File | rev | cut -f3 -d '/' | rev)
    printf "$Species\t$Strain\n"
    cat $File | head -n18 | tail -n+4;printf "\n"
done >> gene_pred/cegma/cegma_results_dna_summary.txt

less gene_pred/cegma/cegma_results_dna_summary.txt
```

** A4
Complete: 95.16%
Partial: 97.98%

Bc16
Complete: 94.35%
Partial: 96.37%

Bc1
Complete: 95.16%
Partial: 97.58%

Bc23
Complete: 95.16%
Partial: 97.58%

Nov27
Complete: 94.76%
Partial: 97.18%

Nov5
Complete: 94.76%
Partial: 97.18%

Nov71
Complete: 95.16%
Partial: 97.98%

Nov77
Complete: 94.76%
Partial: 97.18%

Nov9
Complete: 94.35%
Partial: 97.18%

ONT3
Complete: 95.16%
Partial: 97.18%

SCRP245_v2
Complete: 95.16%
Partial: 97.18% **

#Gene prediction
Gene prediction was performed for the P. fragariae genomes. Two gene prediction approaches were used:

Gene prediction using Braker1 and Prediction of all putative ORFs in the genome using the ORF finder (atg.pl) approach.

##Gene prediction 1 - Braker1 gene model training and prediction

Gene prediction was performed using Braker1.

First, RNAseq data was aligned to P. fragariae genomes.

qc of RNA seq data was performed as part of sequencing the 10300 genome:

```bash
FileF=qc_rna/raw_rna/genbank/P.cactorum/F/SRR1206032_trim.fq.gz
FileR=qc_rna/raw_rna/genbank/P.cactorum/R/SRR1206033_trim.fq.gz
```

#Aligning

```bash
for Assembly in $(ls repeat_masked/*/*/filtered_contigs_repmask/*_contigs_unmasked.fa)
do
    Strain=$(echo $Assembly| rev | cut -d '/' -f3 | rev)
    Organism=$(echo $Assembly | rev | cut -d '/' -f4 | rev)
    echo "$Organism - $Strain"
    for RNA in $(ls qc_rna/genbank/P.cactorum/10300/*/*_trim.fq.gz)
    do
        Timepoint=$(echo $RNA | rev | cut -f1 -d '/' | rev | sed 's/_trim.*//g')
        echo "$Timepoint"
        OutDir=alignment/$Organism/$Strain/$Timepoint
        ProgDir=/home/adamst/git_repos/tools/seq_tools/RNAseq
        qsub $ProgDir/tophat_alignment_unpaired.sh $Assembly $RNA $OutDir
    done
done
```

#Braker prediction

```bash
for Assembly in $(ls repeat_masked/*/*/filtered_contigs_repmask/*_contigs_unmasked.fa)
do
    Strain=$(echo $Assembly| rev | cut -d '/' -f3 | rev)
    Organism=$(echo $Assembly | rev | cut -d '/' -f4 | rev)
    echo "$Organism - $Strain"
    mkdir -p alignment/$Organism/$Strain/concatenated
    samtools merge -f alignment/$Organism/$Strain/concatenated/concatenated.bam \
    alignment/$Organism/$Strain/SRR1206032/accepted_hits.bam \
    alignment/$Organism/$Strain/SRR1206033/accepted_hits.bam
    OutDir=gene_pred/braker/$Organism/"$Strain"_braker
    AcceptedHits=alignment/$Organism/$Strain/concatenated/concatenated.bam
    GeneModelName="$Organism"_"$Strain"_braker
    rm -r /home/armita/prog/augustus-3.1/config/species/"$Organism"_"$Strain"_braker
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/braker1
    qsub $ProgDir/sub_braker_fungi.sh $Assembly $OutDir $AcceptedHits $GeneModelName
done
```

<!-- #Supplementing Braker gene models with CodingQuarry genes

Additional genes were added to Braker gene predictions, using CodingQuarry in pathogen mode to predict additional regions.

Firstly, aligned RNAseq data was assembled into transcripts using Cufflinks.

Note - cufflinks doesn't always predict direction of a transcript and therefore features can not be restricted by strand when they are intersected.

```bash
for Assembly in $(ls repeat_masked/*/*/filtered_contigs_repmask/*_contigs_unmasked.fa)
do
    Strain=$(echo $Assembly| rev | cut -d '/' -f3 | rev)
    Organism=$(echo $Assembly | rev | cut -d '/' -f4 | rev)
    echo "$Organism - $Strain"
    OutDir=gene_pred/cufflinks/$Organism/$Strain/concatenated
    mkdir -p $OutDir
    AcceptedHits=alignment/$Organism/$Strain/concatenated/concatenated.bam
    ProgDir=/home/adamst/git_repos/tools/seq_tools/RNAseq
    qsub $ProgDir/sub_cufflinks.sh $AcceptedHits $OutDir
done
```

Secondly, genes were predicted using CodingQuarry:

```bash
for Assembly in $(ls repeat_masked/*/*/*/*_contigs_softmasked.fa)
do
    Strain=$(echo $Assembly| rev | cut -d '/' -f3 | rev)
    Organism=$(echo $Assembly | rev | cut -d '/' -f4 | rev)
    echo "$Organism - $Strain"
    OutDir=gene_pred/codingquary/$Organism/$Strain
    CufflinksGTF=gene_pred/cufflinks/$Organism/$Strain/concatenated/transcripts.gtf
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/codingquary
    qsub $ProgDir/sub_CodingQuary.sh $Assembly $CufflinksGTF $OutDir
done
```

Then, additional transcripts were added to Braker1 gene models, when CodingQuarry genes were predicted in regions of the genome, not containing Braker1 gene models:


    for BrakerGff in $(ls gene_pred/braker/F.*/*_braker_pacbio/*/augustus.gff3 | grep -e 'Fus2'); do
        Strain=$(echo $BrakerGff| rev | cut -d '/' -f3 | rev | sed 's/_braker_new//g' | sed 's/_braker_pacbio//g')
        Organism=$(echo $BrakerGff | rev | cut -d '/' -f4 | rev)
        echo "$Organism - $Strain"
        # BrakerGff=gene_pred/braker/$Organism/$Strain/F.oxysporum_fsp_cepae_Fus2_braker/augustus_extracted.gff
        Assembly=$(ls repeat_masked/$Organism/$Strain/*/"$Strain"_contigs_softmasked.fa)
        CodingQuaryGff=gene_pred/codingquary/$Organism/$Strain/out/PredictedPass.gff3
        PGNGff=gene_pred/codingquary/$Organism/$Strain/out/PGN_predictedPass.gff3
        AddDir=gene_pred/codingquary/$Organism/$Strain/additional
        FinalDir=gene_pred/codingquary/$Organism/$Strain/final
        AddGenesList=$AddDir/additional_genes.txt
        AddGenesGff=$AddDir/additional_genes.gff
        FinalGff=$AddDir/combined_genes.gff
        mkdir -p $AddDir
        mkdir -p $FinalDir

        bedtools intersect -v -a $CodingQuaryGff -b $BrakerGff | grep 'gene'| cut -f2 -d'=' | cut -f1 -d';' > $AddGenesList
        bedtools intersect -v -a $PGNGff -b $BrakerGff | grep 'gene'| cut -f2 -d'=' | cut -f1 -d';' >> $AddGenesList
        ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/feature_annotation
        $ProgDir/gene_list_to_gff.pl $AddGenesList $CodingQuaryGff CodingQuarry_v2.0 ID CodingQuary > $AddGenesGff
        $ProgDir/gene_list_to_gff.pl $AddGenesList $PGNGff PGNCodingQuarry_v2.0 ID CodingQuary >> $AddGenesGff
        ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/codingquary
        # GffFile=gene_pred/codingquary/F.oxysporum_fsp_cepae/Fus2_edited_v2/additional/additional_genes.gff
        # GffFile=gene_pred/codingquary/F.oxysporum_fsp_cepae/Fus2_edited_v2/out/PredictedPass.gff3

        $ProgDir/add_CodingQuary_features.pl $AddGenesGff $Assembly > $FinalDir/final_genes_CodingQuary.gff3
        $ProgDir/gff2fasta.pl $Assembly $FinalDir/final_genes_CodingQuary.gff3 $FinalDir/final_genes_CodingQuary
        cp $BrakerGff $FinalDir/final_genes_Braker.gff3
        $ProgDir/gff2fasta.pl $Assembly $FinalDir/final_genes_Braker.gff3 $FinalDir/final_genes_Braker
        cat $FinalDir/final_genes_Braker.pep.fasta $FinalDir/final_genes_CodingQuary.pep.fasta | sed -r 's/\*/X/g' > $FinalDir/final_genes_combined.pep.fasta
        cat $FinalDir/final_genes_Braker.cdna.fasta $FinalDir/final_genes_CodingQuary.cdna.fasta > $FinalDir/final_genes_combined.cdna.fasta
        cat $FinalDir/final_genes_Braker.gene.fasta $FinalDir/final_genes_CodingQuary.gene.fasta > $FinalDir/final_genes_combined.gene.fasta
        cat $FinalDir/final_genes_Braker.upstream3000.fasta $FinalDir/final_genes_CodingQuary.upstream3000.fasta > $FinalDir/final_genes_combined.upstream3000.fasta

        GffBraker=$FinalDir/final_genes_CodingQuary.gff3
        GffQuary=$FinalDir/final_genes_Braker.gff3
        GffAppended=$FinalDir/final_genes_appended.gff3
        cat $GffBraker $GffQuary > $GffAppended

        # cat $BrakerGff $AddDir/additional_gene_parsed.gff3 | bedtools sort > $FinalGff
    done
The final number of genes per isolate was observed using:

for DirPath in $(ls -d gene_pred/codingquary/F.*/*/final | grep -w -e'Fus2'); do
echo $DirPath;
cat $DirPath/final_genes_Braker.pep.fasta | grep '>' | wc -l;
cat $DirPath/final_genes_CodingQuary.pep.fasta | grep '>' | wc -l;
cat $DirPath/final_genes_combined.pep.fasta | grep '>' | wc -l;
echo "";
done -->


#4) Extract gff and amino acid sequences

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for File in $(ls gene_pred/braker/*/"$Strain"_braker/*_braker/augustus.gff)
    do
        getAnnoFasta.pl $File
        OutDir=$(dirname $File)
        echo "##gff-version 3" > $OutDir/augustus_extracted.gff
        cat $File | grep -v '#' >> $OutDir/augustus_extracted.gff
    done
done
```

#Use atg.pl to predict all ORFs

This uses the atg.pl script to identify all ORFs in the genome. These can then be used to look for RxLRs and signal peptides.

Illumina sequenced data

```bash
ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
for Strain in A4 Bc1 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for Genome in $(ls assembly/spades/*/$Strain/filtered_contigs/*_500bp_renamed.fasta)
    do
        qsub $ProgDir/run_ORF_finder.sh $Genome
    done
done
```

PacBio sequenced data

```bash
Genome=assembly/merged_canu_spades/*/Bc16/filtered_contigs/*_renamed.fasta
qsub $ProgDir/run_ORF_finder.sh $Genome
```

The Gff files from the ORF finder are not in true Gff3 format. These were corrected using the following commands:

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for ORF_Gff in $(ls gene_pred/ORF_finder/P.*/*/*_ORF.gff | grep -v '_atg_')
    do
        Strain=$(echo $ORF_Gff | rev | cut -f2 -d '/' | rev)
        Organism=$(echo $ORF_Gff | rev | cut -f3 -d '/' | rev)
        ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
        ORF_Gff_mod=gene_pred/ORF_finder/$Organism/$Strain/"$Strain"_ORF_corrected.gff3
        $ProgDir/gff_corrector.pl $ORF_Gff > $ORF_Gff_mod
    done
done
```

The final number of genes per isolate was observed using:

Braker genes:

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov9 Nov71 Nov77 ONT3 SCRP245_v2
do
    for DirPath in $(ls -d gene_pred/braker/P.fragariae/"$Strain"_braker/P.fragariae*)
    do
        echo $DirPath
        cat $DirPath/augustus.aa | grep '>' | wc -l
        echo ""
    done
done
```

```
gene_pred/braker/P.fragariae/A4_braker/P.fragariae_A4_braker
38193

gene_pred/braker/P.fragariae/Bc1_braker/P.fragariae_Bc1_braker
36005

gene_pred/braker/P.fragariae/Bc16_braker/P.fragariae_Bc16_braker
39788

gene_pred/braker/P.fragariae/Bc23_braker/P.fragariae_Bc23_braker
36467

gene_pred/braker/P.fragariae/Nov27_braker/P.fragariae_Nov27_braker
35466

gene_pred/braker/P.fragariae/Nov5_braker/P.fragariae_Nov5_braker
37270

gene_pred/braker/P.fragariae/Nov9_braker/P.fragariae_Nov9_braker
37028

gene_pred/braker/P.fragariae/Nov71_braker/P.fragariae_Nov71_braker
37013

gene_pred/braker/P.fragariae/Nov77_braker/P.fragariae_Nov77_braker
37801

gene_pred/braker/P.fragariae/ONT3_braker/P.fragariae_ONT3_braker
41565

gene_pred/braker/P.fragariae/SCRP245_v2_braker/P.fragariae_SCRP245_v2_braker
41628
```

ORF_finder genes:

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov9 Nov71 Nov77 ONT3 SCRP245_v2
do
    for DirPath in $(ls -d gene_pred/ORF_finder/P.fragariae/$Strain)
    do
        echo $DirPath
        cat $DirPath/"$Strain".aa_cat.fa | grep '>' | wc -l
        echo ""
    done
done
```

```
gene_pred/ORF_finder/P.fragariae/A4
654541

gene_pred/ORF_finder/P.fragariae/Bc1
657485

gene_pred/ORF_finder/P.fragariae/Bc16
821332

gene_pred/ORF_finder/P.fragariae/Bc23
648214

gene_pred/ORF_finder/P.fragariae/Nov27
653883

gene_pred/ORF_finder/P.fragariae/Nov5
654169

gene_pred/ORF_finder/P.fragariae/Nov9
660342

gene_pred/ORF_finder/P.fragariae/Nov71
649628

gene_pred/ORF_finder/P.fragariae/Nov77
653363

gene_pred/ORF_finder/P.fragariae/ONT3
777535

gene_pred/ORF_finder/P.fragariae/SCRP245_v2
691456
```

#Functional annotation

A)Interproscan
Interproscan was used to give gene models functional annotations.

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/interproscan/
for Strain in A4 SCRP245_v2 Nov77; do
    Genes=gene_pred/braker/P.fragariae/$Strain/P.*/augustus.aa
    $ProgDir/sub_interproscan.sh $Genes
done
```

#Genomic analysis

#RxLR genes

A) From Braker1 gene models - signal peptide and RxLR motif

Required programs:

SigP
biopython

Proteins that were predicted to contain signal peptides were identified using the following commands:


```bash
for Strain in Bc1 Bc16 Nov9; do
    for Proteome in $(ls gene_pred/braker/*/$Strain/*/augustus.aa); do
        echo "$Proteome"
        SplitfileDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
        ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
        Organism=$(echo $Proteome | rev | cut -f4 -d '/' | rev)
        SplitDir=gene_pred/braker_split/$Organism/$Strain
        mkdir -p $SplitDir
        BaseName="$Organism""_$Strain"_braker_preds
        $SplitfileDir/splitfile_500.py --inp_fasta $Proteome --out_dir $SplitDir --out_base $BaseName
        for File in $(ls $SplitDir/*_braker_preds_*); do
            Jobs=$(qstat | grep 'pred_sigP' | wc -l)
            while [ $Jobs -ge 32 ]; do
                sleep 10
                printf "."
                Jobs=$(qstat | grep 'pred_sigP' | wc -l)
            done
            printf "\n"
            echo $File
            qsub $ProgDir/pred_sigP.sh $File
            # qsub $ProgDir/pred_sigP.sh $File signalp-4.1
        done
    done
done
```
This produces batch files. They need to be combined into a single file for each strain using the following commands:

```bash
for Strain in Bc1 Bc16 Nov9; do
    for SplitDir in $(ls -d gene_pred/braker_split/P.*/$Strain); do
        Organism=$(echo $SplitDir | rev | cut -d '/' -f2 | rev)
        InStringAA=''
        InStringNeg=''
        InStringTab=''
        InStringTxt=''
        for GRP in $(ls -l $SplitDir/*_braker_preds_*.fa | rev | cut -d '_' -f1 | rev | sort -n); do
            InStringAA="$InStringAA gene_pred/braker_sigP/$Organism/$Strain/split/"$Organism"_"$Strain"_braker_preds_$GRP""_sp.aa";
            InStringNeg="$InStringNeg gene_pred/braker_sigP/$Organism/$Strain/split/"$Organism"_"$Strain"_braker_preds_$GRP""_sp_neg.aa";
            InStringTab="$InStringTab gene_pred/braker_sigP/$Organism/$Strain/split/"$Organism"_"$Strain"_braker_preds_$GRP""_sp.tab";
            InStringTxt="$InStringTxt gene_pred/braker_sigP/$Organism/$Strain/split/"$Organism"_"$Strain"_braker_preds_$GRP""_sp.txt";
        done
        cat $InStringAA > gene_pred/braker_sigP/$Organism/$Strain/"$Strain"_braker_sp.aa
        cat $InStringNeg > gene_pred/braker_sigP/$Organism/$Strain/"$Strain"_braker_neg_sp.aa
        tail -n +2 -q $InStringTab > gene_pred/braker_sigP/$Organism/$Strain/"$Strain"_braker_sp.tab
        cat $InStringTxt > gene_pred/braker_sigP/$Organism/$Strain/"$Strain"_braker_sp.txt
    done
done
```
The RxLR_EER_regex_finder.py script was used to search for this regular expression R.LR.{,40}[ED][ED][KR] and annotate the EER domain where present. Done separate for each strain.

```bash
for Strain in A4 Bc23 Nov5 Nov77 ONT3 SCRP245_v2 Bc16 62471 Nov27 Nov71 Bc1 Nov9; do
    for Secretome in $(ls gene_pred/braker_sigP/*/$Strain/*braker_sp.aa); do
        ProgDir=/home/adamst/git_repos/tools/pathogen/RxLR_effectors;
        Organism=$(echo $Secretome | rev |  cut -d '/' -f3 | rev) ;
        OutDir=analysis/RxLR_effectors/RxLR_EER_regex_finder/"$Organism"/"$Strain";
        mkdir -p $OutDir;
        printf "\nstrain: $Strain\tspecies: $Organism\n";
        printf "the number of SigP gene is:\t";
        cat $Secretome | grep '>' | wc -l;
        printf "the number of SigP-RxLR genes are:\t";
        $ProgDir/RxLR_EER_regex_finder.py $Secretome > $OutDir/"$Strain"_braker_RxLR_regex.fa;
        cat $OutDir/"$Strain"_braker_RxLR_regex.fa | grep '>' | cut -f1 | tr -d '>' | sed -r 's/\.t.*//' > $OutDir/"$Strain"_braker_RxLR_regex.txt
        cat $OutDir/"$Strain"_braker_RxLR_regex.txt | wc -l
        printf "the number of SigP-RxLR-EER genes are:\t";
        cat $OutDir/"$Strain"_braker_RxLR_regex.fa | grep '>' | grep 'EER_motif_start' | cut -f1 | tr -d '>' | sed -r 's/\.t.*//' > $OutDir/"$Strain"_braker_RxLR_EER_regex.txt
        cat $OutDir/"$Strain"_braker_RxLR_EER_regex.txt | wc -l
        printf "\n"
        ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
        # $ProgDir/extract_from_fasta.py --fasta $OutDir/"$Strain"_pub_RxLR_regex.fa --headers $OutDir/"$Strain"_pub_RxLR_EER_regex.txt > $OutDir/"$Strain"_pub_RxLR_EER_regex.fa
        # GeneModels=$(ls assembly/external_group/P.*/$Strain/pep/*.gff*)
        # cat $GeneModels | grep -w -f $OutDir/"$Strain"_pub_RxLR_regex.txt > $OutDir/"$Strain"_pub_RxLR_regex.gff3
        # cat $GeneModels | grep -w -f $OutDir/"$Strain"_pub_RxLR_EER_regex.txt > $OutDir/"$Strain"_pub_RxLR_EER_regex.gff3
    done
done
```

```
strain: A4	species: P.fragariae
the number of SigP gene is:	2432
the number of SigP-RxLR genes are: 291
the number of SigP-RxLR-EER genes are: 170


strain: Bc23	species: P.fragariae
the number of SigP gene is: 2194
the number of SigP-RxLR genes are: 284
the number of SigP-RxLR-EER genes are: 166


strain: Nov5	species: P.fragariae
the number of SigP gene is:	2561
the number of SigP-RxLR genes are: 308
the number of SigP-RxLR-EER genes are: 180


strain: Nov77	species: P.fragariae
the number of SigP gene is:	2489
the number of SigP-RxLR genes are: 289
the number of SigP-RxLR-EER genes are: 165


strain: ONT3	species: P.fragariae
the number of SigP gene is: 3149
the number of SigP-RxLR genes are: 297
the number of SigP-RxLR-EER genes are: 174


strain: SCRP245_v2	species: P.fragariae
the number of SigP gene is: 2544
the number of SigP-RxLR genes are: 286
the number of SigP-RxLR-EER genes are: 156


strain: Bc16    species: P.fragariae
the number of SigP gene is: 2517
the number of SigP-RxLR genes are: 304
the number of SigP-RxLR-EER genes are: 173


strain: 62471   species: P.fragariae
the number of SigP gene is: 2134
the number of SigP-RxLR genes are: 201
the number of SigP-RxLR-EER genes are: 108


strain: Nov27   species: P.fragariae
the number of SigP gene is: 2450
the number of SigP-RxLR genes are: 297
the number of SigP-RxLR-EER genes are: 172


strain: Nov71   species: P.fragariae
the number of SigP gene is: 2525
the number of SigP-RxLR genes are: 324
the number of SigP-RxLR-EER genes are: 191


strain: Bc1     species: P.fragariae
the number of SigP gene is:     2570
the number of SigP-RxLR genes are:      336
the number of SigP-RxLR-EER genes are:  193


strain: Nov9    species: P.fragariae
the number of SigP gene is:     2531
the number of SigP-RxLR genes are:      313
the number of SigP-RxLR-EER genes are:  182
```

#B) From braker1 gene models - Hmm evidence for WY domains

Hmm models for the WY domain contained in many RxLRs were used to search gene models predicted with Braker1. These were run with the following commands:

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer
HmmModel=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer/WY_motif.hmm
for Strain in A4 Bc23 Nov5 Nov77 ONT3 SCRP245_v2 Bc16 62471 Nov27 Nov71 Bc1 Nov9; do
    for Proteome in $(ls gene_pred/braker/*/$Strain/*/augustus.aa); do
        Organism=$(echo $Proteome | rev | cut -f4 -d '/' | rev)
        OutDir=analysis/RxLR_effectors/hmmer_WY/$Organism/$Strain
        mkdir -p $OutDir
        HmmResults="$Strain"_pub_WY_hmmer.txt
        hmmsearch -T 0 $HmmModel $Proteome > $OutDir/$HmmResults
        echo "$Organism $Strain"
        cat $OutDir/$HmmResults | grep 'Initial search space'
        cat $OutDir/$HmmResults | grep 'number of targets reported over threshold'
        HmmFasta="$Strain"_pub_WY_hmmer.fa
        $ProgDir/hmmer2fasta.pl $OutDir/$HmmResults $Proteome > $OutDir/$HmmFasta
        Headers="$Strain"_pub_WY_hmmer_headers.txt
        cat $OutDir/$HmmFasta | grep '>' | cut -f1 | tr -d '>' | sed -r 's/\.t.*//' > $OutDir/$Headers
        # GeneModels=$(ls assembly/external_group/P.*/$Strain/pep/*.gff*)
        # cat $GeneModels | grep -w -f $OutDir/$Headers > $OutDir/"$Strain"_pub_WY_hmmer.gff3
    done
done
```

```
P.fragariae A4
Initial search space (Z):              37530  [actual number of targets]
Domain search space  (domZ):             174  [number of targets reported over threshold]
P.fragariae Bc23
Initial search space (Z):              29580  [actual number of targets]
Domain search space  (domZ):             161  [number of targets reported over threshold]
P.fragariae Nov5
Initial search space (Z):              36640  [actual number of targets]
Domain search space  (domZ):             174  [number of targets reported over threshold]
P.fragariae Nov77
Initial search space (Z):              36932  [actual number of targets]
Domain search space  (domZ):             177  [number of targets reported over threshold]
P.fragariae ONT3
Initial search space (Z):              40875  [actual number of targets]
Domain search space  (domZ):             190  [number of targets reported over threshold]
P.fragariae SCRP245_v2
Initial search space (Z):              36021  [actual number of targets]
Domain search space  (domZ):             172  [number of targets reported over threshold]
P.fragariae Bc16
Initial search space (Z):              38314  [actual number of targets]
Domain search space  (domZ):             178  [number of targets reported over threshold]
P.fragariae 62471
Initial search space (Z):              24212  [actual number of targets]
Domain search space  (domZ):             150  [number of targets reported over threshold]
P.fragariae Nov27
Initial search space (Z):              35993  [actual number of targets]
Domain search space  (domZ):             170  [number of targets reported over threshold]
P.fragariae Nov71
Initial search space (Z):              34902  [actual number of targets]
Domain search space  (domZ):             179  [number of targets reported over threshold]
P.fragariae Bc1
Initial search space (Z):              39733  [actual number of targets]
Domain search space  (domZ):             183  [number of targets reported over threshold]
P.fragariae Nov9
Initial search space (Z):              35898  [actual number of targets]
Domain search space  (domZ):             180  [number of targets reported over threshold]
```

#C) From Braker1 gene models - Hmm evidence of RxLR effectors

```bash
for Strain in A4 Bc23 Nov5 Nov77 ONT3 SCRP245_v2 Bc16 62471 Nov27 Nov71 Bc1 Nov9; do
    for Proteome in $(ls gene_pred/braker/*/$Strain/*/augustus.aa); do
        ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer
        HmmModel=/home/armita/git_repos/emr_repos/SI_Whisson_et_al_2007/cropped.hmm
        Organism=$(echo $Proteome | rev | cut -f4 -d '/' | rev)
        OutDir=analysis/RxLR_effectors/hmmer_RxLR/$Organism/$Strain
        mkdir -p $OutDir
        HmmResults="$Strain"_braker1_RxLR_hmmer.txt
        hmmsearch -T 0 $HmmModel $Proteome > $OutDir/$HmmResults
        echo "$Organism $Strain"
        cat $OutDir/$HmmResults | grep 'Initial search space'
        cat $OutDir/$HmmResults | grep 'number of targets reported over threshold'
        HmmFasta="$Strain"_Braker1_RxLR_hmmer.fa
        $ProgDir/hmmer2fasta.pl $OutDir/$HmmResults $Proteome > $OutDir/$HmmFasta
        Headers="$Strain"_pub_RxLR_hmmer_headers.txt
        cat $OutDir/$HmmFasta | grep '>' | cut -f1 | tr -d '>' > $OutDir/$Headers
        # ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/feature_annotation
        # Col2=cropped.hmm
        # GeneModels=$(ls assembly/external_group/P.*/$Strain/pep/*.gff*)
        # $ProgDir/gene_list_to_gff.pl $OutDir/$Headers $GeneModels $Col2 Name > $OutDir/"$Strain"_pub_RxLR_hmmer.gff3
        # cat $GeneModels | grep -w -f $OutDir/$Headers > $OutDir/"$Strain"_pub_RxLR_hmmer.gff3
    done
done
```

```
P.fragariae A4
Initial search space (Z):              37530  [actual number of targets]
Domain search space  (domZ):             186  [number of targets reported over threshold]
P.fragariae Bc23
Initial search space (Z):              29580  [actual number of targets]
Domain search space  (domZ):             171  [number of targets reported over threshold]
dP.fragariae Nov5
Initial search space (Z):              36640  [actual number of targets]
Domain search space  (domZ):             193  [number of targets reported over threshold]                                                                                                                                                                                                                                 P.fragariae Nov77
Initial search space (Z):              36932  [actual number of targets]
Domain search space  (domZ):             194  [number of targets reported over threshold]
P.fragariae ONT3
Initial search space (Z):              40875  [actual number of targets]
Domain search space  (domZ):             195  [number of targets reported over threshold]
P.fragariae SCRP245_v2
Initial search space (Z):              36021  [actual number of targets]
Domain search space  (domZ):             175  [number of targets reported over threshold]
P.fragariae Bc16
Initial search space (Z):              38314  [actual number of targets]
Domain search space  (domZ):             198  [number of targets reported over threshold]
P.fragariae 62471
Initial search space (Z):              24212  [actual number of targets]
Domain search space  (domZ):             112  [number of targets reported over threshold]
P.fragariae Nov27
Initial search space (Z):              35993  [actual number of targets]
Domain search space  (domZ):             187  [number of targets reported over threshold]
P.fragariae Nov71
Initial search space (Z):              34902  [actual number of targets]
Domain search space  (domZ):             205  [number of targets reported over threshold]
P.fragariae Bc1
Initial search space (Z):              39733  [actual number of targets]
Domain search space  (domZ):             206  [number of targets reported over threshold]
P.fragariae Nov9
Initial search space (Z):              35898  [actual number of targets]
Domain search space  (domZ):             195  [number of targets reported over threshold]
```

#D) From Braker1 gene models - Hmm evidence of CRN effectors

A hmm model relating to crinkler domains was used to identify putative crinklers in Augustus gene models. This was done with the following commands:

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer
HmmModel=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer/Phyt_annot_CRNs_D1.hmm
for Strain in A4 Bc23 Nov5 Nov77 ONT3 SCRP245_v2 Bc16 62471 Nov27 Nov71 Bc1 Nov9; do
    for Proteome in $(ls gene_pred/braker/*/$Strain/*/augustus.aa); do
        Organism=$(echo $Proteome | rev | cut -f4 -d '/' | rev)
        OutDir=analysis/CRN_effectors/hmmer_CRN/$Organism/$Strain
        mkdir -p $OutDir
        HmmResults="$Strain"_braker1_CRN_hmmer.txt
        hmmsearch -T 0 $HmmModel $Proteome > $OutDir/$HmmResults
        echo "$Organism $Strain"
        cat $OutDir/$HmmResults | grep 'Initial search space'
        cat $OutDir/$HmmResults | grep 'number of targets reported over threshold'
        HmmFasta="$Strain"_pub_CRN_hmmer_out.fa
        $ProgDir/hmmer2fasta.pl $OutDir/$HmmResults $Proteome > $OutDir/$HmmFasta
        # Headers="$Strain"_pub_RxLR_hmmer_headers.txt
        # cat $OutDir/$HmmFasta | grep '>' | cut -f1 | tr -d '>' | sed -r 's/\.t.*//' > $OutDir/$Headers
        # GeneModels=$(ls assembly/external_group/P.*/$Strain/pep/*.gff*)
        # cat $GeneModels | grep -w -f $OutDir/$Headers > $OutDir/"$Strain"_pub_CRN_hmmer.gff3
    done
done
```

```
P.fragariae A4
Initial search space (Z):              37530  [actual number of targets]
Domain search space  (domZ):             125  [number of targets reported over threshold]
P.fragariae Bc23
Initial search space (Z):              29580  [actual number of targets]
Domain search space  (domZ):             105  [number of targets reported over threshold]
P.fragariae Nov5
Initial search space (Z):              36640  [actual number of targets]
Domain search space  (domZ):             123  [number of targets reported over threshold]
P.fragariae Nov77
Initial search space (Z):              36932  [actual number of targets]
Domain search space  (domZ):             121  [number of targets reported over threshold]
P.fragariae ONT3
Initial search space (Z):              40875  [actual number of targets]
Domain search space  (domZ):             117  [number of targets reported over threshold]
P.fragariae SCRP245_v2
Initial search space (Z):              36021  [actual number of targets]
Domain search space  (domZ):             109  [number of targets reported over threshold]
P.fragariae Bc16
Initial search space (Z):              38314  [actual number of targets]
Domain search space  (domZ):             119  [number of targets reported over threshold]
P.fragariae 62471
Initial search space (Z):              24212  [actual number of targets]
Domain search space  (domZ):             171  [number of targets reported over threshold]
P.fragariae Nov27
Initial search space (Z):              35993  [actual number of targets]
Domain search space  (domZ):             115  [number of targets reported over threshold]
P.fragariae Nov71
Initial search space (Z):              34902  [actual number of targets]
Domain search space  (domZ):             127  [number of targets reported over threshold]
P.fragariae Bc1
Initial search space (Z):              39733  [actual number of targets]
Domain search space  (domZ):             123  [number of targets reported over threshold]
P.fragariae Nov9
Initial search space (Z):              35898  [actual number of targets]
Domain search space  (domZ):             130  [number of targets reported over threshold]
```

#E) From ORF gene models - Signal peptide & RxLR motif

Required programs:

SigP
biopython

Proteins that were predicted to contain signal peptides were identified using the following commands:

```bash
for Strain in A4 SCRP245_v2 Nov77; do
    for Proteome in $(ls gene_pred/ORF_finder_spades/*/$Strain/*.aa_cat.fa); do
        echo "$Proteome"
        SplitfileDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
        ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
        Organism=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
        SplitDir=gene_pred/ORF_split_spades/$Organism/$Strain
        mkdir -p $SplitDir
        BaseName="$Organism""_$Strain"_ORF_preds
        $SplitfileDir/splitfile_500.py --inp_fasta $Proteome --out_dir $SplitDir --out_base $BaseName
        for File in $(ls $SplitDir/*_ORF_preds_*); do
            Jobs=$(qstat | grep 'pred_sigP' | grep 'qw' | wc -l)
            while [ $Jobs -gt 1 ]; do
                sleep 10
                printf "."
                Jobs=$(qstat | grep 'pred_sigP' | grep 'qw' | wc -l)
            done
            printf "\n"
            echo $File
            qsub $ProgDir/pred_sigP.sh $File
            # qsub $ProgDir/pred_sigP.sh $File signalp-4.1
        done
    done
done
```
The batch files of predicted secreted proteins needed to be combined into a single file for each strain. This was done with the following commands:
```bash
for Strain in A4 SCRP245_v2 Nov77; do
    for SplitDir in $(ls -d gene_pred/ORF_split_spades/P.*/$Strain); do
        Organism=$(echo $SplitDir | rev | cut -d '/' -f2 | rev)
        InStringAA=''
        InStringNeg=''
        InStringTab=''
        InStringTxt=''
        for GRP in $(ls -l $SplitDir/*_ORF_preds_*.fa | rev | cut -d '_' -f1 | rev | sort -n); do
            InStringAA="$InStringAA gene_pred/ORF_spades_sigP/$Organism/$Strain/split/"$Organism"_"$Strain"_ORF_preds_$GRP""_sp.aa";
            InStringNeg="$InStringNeg gene_pred/ORF_spades_sigP/$Organism/$Strain/split/"$Organism"_"$Strain"_ORF_preds_$GRP""_sp_neg.aa";
            InStringTab="$InStringTab gene_pred/ORF_spades_sigP/$Organism/$Strain/split/"$Organism"_"$Strain"_ORF_preds_$GRP""_sp.tab";
            InStringTxt="$InStringTxt gene_pred/ORF_spades_sigP/$Organism/$Strain/split/"$Organism"_"$Strain"_ORF_preds_$GRP""_sp.txt";
        done
        cat $InStringAA > gene_pred/ORF_spades_sigP/$Organism/$Strain/"$Strain"_ORF_sp.aa
        cat $InStringNeg > gene_pred/ORF_spades_sigP/$Organism/$Strain/"$Strain"_ORF_neg_sp.aa
        tail -n +2 -q $InStringTab > gene_pred/ORF_spades_sigP/$Organism/$Strain/"$Strain"_ORF_sp.tab
        cat $InStringTxt > gene_pred/ORF_spades_sigP/$Organism/$Strain/"$Strain"_ORF_sp.txt
    done
done
```

Names of ORFs containing signal peptides were extracted from fasta files. This included information on the position and hmm score of RxLRs.
```bash
for Strain in A4 SCRP245_v2 Nov77; do
    for FastaFile in $(ls gene_pred/ORF_spades_sigP/*/$Strain/*_ORF_sp.aa); do
        Organism=$(echo $FastaFile | rev | cut -d '/' -f3 | rev)
        echo "$Strain"
        SigP_headers=gene_pred/ORF_spades_sigP/$Organism/$Strain/"$Strain"_ORF_sp_names.txt
        cat $FastaFile | grep '>' | sed -r 's/>//g' | sed -r 's/\s+/\t/g'| sed 's/=\t/=/g' | sed 's/--//g' > $SigP_headers
    done
done
```

Due to the nature of predicting ORFs, some features overlapped with one another. A single ORF was selected from each set of overlapped ORFs. This was selected on the basis of its SignalP Hmm score. Biopython was used to identify overlaps and identify the ORF with the best SignalP score.

```bash
for Strain in A4 Nov77 SCRP245_v2; do
    for SigP_fasta in $(ls gene_pred/ORF_spades_sigP/P.*/$Strain/*_ORF_sp.aa); do
        Organism=$(echo $SigP_fasta | rev | cut -d '/' -f3 | rev)
        echo "$Strain"
        ORF_Gff=gene_pred/ORF_finder_spades/$Organism/$Strain/"$Strain"_ORF_corrected.gff3
        SigP_fasta=gene_pred/ORF_spades_sigP/$Organism/$Strain/"$Strain"_ORF_sp.aa
        SigP_headers=gene_pred/ORF_spades_sigP/$Organism/$Strain/"$Strain"_ORF_sp_names.txt
        SigP_Gff=gene_pred/ORF_spades_sigP/$Organism/$Strain/"$Strain"_ORF_sp_unmerged.gff
        SigP_Merged_Gff=gene_pred/ORF_spades_sigP/$Organism/$Strain/"$Strain"_ORF_sp_merged.gff
        SigP_Merged_txt=gene_pred/ORF_spades_sigP/$Organism/$Strain/"$Strain"_ORF_sp_merged.txt
        SigP_Merged_AA=gene_pred/ORF_spades_sigP/$Organism/$Strain/"$Strain"_ORF_sp_merged.aa
        ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
        $ProgDir/extract_gff_for_sigP_hits.pl $SigP_headers $ORF_Gff SigP Name > $SigP_Gff
        ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/merge_gff
        $ProgDir/make_gff_database.py --inp $SigP_Gff --db sigP_ORF.db
        ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
        $ProgDir/merge_sigP_ORFs.py --inp sigP_ORF.db --id sigP_ORF --out sigP_ORF_merged.db --gff > $SigP_Merged_Gff
        cat $SigP_Merged_Gff | grep 'transcript' | rev | cut -f1 -d'=' | rev > $SigP_Merged_txt
        $ProgDir/extract_from_fasta.py --fasta $SigP_fasta --headers $SigP_Merged_txt > $SigP_Merged_AA
    done
done
```

The regular expression R.LR.{,40}[ED][ED][KR] has previously been used to identify RxLR effectors. The addition of an EER motif is significant as it has been shown as required for host uptake of the protein.

The RxLR_EER_regex_finder.py script was used to search for this regular expression and annotate the EER domain where present.

```bash
for Strain in A4 Nov77 SCRP245_v2; do
    for Secretome in $(ls gene_pred/ORF_spades_sigP/P.*/$Strain/*_ORF_sp_merged.aa); do
        ProgDir=/home/adamst/git_repos/tools/pathogen/RxLR_effectors
        Organism=$(echo $Secretome | rev |  cut -d '/' -f3 | rev) ;
        OutDir=analysis/RxLR_effectors/RxLR_EER_regex_finder/"$Organism"/"$Strain";
        SigP_Merged_Gff=gene_pred/ORF_spades_sigP/$Organism/$Strain/"$Strain"_ORF_sp_merged.gff
        mkdir -p $OutDir;
        printf "\nstrain: $Strain\tspecies: $Organism\n";
        printf "the number of SigP gene is:\t";
        cat $Secretome | grep '>' | wc -l;
        printf "the number of SigP-RxLR genes are:\t";
        $ProgDir/RxLR_EER_regex_finder.py $Secretome > $OutDir/"$Strain"_ORF_RxLR_EER_regex.fa;
        cat $OutDir/"$Strain"_ORF_RxLR_EER_regex.fa | grep '>' | cut -f1 | tr -d '>' | sed -r 's/\.t.*//' | tr -d ' ' > $OutDir/"$Strain"_ORF_RxLR_regex.txt
        cat $OutDir/"$Strain"_ORF_RxLR_regex.txt | wc -l
        printf "the number of SigP-RxLR-EER genes are:\t";
        cat $OutDir/"$Strain"_ORF_RxLR_EER_regex.fa | grep '>' | grep 'EER_motif_start' | cut -f1 | tr -d '>' | sed -r 's/\.t.*//' | tr -d ' '> $OutDir/"$Strain"_ORF_RxLR_EER_regex.txt
        cat $OutDir/"$Strain"_ORF_RxLR_EER_regex.txt | wc -l
        printf "\n"
        ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
        $ProgDir/gene_list_to_gff.pl $OutDir/"$Strain"_ORF_RxLR_regex.txt $SigP_Merged_Gff RxLR_EER_regex_finder.py Name Augustus > $OutDir/"$Strain"_ORF_RxLR_regex.gff
        ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
        $ProgDir/gene_list_to_gff.pl $OutDir/"$Strain"_ORF_RxLR_EER_regex.txt $SigP_Merged_Gff RxLR_EER_regex_finder.py Name Augustus > $OutDir/"$Strain"_ORF_RxLR_EER_regex.gff
    done
done
```

```
strain: A4	species: P.fragariae
the number of SigP gene is:	22261
the number of SigP-RxLR genes are:	1532
the number of SigP-RxLR-EER genes are:	244


strain: Bc23	species: P.fragariae
the number of SigP gene is:	19663
the number of SigP-RxLR genes are:	1370
the number of SigP-RxLR-EER genes are:	222


strain: Nov5	species: P.fragariae
the number of SigP gene is:	22147
the number of SigP-RxLR genes are:	1533
the number of SigP-RxLR-EER genes are:	244


strain: Nov77	species: P.fragariae
the number of SigP gene is:	22122
the number of SigP-RxLR genes are:	1502
the number of SigP-RxLR-EER genes are:	231


strain: ONT3	species: P.fragariae
the number of SigP gene is:	25346
the number of SigP-RxLR genes are:	1637
the number of SigP-RxLR-EER genes are:	258


strain: SCRP245_v2	species: P.fragariae
the number of SigP gene is:	21033
the number of SigP-RxLR genes are:	1396
the number of SigP-RxLR-EER genes are:	221


strain: Bc16	species: P.fragariae
the number of SigP gene is:	23160
the number of SigP-RxLR genes are:	1602
the number of SigP-RxLR-EER genes are:	243


strain: 62471	species: P.fragariae
the number of SigP gene is:	15873
the number of SigP-RxLR genes are:	997
the number of SigP-RxLR-EER genes are:	177


strain: Nov27	species: P.fragariae
the number of SigP gene is:	22404
the number of SigP-RxLR genes are:	1536
the number of SigP-RxLR-EER genes are:	246


strain: Nov71	species: P.fragariae
the number of SigP gene is:	22615
the number of SigP-RxLR genes are:	1539
the number of SigP-RxLR-EER genes are:	242


strain: Bc1	species: P.fragariae
the number of SigP gene is:	23184
the number of SigP-RxLR genes are:	1585
the number of SigP-RxLR-EER genes are:	245


strain: Nov9	species: P.fragariae
the number of SigP gene is:	23374
the number of SigP-RxLR genes are:	1580
the number of SigP-RxLR-EER genes are:	242
```

#F) From ORF gene models - Hmm evidence of WY domains Hmm models for the WY domain contained in many RxLRs were used to search ORFs predicted with atg.pl. These were run with the following commands:

```bash
for Strain in A4 Nov77 SCRP245_v2; do
    for Secretome in $(ls gene_pred/ORF_spades_sigP/P.*/$Strain/*_ORF_sp_merged.aa); do
        ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer
        HmmModel=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer/WY_motif.hmm
        Organism=$(echo $Secretome | rev | cut -f3 -d '/' | rev)
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
        SigP_Merged_Gff=gene_pred/ORF_sigP/$Organism/$Strain/"$Strain"_ORF_sp_merged.gff
        ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/feature_annotation
        $ProgDir/gene_list_to_gff.pl $OutDir/$Headers $SigP_Merged_Gff $HmmModel Name Augustus > $OutDir/"$Strain"_ORF_WY_hmmer.gff
    done
done
```

```
P.fragariae A4
Initial search space (Z):              22261  [actual number of targets]
Domain search space  (domZ):             112  [number of targets reported over threshold]
P.fragariae Bc23
Initial search space (Z):              19663  [actual number of targets]
Domain search space  (domZ):             103  [number of targets reported over threshold]
P.fragariae Nov5
Initial search space (Z):              22147  [actual number of targets]
Domain search space  (domZ):             113  [number of targets reported over threshold]
P.fragariae Nov77
Initial search space (Z):              22122  [actual number of targets]
Domain search space  (domZ):              99  [number of targets reported over threshold]
P.fragariae ONT3
Initial search space (Z):              25346  [actual number of targets]
Domain search space  (domZ):             119  [number of targets reported over threshold]
P.fragariae SCRP245_v2
Initial search space (Z):              21033  [actual number of targets]
Domain search space  (domZ):             102  [number of targets reported over threshold]
P.fragariae Bc16
Initial search space (Z):              23160  [actual number of targets]
Domain search space  (domZ):             114  [number of targets reported over threshold]
P.fragariae 62471
Initial search space (Z):              15873  [actual number of targets]
Domain search space  (domZ):             105  [number of targets reported over threshold]
P.fragariae Nov27
Initial search space (Z):              22404  [actual number of targets]
Domain search space  (domZ):             113  [number of targets reported over threshold]
P.fragariae Nov71
Initial search space (Z):              22615  [actual number of targets]
Domain search space  (domZ):             115  [number of targets reported over threshold]
P.fragariae Bc1
Initial search space (Z):              23184  [actual number of targets]
Domain search space  (domZ):             113  [number of targets reported over threshold]
P.fragariae Nov9
Initial search space (Z):              23374  [actual number of targets]
Domain search space  (domZ):             114  [number of targets reported over threshold]
```

#G) From ORF gene models - Hmm evidence of RxLR effectors

```bash
for Strain in A4 Nov77 SCRP245_v2; do
    for Secretome in $(ls gene_pred/ORF_spades_sigP/P.*/$Strain/*_ORF_sp_merged.aa); do
        ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer
        HmmModel=/home/armita/git_repos/emr_repos/SI_Whisson_et_al_2007/cropped.hmm
        Organism=$(echo $Secretome | rev | cut -f3 -d '/' | rev)
        OutDir=analysis/RxLR_effectors/hmmer_RxLR/$Organism/$Strain
        mkdir -p $OutDir
        HmmResults="$Strain"_ORF_RxLR_hmmer.txt
        hmmsearch -T 0 $HmmModel $Secretome > $OutDir/$HmmResults
        echo "$Organism $Strain"
        cat $OutDir/$HmmResults | grep 'Initial search space'
        cat $OutDir/$HmmResults | grep 'number of targets reported over threshold'
        HmmFasta="$Strain"_ORF_RxLR_hmmer.fa
        $ProgDir/hmmer2fasta.pl $OutDir/$HmmResults $Secretome > $OutDir/$HmmFasta
        Headers="$Strain"_ORF_RxLR_hmmer_headers.txt
        cat $OutDir/$HmmFasta | grep '>' | cut -f1 | tr -d '>' | sed -r 's/\.t.*//' | tr -d ' ' > $OutDir/$Headers
        SigP_Merged_Gff=gene_pred/ORF_sigP/$Organism/$Strain/"$Strain"_ORF_sp_merged.gff
        ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/feature_annotation
        $ProgDir/gene_list_to_gff.pl $OutDir/$Headers $SigP_Merged_Gff $HmmModel Name Augustus > $OutDir/"$Strain"_ORF_RxLR_hmmer.gff3
    done
done
```

```
P.fragariae A4
Initial search space (Z):              22261  [actual number of targets]
Domain search space  (domZ):             202  [number of targets reported over threshold]
P.fragariae Bc23
Initial search space (Z):              19663  [actual number of targets]
Domain search space  (domZ):             183  [number of targets reported over threshold]
P.fragariae Nov5
Initial search space (Z):              22147  [actual number of targets]
Domain search space  (domZ):             200  [number of targets reported over threshold]
P.fragariae Nov77
Initial search space (Z):              22122  [actual number of targets]
Domain search space  (domZ):             193  [number of targets reported over threshold]
P.fragariae ONT3
Initial search space (Z):              25346  [actual number of targets]
Domain search space  (domZ):             211  [number of targets reported over threshold]
P.fragariae SCRP245_v2
Initial search space (Z):              21033  [actual number of targets]
Domain search space  (domZ):             184  [number of targets reported over threshold]
P.fragariae Bc16
Initial search space (Z):              23160  [actual number of targets]
Domain search space  (domZ):             200  [number of targets reported over threshold]
P.fragariae 62471
Initial search space (Z):              15873  [actual number of targets]
Domain search space  (domZ):             140  [number of targets reported over threshold]
P.fragariae Nov27
Initial search space (Z):              22404  [actual number of targets]
Domain search space  (domZ):             202  [number of targets reported over threshold]
P.fragariae Nov71
Initial search space (Z):              22615  [actual number of targets]
Domain search space  (domZ):             201  [number of targets reported over threshold]
P.fragariae Bc1
Initial search space (Z):              23184  [actual number of targets]
Domain search space  (domZ):             201  [number of targets reported over threshold]
P.fragariae Nov9
Initial search space (Z):              23374  [actual number of targets]
Domain search space  (domZ):             199  [number of targets reported over threshold]
```

#H) From ORF gene models - Hmm evidence of CRN effectors

A hmm model relating to crinkler domains was used to identify putative crinklers in ORF gene models. This was done with the following commands:

```bash
for Strain in A4 Nov77 SCRP245_v2; do
    for Proteome in $(ls gene_pred/ORF_finder_spades/*/$Strain/*.aa_cat.fa); do
        ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer
        HmmModel=/home/armita/git_repos/emr_repos/scripts/phytophthora/pathogen/hmmer/Phyt_annot_CRNs_D1.hmm
        Organism=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
        OutDir=analysis/CRN_effectors/hmmer_CRN/$Organism/$Strain
        mkdir -p $OutDir
        HmmResults="$Strain"_ORF_CRN_unmerged_hmmer.txt
        hmmsearch -T 0 $HmmModel $Proteome > $OutDir/$HmmResults
        echo "$Organism $Strain"
        cat $OutDir/$HmmResults | grep 'Initial search space'
        cat $OutDir/$HmmResults | grep 'number of targets reported over threshold'
        HmmFasta="$Strain"_ORF_CRN_hmmer_unmerged_out.fa
        $ProgDir/hmmer2fasta.pl $OutDir/$HmmResults $Proteome > $OutDir/$HmmFasta
        Headers="$Strain"_CRN_hmmer_unmerged_headers.txt
        cat $OutDir/$HmmFasta | grep '>' | tr -d '>' | sed -r 's/\s+/\t/g'| sed 's/=\t/=/g' | tr -d '-' | sed 's/hmm_score/HMM_score/g' > $OutDir/$Headers
        cat $OutDir/$Headers | sed 's/:/_a_/g' | sed 's/supercont1./supercont1_b_/g' | sed 's/Supercontig_2./Supercontig_c_/g' > tmp.txt
        ORF_Gff=$(ls gene_pred/ORF_finder/$Organism/$Strain/*_ORF_corrected.gff3)
        cat $ORF_Gff | sed 's/:/_a_/g' | sed 's/supercont1./supercont1_b_/g' | sed 's/Supercontig_2./Supercontig_c_/g' > tmp.gff
        CRN_unmerged_Gff=$OutDir/"$Strain"_CRN_unmerged_hmmer.gff3
        ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
        $ProgDir/extract_gff_for_sigP_hits.pl tmp.txt tmp.gff CRN_HMM Name > $CRN_unmerged_Gff
        DbDir=analysis/databases/$Organism/$Strain
        mkdir -p $DbDir
        ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/merge_gff
        $ProgDir/make_gff_database.py --inp $CRN_unmerged_Gff --db $DbDir/CRN_ORF.db
        CRN_Merged_Gff=$OutDir/"$Strain"_CRN_merged_hmmer.gff3
        ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
        $ProgDir/merge_sigP_ORFs.py --inp $DbDir/CRN_ORF.db --id $HmmModel --out $DbDir/CRN_ORF_merged.db --gff > $CRN_Merged_Gff
        sed -i 's/_a_/:/g' $CRN_Merged_Gff
        sed -i 's/supercont1_b_/supercont1./g' $CRN_Merged_Gff
        sed -i 's/Supercontig_c_/Supercontig_2./g' $CRN_Merged_Gff
        echo "Number of CRN ORFs after merging:"
        cat $CRN_Merged_Gff | grep 'gene' | wc -l
        rm tmp.txt
        rm tmp.gff
    done
done
```

```
P.fragariae A4
Initial search space (Z):             667992  [actual number of targets]
Domain search space  (domZ):             273  [number of targets reported over threshold]
Number of CRN ORFs after merging:        151
P.fragariae Bc23
Initial search space (Z):             576779  [actual number of targets]
Domain search space  (domZ):             239  [number of targets reported over threshold]
Number of CRN ORFs after merging:        126
P.fragariae Nov5
Initial search space (Z):             659155  [actual number of targets]
Domain search space  (domZ):             269  [number of targets reported over threshold]
Number of CRN ORFs after merging:        142
P.fragariae Nov77
Initial search space (Z):             657610  [actual number of targets]
Domain search space  (domZ):             249  [number of targets reported over threshold]
Number of CRN ORFs after merging:        136
P.fragariae ONT3
Initial search space (Z):             789618  [actual number of targets]
Domain search space  (domZ):             262  [number of targets reported over threshold]
Number of CRN ORFs after merging:        140
P.fragariae SCRP245_v2
Initial search space (Z):             627904  [actual number of targets]
Domain search space  (domZ):             252  [number of targets reported over threshold]
Number of CRN ORFs after merging:        160
P.fragariae Bc16
Initial search space (Z):             696773  [actual number of targets]
Domain search space  (domZ):             273  [number of targets reported over threshold]
Number of CRN ORFs after merging:        146
P.fragariae 62471
Initial search space (Z):             500487  [actual number of targets]
Domain search space  (domZ):             298  [number of targets reported over threshold]
Number of CRN ORFs after merging:        178
P.fragariae Nov27
Initial search space (Z):             670486  [actual number of targets]
Domain search space  (domZ):             279  [number of targets reported over threshold]
Number of CRN ORFs after merging:        150
P.fragariae Nov71
Initial search space (Z):             671887  [actual number of targets]
Domain search space  (domZ):             282  [number of targets reported over threshold]
Number of CRN ORFs after merging:        158
P.fragariae Bc1
Initial search space (Z):             704136  [actual number of targets]
Domain search space  (domZ):             270  [number of targets reported over threshold]
Number of CRN ORFs after merging:        143
P.fragariae Nov9
Initial search space (Z):             705534  [actual number of targets]
Domain search space  (domZ):             274  [number of targets reported over threshold]
Number of CRN ORFs after merging:        145
```

#Downstream analysis has raised potential issues with predicted genes.

These commands were used to visualise aligned reads against the genomes on my local machine

```bash
for Strain in A4 Bc23 Nov5 Nov77 ONT3 SCRP245_v2 Bc16 Nov27 Nov71 Bc1 Nov9
do
    InBam=alignment/P.fragariae/$Strain/accepted_hits.bam
    ViewBam=alignment/P.fragariae/$Strain/accepted_hits_view.bam
    SortBam=alignment/P.fragariae/$Strain/accepted_hits_sort.bam
    samtools view -b $InBam > $ViewBam
    samtools sort $ViewBam $SortBam
    samtools index $SortBam.bam
done
```
