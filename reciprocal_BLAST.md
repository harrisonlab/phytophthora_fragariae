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
