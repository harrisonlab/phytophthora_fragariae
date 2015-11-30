# phytophthora_fragariae
Commands used in the analysis of P. fragariae genomes
# fusarium_ex_strawberry
Commands used in the analysis of Fusarium oxysporum isolates ex. strawberry.

Fusarium oxysporum fsp. fragariae
====================

Commands used during analysis of the Fusarium oxysporum fsp. fragariae genome. Note - all this work was performed in the directory: /home/groups/harrisonlab/project_files/Fusarium oxysporum fsp. fragariae

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
```


#Data qc

programs: fastqc fastq-mcf kmc

Data quality was visualised using fastqc:

```bash
	for RawData in $(ls raw_dna/paired/P.fragariae/*/*/*.fastq.gz); do
		echo $RawData;
		ProgDir=/home/adamst/git_repos/tools/seq_tools/dna_qc;
		qsub $ProgDir/run_fastqc.sh $RawData;
	done
```

Trimming was performed on data to trim adapters from sequences and remove poor quality data.
This was done with fastq-mcf


```bash
	for Strain in "A4" "Bc23" "SCRP245_v2" "Nov5" "Nov77" "ONT3"; do
		echo $Strain
		Read_F=$(ls raw_dna/paired/P.fragariae/$Strain/F/*.fastq.gz)
		Read_R=$(ls raw_dna/paired/P.fragariae/$Strain/R/*.fastq.gz)
		IluminaAdapters=/home/adamst/git_repos/tools/seq_tools/ncbi_adapters.fa
		ProgDir=/home/adamst/git_repos/tools/seq_tools/rna_qc
		qsub $ProgDir/rna_qc_fastq-mcf.sh $Read_F $Read_R $IluminaAdapters DNA
	done
```


Data quality was visualised once again following trimming:

```bash
	for RawData in $(ls qc_dna/paired/P.fragariae/*/*/*.fq.gz); do
		echo $RawData;
		ProgDir=/home/adamst/git_repos/tools/seq_tools/dna_qc;
		qsub $ProgDir/run_fastqc.sh $RawData;
	done
```


kmer counting was performed using kmc.
This allowed estimation of sequencing depth and total genome size:

```bash  
	for Strain in "A4" "SCRP245_v2" "Bc23" "Nov5" "Nov77" "ONT3"; do
		echo $Strain;
		Trim_F=$(ls qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz);
		Trim_R=$(ls qc_dna/paired/P.fragariae/$Strain/R/*.fq.gz);
		ProgDir=/home/adamst/git_repos/tools/seq_tools/dna_qc;
		qsub $ProgDir/kmc_kmer_counting.sh $Trim_F $Trim_R;
	done
```

** Estimated Genome Size is:
A4: 93413554
SCRP245_v2: 127550025
Bc23: 103251773
Nov5: 95350039
Nov77: 92399813
ONT3: 103869049

** Esimated Coverage is:
A4: 23
SCRP245_v2: 23
Bc23: 24
Nov5: 25
Nov77: 30
ONT3: 26

# Assembly
Assembly was performed using: Spades

## Spades Assembly

```bash
	for Strain in A4 SCRP245_v2 Bc23 Nov5 Nov77 ONT3; do
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

##Spades Assembly failed for SCRP245_v2, hammer ran out of memory. Resubmitting as a single job

```bash
	Strain=SCRP245_v2
	F_Read=$(ls qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz)
	R_Read=$(ls qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz)
	CovCutoff='10'
	ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/spades
	Species=$(echo $F_Read | rev | cut -f4 -d '/' | rev)
	OutDir=assembly/spades/$Species/$Strain
	echo $Species
	echo $Strain
	qsub $ProgDir/submit_SPAdes.sh $F_Read $R_Read $OutDir correct $CovCutoff
```

##Previous code submitted a forward read as both forward and reverse reads, rejected by Spades. Code corrected and resubmitted.

```bash
	Strain=SCRP245_v2
	F_Read=$(ls qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz)
	R_Read=$(ls qc_dna/paired/P.fragariae/$Strain/R/*.fq.gz)
	CovCutoff='10'
	ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/spades
	Species=$(echo $F_Read | rev | cut -f4 -d '/' | rev)
	OutDir=assembly/spades/$Species/$Strain
	echo $Species
	echo $Strain
	qsub $ProgDir/submit_SPAdes.sh $F_Read $R_Read $OutDir correct $CovCutoff
```

## Filter the contigs

```bash
```
##Quast

```bash
```

-->
# Repeat masking
Repeat masking was performed and used the following programs: Repeatmasker Repeatmodeler

The best assembly was used to perform repeatmasking

```bash
 ```

** % bases masked by repeatmasker: 11.73%

** % bases masked by transposon psi: **


# Gene Prediction
Gene prediction followed two steps:
Pre-gene prediction - Quality of genome assemblies were assessed using Cegma to see how many core eukaryotic genes can be identified.
Gene models were used to predict genes in the fusarium genome. This used results from CEGMA as hints for gene models.

## Pre-gene prediction
Quality of genome assemblies was assessed by looking for the gene space in the assemblies.

```bash
```

** Number of cegma genes present and complete: 95.16
** Number of cegma genes present and partial: 97.18

##Gene prediction

Gene prediction was performed for the neonectria genome.
CEGMA genes were used as Hints for the location of CDS.

```bash
```

** Number of genes predicted: 12712


#Functional annotation

A)Interproscan
Interproscan was used to give gene models functional annotations.

```bash
```

```bash
```
B) SwissProt

```bash
```

#Genomic analysis
The first analysis was based upon BLAST searches for genes known to be involved in toxin production


##Genes with homology to PHIbase
Predicted gene models were searched against the PHIbase database using tBLASTx.

```bash
```

Top BLAST hits were used to annotate gene models.

The second analysis was based upon BLAST searches for genes known to be SIX genes 


##Genes with homology to SIX genes
Predicted gene models were searched against the SIX genes database using tBLASTx.

```bash
```

##Mimps

The presence of Mimp promotors in Fusarium genomes were identified. This was done in three steps:
•Position of Mimps were identified in the genome
•Genes within 1000bp downstream of the mimp were identified from Augustus predictions
•ORFs within 1000bp downstream of the mimp were identified from ORF predictions

A) Position of Mimps were identified

Position of Mimps gff predictions for the position of mimps in the genome were identified Fus2 was performed separately to ensure mimps are predicted from the correct assembly

```bash
```
B) Augustus genes flanking Mimps

```bash
```
<!--
