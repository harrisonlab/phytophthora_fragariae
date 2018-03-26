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
qsub $ProgDir/sub_WGCNA_input_clean.sh $gene_table $OutDir
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
qsub $ProgDir/sub_choose_softthreshold.sh $OutDir
```

```
scale-free topology fit index values seem to peak and then decline.
WGCNA tutorial recommends getting as close to 0.9 as possible,
but 15 has a value of 0.8340 and is the highest reached before declining.
```

Build the coexpression network
Merging threshold value may need tweaking

```bash
OutDir=analysis/coexpression
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae/RNA_Seq_scripts
qsub $ProgDir/sub_create_network.sh $OutDir 15 30 0.25
```

```
Reducing the minimum module size to 5, with a merging threshold of 0.1:
Gives 159 before merging, 136 afterwards
103 modules were created before merging
101 modules were created after merging with a threshold of 0.05
74 modules were created after merging with a threshold of 0.10
54 modules were created after merging with a threshold of 0.15
30 modules were created after merging with a threshold of 0.25
```

Export gene lists

Y or N denotes whether unmerged modules will be exported too

```bash
OutDir=analysis/coexpression
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae/RNA_Seq_scripts
qsub $ProgDir/sub_Export_Gene_Lists.sh $OutDir Y
```

```
Reducing the minimum module size to 5, with a merging threshold of 0.1:
Target in lightcoral, with 205 genes, or palevioletred3 before merging, with 115 genes.
Before merging, g24882.t1 is in the steelblue network, with 212 other genes
After merging with a threshold of 0.05:
g24882.t1 is in the steelblue network, with 212 other genes
After merging with a threshold of 0.10:
g24882.t1 is in the steelblue network, with 212 other genes
After merging with a threshold of 0.15:
g24882.t1 is in the steelblue network, with 212 other genes
After merging with a threshold of 0.25:
g24882.t1 is in the darkolivegreen network, with 953 other genes

0.10 seems the most appropriate as a threshold
```

Export network for external visualisation with Cytoscape
<http://www.cytoscape.org/?gclid=CjwKCAjws6jVBRBZEiwAkIfZ2lpzRXx8WFD-1wk-tD4KOHW6ZIafetKcptpSIfnyc82PDbFt83h9HBoCtjEQAvD_BwE>

```bash
OutDir=analysis/coexpression
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae/RNA_Seq_scripts
Module=steelblue
qsub $ProgDir/sub_export_network_cytoscape.sh $OutDir $Module
```
