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

Create a file for the upstream regions of non-target genes
These are used as the control when testing for significant enrichment

Create lists of genes to extract

```bash
# Create list of all IDs to search against

File=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors.upstream3000.fasta
cat $File | grep '>' | sed 's/>//g' | tr -d '>' | tr -d ' ' | sort | uniq > promotor_id/Total_Gene_Set.txt

# Create lists of genes to use as comparison set

for File in $(ls promotor_id/*_genes.txt)
do
    Prefix=$(echo $File | cut -f2 -d '/' | cut -f1 -d '_')
    OutDir=promotor_id
    Output="$Prefix"_comparison_set.txt
    TotalSet=promotor_id/Total_Gene_Set.txt
    cat $TotalSet | grep -v -f $File > "$OutDir"/"$Output"
done
```

Extract fastas of gene sets

```bash
for Headers in $(ls promotor_id/*comparison_set.txt)
do
    Sequences=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors.upstream3000.fasta
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    OutDir=promotor_id
    File_ID=$(echo $Headers | cut -f2 -d '/' | cut -f1 -d '_')
    $ProgDir/extract_from_fasta.py --fasta $Sequences --headers $Headers > $OutDir/"$File_ID"_comparison_set_upstream3000.fasta
done
```

Convert all bases to uppercase, my be causing issues with creating index files

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

## B) Counting kmers with dsm-framework

Before running add the following line to your profile:

```bash
export DSM_FRAMEWORK_PATH=/home/adamst/prog/dsm-framework
```

### B.1) Pre-processing of fasta files

```bash
for File in $(ls promotor_id/*.fasta)
do
    ProgDir=/home/adamst/git_repos/tools/seq_tools/kmer_enrichment
    File_ID=$(echo $File | cut -f2 -d "/")
    qsub $ProgDir/sub_dsm_preprocessing.sh $File
done
```

### B.2) Initialise server

Create text file containing the names of input files

```bash
for Set in all all_comparison_set highconfidence highconfidence_comparison_set \
highexpressed highexpressed_comparison_set
do
    Name="$Set"_upstream3000
    Txt_File=sample-names_"$Set".txt
    WorkDir=promotor_id
    echo $Name > $WorkDir/$Txt_File
done
```

Ensure that the fasta, fmi and sample-names files are in their own directory
Otherwise the script errors when trying to read files correctly

```bash
for Set in all all_comparison_set highconfidence highconfidence_comparison_set \
highexpressed highexpressed_comparison_set
do
    mkdir -p promotor_id/$Set
    fasta=promotor_id/"$Set"_upstream3000.fasta
    index=promotor_id/"$Set"_upstream3000.fasta.fmi
    sample_names=promotor_id/sample-names_"$Set".txt
    mv $fasta promotor_id/$Set/.
    mv $index promotor_id/$Set/.
    mv $sample_names promotor_id/$Set/.
done
```

Now initialise the server-side processes

Parallel processes can be set at 4, 16 or 64

#### Set "all"

```bash
Set=all
WorkDir=promotor_id/$Set
tmp_dir=$WorkDir/$Set/tmp_dsmframework_"$Set"_config
mkdir -p $tmp_dir
ProgDir=/home/adamst/git_repos/tools/seq_tools/kmer_enrichment
sample_IDs=$WorkDir/sample-names_"$Set".txt
Parallel_processes=16
$ProgDir/server_set_up.sh $sample_IDs $tmp_dir $Parallel_processes $WorkDir $Set
```

Now run the client side processes

IMPORTANT: Ensure all the server side processes are running first

```bash
Set=all
Sample_Names=promotor_id/$Set/sample-names_"$Set".txt
ScriptDir=/home/adamst/git_repos/tools/seq_tools/kmer_enrichment
ProjDir=/home/groups/harrisonlab/project_files/phytophthora_fragariae
tmp_dir=$ProjDir/promotor_id/$Set/tmp_dsmframework_"$Set"_config
WorkDir=$ProjDir/promotor_id/$Set/
$ScriptDir/client_execution.sh $Sample_Names $tmp_dir $WorkDir
```

#### Set "all_comparison_set"

```bash
Set=all_comparison_set
WorkDir=promotor_id
tmp_dir=$WorkDir/tmp_dsmframework_"$Set"_config
mkdir -p $tmp_dir
ProgDir=/home/adamst/git_repos/tools/seq_tools/kmer_enrichment
sample_IDs=$WorkDir/sample-names_"$Set".txt
Parallel_processes=16
$ProgDir/server_set_up.sh $sample_IDs $tmp_dir $Parallel_processes $WorkDir $Set
```

Now run the client side processes

IMPORTANT: Ensure all the server side processes are running first

```bash
Set=all_comparison_set
Sample_Names=promotor_id/sample-names_"$Set".txt
ScriptDir=/home/adamst/git_repos/tools/seq_tools/kmer_enrichment
ProjDir=/home/groups/harrisonlab/project_files/phytophthora_fragariae
tmp_dir=$ProjDir/promotor_id/tmp_dsmframework_"$Set"_config
WorkDir=$ProjDir/promotor_id
$ScriptDir/client_execution.sh $Sample_Names $tmp_dir $WorkDir
```

#### Set "highconfidence"

```bash
Set=highconfidence
WorkDir=promotor_id
tmp_dir=$WorkDir/tmp_dsmframework_"$Set"_config
mkdir -p $tmp_dir
ProgDir=/home/adamst/git_repos/tools/seq_tools/kmer_enrichment
sample_IDs=$WorkDir/sample-names_"$Set".txt
Parallel_processes=16
$ProgDir/server_set_up.sh $sample_IDs $tmp_dir $Parallel_processes $WorkDir $Set
```

Now run the client side processes

IMPORTANT: Ensure all the server side processes are running first

```bash
Set=highconfidence
Sample_Names=promotor_id/sample-names_"$Set".txt
ScriptDir=/home/adamst/git_repos/tools/seq_tools/kmer_enrichment
tmp_dir=promotor_id/tmp_dsmframework_"$Set"_config
WorkDir=promotor_id
$ScriptDir/client_execution.sh $Sample_Names $tmp_dir $WorkDir
```

#### Set "highconfidence_comparison_set"

```bash
Set=highconfidence_comparison_set
WorkDir=promotor_id
tmp_dir=$WorkDir/tmp_dsmframework_"$Set"_config
mkdir -p $tmp_dir
ProgDir=/home/adamst/git_repos/tools/seq_tools/kmer_enrichment
sample_IDs=$WorkDir/sample-names_"$Set".txt
Parallel_processes=16
$ProgDir/server_set_up.sh $sample_IDs $tmp_dir $Parallel_processes $WorkDir $Set
```

Now run the client side processes

IMPORTANT: Ensure all the server side processes are running first

```bash
Set=highconfidence_comparison_set
Sample_Names=promotor_id/sample-names_"$Set".txt
ScriptDir=/home/adamst/git_repos/tools/seq_tools/kmer_enrichment
ProjDir=/home/groups/harrisonlab/project_files/phytophthora_fragariae
tmp_dir=$ProjDir/promotor_id/tmp_dsmframework_"$Set"_config
WorkDir=$ProjDir/promotor_id
$ScriptDir/client_execution.sh $Sample_Names $tmp_dir $WorkDir
```

#### Set "highexpressed"

```bash
Set=highexpressed
WorkDir=promotor_id
tmp_dir=$WorkDir/tmp_dsmframework_"$Set"_config
mkdir -p $tmp_dir
ProgDir=/home/adamst/git_repos/tools/seq_tools/kmer_enrichment
sample_IDs=$WorkDir/sample-names_"$Set".txt
Parallel_processes=16
$ProgDir/server_set_up.sh $sample_IDs $tmp_dir $Parallel_processes $WorkDir $Set
```

Now run the client side processes

IMPORTANT: Ensure all the server side processes are running first

```bash
Set=highexpressed
Sample_Names=promotor_id/sample-names_"$Set".txt
ScriptDir=/home/adamst/git_repos/tools/seq_tools/kmer_enrichment
tmp_dir=promotor_id/tmp_dsmframework_"$Set"_config
WorkDir=promotor_id
$ScriptDir/client_execution.sh $Sample_Names $tmp_dir $WorkDir
```

#### Set "highexpressed_comparison_set"

```bash
Set=highexpressed_comparison_set
WorkDir=promotor_id
tmp_dir=$WorkDir/tmp_dsmframework_"$Set"_config
mkdir -p $tmp_dir
ProgDir=/home/adamst/git_repos/tools/seq_tools/kmer_enrichment
sample_IDs=$WorkDir/sample-names_"$Set".txt
Parallel_processes=16
$ProgDir/server_set_up.sh $sample_IDs $tmp_dir $Parallel_processes $WorkDir $Set
```

Now run the client side processes

IMPORTANT: Ensure all the server side processes are running first

```bash
Set=highexpressed_comparison_set
Sample_Names=promotor_id/sample-names_"$Set".txt
ScriptDir=/home/adamst/git_repos/tools/seq_tools/kmer_enrichment
ProjDir=/home/groups/harrisonlab/project_files/phytophthora_fragariae
tmp_dir=$ProjDir/promotor_id/tmp_dsmframework_"$Set"_config
WorkDir=$ProjDir/promotor_id
$ScriptDir/client_execution.sh $Sample_Names $tmp_dir $WorkDir
```
