#In order to check for duplication of effectors in order to explain the large number of candidates from Maria's reciprocal BLAST, BLAST the putative target effectors against the BC-16 gene set

##Firstly extract fasta of gene sequence of targets from output from Maria's RBB

```bash
mkdir BLAST
cp /home/sobczm/popgen/other/phytophthora/RBB/Bc16_vs_Bc1.none BLAST/.
ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
headers=BLAST/Bc16_vs_Bc1.none
fasta=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors.gene.fasta
$ProgDir/extract_from_fasta.py --fasta $fasta --headers $headers > BLAST/putative_targets.fa
```

##Then, BLAST this fasta againt the BC-16 gene set to check for duplication
