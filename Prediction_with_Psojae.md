#Phytophthora fragariae
Commands used to predict genes in Phytophthora fragariae using published RNAseq data from Phytophthora sojae
====================

All commands run in the directory:
/home/groups/harrisonlab/project_files/phytophthora_fragariae

#Download RNAseq data from SRA

```bash
cd raw_rna/genbank
mkdir -p P.sojae/P6497/F
mkdir -p P.sojae/P6497/R
cd P.sojae/P6497/F
fastq-dump SRR243567
cd ../R
cp /home/groups/harrisonlab/project_files/phytophthora_fragariae/raw_rna/genbank/P.cactorum/10300/R/SRR1206033.fastq
```

#1) QC

Perform qc of RNAseq zoospore data. These reads are not actually paired reads but this is irrelevant for processing using fast-mcf
Leaving a cactorum reverse read to allow the script to accept it, but shouldn't affect the output results
```bash
FileF=raw_rna/genbank/P.sojae/P6497/SRR243567.fastq
FileR=raw_rna/genbank/P.cactorum/10300/R/SRR1206033.fastq
IlluminaAdapters=/home/armita/git_repos/emr_repos/tools/seq_tools/ncbi_adapters.fa
qsub /home/armita/git_repos/emr_repos/tools/seq_tools/rna_qc/rna_qc_fastq-mcf.sh $FileF $FileR $IlluminaAdapters RNA
```

#2) Align reads vs. genome
Aligments of RNAseq reads were made against assemblies from each strain using tophat:

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/RNAseq
RNA=qc_rna/raw_rna/genbank/P.sojae/F/SRR243567_trim.fq.gz
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for Genome in $(ls assembly/spades/*/$Strain/filtered_contigs/*_500bp_renamed.fasta)
    do
        Strain=$(echo $Genome | rev | cut -d '/' -f3 | rev)
        Organism=$(echo $Genome | rev | cut -d '/' -f4 | rev)
        OutDir=alignment/sojae_test/$Organism/$Strain
        echo $Organism $Strain
        qsub $ProgDir/tophat_alignment_unpaired.sh $Genome $RNA $OutDir
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
    for Genome in $(ls repeat_masked/*/$Strain/filtered_contigs_repmask/*_contigs_unmasked.fa); do
        Organism=$(echo $Genome | rev | cut -d '/' -f4 | rev)
        OutDir=gene_pred/braker/sojae_test/$Organism/$Strain
        AcceptedHits=alignment/sojae_test/$Organism/$Strain/accepted_hits.bam
        GeneModelName="$Organism"_"$Strain"_braker
        echo $Strain
        echo $Organism
        echo $Genome
        qsub $ProgDir/sub_braker.sh $Genome $OutDir $AcceptedHits $GeneModelName
    done
done
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
