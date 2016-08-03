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

The final number of genes per isolate was observed using:

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov9 Nov71 Nov77 ONT3 SCRP245_v2
do
    for DirPath in $(ls -d gene_pred/braker/*/"$Strain"_braker/P.fragariae_*_braker)
    do
        echo $DirPath
        cat $DirPath/augustus.aa | grep '>' | wc -l
        echo ""
    done
done
```

```
Braker - A4
38193

Braker - Bc1
36005

Braker - Bc16
39788

Braker - Bc23
36467

Braker - Nov27
35466

Braker - Nov5
37270

Braker - Nov9
37028

Braker - Nov71
37013

Braker - Nov77
37801

Braker - ONT3
41565

Braker - SCRP245_v2
41628
```

#Gene prediction 2 - atg.pl prediction of ORFs

Open reading frame predictions were made using the atg.pl script as part of the path_pipe.sh pipeline. This pipeline also identifies open reading frames containing Signal peptide sequences and RxLRs. This pipeline was run with the following commands:

```bash
ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
for Genome in $(ls repeat_masked/P.*/*/filtered_contigs_repmask/*_contigs_unmasked.fa)
do
    echo "$Genome"
    qsub $ProgDir/run_ORF_finder.sh $Genome
done
```

The Gff files from the the ORF finder are not in true Gff3 format. These were corrected using the following commands:

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
for OrfGff in $(ls gene_pred/ORF_finder/P.*/*/*_ORF.gff | grep -v 'atg')
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
654541

ORF_finder - Bc1
657485

ORF_finder - Bc16
821804

ORF_finder - Bc23
648214

ORF_finder - Nov27
653883

ORF_finder - Nov5
654169

ORF_finder - Nov9
660342

ORF_finder - Nov71
649628

ORF_finder - Nov77
653363

ORF_finder - ONT3
777535

ORF_finder - SCRP245_v2
691456
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

##A) From Augustus gene models - Signal peptide & RxLR motif

Required programs:

SigP
biopython

####A.1) Signal peptide prediction using SignalP 2.0

Proteins that were predicted to contain signal peptides were identified using the following commands:

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for Proteome in $(ls gene_pred/braker/*/"$Strain"_braker/*/augustus.aa)
    do
        SplitfileDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
        ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
        Organism=P.fragariae
        SplitDir=gene_pred/braker_split/$Organism/$Strain
        mkdir -p $SplitDir
        BaseName="$Organism""_$Strain"_braker
        $SplitfileDir/splitfile_500.py --inp_fasta $Proteome --out_dir $SplitDir --out_base $BaseName
        for File in $(ls $SplitDir/*_braker_*)
        do
            Jobs=$(qstat | grep 'pred_sigP' | grep -w 'qw'| wc -l)
            while [ $Jobs -gt 4 ]
            do
                sleep 1
                printf "."
                Jobs=$(qstat | grep 'pred_sigP' | grep -w 'qw'| wc -l)
            done
            printf "\n"
            echo $File
            qsub $ProgDir/pred_sigP.sh $File
            qsub $ProgDir/pred_sigP.sh $File signalp-4.1
        done
    done
done
```

The batch files of predicted secreted proteins needed to be combined into a single file for each strain. This was done with the following commands:

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for SplitDir in $(ls -d gene_pred/braker_split/P.*/$Strain)
    do
        Organism=P.fragariae
        echo "$Organism - $Strain"
        InStringAA=''
        InStringNeg=''
        InStringTab=''
        InStringTxt=''
        for SigpDir in $(ls -d gene_pred/braker_sig* | cut -f2 -d'/')
        do
            for GRP in $(ls -l $SplitDir/*_braker_*.fa | rev | cut -d '_' -f1 | rev | sort -n)
            do  
                InStringAA="$InStringAA gene_pred/$SigpDir/$Organism/$Strain/split/"$Organism"_"$Strain"_braker_$GRP""_sp.aa"
                InStringNeg="$InStringNeg gene_pred/$SigpDir/$Organism/$Strain/split/"$Organism"_"$Strain"_braker_$GRP""_sp_neg.aa"
                InStringTab="$InStringTab gene_pred/$SigpDir/$Organism/$Strain/split/"$Organism"_"$Strain"_braker_$GRP""_sp.tab"
                InStringTxt="$InStringTxt gene_pred/$SigpDir/$Organism/$Strain/split/"$Organism"_"$Strain"_braker_$GRP""_sp.txt"
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
    for Proteome in $(ls gene_pred/braker/*/"$Strain"_braker/*/augustus.aa)
    do
        Organism=P.fragariae
        echo "$Organism - $Strain"
        OutDir=analysis/phobius/$Organism/$Strain
        mkdir -p $OutDir
        phobius.pl $Proteome > $OutDir/"$Strain"_phobius.txt
        ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
        $ProgDir/phobius_parser.py --inp_fasta $Proteome --phobius_txt $OutDir/"$Strain"_phobius.txt --out_fasta $OutDir/"$Strain"_phobius.fa
    done
done
```

Secreted proteins from different sources were combined into a single file:

```bash
for Strain in A4 Bc16 Bc1 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for Proteome in $(ls gene_pred/braker/*/"$Strain"_braker/*/augustus.aa)
    do
        Organism=$(echo $Proteome | rev | cut -f4 -d '/' | rev)
        echo "$Organism - $Strain"
        OutDir=gene_pred/combined_sigP/$Organism/$Strain
        mkdir -p $OutDir
        echo "The following number of sequences were predicted as secreted:"
        cat gene_pred/braker_sig*/$Organism/$Strain/*_aug_sp.aa analysis/phobius/$Organism/$Strain/"$Strain"_phobius.fa > $OutDir/"$Strain"_all_secreted.fa
        cat $OutDir/"$Strain"_all_secreted.fa | grep '>' | wc -l
        echo "This represented the following number of unique genes:"
        cat gene_pred/braker_sig*/$Organism/$Strain/*_aug_sp.aa analysis/phobius/$Organism/$Strain/"$Strain"_phobius.fa | grep '>' | cut -f1 | tr -d ' >' | sort -g | uniq > $OutDir/"$Strain"_secreted.txt
        ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
        $ProgDir/extract_from_fasta.py --fasta $Proteome --headers $OutDir/"$Strain"_secreted.txt > $OutDir/"$Strain"_secreted.fa
        cat $OutDir/"$Strain"_secreted.fa | grep '>' | wc -l
    done
done
```

```
P.fragariae - A4
The following number of sequences were predicted as secreted:
10668
This represented the following number of unique genes:
3850
P.fragariae - Bc16
The following number of sequences were predicted as secreted:
11984
This represented the following number of unique genes:
4207
P.fragariae - Bc1
The following number of sequences were predicted as secreted:
10432
This represented the following number of unique genes:
3700
P.fragariae - Bc23
The following number of sequences were predicted as secreted:
10399
This represented the following number of unique genes:
3706
P.fragariae - Nov27
The following number of sequences were predicted as secreted:
10414
This represented the following number of unique genes:
3714
P.fragariae - Nov5
The following number of sequences were predicted as secreted:
10151
This represented the following number of unique genes:
3689
P.fragariae - Nov71
The following number of sequences were predicted as secreted:
10767
This represented the following number of unique genes:
3850
P.fragariae - Nov77
The following number of sequences were predicted as secreted:
10436
This represented the following number of unique genes:
3754
P.fragariae - Nov9
The following number of sequences were predicted as secreted:
10523
This represented the following number of unique genes:
3772
P.fragariae - ONT3
The following number of sequences were predicted as secreted:
13273
This represented the following number of unique genes:
4736
P.fragariae - SCRP245_v2
The following number of sequences were predicted as secreted:
11414
This represented the following number of unique genes:
4158
```

The regular expression R.LR.{,40}[ED][ED][KR] has previously been used to identify RxLR effectors. The addition of an EER motif is significant as it has been shown as required for host uptake of the protein.

The RxLR_EER_regex_finder.py script was used to search for this regular expression and annotate the EER domain where present.

```bash
for Secretome in $(ls gene_pred/combined_sigP/*/*/*_all_secreted.fa)
do
    Strain=$(echo $Secretome | rev | cut -d '/' -f2 | rev)
    Organism=$(echo $Secretome | rev |  cut -d '/' -f3 | rev)
    Proteome=$(ls gene_pred/braker/$Organism/"$Strain"_braker/*/augustus.aa)
    Gff=$(ls gene_pred/braker/$Organism/"$Strain"_braker/*/augustus_extracted.gff)
    OutDir=analysis/RxLR_effectors/RxLR_EER_regex_finder/"$Organism"/"$Strain"
    mkdir -p $OutDir
    printf "\nstrain: $Strain\tspecies: $Organism\n" >> report.txt
    printf "the total number of SigP gene is:\t" >> report.txt
    cat $Secretome | grep '>' | wc -l >> report.txt
    printf "the number of unique SigP gene is:\t" >> report.txt
    cat $Secretome | grep '>' | cut -f1 | tr -d ' '| sort | uniq | wc -l >> report.txt
    printf "the number of SigP-RxLR genes are:\t" >> report.txt
    ProgDir=/home/adamst/git_repos/tools/pathogen/RxLR_effectors
    $ProgDir/RxLR_EER_regex_finder.py $Secretome > $OutDir/"$Strain"_all_secreted_RxLR_regex.fa
    cat $OutDir/"$Strain"_all_secreted_RxLR_regex.fa | grep '>' | cut -f1 | tr -d '>' | tr -d ' ' | sort -g | uniq > $OutDir/"$Strain"_RxLR_regex.txt
    cat $OutDir/"$Strain"_RxLR_regex.txt | wc -l >> report.txt
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    $ProgDir/extract_from_fasta.py --fasta $Proteome --headers $OutDir/"$Strain"_RxLR_regex.txt > $OutDir/"$Strain"_RxLR_EER_regex.fa
    printf "the number of SigP-RxLR-EER genes are:\t" >> report.txt
    cat $OutDir/"$Strain"_all_secreted_RxLR_regex.fa | grep '>' | grep 'EER_motif_start' | cut -f1 | tr -d '>' | tr -d ' ' | sort -g | uniq > $OutDir/"$Strain"_RxLR_EER_regex.txt
    cat $OutDir/"$Strain"_RxLR_EER_regex.txt | wc -l >> report.txt
    $ProgDir/extract_from_fasta.py --fasta $Proteome --headers $OutDir/"$Strain"_RxLR_EER_regex.txt > $OutDir/"$Strain"_RxLR_EER_regex.fa
    printf "\n" >> report.txt
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
    sed -i -r 's/\.t.*//' $OutDir/"$Strain"_RxLR_regex.txt
    sed -i -r 's/\.t.*//' $OutDir/"$Strain"_RxLR_EER_regex.txt
    cat $Gff | grep -w -f $OutDir/"$Strain"_RxLR_regex.txt> $OutDir/"$Strain"_RxLR_regex.gff3
    cat $Gff | grep -w -f $OutDir/"$Strain"_RxLR_EER_regex.txt > $OutDir/"$Strain"_RxLR_EER_regex.gff3
    echo "$Strain complete"
done
```

```
strain: A4	species: P.fragariae
the total number of SigP gene is:	10668
the number of unique SigP gene is:	3850
the number of SigP-RxLR genes are:	403
the number of SigP-RxLR-EER genes are:	196


strain: Bc16	species: P.fragariae
the total number of SigP gene is:	11984
the number of unique SigP gene is:	4207
the number of SigP-RxLR genes are:	471
the number of SigP-RxLR-EER genes are:	223


strain: Bc1	species: P.fragariae
the total number of SigP gene is:	10432
the number of unique SigP gene is:	3700
the number of SigP-RxLR genes are:	397
the number of SigP-RxLR-EER genes are:	200


strain: Bc23	species: P.fragariae
the total number of SigP gene is:	10399
the number of unique SigP gene is:	3706
the number of SigP-RxLR genes are:	397
the number of SigP-RxLR-EER genes are:	200


strain: Nov27	species: P.fragariae
the total number of SigP gene is:	10414
the number of unique SigP gene is:	3714
the number of SigP-RxLR genes are:	397
the number of SigP-RxLR-EER genes are:	197


strain: Nov5	species: P.fragariae
the total number of SigP gene is:	10151
the number of unique SigP gene is:	3689
the number of SigP-RxLR genes are:	378
the number of SigP-RxLR-EER genes are:	192


strain: Nov71	species: P.fragariae
the total number of SigP gene is:	10767
the number of unique SigP gene is:	3850
the number of SigP-RxLR genes are:	407
the number of SigP-RxLR-EER genes are:	195


strain: Nov77	species: P.fragariae
the total number of SigP gene is:	10436
the number of unique SigP gene is:	3754
the number of SigP-RxLR genes are:	376
the number of SigP-RxLR-EER genes are:	178


strain: Nov9	species: P.fragariae
the total number of SigP gene is:	10523
the number of unique SigP gene is:	3772
the number of SigP-RxLR genes are:	394
the number of SigP-RxLR-EER genes are:	197


strain: ONT3	species: P.fragariae
the total number of SigP gene is:	13273
the number of unique SigP gene is:	4736
the number of SigP-RxLR genes are:	400
the number of SigP-RxLR-EER genes are:	195


strain: SCRP245_v2	species: P.fragariae
the total number of SigP gene is:	11414
the number of unique SigP gene is:	4158
the number of SigP-RxLR genes are:	401
the number of SigP-RxLR-EER genes are:	201
```

####G) From Secreted gene models - Hmm evidence of RxLR effectors

```bash
for Strain in A4 Bc16 Bc1 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for Proteome in $(ls gene_pred/braker/*/"$Strain"_braker/*/augustus.aa)
    do
        ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer
        HmmModel=/home/armita/git_repos/emr_repos/SI_Whisson_et_al_2007/cropped.hmm
        Organism=$(echo $Proteome | rev | cut -f4 -d '/' | rev)
        OutDir=analysis/RxLR_effectors/hmmer_RxLR/$Organism/$Strain
        mkdir -p $OutDir
        HmmResults="$Strain"_RxLR_hmmer.txt
        hmmsearch -T 0 $HmmModel $Proteome > $OutDir/$HmmResults
        echo "$Organism $Strain" >> report.txt
        cat $OutDir/$HmmResults | grep 'Initial search space' >> report.txt
        cat $OutDir/$HmmResults | grep 'number of targets reported over threshold' >> report.txt
        HmmFasta="$Strain"_RxLR_hmmer.fa
        $ProgDir/hmmer2fasta.pl $OutDir/$HmmResults $Proteome > $OutDir/$HmmFasta
        Headers="$Strain"_RxLR_hmmer_headers.txt
        cat $OutDir/$HmmFasta | grep '>' | cut -f1 | tr -d '>' | sed -r 's/\.t.*//' | tr -d ' ' | sort | uniq > $OutDir/$Headers
        Gff=$(ls gene_pred/braker/$Organism/"$Strain"_braker/*/augustus_extracted.gff)
        cat $Gff | grep -w -f $OutDir/$Headers > $OutDir/"$Strain"_Aug_RxLR_regex.gff3
        echo "$Strain complete"
    done
done
```

```
P.fragariae A4
Initial search space (Z):              38193  [actual number of targets]
Domain search space  (domZ):             202  [number of targets reported over threshold]
P.fragariae Bc16
Initial search space (Z):              39788  [actual number of targets]
Domain search space  (domZ):             235  [number of targets reported over threshold]
P.fragariae Bc1
Initial search space (Z):              36005  [actual number of targets]
Domain search space  (domZ):             203  [number of targets reported over threshold]
P.fragariae Bc23
Initial search space (Z):              36467  [actual number of targets]
Domain search space  (domZ):             200  [number of targets reported over threshold]
P.fragariae Nov27
Initial search space (Z):              35466  [actual number of targets]
Domain search space  (domZ):             197  [number of targets reported over threshold]
P.fragariae Nov5
Initial search space (Z):              37270  [actual number of targets]
Domain search space  (domZ):             194  [number of targets reported over threshold]
P.fragariae Nov71
Initial search space (Z):              37013  [actual number of targets]
Domain search space  (domZ):             196  [number of targets reported over threshold]
P.fragariae Nov77
Initial search space (Z):              37801  [actual number of targets]
Domain search space  (domZ):             191  [number of targets reported over threshold]
P.fragariae Nov9
Initial search space (Z):              37028  [actual number of targets]
Domain search space  (domZ):             198  [number of targets reported over threshold]
P.fragariae ONT3
Initial search space (Z):              41565  [actual number of targets]
Domain search space  (domZ):             192  [number of targets reported over threshold]
P.fragariae SCRP245_v2
Initial search space (Z):              41628  [actual number of targets]
Domain search space  (domZ):             205  [number of targets reported over threshold]
```

F) Combining RxLRs from Regex and hmm searches

The total RxLRs are

for RegexRxLR in $(ls analysis/RxLR_effectors/RxLR_EER_regex_finder/*/*/*_RxLR_EER_regex.txt | grep -v -e 'Aug' -e '10300' | grep -e 'P.idaei' -e 'P.cactorum' | grep -v '414'); do
Organism=$(echo $RegexRxLR | rev |  cut -d '/' -f3 | rev)
Strain=$(echo $RegexRxLR | rev | cut -d '/' -f2 | rev)
Gff=$(ls gene_pred/*/$Organism/$Strain/final/final_genes_appended.gff3)
Proteome=$(ls gene_pred/codingquary/$Organism/$Strain/*/final_genes_combined.pep.fasta)
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
Gff=$(ls gene_pred/*/$Organism/$Strain/final/final_genes_appended.gff3)
cat $Gff | grep -w -f $OutDir/"$Strain"_total_RxLR_headers.txt > $OutDir/"$Strain"_total_RxLR.gff
echo "Number of genes in the extracted gff file:"
cat $OutDir/"$Strain"_total_RxLR.gff | grep -w 'gene' | wc -l
done
  P.cactorum - 404
  Number of RxLRs identified by Regex:
  118
  Number of RxLRs identified by Hmm:
  127
  Number of RxLRs in combined dataset:
  149
  P.cactorum - 414
  Number of RxLRs identified by Regex:
  146
  Number of RxLRs identified by Hmm:
  145
  Number of RxLRs in combined dataset:
  173
  P.cactorum - 415
  Number of RxLRs identified by Regex:
  125
  Number of RxLRs identified by Hmm:
  132
  Number of RxLRs in combined dataset:
  159
  P.cactorum - 416
  Number of RxLRs identified by Regex:
  122
  Number of RxLRs identified by Hmm:
  129
  Number of RxLRs in combined dataset:
  155
  P.cactorum - 62471
  Number of RxLRs identified by Regex:
  134
  Number of RxLRs identified by Hmm:
  142
  Number of RxLRs in combined dataset:
  169
  P.idaei - 371
  Number of RxLRs identified by Regex:
  112
  Number of RxLRs identified by Hmm:
  107
  Number of RxLRs in combined dataset:
  136
  P.idaei - SCRP370
  Number of RxLRs identified by Regex:
  111
  Number of RxLRs identified by Hmm:
  105
  Number of RxLRs in combined dataset:
  137

D) From Augustus gene models - Hmm evidence of CRN effectors

A hmm model relating to crinkler domains was used to identify putative crinklers in Augustus gene models. This was done with the following commands:

  HmmDir=/home/groups/harrisonlab/project_files/idris/analysis/CRN_effectors/hmmer_models
  LFLAK_hmm=$(ls $HmmDir/Pinf_Pram_Psoj_Pcap_LFLAK.hmm)
  DWL_hmm=$(ls $HmmDir/Pinf_Pram_Psoj_Pcap_DWL.hmm)
  for Proteome in $(ls gene_pred/codingquary/*/*/*/final_genes_combined.pep.fasta | grep -w -e '414' -e 'P.idaei'); do
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
    ProgDir=/home/armita/git_repos/emr_repos/scripts/phytophthora/pathogen/hmmer
    $ProgDir/hmmer2fasta.pl $CrinklerProts_LFLAK $Proteome > $OutDir/"$Strain"_pub_CRN_LFLAK_hmm.fa
    # Run hmm searches DWL domains
    CrinklerProts_DWL=$OutDir/"$Strain"_pub_CRN_DWL_hmm.txt
    hmmsearch -T0 $DWL_hmm $Proteome > $CrinklerProts_DWL
    cat $CrinklerProts_DWL | grep 'Initial search space'
    cat $CrinklerProts_DWL | grep 'number of targets reported over threshold'
    ProgDir=/home/armita/git_repos/emr_repos/scripts/phytophthora/pathogen/hmmer
    $ProgDir/hmmer2fasta.pl $CrinklerProts_DWL $Proteome > $OutDir/"$Strain"_pub_CRN_DWL_hmm.fa
    # Identify the genes detected in both models
    cat $OutDir/"$Strain"_pub_CRN_LFLAK_hmm.fa $OutDir/"$Strain"_pub_CRN_DWL_hmm.fa | grep '>' | cut -f1 | tr -d '>' | sort | uniq -d > $OutDir/"$Strain"_pub_CRN_LFLAK_DWL.txt
    cat $OutDir/"$Strain"_pub_CRN_LFLAK_DWL.txt | wc -l
  done
  P.cactorum - 404
  Initial search space (Z):              27775  [actual number of targets]
  Domain search space  (domZ):             156  [number of targets reported over threshold]
  Initial search space (Z):              27775  [actual number of targets]
  Domain search space  (domZ):             129  [number of targets reported over threshold]
  113
  P.cactorum - 414
  Initial search space (Z):              32832  [actual number of targets]
  Domain search space  (domZ):             218  [number of targets reported over threshold]
  Initial search space (Z):              32832  [actual number of targets]
  Domain search space  (domZ):             189  [number of targets reported over threshold]
  170
  P.cactorum - 415
  Initial search space (Z):              31944  [actual number of targets]
  Domain search space  (domZ):             201  [number of targets reported over threshold]
  Initial search space (Z):              31944  [actual number of targets]
  Domain search space  (domZ):             169  [number of targets reported over threshold]
  147
  P.cactorum - 416
  Initial search space (Z):              32780  [actual number of targets]
  Domain search space  (domZ):             206  [number of targets reported over threshold]
  Initial search space (Z):              32780  [actual number of targets]
  Domain search space  (domZ):             182  [number of targets reported over threshold]
  155
  P.cactorum - 62471
  Initial search space (Z):              27191  [actual number of targets]
  Domain search space  (domZ):             154  [number of targets reported over threshold]
  Initial search space (Z):              27191  [actual number of targets]
  Domain search space  (domZ):             132  [number of targets reported over threshold]
  112
  P.idaei - 371
  Initial search space (Z):              27253  [actual number of targets]
  Domain search space  (domZ):             127  [number of targets reported over threshold]
  Initial search space (Z):              27253  [actual number of targets]
  Domain search space  (domZ):              98  [number of targets reported over threshold]
  87
  P.idaei - SCRP370
  Initial search space (Z):              26983  [actual number of targets]
  Domain search space  (domZ):             129  [number of targets reported over threshold]
  Initial search space (Z):              26983  [actual number of targets]
  Domain search space  (domZ):             103  [number of targets reported over threshold]
  92
Extract gff annotations for Crinklers:

  for CRNlist in $(ls analysis/CRN_effectors/hmmer_CRN/*/*/*_pub_CRN_LFLAK_DWL.txt | grep -e 'P.idaei' -e 'P.cactorum' | grep -v -e '10300'); do
    Strain=$(echo $CRNlist | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $CRNlist | rev | cut -f3 -d '/' | rev)
    OutName=$(echo $CRNlist | sed 's/.txt/.gff/g')
    echo "$Organism - $Strain"
    Gff=$(ls gene_pred/*/$Organism/$Strain/final/final_genes_appended.gff3)
    cat $CRNlist | sed -r 's/\.t.$//g' > tmp.txt
    cat $Gff | grep -w -f tmp.txt > $OutName
    rm tmp.txt
  done
E) From ORF gene models - Signal peptide & RxLR motif

Required programs:

SigP
Phobius
biopython
E.1) Prediction using SignalP

Proteins that were predicted to contain signal peptides were identified using the following commands:

    for Proteome in $(ls gene_pred/ORF_finder/P.*/*/*.aa_cat.fa | grep -e 'P.cactorum' -e 'P.idaei' | grep -v -e '10300'); do
    SplitfileDir=/home/armita/git_repos/emr_repos/tools/seq_tools/feature_annotation/signal_peptides
    ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/feature_annotation/signal_peptides
    Strain=$(echo $Proteome | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
    SplitDir=gene_pred/ORF_split/$Organism/$Strain
    mkdir -p $SplitDir
    BaseName="$Organism""_$Strain"_ORF_preds
    $SplitfileDir/splitfile_500.py --inp_fasta $Proteome --out_dir $SplitDir --out_base $BaseName
    for File in $(ls $SplitDir/*_ORF_preds_*); do
        Jobs=$(qstat | grep 'pred_sigP' | grep 'qw' | wc -l)
        while [ $Jobs -gt 6 ]; do
            sleep 1
            printf "."
            Jobs=$(qstat | grep 'pred_sigP' | grep 'qw' | wc -l)
        done        
        printf "\n"
        echo $File
        qsub $ProgDir/pred_sigP.sh $File
        qsub $ProgDir/pred_sigP.sh $File signalp-4.1
    done
  done
The batch files of predicted secreted proteins needed to be combined into a single file for each strain. This was done with the following commands:

for SplitDir in $(ls -d gene_pred/ORF_split/*/* | grep -w -e 'P.cactorum' -e 'P.idaei' | grep -v -e '10300' -e '414_v2'); do
Strain=$(echo $SplitDir | cut -d '/' -f4)
Organism=$(echo $SplitDir | cut -d '/' -f3)
echo "$Organism - $Strain"
InStringAA=''
InStringNeg=''
InStringTab=''
InStringTxt=''
for SigpDir in $(ls -d gene_pred/ORF_sig* | cut -f2 -d'/'); do
for GRP in $(ls -l $SplitDir/*_ORF_*.fa | rev | cut -d '_' -f1 | rev | sort -n); do  
InStringAA="$InStringAA gene_pred/$SigpDir/$Organism/$Strain/split/"$Organism"_"$Strain"_ORF_preds_$GRP""_sp.aa";
InStringNeg="$InStringNeg gene_pred/$SigpDir/$Organism/$Strain/split/"$Organism"_"$Strain"_ORF_preds_$GRP""_sp_neg.aa";
InStringTab="$InStringTab gene_pred/$SigpDir/$Organism/$Strain/split/"$Organism"_"$Strain"_ORF_preds_$GRP""_sp.tab";
InStringTxt="$InStringTxt gene_pred/$SigpDir/$Organism/$Strain/split/"$Organism"_"$Strain"_ORF_preds_$GRP""_sp.txt";
done
cat $InStringAA > gene_pred/$SigpDir/$Organism/$Strain/"$Strain"_aug_sp.aa
cat $InStringNeg > gene_pred/$SigpDir/$Organism/$Strain/"$Strain"_aug_neg_sp.aa
tail -n +2 -q $InStringTab > gene_pred/$SigpDir/$Organism/$Strain/"$Strain"_aug_sp.tab
cat $InStringTxt > gene_pred/$SigpDir/$Organism/$Strain/"$Strain"_aug_sp.txt
done
done
E.2) Prediction using Phobius

Secreted proteins were also predicted using Phobius

    for Proteome in $(ls gene_pred/ORF_finder/P.*/*/*.aa_cat.fa | grep -e 'P.cactorum' -e 'P.idaei' | grep -v '10300' | grep -w -e '404' -e '414' -e '415' -e '416'); do
    Strain=$(echo $Proteome | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
    echo "$Organism - $Strain"
    OutDir=analysis/phobius/$Organism/$Strain
    mkdir -p $OutDir
    phobius.pl $Proteome > $OutDir/"$Strain"_phobius_ORF.txt
    cat $OutDir/"$Strain"_phobius_ORF.txt | grep -B1 'SIGNAL' | grep 'ID' | sed s'/ID.*g/g/g' > $OutDir/"$Strain"_phobius_headers_ORF.txt
  done
Secreted proteins from different sources were combined into a single file:

  for Proteome in $(ls gene_pred/ORF_finder/P.*/*/*.aa_cat.fa | grep -e 'P.cactorum' -e 'P.idaei' | grep -v -e '10300' -e '414_v2' | grep -w -e '404' -e '414' -e '415' -e '416'); do
    Strain=$(echo $Proteome | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
    echo "$Organism - $Strain"
    OutDir=gene_pred/combined_sigP_ORF/$Organism/$Strain
    mkdir -p $OutDir
    echo "The following number of sequences were predicted as secreted:"
    # cat gene_pred/ORF_sig*/$Organism/$Strain/*_aug_sp.aa analysis/phobius/$Organism/$Strain/"$Strain"_phobius.fa > $OutDir/"$Strain"_all_secreted.fa
    cat gene_pred/ORF_sig*/$Organism/$Strain/*_aug_sp.aa > $OutDir/"$Strain"_all_secreted.fa
    cat $OutDir/"$Strain"_all_secreted.fa | grep '>' | tr -d '>' | tr -d ' ' | sed "s/HMM_score\t/HMM_score=\t/g" > $OutDir/"$Strain"_all_secreted_headers.txt
    cat $OutDir/"$Strain"_all_secreted_headers.txt | wc -l
    echo "This represented the following number of unique genes:"
    # cat gene_pred/final_sig*/$Organism/$Strain/*_aug_sp.aa analysis/phobius/$Organism/$Strain/"$Strain"_phobius.fa | grep '>' | cut -f1 | tr -d ' >' | sort -g | uniq > $OutDir/"$Strain"_secreted.txt
    cat gene_pred/ORF_sig*/$Organism/$Strain/*_aug_sp.aa | grep '>' | cut -f1 | tr -d ' >' | sort -g | uniq > $OutDir/"$Strain"_secreted.txt
    ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/ORF_finder
    # $ProgDir/extract_from_fasta.py --fasta $Proteome --headers $OutDir/"$Strain"_secreted.txt > $OutDir/"$Strain"_secreted.fa
    cat $OutDir/"$Strain"_secreted.fa | grep '>' | wc -l
  done
  P.cactorum - 404
  The following number of sequences were predicted as secreted:
  55547
  This represented the following number of unique genes:
  26231
  P.cactorum - 414
  The following number of sequences were predicted as secreted:
  70912
  This represented the following number of unique genes:
  33601
  P.cactorum - 415
  The following number of sequences were predicted as secreted:
  60266
  This represented the following number of unique genes:
  28714
  P.cactorum - 416
  The following number of sequences were predicted as secreted:
  61712
  This represented the following number of unique genes:
  29425
  P.cactorum - 62471
  The following number of sequences were predicted as secreted:
  55686
  This represented the following number of unique genes:
  26324
  P.idaei - 371
  The following number of sequences were predicted as secreted:
  54493
  This represented the following number of unique genes:
  25750
  P.idaei - SCRP370
  The following number of sequences were predicted as secreted:
  54601
  This represented the following number of unique genes:
  25802
E.3) Prediction of RxLRs

Names of ORFs containing signal peptides were extracted from fasta files. This included information on the position and hmm score of RxLRs.

    FastaFile=gene_pred/ORF_sigP/$Organism/$Strain/"$Strain"_ORF_sp.aa
    SigP_headers=gene_pred/ORF_sigP/$Organism/$Strain/"$Strain"_ORF_sp_names.txt
    cat $FastaFile | grep '>' | sed -r 's/>//g' | sed -r 's/\s+/\t/g'| sed 's/=\t/=/g' | sed 's/--//g' > $SigP_headers
Due to the nature of predicting ORFs, some features overlapped with one another. A single ORF was selected from each set of overlapped ORFs. This was was selected on the basis of its SignalP Hmm score. Biopython was used to identify overlaps and identify the ORF with the best signalP score.

  for ORF_Gff in $(ls gene_pred/ORF_finder/*/*/*_ORF.gff3 | grep -v -e 'atg' | grep -e 'P.cactorum' -e 'P.idaei' | grep -v -e '10300' -e '414_v2' | grep -v -w -e '404' -e '414' -e '415' -e '416'); do
    Organism=$(echo $ORF_Gff | rev |  cut -d '/' -f3 | rev) ;
    Strain=$(echo $ORF_Gff | rev | cut -d '/' -f2 | rev);
    OutDir=$(ls -d gene_pred/combined_sigP_ORF/$Organism/$Strain)
    echo "$Organism - $Strain"
    # SigP_fasta=$(ls $OutDir/"$Strain"_all_secreted.fa)
    SigP_headers=$(ls $OutDir/"$Strain"_all_secreted_headers.txt)
    ORF_fasta=$(ls gene_pred/ORF_finder/$Organism/$Strain/"$Strain".aa_cat.fa)

    SigP_Gff=$OutDir/"$Strain"_all_secreted_unmerged.gff
    SigP_Merged_Gff=$OutDir/"$Strain"_all_secreted_merged.gff
    SigP_Merged_txt=$OutDir/"$Strain"_all_secreted_merged.txt
    SigP_Merged_AA=$OutDir/"$Strain"_all_secreted_merged.aa

    ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/ORF_finder
    $ProgDir/extract_gff_for_sigP_hits.pl $SigP_headers $ORF_Gff SigP Name > $SigP_Gff
    ProgDir=~/git_repos/emr_repos/scripts/phytophthora/pathogen/merge_gff
    $ProgDir/make_gff_database.py --inp $SigP_Gff --db sigP_ORF.db
    ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/ORF_finder
    $ProgDir/merge_sigP_ORFs.py --inp sigP_ORF.db --id sigP_ORF --out sigP_ORF_merged.db --gff > $SigP_Merged_Gff
    cat $SigP_Merged_Gff | grep 'transcript' | rev | cut -f1 -d'=' | rev > $SigP_Merged_txt
    # $ProgDir/extract_from_fasta.py --fasta $SigP_fasta --headers $SigP_Merged_txt > $SigP_Merged_AA
    $ProgDir/extract_from_fasta.py --fasta $ORF_fasta --headers $SigP_Merged_txt > $SigP_Merged_AA
  done
<--- Progress up to here

The regular expression R.LR.{,40}[ED][ED][KR] has previously been used to identify RxLR effectors. The addition of an EER motif is significant as it has been shown as required for host uptake of the protein.

The RxLR_EER_regex_finder.py script was used to search for this regular expression and annotate the EER domain where present.

for Secretome in $(ls gene_pred/combined_sigP_ORF/*/*/*_all_secreted.fa | grep -e 'P.cactorum' -e 'P.idaei' | grep -v -e '10300' -e '414_v2' | grep -v -w -e '404' -e '414' -e '415' -e '416'); do
ProgDir=~/git_repos/emr_repos/tools/pathogen/RxLR_effectors
Strain=$(echo $Secretome | rev | cut -d '/' -f2 | rev);
Organism=$(echo $Secretome | rev |  cut -d '/' -f3 | rev) ;
OutDir=analysis/RxLR_effectors/RxLR_EER_regex_finder/"$Organism"/"$Strain";
mkdir -p $OutDir;
printf "\nstrain: $Strain\tspecies: $Organism\n";
printf "the number of SigP gene is:\t";
cat $Secretome | grep '>' | wc -l;
printf "the number of SigP-RxLR genes are:\t";
$ProgDir/RxLR_EER_regex_finder.py $Secretome > $OutDir/"$Strain"_ORF_RxLR_EER_regex_unmerged.fa;
cat $OutDir/"$Strain"_ORF_RxLR_EER_regex_unmerged.fa | grep '>' | cut -f1 | tr -d '>' | sed -r 's/\.t.*//' | tr -d ' ' > $OutDir/"$Strain"_ORF_RxLR_regex_unmerged.txt
cat $OutDir/"$Strain"_ORF_RxLR_regex_unmerged.txt | tr -d ' ' | sort | uniq | wc -l
printf "the number of SigP-RxLR-EER genes are:\t";
cat $OutDir/"$Strain"_ORF_RxLR_EER_regex_unmerged.fa | grep '>' | grep 'EER_motif_start' | cut -f1 | tr -d '>' | sed -r 's/\.t.*//' | tr -d ' '> $OutDir/"$Strain"_ORF_RxLR_EER_regex_unmerged.txt
cat $OutDir/"$Strain"_ORF_RxLR_EER_regex_unmerged.txt | tr -d ' ' | sort | uniq | wc -l
ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/feature_annotation
# $ProgDir/gene_list_to_gff.pl $OutDir/"$Strain"_ORF_RxLR_regex_unmerged.txt  $SigP_Merged_Gff  RxLR_EER_regex_finder.py Name Augustus > $OutDir/"$Strain"_ORF_RxLR_regex_unmerged.gff
SigP_Gff=gene_pred/combined_sigP_ORF/$Organism/$Strain/"$Strain"_all_secreted_unmerged.gff
ORF_fasta=$(ls gene_pred/ORF_finder/$Organism/$Strain/"$Strain".aa_cat.fa)
ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/feature_annotation
$ProgDir/gene_list_to_gff.pl $OutDir/"$Strain"_ORF_RxLR_EER_regex_unmerged.txt  $SigP_Gff   RxLR_EER_regex_finder.py Name Augustus > $OutDir/"$Strain"_ORF_RxLR_regex_unmerged.gff
# ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/feature_annotation
# $ProgDir/gene_list_to_gff.pl $OutDir/"$Strain"_ORF_RxLR_EER_regex_unmerged.txt $SigP_Merged_Gff RxLR_EER_regex_finder.py Name Augustus > $OutDir/"$Strain"_ORF_RxLR_EER_regex.gff
RxLR_Merged_Gff=$OutDir/"$Strain"_ORF_RxLR_EER_regex_merged.gff
RxLR_Merged_txt=$OutDir/"$Strain"_ORF_RxLR_EER_regex_merged.txt
RxLR_Merged_AA=$OutDir/"$Strain"_ORF_RxLR_EER_regex_merged.aa
ProgDir=~/git_repos/emr_repos/scripts/phytophthora/pathogen/merge_gff
$ProgDir/make_gff_database.py --inp $OutDir/"$Strain"_ORF_RxLR_regex_unmerged.gff --db sigP_ORF_RxLR.db
ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/ORF_finder
$ProgDir/merge_sigP_ORFs.py --inp sigP_ORF_RxLR.db --id sigP_ORF_RxLR --out sigP_ORF_RxLR_merged.db --gff > $RxLR_Merged_Gff
cat $RxLR_Merged_Gff | grep 'transcript' | rev | cut -f1 -d '=' | rev > $RxLR_Merged_txt
$ProgDir/extract_from_fasta.py --fasta $ORF_fasta --headers $RxLR_Merged_txt > $RxLR_Merged_AA
printf "Merged RxLR-EER regex proteins:\t"
cat $RxLR_Merged_AA | grep '>' | wc -l
printf "\n"
done
strain: 414 species: P.cactorum
the number of SigP gene is: 70912
the number of SigP-RxLR genes are:  1876
the number of SigP-RxLR-EER genes are:  220
Merged RxLR-EER regex proteins:197

strain: 404 species: P.cactorum
the number of SigP gene is: 55547
the number of SigP-RxLR genes are:  1519
the number of SigP-RxLR-EER genes are:  194
Merged RxLR-EER regex proteins: 170

strain: 415 species: P.cactorum
the number of SigP gene is: 60266
the number of SigP-RxLR genes are:  1591
the number of SigP-RxLR-EER genes are:  192
Merged RxLR-EER regex proteins: 168

strain: 416 species: P.cactorum
the number of SigP gene is: 61712
the number of SigP-RxLR genes are:  1621
the number of SigP-RxLR-EER genes are:  192
Merged RxLR-EER regex proteins: 168
E5) From ORF gene models - Hmm evidence of WY domains

Hmm models for the WY domain contained in many RxLRs were used to search ORFs predicted with atg.pl. These were run with the following commands:

for Secretome in $(ls gene_pred/ORF_sigP/P.cactorum/10300/10300_ORF_sp_merged.aa); do
ProgDir=/home/armita/git_repos/emr_repos/scripts/phytophthora/pathogen/hmmer
HmmModel=/home/armita/git_repos/emr_repos/scripts/phytophthora/pathogen/hmmer/WY_motif.hmm
Strain=$(echo $Secretome | rev | cut -f2 -d '/' | rev)
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
P.cactorum 10300
Initial search space (Z): 14767 [actual number of targets]
Domain search space (domZ): 113 [number of targets reported over threshold]
E6) From ORF gene models - Hmm evidence of RxLR effectors

for Secretome in $(ls gene_pred/combined_sigP_ORF/*/*/*_all_secreted.fa | grep -w -e '414' | grep -v -w -e '404' -e '415' -e '416'); do
ProgDir=/home/armita/git_repos/emr_repos/scripts/phytophthora/pathogen/hmmer
HmmModel=/home/armita/git_repos/emr_repos/SI_Whisson_et_al_2007/cropped.hmm
Strain=$(echo $Secretome | rev | cut -f2 -d '/' | rev)
Organism=$(echo $Secretome | rev | cut -f3 -d '/' | rev)
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
ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/feature_annotation
$ProgDir/gene_list_to_gff.pl $OutDir/$Headers $SigP_Gff $HmmModel Name Augustus > $OutDir/"$Strain"_ORF_RxLR_hmmer_unmerged.gff3
RxLR_Merged_Gff=$OutDir/"$Strain"_ORF_RxLR_hmm_merged.gff
RxLR_Merged_txt=$OutDir/"$Strain"_ORF_RxLR_hmm_merged.txt
RxLR_Merged_AA=$OutDir/"$Strain"_ORF_RxLR_hmm_merged.aa
ProgDir=~/git_repos/emr_repos/scripts/phytophthora/pathogen/merge_gff
$ProgDir/make_gff_database.py --inp $OutDir/"$Strain"_ORF_RxLR_hmmer_unmerged.gff3 --db sigP_ORF_RxLR_hmm.db
ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/ORF_finder
$ProgDir/merge_sigP_ORFs.py --inp sigP_ORF_RxLR_hmm.db --id sigP_ORF_RxLR_hmm --out sigP_ORF_RxLR_hmm_merged.db --gff > $RxLR_Merged_Gff
cat $RxLR_Merged_Gff | grep 'transcript' | rev | cut -f1 -d '=' | rev > $RxLR_Merged_txt
ORF_fasta=$(ls gene_pred/ORF_finder/$Organism/$Strain/"$Strain".aa_cat.fa)
$ProgDir/extract_from_fasta.py --fasta $ORF_fasta --headers $RxLR_Merged_txt > $RxLR_Merged_AA
printf "Merged RxLR-EER Hmm proteins:\t"
cat $RxLR_Merged_AA | grep '>' | wc -l
done
  P.cactorum 404
  Initial search space (Z):              55547  [actual number of targets]
  Domain search space  (domZ):             417  [number of targets reported over threshold]
  Merged RxLR-EER Hmm proteins: 129
  P.cactorum 414
  Initial search space (Z):              70912  [actual number of targets]
  Domain search space  (domZ):             495  [number of targets reported over threshold]
  Merged RxLR-EER Hmm proteins: 154
  P.cactorum 415
  Initial search space (Z):              60266  [actual number of targets]
  Domain search space  (domZ):             421  [number of targets reported over threshold]
  Merged RxLR-EER Hmm proteins: 129
  P.cactorum 416
  Initial search space (Z):              61712  [actual number of targets]
  Domain search space  (domZ):             412  [number of targets reported over threshold]
  Merged RxLR-EER Hmm proteins: 128
P.cactorum 10300
Initial search space (Z): 14767 [actual number of targets]
Domain search space (domZ): 144 [number of targets reported over threshold]
E7) Combining RxLRs from Regex and hmm searches

The total RxLRs are

  for RegexRxLR in $(ls analysis/RxLR_effectors/RxLR_EER_regex_finder/*/*/*_ORF_RxLR_EER_regex_merged.txt | grep -v -e 'Aug' -e '10300' | grep -e 'P.idaei' -e 'P.cactorum' | grep -e '414' -e '404' -e '415' -e '416'); do
    Organism=$(echo $RegexRxLR | rev |  cut -d '/' -f3 | rev)
    Strain=$(echo $RegexRxLR | rev | cut -d '/' -f2 | rev)
    Gff=$(ls gene_pred/ORF_finder/$Organism/$Strain/"$Strain"_ORF.gff3)
    Proteome=$(ls gene_pred/ORF_finder/$Organism/$Strain/"$Strain".aa_cat.fa)
    HmmRxLR=$(ls analysis/RxLR_effectors/hmmer_RxLR/$Organism/$Strain/"$Strain"_ORF_RxLR_hmm_merged.txt)
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
    cat $RegexRxLR $HmmRxLR | sort | uniq > $OutDir/"$Strain"_total_ORF_RxLR_headers.txt
    # cat $Gff | grep -w -f $OutDir/"$Strain"_total_ORF_RxLR_headers.txt > $OutDir/"$Strain"_total_ORF_RxLR.gff
    ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/feature_annotation
    $ProgDir/gene_list_to_gff.pl $OutDir/"$Strain"_total_ORF_RxLR_headers.txt $Gff ORF_RxLR Name Augustus > $OutDir/"$Strain"_total_ORF_RxLR.gff
    echo "Number of genes in the extracted gff file:"
    cat $OutDir/"$Strain"_total_ORF_RxLR.gff | grep -w 'gene' | wc -l
  done
4.2.c Analysis of RxLR effectors - merger of Augustus / published genes with ORFs

Intersection between the coodinates of putative RxLRs from gene models and ORFs were identified to determine the total number of RxLRs predicted in these genomes.

The RxLR effectors from both Gene models and ORF finding approaches were combined into a single file.

This step was complicated by the inconsistency in downloaded gff files for gene models.

for MergeDir in $(ls -d analysis/RxLR_effectors/combined_evidence/*/* | grep -e 'P.idaei' -e 'P.cactorum' | grep -w -e '414' -e '404' -e '415' -e '416'); do
Strain=$(echo "$MergeDir" | rev | cut -f1 -d '/' | rev)
Species=$(echo "$MergeDir" | rev | cut -f2 -d '/' | rev)
AugGff=$MergeDir/"$Strain"_total_RxLR.gff
AugTxt=$MergeDir/"$Strain"_total_RxLR_headers.txt
AugFa=$(ls gene_pred/codingquary/"$Species"/"$Strain"/final/final_genes_combined.pep.fasta)

ORFGff=$(ls $MergeDir/"$Strain"_total_ORF_RxLR.gff)
ORFsFa=$(ls gene_pred/ORF_finder/"$Species"/"$Strain"/"$Strain".aa_cat.fa)
ORFsTxt=$(ls $MergeDir/"$Strain"_total_ORF_RxLR_headers.txt)

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
# cat $ORFsUniq | grep -w 'transcript' | cut -f9 | cut -f1 -d ';' | cut -f2 -d '=' >> $TotalRxLRsTxt
echo "The number of RxLRs unique to Augustus models:"
cat $AugUniq | grep -w -e 'transcript' -e 'mRNA' | wc -l
echo "The total number of putative RxLRs are:"
cat $AugInORFs | grep -w -e 'transcript' -e 'mRNA'  | cut -f9 | cut -f1 -d ';' | cut -f2 -d '=' > $TotalRxLRsTxt
cat $AugUniq | grep -w -e 'transcript' -e 'mRNA'  | cut -f9 | cut -f1 -d ';' | cut -f2 -d '=' >> $TotalRxLRsTxt
cat $ORFsUniq | grep -w -e 'transcript' -e 'mRNA'  | cut -f9 | cut -f3 -d ';' | cut -f2 -d '=' >> $TotalRxLRsTxt
cat $TotalRxLRsTxt | wc -l
cat $AugInORFs $AugUniq $ORFsUniq | grep -w -f $TotalRxLRsTxt > $TotalRxLRsGff

RxLRsFa=$MergeDir/"$Strain"_final_RxLR_EER.fa
ProgDir=~/git_repos/emr_repos/tools/seq_tools/feature_annotation
# $ProgDir/unwrap_fasta.py --inp_fasta $AugFa | grep -A1 -w -f $AugTxt | grep -v -E '^--$' > $RxLRsFa
ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/ORF_finder
$ProgDir/extract_from_fasta.py --fasta $AugFa --headers $TotalRxLRsTxt > $RxLRsFa
# echo "$Strain"
$ProgDir/extract_from_fasta.py --fasta $ORFsFa --headers $TotalRxLRsTxt >> $RxLRsFa
# echo "$Strain"
echo "The number of sequences extracted is"
cat $RxLRsFa | grep '>' | wc -l
done
  P.cactorum - 404
  The number of ORF RxLRs overlapping Augustus RxLRs:
  129
  The number of Augustus RxLRs overlapping ORF RxLRs:
  129
  The number of RxLRs unique to ORF models:
  58
  The number of RxLRs unique to Augustus models:
  20
  The total number of putative RxLRs are:
  207
  P.cactorum - 414
  The number of ORF RxLRs overlapping Augustus RxLRs:
  153
  The number of Augustus RxLRs overlapping ORF RxLRs:
  153
  The number of RxLRs unique to ORF models:
  62
  The number of RxLRs unique to Augustus models:
  20
  The total number of putative RxLRs are:
  235
  P.cactorum - 415
  The number of ORF RxLRs overlapping Augustus RxLRs:
  134
  The number of Augustus RxLRs overlapping ORF RxLRs:
  134
  The number of RxLRs unique to ORF models:
  52
  The number of RxLRs unique to Augustus models:
  25
  The total number of putative RxLRs are:
  211
  P.cactorum - 416
  The number of ORF RxLRs overlapping Augustus RxLRs:
  130
  The number of Augustus RxLRs overlapping ORF RxLRs:
  130
  The number of RxLRs unique to ORF models:
  55
  The number of RxLRs unique to Augustus models:
  25
  The total number of putative RxLRs are:
  210
H) From ORF gene models - Hmm evidence of CRN effectors

A hmm model relating to crinkler domains was used to identify putative crinklers in ORF gene models. This was done with the following commands:

for Proteome in $(ls gene_pred/ORF_finder/*/*/*.aa_cat.fa | grep -w -e 'P.cactorum' -e 'P.idaei' | grep -v -e 'atg' -e '10300' -e '414_v2' | grep -v -w -e '404' -e '414' -e '415' -e '416'); do
# Setting variables
Strain=$(echo $Proteome | rev | cut -f2 -d '/' | rev)
Organism=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
OutDir=analysis/CRN_effectors/hmmer_CRN/$Organism/$Strain
mkdir -p $OutDir
# Hmmer variables
ProgDir=/home/armita/git_repos/emr_repos/scripts/phytophthora/pathogen/hmmer
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
ORF_Gff=$(ls gene_pred/ORF_finder/$Organism/$Strain/*_ORF.gff3)
# Gff features were extracted for each header
CRN_unmerged_Gff=$OutDir/"$Strain"_CRN_unmerged_hmmer.gff3
ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/ORF_finder
$ProgDir/extract_gff_for_sigP_hits.pl $Headers $ORF_Gff CRN_HMM Name > $CRN_unmerged_Gff
# Gff features were merged based upon the DWL hmm score
DbDir=analysis/databases/$Organism/$Strain
mkdir -p $DbDir
ProgDir=~/git_repos/emr_repos/scripts/phytophthora/pathogen/merge_gff
$ProgDir/make_gff_database.py --inp $CRN_unmerged_Gff --db $DbDir/CRN_ORF.db
CRN_Merged_Gff=$OutDir/"$Strain"_CRN_merged_hmmer.gff3
ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/ORF_finder
$ProgDir/merge_sigP_ORFs.py --inp $DbDir/CRN_ORF.db --id LFLAK_DWL_CRN --out $DbDir/CRN_ORF_merged.db --gff > $CRN_Merged_Gff
# Final results are reported:
echo "Number of CRN ORFs after merging:"
cat $CRN_Merged_Gff | grep 'gene' | wc -l
done
Searching for LFLAK domains in: P.cactorum 404
Initial search space (Z):             487049  [actual number of targets]
Domain search space  (domZ):             238  [number of targets reported over threshold]
Searching for DWL domains in: P.cactorum 404
Initial search space (Z):             487049  [actual number of targets]
Domain search space  (domZ):             293  [number of targets reported over threshold]
The number of CRNs common to both models are:
139
Number of CRN ORFs after merging:
97
Searching for LFLAK domains in: P.cactorum 414
Initial search space (Z):             631759  [actual number of targets]
Domain search space  (domZ):             342  [number of targets reported over threshold]
Searching for DWL domains in: P.cactorum 414
Initial search space (Z):             631759  [actual number of targets]
Domain search space  (domZ):             455  [number of targets reported over threshold]
The number of CRNs common to both models are:
223
Number of CRN ORFs after merging:
155
Searching for LFLAK domains in: P.cactorum 415
Initial search space (Z):             542852  [actual number of targets]
Domain search space  (domZ):             310  [number of targets reported over threshold]
Searching for DWL domains in: P.cactorum 415
Initial search space (Z):             542852  [actual number of targets]
Domain search space  (domZ):             375  [number of targets reported over threshold]
The number of CRNs common to both models are:
178
Number of CRN ORFs after merging:
130
Searching for LFLAK domains in: P.cactorum 416
Initial search space (Z):             557317  [actual number of targets]
Domain search space  (domZ):             319  [number of targets reported over threshold]
Searching for DWL domains in: P.cactorum 416
Initial search space (Z):             557317  [actual number of targets]
Domain search space  (domZ):             404  [number of targets reported over threshold]
The number of CRNs common to both models are:
200
Number of CRN ORFs after merging:
141
Searching for LFLAK domains in: P.cactorum 62471
Initial search space (Z):             488325  [actual number of targets]
Domain search space  (domZ):             245  [number of targets reported over threshold]
Searching for DWL domains in: P.cactorum 62471
Initial search space (Z):             488325  [actual number of targets]
Domain search space  (domZ):             308  [number of targets reported over threshold]
The number of CRNs common to both models are:
153
Number of CRN ORFs after merging:
100
Searching for LFLAK domains in: P.idaei 371
Initial search space (Z):             487686  [actual number of targets]
Domain search space  (domZ):             217  [number of targets reported over threshold]
Searching for DWL domains in: P.idaei 371
Initial search space (Z):             487686  [actual number of targets]
Domain search space  (domZ):             254  [number of targets reported over threshold]
The number of CRNs common to both models are:
122
Number of CRN ORFs after merging:
86
Searching for LFLAK domains in: P.idaei SCRP370
Initial search space (Z):             486809  [actual number of targets]
Domain search space  (domZ):             220  [number of targets reported over threshold]
Searching for DWL domains in: P.idaei SCRP370
Initial search space (Z):             486809  [actual number of targets]
Domain search space  (domZ):             256  [number of targets reported over threshold]
The number of CRNs common to both models are:
125
Number of CRN ORFs after merging:
89
Extract crinklers from published gene models

  for MergeDir in $(ls -d analysis/CRN_effectors/hmmer_CRN/*/* | grep -w -e 'P.cactorum' -e 'P.idaei' | grep -v -e 'atg' -e '10300' -e '414_v2' | grep -w -e '404' -e '414' -e '415' -e '416'); do
    Strain=$(echo "$MergeDir" | rev | cut -f1 -d '/' | rev)
    Species=$(echo "$MergeDir" | rev | cut -f2 -d '/' | rev)
    AugGff=$(ls $MergeDir/"$Strain"_pub_CRN_LFLAK_DWL.gff)
    AugFa=$(ls gene_pred/codingquary/"$Species"/"$Strain"/final/final_genes_combined.pep.fasta)
    ORFsFa=$(ls gene_pred/ORF_finder/"$Species"/"$Strain"/"$Strain".aa_cat.fa)
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
    ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/ORF_finder
    $ProgDir/extract_from_fasta.py --fasta $AugFa --headers $TotalCRNsTxt > $CRNsFa
    $ProgDir/extract_from_fasta.py --fasta $ORFsFa --headers $TotalCRNsTxt >> $CRNsFa
    echo "The number of sequences extracted is"
    cat $CRNsFa | grep '>' | wc -l

  done
P.cactorum - 404
The number of ORF CRNs overlapping Augustus CRNs:
93
The number of Augustus CRNs overlapping ORF CRNs:
93
The number of CRNs unique to ORF models:
4
The number of CRNs unique to Augustus models:
19
The number of sequences extracted is
113
P.cactorum - 414
The number of ORF CRNs overlapping Augustus CRNs:
151
The number of Augustus CRNs overlapping ORF CRNs:
151
The number of CRNs unique to ORF models:
4
The number of CRNs unique to Augustus models:
17
The number of sequences extracted is
173
P.cactorum - 415
The number of ORF CRNs overlapping Augustus CRNs:
126
The number of Augustus CRNs overlapping ORF CRNs:
126
The number of CRNs unique to ORF models:
4
The number of CRNs unique to Augustus models:
20
The number of sequences extracted is
147
P.cactorum - 416
The number of ORF CRNs overlapping Augustus CRNs:
137
The number of Augustus CRNs overlapping ORF CRNs:
137
The number of CRNs unique to ORF models:
4
The number of CRNs unique to Augustus models:
17
The number of sequences extracted is
155

4. 2 Ananlysis of RxLR effectors

Due to RxLR effectors being predicted from a number of sources the number of unique RxLRs were identified from motif and Hmm searches within gene models.

Details on the commands run to identify this can be found within this repository in 10300_analysis/effector_charactisation.md -->
