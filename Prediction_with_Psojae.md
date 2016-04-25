#Phytophthora fragariae
Commands used to predict genes in Phytophthora fragariae using published RNAseq data from Phytophthora sojae
Alignment fails so cannot run gene prediction
====================

All commands run in the directory:
/home/groups/harrisonlab/project_files/phytophthora_fragariae

Multiple RNAseq files tried

#Download RNAseq data from SRA

Zoospores

```bash
cd raw_rna/genbank
mkdir -p P.sojae/P6497/F
cd P.sojae/P6497/F
fastq-dump SRR243567
```

Infection site after 1.5 hrs

```bash
cd raw_rna/genbank
mkdir -p P.sojae/P6497_90min/F
cd P.sojae/P6497_90min/F
fastq-dump SRR243570
```

Infection site after 3hrs

```bash
cd raw_rna/genbank
mkdir -p P.sojae/P6497_3hr/F
cd P.sojae/P6497_3hr/F
fastq-dump SRR243571
```

Infection site after 6hrs

```bash
cd raw_rna/genbank
mkdir -p P.sojae/P6497_6hr/F
cd P.sojae/P6497_6hr/F
fastq-dump SRR243572
```

```
Error downloading file, repeats multiple times
```

Infection site after 12hrs

```bash
cd raw_rna/genbank
mkdir -p P.sojae/P6497_12hr/F
cd P.sojae/P6497_12hr/F
fastq-dump SRR243573
```

Infections site after 24hrs

```bash
cd raw_rna/genbank
mkdir -p P.sojae/P6497_24hr/F
cd P.sojae/P6497_24hr/F
fastq-dump SRR243574
```

#1) QC

Perform qc of RNAseq zoospore data. These reads are not actually paired reads but this is irrelevant for processing using fast-mcf
Leaving a cactorum reverse read to allow the script to accept it, but shouldn't affect the output results

```bash
for Point in 90min 3hr 6hr 12hr 24hr
do
    FileF=raw_rna/genbank/P.sojae/P6497_"$Point"/F/*
    IlluminaAdapters=/home/armita/git_repos/emr_repos/tools/seq_tools/ncbi_adapters.fa
    qsub /home/adamst/git_repos/scripts/phytophthora_fragariae/fastqc.sh $FileF $IlluminaAdapters RNA
done
```

#2) Align reads vs. genome
Aligments of RNAseq reads were made against assemblies from each strain using tophat:

```bash
for Point in 90min 3hr 6hr 12hr 24hr
do
    ProgDir=/home/adamst/git_repos/tools/seq_tools/RNAseq
    RNA=qc_rna/genbank/P.sojae/P6497_"$Point"/F/*
    for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
    do
        for Genome in $(ls assembly/spades/*/$Strain/filtered_contigs/*_500bp_renamed.fasta)
        do
            Strain=$(echo $Genome | rev | cut -d '/' -f3 | rev)
            Organism=$(echo $Genome | rev | cut -d '/' -f4 | rev)
            OutDir=alignment/sojae_test/$Point/$Organism/$Strain
            echo $Organism $Strain
            qsub $ProgDir/tophat_alignment_unpaired.sh $Genome $RNA $OutDir
        done
    done
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

#3) Run Braker1

```bash
ProgDir=/home/adamst/git_repos/tools/gene_prediction/braker1
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for Genome in $(ls repeat_masked/*/$Strain/filtered_contigs_repmask/*_contigs_unmasked.fa)
    do
        Organism=$(echo $Genome | rev | cut -d '/' -f4 | rev)
        OutDir=gene_pred/braker/sojae_test/24hr/$Organism/$Strain
        AcceptedHits=alignment/sojae_test/24hr/$Organism/$Strain/accepted_hits.bam
        GeneModelName="$Organism"_"$Strain"_braker
        echo $Strain
        echo $Organism
        echo $Genome
        qsub $ProgDir/sub_braker.sh $Genome $OutDir $AcceptedHits $GeneModelName
    done
done
```

```
Fails for all data, perhaps poor RNAseq data
```

#4) Extract gff and amino acid sequences

```bash
for Strain in Bc1 Bc16 Nov9; do
    for File in $(ls gene_pred/braker/*/$Strain/*_braker/augustus.gff); do
        getAnnoFasta.pl $File
        OutDir=$(dirname $File)
        echo "##gff-version 3" > $OutDir/augustus_extracted.gff
        cat $File | grep -v '#' >> $OutDir/augustus_extracted.gff
    done
done
```
