# phytophthora_fragariae
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
Nov71: 810,779,109

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
Nov71: 5 (41)

Target coverage is 20.
The ones at value 5 are errors from filtering of error kmers, estimate from plots follow in ().

# Assembly
Assembly was performed using: Spades

# Spades Assembly

For single runs

```bash
for Strain in A4 Bc23 Nov27 Nov5 Nov77 ONT3 SCRP245_v2
do
    F_Read=$(ls qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz)
    R_Read=$(ls qc_dna/paired/P.fragariae/$Strain/R/*.fq.gz)
    CovCutoff='10'
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/spades
    Species=$(echo $F_Read | rev | cut -f4 -d '/' | rev)
    OutDir=assembly/spades/$Species/$Strain
    echo $Species
    echo $Strain
    qsub $ProgDir/submit_SPAdes.sh $F_Read $R_Read $OutDir correct $CovCutoff
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
    qsub $ProgDir/subSpades_2lib.sh $F_Read1 $R_Read1 $F_Read2 $R_Read2 $OutDir correct 10
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
    qsub $ProgDir/subSpades_3lib.sh $F_Read1 $R_Read1 $F_Read2 $R_Read2 $F_Read3 $R_Read3 $OutDir correct 10
done
```

#Quast

```bash
for Strain in Bc1 Bc16 Nov9; do
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

#QUAST used to summarise assembly statistics

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/quast
for Strain in Bc1 Bc16 Nov9; do
    for Assembly in $(ls assembly/spades/*/$Strain/filtered_contigs/*_500bp_renamed.fasta); do
        Strain=$(echo $Assembly | rev | cut -d '/' -f3 | rev)
        Organism=$(echo $Assembly | rev | cut -d '/' -f4 | rev)
        OutDir=assembly/spades/$Organism/$Strain/filtered_contigs
        qsub $ProgDir/sub_quast.sh $Assembly $OutDir
    done
done
```
**N50:
A4: 14018
62471: 30981
BC-16: 437436
BC-23: 18939
NOV-27: 15300
NOV-5: 14404
NOV-77: 15180
ONT-3: 17405
SCRP245_v2: 22809
NOV-71: 16894
NOV-9: 20065
BC-1: 20508**

**L50:
A4: 1452
62471: 561
BC-16: 59
BC-23: 987
NOV-27: 1312
NOV-5: 1394
NOV-77: 1324
ONT-3: 1132
SCRP245_v2: 796
NOV-71: 1233
NOV-9: 1093
BC-1: 1068**

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
  ls assembly/spades/*/$Strain/filtered_contigs/*_500bp_renamed.fasta
The number of bases masked by transposonPSI and Repeatmasker were summarised using the following commands:

  for RepDir in $(ls -d repeat_masked/P.*/*/filtered_contigs_repmask | grep -w -e '414'); do
    Strain=$(echo $RepDir | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $RepDir | rev | cut -f3 -d '/' | rev)  
    RepMaskGff=$(ls $RepDir/*_contigs_hardmasked.gff)
    TransPSIGff=$(ls $RepDir/*_contigs_unmasked.fa.TPSI.allHits.chains.gff3)
    printf "$Organism\t$Strain\n"
    printf "The number of bases masked by RepeatMasker:\t"
    sortBed -i $RepMaskGff | bedtools merge | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
    printf "The number of bases masked by TransposonPSI:\t"
    sortBed -i $TransPSIGff | bedtools merge | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
    printf "The total number of masked bases are:\t"
    cat $RepMaskGff $TransPSIGff | sortBed | bedtools merge | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
    echo
  done
  P.cactorum    414
  The number of bases masked by RepeatMasker:   16199492
  The number of bases masked by TransposonPSI:  4951212
  The total number of masked bases are: 17347836
Gene Prediction
Gene prediction followed three steps: Pre-gene prediction - Quality of genome assemblies were assessed using Cegma to see how many core eukaryotic genes can be identified. Gene model training - Gene models were trained using assembled RNAseq data as part of the Braker1 pipeline Gene prediction - Gene models were used to predict genes in genomes as part of the the Braker1 pipeline. This used RNAseq data as hints for gene models.

Pre-gene prediction

Quality of genome assemblies was assessed by looking for the gene space in the assemblies.

  ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/cegma
  for Genome in $(ls repeat_masked/P.*/*/filtered_contigs_repmask/*_contigs_unmasked.fa | grep -e '414'); do
    echo $Genome;
    qsub $ProgDir/sub_cegma.sh $Genome dna;
  done
Outputs were summarised using the commands:

    for File in $(ls gene_pred/cegma/F*/FUS2/*_dna_cegma.completeness_report); do
        Strain=$(echo $File | rev | cut -f2 -d '/' | rev);
        Species=$(echo $File | rev | cut -f3 -d '/' | rev);
        printf "$Species\t$Strain\n";
        cat $File | head -n18 | tail -n+4;printf "\n";
    done > gene_pred/cegma/cegma_results_dna_summary.txt

    less gene_pred/cegma/cegma_results_dna_summary.txt
Gene prediction
Gene prediction was performed for the P. cactorum genome. Two gene prediction approaches were used:

Gene prediction using Braker1 Prediction of all putative ORFs in the genome using the ORF finder (atg.pl) approach.

Gene prediction 1 - Braker1 gene model training and prediction

Gene prediction was performed using Braker1.

First, RNAseq data was aligned to Fusarium genomes.

qc of RNA seq data was performed as part of sequencing the 10300 genome:
FileF=qc_rna/raw_rna/genbank/P.cactorum/F/SRR1206032_trim.fq.gz
FileR=qc_rna/raw_rna/genbank/P.cactorum/R/SRR1206033_trim.fq.gz
Aligning

  for Assembly in $(ls repeat_masked/*/*/filtered_contigs_repmask/*_contigs_unmasked.fa | grep -w -e '414'); do
    Strain=$(echo $Assembly| rev | cut -d '/' -f3 | rev)
    Organism=$(echo $Assembly | rev | cut -d '/' -f4 | rev)
    echo "$Organism - $Strain"
    for RNA in $(ls qc_rna/raw_rna/genbank/*/*/*_trim.fq.gz); do
      Timepoint=$(echo $RNA | rev | cut -f1 -d '/' | rev | sed 's/_trim.*//g')
      echo "$Timepoint"
      OutDir=alignment/$Organism/$Strain/$Timepoint
      ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/RNAseq
      qsub $ProgDir/tophat_alignment_unpaired.sh $Assembly $RNA $OutDir
    done
  done
Braker prediction

    for Assembly in $(ls repeat_masked/*/*/filtered_contigs_repmask/*_contigs_unmasked.fa | grep -w -e '414'); do
        Strain=$(echo $Assembly| rev | cut -d '/' -f3 | rev)
        Organism=$(echo $Assembly | rev | cut -d '/' -f4 | rev)
        echo "$Organism - $Strain"
        mkdir -p alignment/$Organism/$Strain/concatenated
        samtools merge -f alignment/$Organism/$Strain/concatenated/concatenated.bam \
      alignment/$Organism/$Strain/SRR1206032/accepted_hits.bam \
        alignment/$Organism/$Strain/SRR1206033/accepted_hits.bam
        OutDir=gene_pred/braker/$Organism/"$Strain"_braker_pacbio
        AcceptedHits=alignment/$Organism/$Strain/concatenated/concatenated.bam
        GeneModelName="$Organism"_"$Strain"_braker_pacbio
        rm -r /home/armita/prog/augustus-3.1/config/species/"$Organism"_"$Strain"_braker_pacbio
        ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/braker1
        qsub $ProgDir/sub_braker_fungi.sh $Assembly $OutDir $AcceptedHits $GeneModelName
    done
Supplimenting Braker gene models with CodingQuary genes

Additional genes were added to Braker gene predictions, using CodingQuary in pathogen mode to predict additional regions.

Firstly, aligned RNAseq data was assembled into transcripts using Cufflinks.

Note - cufflinks doesn't always predict direction of a transcript and therefore features can not be restricted by strand when they are intersected.

    for Assembly in $(ls repeat_masked/*/*/filtered_contigs_repmask/*_contigs_unmasked.fa | grep -w -e '414'); do
        Strain=$(echo $Assembly| rev | cut -d '/' -f3 | rev)
        Organism=$(echo $Assembly | rev | cut -d '/' -f4 | rev)
        echo "$Organism - $Strain"
        OutDir=gene_pred/cufflinks/$Organism/$Strain/concatenated
        mkdir -p $OutDir
        AcceptedHits=alignment/$Organism/$Strain/concatenated/concatenated.bam
        ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/RNAseq
        qsub $ProgDir/sub_cufflinks.sh $AcceptedHits $OutDir
    done
Secondly, genes were predicted using CodingQuary:

    for Assembly in $(ls repeat_masked/*/*/*/*_contigs_softmasked.fa | grep -w -e 'Fus2'); do
        Strain=$(echo $Assembly| rev | cut -d '/' -f3 | rev)
        Organism=$(echo $Assembly | rev | cut -d '/' -f4 | rev)
        echo "$Organism - $Strain"
        OutDir=gene_pred/codingquary/$Organism/$Strain
        CufflinksGTF=gene_pred/cufflinks/$Organism/$Strain/concatenated/transcripts.gtf
        ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/codingquary
        qsub $ProgDir/run_CQ-PM_unstranded_EMR.sh $Assembly $CufflinksGTF $OutDir
    done
Then, additional transcripts were added to Braker gene models, when CodingQuary genes were predicted in regions of the genome, not containing Braker gene models:

    # for BrakerGff in $(ls gene_pred/braker/F.*/*_braker_new/*/augustus.gff3 | grep -w -e 'Fus2'); do
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
done
