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
Gives 195 before merging, 136 afterwards
Reducing the merging threshold to 0.05:
Gives 189 modules.

With a minimum size of 30:
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
Target in lightcoral, with 205 genes
Target in palevioletred3 before merging, with 115 genes
Reducing the merging threshold to 0.05:
Keeps it in palevioletred3 with 115 genes

With a minimum size of 30:
Before merging, g24882.t1 is in the steelblue network, with 212 other genes
After merging with a threshold of 0.05:
g24882.t1 is in the steelblue network, with 212 other genes
After merging with a threshold of 0.10:
g24882.t1 is in the steelblue network, with 212 other genes
After merging with a threshold of 0.15:
g24882.t1 is in the steelblue network, with 212 other genes
After merging with a threshold of 0.25:
g24882.t1 is in the darkolivegreen network, with 953 other genes

Decided on a minimum module size of 5, with a merging threshold of 0.05
```

Export network for external visualisation with Cytoscape
<http://www.cytoscape.org/?gclid=CjwKCAjws6jVBRBZEiwAkIfZ2lpzRXx8WFD-1wk-tD4KOHW6ZIafetKcptpSIfnyc82PDbFt83h9HBoCtjEQAvD_BwE>

```bash
OutDir=analysis/coexpression
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae/RNA_Seq_scripts
Module=palevioletred3
qsub $ProgDir/sub_export_network_cytoscape.sh $OutDir $Module
```

Genes from the module were visually inspected for promotor hunting
This gave 11 high confidence genes and 22 lower confidence genes
Also analyse all genes with an fpkm value above 9,000
in at least one BC-16 timepoint, 10 genes

Extract the 3000 bases upstream of these genes

```bash
for Headers in $(ls promotor_id/*genes.txt)
do
    Sequences=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors.upstream3000.fasta
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    OutDir=promotor_id
    File_ID=$(echo $Headers | cut -f2 -d '/' | cut -f1 -d '_')
    $ProgDir/extract_from_fasta.py --fasta $Sequences --headers $Headers > $OutDir/"$File_ID"_upstream3000.fasta
done
```

Convert all bases to uppercase

```bash
for input in $(ls promotor_id/*.fasta)
do
    filename=$(echo $input | cut -f1 -d '.')
    input_modified="$filename"_modified.fasta
    cat $input | awk 'BEGIN{FS=" "}{if(!/>/){print toupper($0)}else{print $1}}' \
    > $input_modified
    rm $input
    mv $input_modified $input
done
```

Remove duplicate genes

```bash
for input in $(ls promotor_id/*.fasta)
do
    filename=$(echo $input | cut -f1 -d '.')
    input_modified="$filename"_modified.fasta
    awk 'BEGIN{RS=">"}NR>1{sub("\n","\t"); gsub("\n",""); print RS$0}' $input | awk '!seen[$1]++' | awk -v OFS="\n" '{print $1,$2}' > $input_modified
    rm $input
    mv $input_modified $input
done
```

## B) Identifying novel motifs using DREME

### Set up files

Organise directories and create files for a comparison set to sample from

```bash
for Set in all highconfidence highexpressed
do
    mkdir -p promotor_id/$Set
    mv promotor_id/"$Set"_genes.txt promotor_id/$Set/.
    mv promotor_id/"$Set"_upstream3000.fasta promotor_id/$Set/.
    cat promotor_id/Total_Gene_Set.txt | grep -vf promotor_id/$Set/"$Set"_genes.txt > promotor_id/$Set/"$Set"_nontarget.txt
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    Fasta=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors.upstream3000.fasta
    Headers=promotor_id/$Set/"$Set"_nontarget.txt
    Output=promotor_id/$Set/"$Set"_nontarget_upstream3000.fasta
    echo "Extracting fasta for $Set"
    $ProgDir/extract_from_fasta.py --fasta $Fasta --headers $Headers > $Output
    echo "$Set done"
done
```

Split fasta file into 100bp sequences

Before running, install pyfasta

```bash
pip install https://pypi.python.org/packages/be/3f/794fbcdaaa2113f0a1d16a962463896c1a6bdab77bd63f33a8f16aae6cdc/pyfasta-0.5.2.tar.gz --user
```

To use this module, add the following line to your profile

```bash
export PYTHONPATH="$PYTHONPATH:/home/adamst/.local/lib/python2.7/site-packages"
export PATH=${PATH}:/home/adamst/.local/bin
```

Now split target files into 100bp sequences

```bash
for Set in all highconfidence highexpressed
do
    WorkDir=promotor_id/$Set
    Fasta=$WorkDir/"$Set"_upstream3000.fasta
    pyfasta split -n 1 -k 100 $Fasta
done
```

Convert all bases to uppercase in non-target files

```bash
for Set in all highconfidence highexpressed
do
    for input in $(ls promotor_id/$Set/"$Set"_nontarget_upstream3000.fasta)
    do
        filename=$(echo $input | cut -f1 -d '.')
        input_modified="$filename"_modified.fasta
        cat $input | awk 'BEGIN{FS=" "}{if(!/>/){print toupper($0)}else{print $1}}' \
        > $input_modified
        rm $input
        mv $input_modified $input
    done
done
```

Remove duplicate genes in non-target files

```bash
for Set in all highconfidence highexpressed
do
    for input in $(ls promotor_id/$Set/"$Set"_nontarget_upstream3000.fasta)
    do
        filename=$(echo $input | cut -f1 -d '.')
        input_modified="$filename"_modified.fasta
        awk 'BEGIN{RS=">"}NR>1{sub("\n","\t"); gsub("\n",""); print RS$0}' $input | awk '!seen[$1]++' | awk -v OFS="\n" '{print $1,$2}' > $input_modified
        rm $input
        mv $input_modified $input
    done
done
```

Now split non-target files into 100bp sequences

```bash
for Set in all highconfidence highexpressed
do
    WorkDir=promotor_id/$Set
    Fasta=$WorkDir/"$Set"_nontarget_upstream3000.fasta
    pyfasta split -n 1 -k 100 $Fasta
done
```

### Create negative samples for each set

```bash
for Set in all highconfidence highexpressed
do
    for Rep in {1..100}
    do
        WorkDir=promotor_id/$Set
        Pos_Fasta=$WorkDir/"$Set"_upstream3000.split.100mer.fasta
        Neg_Fasta=$WorkDir/"$Set"_nontarget_upstream3000.split.100mer.fasta
        Num_of_Seqs=$(cat $Pos_Fasta | grep '>' | wc -l)
        ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae/RNA_Seq_scripts
        OutDir=/data/scratch/adamst/$Set
        mkdir -p $OutDir
        Jobs=$(qstat | grep 'sub_fasta' | wc -l)
        while [ $Jobs -gt 20 ]
        do
            sleep 1
            printf "."
            Jobs=$(qstat | grep 'sub_fasta' | wc -l)
        done
        qsub $ProgDir/sub_fasta_subsample.sh $Neg_Fasta $Num_of_Seqs $Rep $OutDir
    done
done
```

### DREME motif analysis

fifth command line argument is e-value, default and recommended is 0.05
Increasing will provide more motifs, but they may not be significantly enriched

```bash
for Rep in {1..100}
do
    for Set in all highconfidence highexpressed
    do
        WorkDir=promotor_id/$Set
        NegDir=/data/scratch/adamst/$Set
        Positive=$WorkDir/"$Set"_upstream3000.split.100mer.fasta
        Negative=$NegDir/"$Set"_nontarget_upstream3000.split.100mer_random_*_"$Rep".fasta
        ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae/RNA_Seq_scripts
        Jobs=$(qstat | grep 'sub_dreme' | wc -l)
        while [ $Jobs -gt 20 ]
        do
            sleep 1
            printf "."
            Jobs=$(qstat | grep 'sub_dreme' | wc -l)
        done
        qsub $ProgDir/sub_dreme.sh $Positive $Negative $NegDir $Rep 0.25
    done
done
```

Combine results from multiple repeats

```bash
for Set in all highconfidence highexpressed
do
    OutDir=promotor_id/$Set
    DremeDir=/data/scratch/adamst/$Set
    DremeRes=$DremeDir/*dreme*/dreme.txt
    Percentage=90
    OutDir=promotor_id/$Set
    ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae/RNA_Seq_scripts
    python $ProgDir/Combine_DREME_Repeats.py --inputs $DremeRes \
    --percentage $Percentage --outdir $OutDir
done
```

Nothing can be reproducibly pulled out, possibly due to the small input sample size

## Investigate enrichment of effector class genes in co-expression modules
