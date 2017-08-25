#BLASTs the 205 high confidence RxLRs, merged with the expressed low confidence RxLRs.

##Create a fasta file of the genes required for BLAST

Merge header files together in new folder and create fasta file

```bash
NewDir=analysis/reciprocal_BLAST/
mkdir -p $NewDir
WorkDir=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/
cat $WorkDir/Bc16_total_RxLR_EER_headers.txt > $NewDir/Bc16_RxLRs_headers.txt
cat $WorkDir/Bc16_expressed_low_confidence_RxLRs.txt | sed 's/.t1//g' >> $NewDir/Bc16_RxLRs_headers.txt
GeneDir=gene_pred/annotation/P.fragariae/Bc16/
ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
$ProgDir/extract_from_fasta.py --fasta $GeneDir/Bc16_genes_incl_ORFeffectors.gene.fasta --headers $NewDir/Bc16_RxLRs_headers.txt > $NewDir/Bc16_RxLRs.fa
```

##Create BLAST databases for race 1 and race 3

```bash
WorkDir=analysis/reciprocal_BLAST
for Strain in Nov5 Bc1
do
    Assembly=repeat_masked/P.fragariae/$Strain/deconseq_Paen_repmask/"$Strain"_contigs_unmasked.fa
    cat $Assembly | sed "s/>/>"$Strain"_/g" >> $WorkDir/UK1_genomes.fa
done
```

```bash
WorkDir=analysis/reciprocal_BLAST
for Strain in Nov71 Nov9 Nov27
do
    Assembly=repeat_masked/P.fragariae/$Strain/deconseq_Paen_repmask/"$Strain"_contigs_unmasked.fa
    cat $Assembly | sed "s/>/>"$Strain"_/g" >> $WorkDir/UK3_genomes.fa
done
```

##Create databases from these sequences

```bash
WorkDir=analysis/reciprocal_BLAST
cd $WorkDir
makeblastdb -in UK1_genomes.fa -dbtype 'nucl' -out UK1_genomes
makeblastdb -in UK3_genomes.fa -dbtype 'nucl' -out UK3_genomes
```

##Run blastn search in a screen session with a qlogin

```bash
screen -a

qlogin -pe smp 8

WorkDir=/home/groups/harrisonlab/project_files/phytophthora_fragariae/analysis/reciprocal_BLAST
cd $WorkDir
blastn -db UK1_genomes -query Bc16_RxLRs.fa -out RxLRs_vs_UK1.tbl -evalue 1e-10 -outfmt 6 -num_threads 8
blastn -db UK3_genomes -query Bc16_RxLRs.fa -out RxLRs_vs_UK3.tbl -evalue 1e-10 -outfmt 6 -num_threads 8
```
