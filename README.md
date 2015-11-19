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
    mkdir -p /home/groups/harrisonlab/project_files/fusarium_ex_strawberry
    cd /home/groups/harrisonlab/project_files/fusarium_ex_strawberry
  	Species=F.oxysporum_fsp_fragariae
  	Strain=FeChina
    mkdir -p raw_dna/paired/fusarium_ex_strawberry/FeChina/F
    mkdir -p raw_dna/paired/fusarium_ex_strawberry/FeChina/R
    RawDat=/home/groups/harrisonlab/raw_data/raw_seq/raw_reads/150925_M01678_0029_AC669
    cp $RawDat/FeChina_S1_L001_R1_001.fastq.gz raw_dna/paired/fusarium_ex_strawberry/FeChina/F/.
    cp $RawDat/FeChina_S1_L001_R2_001.fastq.gz raw_dna/paired/fusarium_ex_strawberry/FeChina/R/.
```


#Data qc

programs: fastqc fastq-mcf kmc

Data quality was visualised using fastqc:

```bash
```

Trimming was performed on data to trim adapters from sequences and remove poor quality data.
This was done with fastq-mcf


```bash
```


Data quality was visualised once again following trimming:

```bash
```


kmer counting was performed using kmc.
This allowed estimation of sequencing depth and total genome size:

```bash
```

** Estimated Genome Size is: 8156187 

** Esimated Coverage is: 35

# Assembly
Assembly was performed using: Velvet / Abyss / Spades

## Velvet Assembly
A range of hash lengths were used and the best assembly selected for subsequent analysis

```bash
```

## Spades Assembly

```bash
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
