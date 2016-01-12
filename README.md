# phytophthora_fragariae
Commands used in the analysis of P. fragariae genomes
A4, Bc23, Nov5, Nov77, ONT3 and SCRP245_v2
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

##Quast

```bash
for Strain in A4 SCRP245_v2 Bc23 Nov5 Nov77 ONT3; do
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

##QUAST used to summarise assembly statistics

```bash
ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/assemblers/assembly_qc/quast
for Assembly in $(ls assembly/spades/*/*/filtered_contigs/*_500bp_renamed.fasta); do
	Strain=$(echo $Assembly | rev | cut -d '/' -f3 | rev)
	Organism=$(echo $Assembly | rev | cut -d '/' -f4 | rev)
	OutDir=assembly/spades/$Organism/$Strain/filtered_contigs
	qsub $ProgDir/sub_quast.sh $Assembly $OutDir
done
```

-->
# Repeat masking
Repeat masking was performed and used the following programs: Repeatmasker Repeatmodeler

The best assembly was used to perform repeatmasking

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/repeat_masking
for BestAss in $(ls assembly/spades/*/*/filtered_contigs/*_500bp_renamed.fasta); do
	echo $BestAss
	qsub $ProgDir/rep_modeling.sh $BestAss
done
 ```
 
```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/repeat_masking
for BestAss in $(ls assembly/spades/*/*/filtered_contigs/*_500bp_renamed.fasta); do
	echo $BestAss
	qsub $ProgDir/transposonPSI.sh $BestAss
done
 ``` 

** % bases masked by repeatmasker: 
A4: 33.90%
Bc23: 21.63%
Nov5: 31.91%
Nov77: 31.54%
ONT3: 29.92%
SCRP245_v2: 21.14% **

Summary for transposonPSI output:

```bash
Organism=P.fragariae
for Strain in A4 SCRP245_v2 Bc23 Nov5 Nov77 ONT3; do
	RepDir=repeat_masked/$Organism/$Strain/filtered_contigs_repmask
	TransPSIGff=$(ls $RepDir/*_contigs_unmasked.fa.TPSI.allHits.chains.gff3)
	echo $Strain
	printf "The number of bases masked by TransposonPSI:\t"
	sortBed -i $TransPSIGff > $RepDir/TPSI_sorted.bed
	bedtools merge -i $RepDir/TPSI_sorted.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
	rm $RepDir/TPSI_sorted.bed
done
```
	
** % bases masked by transposon psi:
A4: 0.83%
Bc23: 6.76% 
Nov5: 8.00%
Nov77: 8.01%
ONT3: 7.29%
SCRP245_v2: 6.37%**


# Gene Prediction
Gene prediction followed two steps:
Pre-gene prediction - Quality of genome assemblies were assessed using Cegma to see how many core eukaryotic genes can be identified.
Gene models were used to predict genes in the fusarium genome. This used results from CEGMA as hints for gene models.

## Pre-gene prediction
Quality of genome assemblies was assessed by looking for the gene space in the assemblies.

```bash
ProgDir=/home/adamst/git_repos/tools/gene_prediction/cegma
for BestAss in $(ls assembly/spades/*/*/filtered_contigs/*_500bp_renamed.fasta); do
	echo $BestAss
	qsub $ProgDir/sub_cegma.sh $BestAss dna
done
```

** Number of cegma genes present and complete: 
A4: 94.35%
Bc23: 94.76%
Nov5: 95.16%
Nov77: 94.35%
ONT3: 94.76%
SCRP245_v2: 93.95% **

** Number of cegma genes present and partial:
A4: 97.98%
Bc23: 96.77%
Nov5: 97.18%
Nov77: 96.37%
ONT3: 97.18%
SCRP245_v2: 96.37% **

##Gene prediction

Copy over RNA seq data for P. cactorum 10300

```bash
RawDatDir=/home/groups/harrisonlab/project_files/idris/raw_rna/genbank/P.cactorum/10300
ProjectDir=/home/groups/harrisonlab/project_files/phytophthora_fragariae/
mkdir -p $ProjectDir/raw_rna/genbank/P.cactorum/10300/F
mkdir -p $ProjectDir/raw_rna/genbank/P.cactorum/10300/R
cp $RawDatDir/SRR1206032.fastq $ProjectDir/raw_rna/genbank/P.cactorum/10300/F
cp $RawDatDir/SRR1206033.fastq $ProjectDir/raw_rna/genbank/P.cactorum/10300/R
```

##1) QC

Perform qc of RNAseq timecourse data. These reads are not actually paired reads but this is irrelevant for processing using fast-mcf

```bash
FileF=raw_rna/genbank/P.cactorum/10300/F/SRR1206032.fastq
FileR=raw_rna/genbank/P.cactorum/10300/R/SRR1206033.fastq
IlluminaAdapters=/home/armita/git_repos/emr_repos/tools/seq_tools/ncbi_adapters.fa
qsub /home/armita/git_repos/emr_repos/tools/seq_tools/rna_qc/rna_qc_fastq-mcf.sh $FileF $FileR $IlluminaAdapters RNA
```

##2) Align reads vs. genome
Aligments of RNAseq reads were made against assemblies from each strain using tophat:

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/RNAseq
FileF=qc_rna/genbank/P.cactorum/10300/F/SRR1206032_trim.fq.gz
FileR=qc_rna/genbank/P.cactorum/10300/R/SRR1206033_trim.fq.gz
for Genome in $(ls assembly/spades/*/*/filtered_contigs/*_500bp_renamed.fasta); do
	Strain=$(echo $Genome | rev | cut -d '/' -f3 | rev)
	Organism=$(echo $Genome | rev | cut -d '/' -f4 | rev)
	OutDir=alignment/$Organism/$Strain
	echo $Organism $Strain
	qsub $ProgDir/tophat_alignment.sh $Genome $FileF $FileR $OutDir
done
```

Alignment files were merged into a single file so as to be passed to a gene prediction program to indicate the location of aligned RNAseq data against a particular genome.

<!-- 
```bash
for StrainDir in $(ls -d alignment/*/*); do
	Strain=$(echo $StrainDir | rev | cut -d '/' -f1 | rev)
	ls alignment/*/$Strain/accepted_hits.bam > bamlist.txt
	mkdir -p $StrainDir/merged
	bamtools merge -list bamlist.txt -out $StrainDir/merged
done
```
 -->

##3) Run Braker1

As this is the first time I have run Braker I need to copy the licence key for genemarkET
to my user directory

```bash
cp /home/armita/.gm_key ~/.gm_key
```

```bash
ProgDir=/home/adamst/git_repos/tools/gene_prediction/braker1
for Genome in $(ls repeat_masked/*/*/filtered_contigs_repmask/*_contigs_unmasked.fa); do
	Strain=$(echo $Genome| rev | cut -d '/' -f3 | rev)
	Organism=$(echo $Genome | rev | cut -d '/' -f4 | rev)
	OutDir=gene_pred/braker/$Organism/$Strain
	AcceptedHits=alignment/$Organism/$Strain/accepted_hits.bam
	GeneModelName="$Organism"_"$Strain"_braker
	qsub $ProgDir/sub_braker.sh $Genome $OutDir $AcceptedHits $GeneModelName
done
```

##4) Extract gff and amino acid sequences

```bash
for File in $(ls gene_pred/braker/*/*/*_braker/augustus.gff); do
	getAnnoFasta.pl $File
	OutDir=$(dirname $File)
	echo "##gff-version 3" > $OutDir/augustus_extracted.gff
	cat $File | grep -v '#' >> $OutDir/augustus_extracted.gff
done
```bash

##Use atg.pl to predict all ORFs

This uses the atg.pl script to identify all ORFs in the genome. These can then be used to look for RxLRs and signal peptides.

```bash
ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder 
for Genome in $(ls assembly/spades/*/*/filtered_contigs/*_500bp_renamed.fasta); do
	qsub $ProgDir/run_ORF_finder.sh $Genome
done
```

#Functional annotation

A)Interproscan
Interproscan was used to give gene models functional annotations.

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/interproscan/
for Strain in A4 SCRP245_v2 Bc23 Nov5 Nov77 ONT3; do
	Genes=gene_pred/braker/P.fragariae/$Strain/P.*/augustus.aa
	$ProgDir/sub_interproscan.sh $Genes
done
```

```bash
```
B) SwissProt

```bash
```

#Genomic analysis

##RxLR genes

A) From Braker1 gene models - signal peptide and RxLR motif

Required programs:

SigP
biopython

Proteins that were predicted to contain signal peptides were identified using the following commands: 


```bash
for Proteome in $(ls gene_pred/braker/*/*/*/augustus.aa); do
    echo "$Proteome"
    SplitfileDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
    Strain=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
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
```
This produces batch files. They need to be combined into a single file for each strain using the following commands:

```bash
for SplitDir in $(ls -d gene_pred/braker_split/P.*/*); do
	Strain=$(echo $SplitDir | rev | cut -d '/' -f1 | rev)
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
```
The RxLR_EER_regex_finder.py script was used to search for this regular expression R.LR.{,40}[ED][ED][KR] and annotate the EER domain where present. Done separate for each strain.

```bash
for Secretome in $(ls gene_pred/braker_sigP/*/*/*braker_sp.aa); do
	ProgDir=/home/adamst/git_repos/tools/pathogen/RxLR_effectors;
	Strain=$(echo $Secretome | rev | cut -d '/' -f2 | rev);
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
```

```
strain: A4	species: P.fragariae
the number of SigP gene is:	2432
the number of SigP-RxLR genes are:	291
the number of SigP-RxLR-EER genes are:	170


strain: Bc23	species: P.fragariae
the number of SigP gene is:	2194
the number of SigP-RxLR genes are:	284
the number of SigP-RxLR-EER genes are:	166


strain: Nov5	species: P.fragariae
the number of SigP gene is:	2561
the number of SigP-RxLR genes are:	308
the number of SigP-RxLR-EER genes are:	180


strain: Nov77	species: P.fragariae
the number of SigP gene is:	2489
the number of SigP-RxLR genes are:	289
the number of SigP-RxLR-EER genes are:	165


strain: ONT3	species: P.fragariae
the number of SigP gene is:	3149
the number of SigP-RxLR genes are:	297
the number of SigP-RxLR-EER genes are:	174


strain: SCRP245_v2	species: P.fragariae
the number of SigP gene is:	2544
the number of SigP-RxLR genes are:	286
the number of SigP-RxLR-EER genes are:	156
```

##B) From braker1 gene models - Hmm evidence for WY domains

Hmm models for the WY domain contained in many RxLRs were used to search gene models predicted with Braker1. These were run with the following commands:

```
ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer
HmmModel=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer/WY_motif.hmm
for Proteome in $(ls gene_pred/braker/*/*/*/augustus.aa); do
	Strain=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
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
```

##C) From Braker1 gene models - Hmm evidence of RxLR effectors

```
for Proteome in $(ls gene_pred/braker/*/*/*/augustus.aa); do
	ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer
	HmmModel=/home/armita/git_repos/emr_repos/SI_Whisson_et_al_2007/cropped.hmm
	Strain=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
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
		# # ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/feature_annotation
		# Col2=cropped.hmm
		# GeneModels=$(ls assembly/external_group/P.*/$Strain/pep/*.gff*)
		# # $ProgDir/gene_list_to_gff.pl $OutDir/$Headers $GeneModels $Col2 Name > $OutDir/"$Strain"_pub_RxLR_hmmer.gff3
		# cat $GeneModels | grep -w -f $OutDir/$Headers > $OutDir/"$Strain"_pub_RxLR_hmmer.gff3
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
```

##D) From Braker1 gene models - Hmm evidence of CRN effectors

A hmm model relating to crinkler domains was used to identify putative crinklers in Augustus gene models. This was done with the following commands:

```
ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer
HmmModel=/home/adamst/git_repos/scripts/phytophthora/pathogen/hmmer/Phyt_annot_CRNs_D1.hmm
for Proteome in $(ls gene_pred/braker/*/*/*/augustus.aa); do
	Strain=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
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
```

##E) From ORF gene models - Signal peptide & RxLR motif

Required programs:

SigP
biopython

Proteins that were predicted to contain signal peptides were identified using the following commands:

```
for Proteome in $(ls gene_pred/ORF_finder/*/*/*.aa_cat.fa); do
	echo "$Proteome"
	SplitfileDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
	ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
	Strain=$(echo $Proteome | rev | cut -f2 -d '/' | rev)
	Organism=$(echo $Proteome | rev | cut -f3 -d '/' | rev)
	SplitDir=gene_pred/ORF_split/$Organism/$Strain
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
```
The batch files of predicted secreted proteins needed to be combined into a single file for each strain. This was done with the following commands:
```
for SplitDir in $(ls -d gene_pred/ORF_split/P.*/*); do
	Strain=$(echo $SplitDir | rev | cut -d '/' -f1 | rev)
	Organism=$(echo $SplitDir | rev | cut -d '/' -f2 | rev)
	InStringAA=''
	InStringNeg=''
	InStringTab=''
	InStringTxt=''
	for GRP in $(ls -l $SplitDir/*_ORF_preds_*.fa | rev | cut -d '_' -f1 | rev | sort -n); do  
		InStringAA="$InStringAA gene_pred/ORF_sigP/$Organism/$Strain/split/"$Organism"_"$Strain"_ORF_preds_$GRP""_sp.aa";  
		InStringNeg="$InStringNeg gene_pred/ORF_sigP/$Organism/$Strain/split/"$Organism"_"$Strain"_ORF_preds_$GRP""_sp_neg.aa";  
		InStringTab="$InStringTab gene_pred/ORF_sigP/$Organism/$Strain/split/"$Organism"_"$Strain"_ORF_preds_$GRP""_sp.tab";
		InStringTxt="$InStringTxt gene_pred/ORF_sigP/$Organism/$Strain/split/"$Organism"_"$Strain"_ORF_preds_$GRP""_sp.txt";  
	done
	cat $InStringAA > gene_pred/ORF_sigP/$Organism/$Strain/"$Strain"_ORF_sp.aa
	cat $InStringNeg > gene_pred/ORF_sigP/$Organism/$Strain/"$Strain"_ORF_neg_sp.aa
	tail -n +2 -q $InStringTab > gene_pred/ORF_sigP/$Organism/$Strain/"$Strain"_ORF_sp.tab
	cat $InStringTxt > gene_pred/ORF_sigP/$Organism/$Strain/"$Strain"_ORF_sp.txt
done
```