Initial analysis of RNA-Seq data was performed in RNA-Seq_analysis.md
this performs co-expression analyses and searches for potential promotor motifs.

# Four key stages of analysis to be performed

A) Building a coexpression network and export it
B) Counting kmers in the 3kb upstream region of all genes in the coexpressed set
C) Test these kmers for enrichment

## A) Building a coexpression network

The threshold for samples depends on the dataset,
make sure to sanity check with the output graph
cluster to keep may also need to be modified

```bash
OutDir=analysis/coexpression
mkdir -p $OutDir
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae/RNA_Seq_scripts
gene_table=gene_pred/annotation/P.fragariae/Bc16/Bc16_gene_table_incl_exp.tsv
$ProgDir/WGCNA_input_clean.R --gene_table $gene_table --out_dir $OutDir
```

```
40,675 genes were removed due to too many missing samples or zero variance.
Listed in analysis/coexpression/removed_genes.txt
The candidate Avr is not in this list, so it is not too strict about genes
with low expression in some samples
```

Test various values of soft thresholding for building the network

```bash
OutDir=analysis/coexpression
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae/RNA_Seq_scripts
qsub $ProgDir/sub_sft.sh $OutDir
```

```
scale-free topology fit index values seem to peak and then decline.
WGCNA tutorial recommends getting as close to 0.9 as possible,
but 16 has a value of x and is the highest reached before declining.
```

Build the coexpression network
Merging threshold value may need tweaking

```bash
OutDir=analysis/coexpression
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae/RNA_Seq_scripts
qsub $ProgDir/sub_create_network.sh $OutDir 16 30 0.25
```
