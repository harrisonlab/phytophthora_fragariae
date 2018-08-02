# Compare OrthoFinder to orthoMCL

Done at Maria's suggestion

Run on old gene models as below, comparison listed here for reference

##Compare OrthoFinder with orthoMCL

OrthoFinder produces a set of statistics, generate what of these I can for orthoMCL, some others will be calculated manually

```bash
for num in 1
do
    echo "Number of genes:"
    GoodProts=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/goodProteins/goodProteins.fasta
    cat $GoodProts | grep '>' | wc -l
    echo "Number of genes in orthogroups:"
    OrthoGroups=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/All_Strains_plus_rubi_no_removal_orthogroups.txt
    fgrep -o '|' $OrthoGroups | wc -l
    echo "Number of orthogroups:"
    fgrep -o ':' $OrthoGroups | wc -l
    echo "Median orthogroup size:"
    ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
    python $ProgDir/calc_orthogroup_median.py --orthogroups $OrthoGroups
done
```

```
OrthoMCL:
Number of genes input: 478,997
Number of genes in orthogroups: 455,838
Number of unassigned genes: 23,159
Percentage of unassigned genes: 4.8%
Number of orthogroups: 24,041
Mean orthogroup size: 19.0
Median orthogroup size: 14

OrthoFinder:
Number of genes input: 479,008
Number of genes in orthogroups: 469,036
Number of unassigned genes: 9,972
Percentage of unassigned genes: 2.1%
Number of orthogroups: 38,179 - this does not include singletons
Mean orthogroup size: 12.3
Median orthogroup size: 12

Unclear where there are 11 more genes fed into OrthoFinder, but there are 2.7 percentage points fewer genes in unassigned groups, with 14,138 more orthogroups, with a 6.7 smaller mean orthogroup size and a 2 smaller median orthogroup size. So, OrthoFinder seems better than OrthoMCL for my requirements.
```

Analysis on corrected models submitted to NCBI

## Setting of variables

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/analysis/orthology/OrthoFinder
scripts=/home/adamst/git_repos/scripts/popgen/clock/motif_discovery
WorkDir=/home/groups/harrisonlab/project_files/phytophthora_fragariae/analysis/orthology/OrthoFinder/formatted/Results_Aug18
```

## 4.1 Format fasta files


### for A4

```bash
Taxon_code=A4
Fasta_file=gene_pred/annotation/P.fragariae/A4/A4_genes_incl_ORFeffectors_renamed.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

### for BC-1

```bash
Taxon_code=Bc1
Fasta_file=gene_pred/annotation/P.fragariae/Bc1/Bc1_genes_incl_ORFeffectors_renamed.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

### for BC-16

```bash
Taxon_code=Bc16
Fasta_file=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors_renamed.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

### for BC-23

```bash
Taxon_code=Bc23
Fasta_file=gene_pred/annotation/P.fragariae/Bc23/Bc23_genes_incl_ORFeffectors_renamed.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

### for NOV-27

```bash
Taxon_code=Nov27
Fasta_file=gene_pred/annotation/P.fragariae/Nov27/Nov27_genes_incl_ORFeffectors_renamed.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

### for NOV-5

```bash
Taxon_code=Nov5
Fasta_file=gene_pred/annotation/P.fragariae/Nov5/Nov5_genes_incl_ORFeffectors_renamed.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

### for NOV-71

```bash
Taxon_code=Nov71
Fasta_file=gene_pred/annotation/P.fragariae/Nov71/Nov71_genes_incl_ORFeffectors_renamed.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

### for NOV-77

```bash
Taxon_code=Nov77
Fasta_file=gene_pred/annotation/P.fragariae/Nov77/Nov77_genes_incl_ORFeffectors_renamed.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

### for NOV-9

```bash
Taxon_code=Nov9
Fasta_file=gene_pred/annotation/P.fragariae/Nov9/Nov9_genes_incl_ORFeffectors_renamed.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

### for ONT-3

```bash
Taxon_code=ONT3
Fasta_file=gene_pred/annotation/P.fragariae/ONT3/ONT3_genes_incl_ORFeffectors_renamed.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

### for SCRP245_v2

```bash
Taxon_code=SCRP245_v2
Fasta_file=gene_pred/annotation/P.fragariae/SCRP245_v2/SCRP245_v2_genes_incl_ORFeffectors_renamed.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

### for SCRP249

```bash
Taxon_code=SCRP249
Fasta_file=../phytophthora_rubi/gene_pred/annotation/P.rubi/SCRP249/SCRP249_genes_incl_ORFeffectors_renamed.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

### for SCRP324

```bash
Taxon_code=SCRP324
Fasta_file=../phytophthora_rubi/gene_pred/annotation/P.rubi/SCRP324/SCRP324_genes_incl_ORFeffectors_renamed.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

### for SCRP333

```bash
Taxon_code=SCRP333
Fasta_file=../phytophthora_rubi/gene_pred/annotation/P.rubi/SCRP333/SCRP333_genes_incl_ORFeffectors_renamed.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

### Create goodproteins file

```bash
Input_dir=$WorkDir/formatted
Min_length=10
Max_percent_stops=20
Good_proteins_file=$WorkDir/goodProteins/goodProteins.fasta
Poor_proteins_file=$WorkDir/badProteins/poorProteins.fasta
orthomclFilterFasta $Input_dir $Min_length $Max_percent_stops $Good_proteins_file $Poor_proteins_file
```

### Runs orthofinder

```bash
screen -a
qlogin -pe smp 24
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/analysis/orthology/OrthoFinder
scripts=/home/adamst/git_repos/scripts/popgen/clock/motif_discovery
cd $input
IsolateAbrv=All_Strains_plus_rubi_no_removal
orthofinder -f formatted -t 24
```

```
Best outgroup(s) for species tree
---------------------------------
Observed 250 duplications. 228 support the best root and 22 contradict it.
Best outgroup for species tree:
SCRP249, SCRP333, SCRP324

OrthoFinder assigned 469036 genes (97.9% of total) to 38179 orthogroups. Fifty percent of all genes were in orthogroups with 14 or more genes (G50 was 14) and were contained in the largest 12233 orthogroups (O50 was 12233). There were 17388 orthogroups with all species present and 13444 of these consisted entirely of single-copy genes.
```

##4.5.a Manual identification of numbers of orthologous and unique genes

```bash
for num in 1
do
    echo "The total number of orthogroups is:"
    cat $WorkDir/Orthogroups.txt | wc -l
    echo "The total number of genes in orthogroups is:"
    cat $WorkDir/Orthogroups.txt | grep -o '|' | wc -l
    echo "The number of orthogroups common to P. rubi is:"
    cat $WorkDir/Orthogroups.txt | grep -e 'SCRP249|' | grep -e 'SCRP324|' | grep -e 'SCRP333|' | grep -v -e 'A4|' -e 'Bc1|' -e 'Bc16|' -e 'Bc23|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/Orthogroups.txt | grep -e 'SCRP249|' | grep -e 'SCRP324|' | grep -e 'SCRP333|' | grep -v -e 'A4|' -e 'Bc1|' -e 'Bc16|' -e 'Bc23|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to P. fragariae is:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'A4|' | grep -e 'Bc1|' | grep -e 'Bc16|' | grep -e 'Bc23|' | grep -e 'Nov5|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov77|' | grep -e 'Nov9|' | grep -e 'ONT3|' | grep -e 'SCRP245_v2|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'A4|' | grep -e 'Bc1|' | grep -e 'Bc16|' | grep -e 'Bc23|' | grep -e 'Nov5|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov77|' | grep -e 'Nov9|' | grep -e 'ONT3|' | grep -e 'SCRP245_v2|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to UK1 isolates is:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc1|' | grep -e 'Nov5|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc1|' | grep -e 'Nov5|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to UK2 isolates is:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'Bc1|' -e 'Bc23|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'Nov5|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc16|' | grep -e 'A4|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'Bc1|' -e 'Bc23|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'Nov5|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc16|' | grep -e 'A4|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to UK3 isolates is:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov9|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov9|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to CA4 isolates is:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'Nov9|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'ONT3|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'Nov9|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'ONT3|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to CA5 isolates is:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'ONT3|' -e 'Nov9|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc23|' | grep -e 'Nov77|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'ONT3|' -e 'Nov9|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc23|' | grep -e 'Nov77|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to Unknown race isolates is:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'Nov9|' -e 'A4|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'SCRP245_v2|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'Nov9|' -e 'A4|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'SCRP245_v2|' | grep -o '|' | wc -l
    echo "The number of orthogroups with only seven highly conserved target isolates is:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc23|' -e 'Nov77|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' -e 'SCRP245_v2|' | grep -e 'Nov5|' | grep -e 'Nov27' | grep -e 'Nov71' | grep -e 'Bc16' | grep -e 'Nov9' | grep -e 'Bc1' | grep -e 'A4' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc23|' -e 'Nov77|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' -e 'SCRP245_v2|' | grep -e 'Nov5|' | grep -e 'Nov27' | grep -e 'Nov71' | grep -e 'Bc16' | grep -e 'Nov9' | grep -e 'Bc1' | grep -e 'A4' | grep -o '|' | wc -l
    echo "The number of orthogroups containing all seven highly conserved target isolates is:"
    cat $WorkDir/Orthogroups.txt | grep -e 'Nov5|' | grep -e 'Nov27' | grep -e 'Nov71' | grep -e 'Bc16' | grep -e 'Nov9' | grep -e 'Bc1' | grep -e 'A4' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/Orthogroups.txt | grep -e 'Nov5|' | grep -e 'Nov27' | grep -e 'Nov71' | grep -e 'Bc16' | grep -e 'Nov9' | grep -e 'Bc1' | grep -e 'A4' | grep -o '|' | wc -l
done
```

```
The total number of orthogroups is:
48,151
The total number of genes in orthogroups is:
479,008
The number of orthogroups common to P. rubi is:
2,531
This represents the following number of genes:
7,985
The number of orthogroups common to P. fragariae is:
1,845
This represents the following number of genes:
21,663
The number of orthogroups common to UK1 isolates is:
13
This represents the following number of genes:
26
The number of orthogroups common to UK2 isolates is:
24
This represents the following number of genes:
57
The number of orthogroups common to UK3 isolates is:
2
This represents the following number of genes:
6
The number of orthogroups common to CA4 isolates is:
2,199
This represents the following number of genes:
2,202
The number of orthogroups common to CA5 isolates is:
25
This represents the following number of genes:
51
The number of orthogroups common to Unknown race isolates is:
2,559
This represents the following number of genes:
2,560
The number of orthogroups with only seven highly conserved target isolates is:
42
This represents the following number of genes:
293
The number of orthogroups containing all seven highly conserved target isolates is:
22,824
This represents the following number of genes:
367,953
```

Identification of orthogroups of closely related isolates for further analysis

```bash
for num in 1
do
    echo "The total number of shared orthogroups is:"
    cat $WorkDir/Orthogroups.txt | grep -e 'A4|' | grep -e 'Nov5|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Bc16|' | grep -e 'Nov9|' | grep -e 'Bc1|' | wc -l
    echo "The total number of genes in shared orthogroups is:"
    cat $WorkDir/Orthogroups.txt | grep -e 'A4|' | grep -e 'Nov5|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Bc16|' | grep -e 'Nov9|' | grep -e 'Bc1|' | grep -o '|' | wc -l
    echo "The total number of orthogroups is:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc23|' -e 'SCRP245_v2' -e 'Nov77|' -e 'SCRP249' -e 'SCRP324' -e 'SCRP333' | wc -l
    echo "The total number of genes in orthogroups is:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc23|' -e 'SCRP245_v2' -e 'Nov77|' -e 'SCRP249' -e 'SCRP324' -e 'SCRP333' | grep -o '|' | wc -l
    echo "The total number of UK1 orthogroups is:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'A4|' -e 'Nov27|' -e 'Nov71|' -e 'Bc16|' -e 'Nov9|' | grep -e 'Nov5|' | grep -e 'Bc1|' | wc -l
    echo "The total number of genes in UK1 orthogroups is:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'A4|' -e 'Nov27|' -e 'Nov71|' -e 'Bc16|' -e 'Nov9|' | grep -e 'Nov5|' | grep -e 'Bc1|' | grep -o '|' | wc -l
    echo "The total number of UK2 orthogroups is:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'Bc1|' -e 'Nov9|' | grep -e 'A4|' | grep -e 'Bc16|' | wc -l
    echo "The total number of genes in UK2 orthogroups is:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'Bc1|' -e 'Nov9|' | grep -e 'A4|' | grep -e 'Bc16|' | grep -o '|' | wc -l
    echo "The total number of UK3 orthogroups is:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'Nov5|' -e 'A4|' -e 'Bc16|' -e 'Bc1|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov9|' | wc -l
    echo "The total number of genes in UK3 orthogroups is:"
    cat $WorkDir/Orthogroups.txt | grep -v -e 'Nov5|' -e 'A4|' -e 'Bc16|' -e 'Bc1|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov9|' | grep -o '|' | wc -l
done
```

```
The total number of shared orthogroups is:
22,522
The total number of genes in shared orthogroups is:
363,776
The total number of orthogroups is:
2,919
The total number of genes in orthogroups is:
4,406
The total number of UK1 orthogroups is:
36
The total number of genes in UK1 orthogroups is:
164
The total number of UK2 orthogroups is:
104
The total number of genes in UK2 orthogroups is:
503
The total number of UK3 orthogroups is:
22
The total number of genes in UK3 orthogroups is:
121
```

## 4.5.b Creates tab file and Plot venn diagrams:

```bash
ProgDir=/home/armita/git_repos/emr_repos/tools/pathogen/orthology/orthoMCL
$ProgDir/orthoMCLgroups2tab.py $WorkDir/goodProteins/goodProteins.fasta $WorkDir/Orthogroups.txt > $WorkDir/Orthogroups.tab
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
$ProgDir/UK1_Pf_venn_diag.r --inp $WorkDir/Orthogroups.tab --out $WorkDir/UK1_orthogroups.pdf
$ProgDir/UK2_Pf_venn_diag.r --inp $WorkDir/Orthogroups.tab --out $WorkDir/UK2_orthogroups.pdf
$ProgDir/UK3_Pf_venn_diag.r --inp $WorkDir/Orthogroups.tab --out $WorkDir/UK3_orthogroups.pdf
```

Output was a pdf file of the venn diagram.

The following additional information was also provided.
The format of the following lines is as follows:

Isolate name (total number of orthogroups) number of unique singleton genes
number of unique groups of inparalogs

Singletons will always show up as zeros due to different naming by OrthoFinder

### UK race 1 focused analysis

```
A4
The total number of orthogroups and singleton genes in this isolate:  28,179
The total number of orthogroups and singleton genes not in the venn diagram:  5,090
The total number of singleton genes not in the venn diagram:  0
NOV-5
The total number of orthogroups and singleton genes in this isolate:  28,226
The total number of orthogroups and singleton genes not in the venn diagram:  5,103
The total number of singleton genes not in the venn diagram:  0
NOV-27
The total number of orthogroups and singleton genes in this isolate:  28,243
The total number of orthogroups and singleton genes not in the venn diagram:  5,154
The total number of singleton genes not in the venn diagram:  0
NOV-71
The total number of orthogroups and singleton genes in this isolate:  28,012
The total number of orthogroups and singleton genes not in the venn diagram:  4,923
The total number of singleton genes not in the venn diagram:  0
BC-16
The total number of orthogroups and singleton genes in this isolate:  28,908
The total number of orthogroups and singleton genes not in the venn diagram:  5,819
The total number of singleton genes not in the venn diagram:  0
NOV-9
The total number of orthogroups and singleton genes in this isolate:  28,025
The total number of orthogroups and singleton genes not in the venn diagram:  4,936
The total number of singleton genes not in the venn diagram:  0
BC-1
The total number of orthogroups and singleton genes in this isolate:  28,162
The total number of orthogroups and singleton genes not in the venn diagram:  4,918
The total number of singleton genes not in the venn diagram:  0
```

### UK race 2 focused analysis

```
A4
The total number of orthogroups and singleton genes in this isolate:  28,179
The total number of orthogroups and singleton genes not in the venn diagram:  3,783
The total number of singleton genes not in the venn diagram:  0
NOV-5
The total number of orthogroups and singleton genes in this isolate:  28,226
The total number of orthogroups and singleton genes not in the venn diagram:  3,841
The total number of singleton genes not in the venn diagram:  0
NOV-27
The total number of orthogroups and singleton genes in this isolate:  28,243
The total number of orthogroups and singleton genes not in the venn diagram:  3,858
The total number of singleton genes not in the venn diagram:  0
NOV-71
The total number of orthogroups and singleton genes in this isolate:  28,012
The total number of orthogroups and singleton genes not in the venn diagram:  3,627
The total number of singleton genes not in the venn diagram:  0
BC-16
The total number of orthogroups and singleton genes in this isolate:  28,908
The total number of orthogroups and singleton genes not in the venn diagram:  3,806
The total number of singleton genes not in the venn diagram:  0
NOV-9
The total number of orthogroups and singleton genes in this isolate:  28,025
The total number of orthogroups and singleton genes not in the venn diagram:  3,640
The total number of singleton genes not in the venn diagram:  0
BC-1
The total number of orthogroups and singleton genes in this isolate:  28,162
The total number of orthogroups and singleton genes not in the venn diagram:  3,640
The total number of singleton genes not in the venn diagram:  0
```

### UK race 3 focused analysis

```
A4
The total number of orthogroups and singleton genes in this isolate:  28,179
The total number of orthogroups and singleton genes not in the venn diagram:  4,760
The total number of singleton genes not in the venn diagram:  0
NOV-5
The total number of orthogroups and singleton genes in this isolate:  28,226
The total number of orthogroups and singleton genes not in the venn diagram:  4,807
The total number of singleton genes not in the venn diagram:  0
NOV-27
The total number of orthogroups and singleton genes in this isolate:  28,243
The total number of orthogroups and singleton genes not in the venn diagram:  4,795
The total number of singleton genes not in the venn diagram:  0
NOV-71
The total number of orthogroups and singleton genes in this isolate:  28,012
The total number of orthogroups and singleton genes not in the venn diagram:  4,647
The total number of singleton genes not in the venn diagram:  0
BC-16
The total number of orthogroups and singleton genes in this isolate:  28,908
The total number of orthogroups and singleton genes not in the venn diagram:  5,489
The total number of singleton genes not in the venn diagram:  0
NOV-9
The total number of orthogroups and singleton genes in this isolate:  28,025
The total number of orthogroups and singleton genes not in the venn diagram:  4,626
The total number of singleton genes not in the venn diagram:  0
BC-1
The total number of orthogroups and singleton genes in this isolate:  28,162
The total number of orthogroups and singleton genes not in the venn diagram:  4,606
The total number of singleton genes not in the venn diagram:  0
```

## Analysis of orthogroups unique to UK race 2 (Strains BC-16 & A4)

These values will contain singletons

### The genes unique to Race 2 were identified within the orthology analysis

### First variables were set

```bash
WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18
UK2UniqDir=$WorkDir/UK2_unique
Orthogroups=$WorkDir/Orthogroups.txt
Final_genes_Bc16=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors_renamed.pep.fasta
Final_genes_A4=gene_pred/annotation/P.fragariae/A4/A4_genes_incl_ORFeffectors_renamed.pep.fasta
Uniq_UK2_groups=$UK2UniqDir/UK2_uniq_orthogroups.txt
mkdir -p $UK2UniqDir
```

## Orthogroups only containing Race 2 genes were extracted:

```bash
for num in 1
do
    cat $Orthogroups | grep -v -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'Bc1|' -e 'Nov9|' | grep -e 'A4|' | grep -e 'Bc16|' > $Uniq_UK2_groups
    echo "The number of orthogroups unique to Race UK2 are:"
    cat $Uniq_UK2_groups | wc -l
    echo "The following number genes are contained in these orthogroups:"
    cat $Uniq_UK2_groups | grep -v -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'Bc1|' -e 'Nov9|' | grep -e 'A4|' | grep -e 'Bc16|' | grep -o '|' | wc -l
done
```

```
The number of orthogroups unique to Race 2 are:
104
The following number genes are contained in these orthogroups:
503
```

## Race 2 unique RxLR families

## Race 2 RxLR genes were parsed to same format as names used in analysis

```bash
for num in 1
do
    RxLR_Names_Bc16=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_Total_RxLR_motif_hmm_renamed.txt
    RxLR_Names_A4=analysis/RxLR_effectors/combined_evidence/P.fragariae/A4/A4_Total_RxLR_motif_hmm_renamed.txt
    WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18
    RxLR_Dir=$WorkDir/UK2_RxLR
    Orthogroups=$WorkDir/Orthogroups.txt
    RxLR_ID=$RxLR_Dir/UK2_aug_RxLR_EER_IDs.txt
    mkdir -p $RxLR_Dir
    cat $RxLR_Names_Bc16 | sed -r 's/^/Bc16|/g' > $RxLR_ID
    cat $RxLR_Names_A4 | sed -r 's/^/A4|/g' >> $RxLR_ID
done
```

## Orthogroups containing RxLR proteins were identified

```bash
for num in 1
do
    echo "The number of RxLRs searched for is:"
    cat $RxLR_ID | wc -l
    echo "Of these, the following number were found in orthogroups:"
    RxLR_Orthogroup_hits=$RxLR_Dir/UK2_RxLR_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $RxLR_ID > $RxLR_Orthogroup_hits
    cat $RxLR_Orthogroup_hits | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    RxLR_Orthogroup=$RxLR_Dir/UK2_RxLR_Orthogroups.txt
    cat $Orthogroups | grep -w -f $RxLR_ID > $RxLR_Orthogroup
    cat $RxLR_Orthogroup | wc -l
    echo "The following RxLRs were found in Race 2 unique orthogroups:"
    RxLR_UK2_uniq_groups=$RxLR_Dir/UK2_uniq_RxLR_Orthogroups_hits.txt
    cat $RxLR_Orthogroup | grep -v -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'Bc1|' -e 'Nov9|' | grep -e 'A4|' | grep -e 'Bc16|' > $RxLR_UK2_uniq_groups
    cat $RxLR_UK2_uniq_groups | wc -l
    echo "These orthogroups contain the following number of RxLRs:"
    cat $RxLR_UK2_uniq_groups | grep -w -o -f $RxLR_ID | wc -l
    echo "The following RxLRs were found in P.fragariae unique orthogroups:"
    RxLR_Pf_uniq_groups=$RxLR_Dir/Pf_RxLR_Orthogroups_hits.txt
    cat $RxLR_Orthogroup > $RxLR_Pf_uniq_groups
    cat $RxLR_Pf_uniq_groups | wc -l
    echo "These orthogroups contain the following number of RxLRs:"
    cat $RxLR_Pf_uniq_groups | grep -w -o -f $RxLR_ID | wc -l
done
```

```
The number of RxLRs searched for is:
4,859
Of these, the following number were found in orthogroups:
4,859
These were distributed through the following number of Orthogroups:
2,309
The following RxLRs were found in Race 2 unique orthogroups:
6
These orthogroups contain the following number of RxLRs:
14
The following RxLRs were found in P.fragariae unique orthogroups:
2,309
These orthogroups contain the following number of RxLRs:
4,859
```

## The Race 2 RxLR genes that were not found in orthogroups were identified

```bash
for num in 1
do
    RxLR_UK2_uniq=$RxLR_Dir/UK2_unique_RxLRs.txt
    cat $RxLR_ID | grep -v -w -f $RxLR_Orthogroup_hits > $RxLR_UK2_uniq
    echo "The number of UK2 unique RxLRs are:"
    cat $RxLR_UK2_uniq | wc -l
    RxLR_Seq_Bc16=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_final_RxLR_renamed.fa
    RxLR_Seq_A4=analysis/RxLR_effectors/combined_evidence/P.fragariae/A4/A4_final_RxLR_renamed.fa
    Final_genes_Bc16=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors_renamed.pep.fasta
    Final_genes_A4=gene_pred/annotation/P.fragariae/A4/A4_genes_incl_ORFeffectors_renamed.pep.fasta
    Bc16_RxLR_UK2_uniq_fa=$RxLR_Dir/Bc16_UK2_unique_RxLRs.fa
    A4_RxLR_UK2_uniq_fa=$RxLR_Dir/A4_UK2_unique_RxLRs.fa
    Bc16_to_extract=$RxLR_Dir/Bc16_to_extract.txt
    A4_to_extract=$RxLR_Dir/A4_to_extract.txt
    cat $RxLR_UK2_uniq | grep 'Bc16|' | cut -f2 -d "|" > $Bc16_to_extract
    cat $RxLR_UK2_uniq | grep 'A4|' | cut -f2 -d "|" > $A4_to_extract
    cat $Final_genes_Bc16 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Bc16_to_extract | grep -E -v '^--' > $Bc16_RxLR_UK2_uniq_fa
    cat $Final_genes_A4 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $A4_to_extract | grep -E -v '^--' > $A4_RxLR_UK2_uniq_fa
    echo "The number of BC-16 genes extracted is:"
    cat $Bc16_RxLR_UK2_uniq_fa | grep '>' | wc -l
    echo "The number of A4 genes extracted is:"
    cat $A4_RxLR_UK2_uniq_fa | grep '>' | wc -l
done
```

```
The number of UK2 unique RxLRs are:
0
The number of BC-16 genes extracted is:
0
The number of A4 genes extracted is:
0
```

## Extracting fasta files for orthogroups containing Race 2 putative RxLRs

```bash
for num in 1
do
    /home/groups/harrisonlab/project_files/phytophthora_fragariae/analysis/orthology/OrthoFinder/formatted/Results_Aug18
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_RxLR/UK2_RxLR_Orthogroups.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_RxLR/orthogroups_fasta_UK2_RxLR
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Extracting fasta files for P. fragariae orthogroups containing Race 2 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_RxLR/Pf_RxLR_Orthogroups_hits.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_RxLR/orthogroups_fasta_Pf_RxLR
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Race 2 unique Crinkler families

### Race 2 crinkler genes were parsed to the same format as the gene names used in the analysis:

```bash
for num in 1
do
    CRN_Names_Bc16=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc16/Bc16_final_CRN_renamed.txt
    CRN_Names_A4=analysis/CRN_effectors/hmmer_CRN/P.fragariae/A4/A4_final_CRN_renamed.txt
    WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18
    CRN_Dir=$WorkDir/UK2_CRN
    Orthogroups=$WorkDir/Orthogroups.txt
    CRN_ID_UK2=$CRN_Dir/UK2_CRN_hmmer_IDs.txt
    mkdir -p $CRN_Dir
    cat $CRN_Names_Bc16 | sed -r 's/^/Bc16|/g' > $CRN_ID_UK2
    cat $CRN_Names_A4 | sed -r 's/^/A4|/g' >> $CRN_ID_UK2
done
```

## Orthology groups containing CRN proteins were identified=

```bash
for num in 1
do
    echo "The number of CRNs searched for is:"
    cat $CRN_ID_UK2 | wc -l
    echo "Of these, the following number were found in orthogroups:"
    CRN_Orthogroup_hits_UK2=$CRN_Dir/UK2_CRN_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $CRN_ID_UK2 > $CRN_Orthogroup_hits_UK2
    cat $CRN_Orthogroup_hits_UK2 | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    CRN_Orthogroup_UK2=$CRN_Dir/UK2_CRN_Orthogroups.txt
    cat $Orthogroups | grep -w -f $CRN_ID_UK2 > $CRN_Orthogroup_UK2
    cat $CRN_Orthogroup_UK2 | wc -l
    echo "The following CRNs were found in Race 2 unique orthogroups:"
    CRN_UK2_uniq_groups=$CRN_Dir/UK2_uniq_CRN_Orthogroups_hits.txt
    cat $CRN_Orthogroup_UK2 | grep -v -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'Bc1|' -e 'Nov9|' | grep -e 'A4|' | grep -e 'Bc16|' > $CRN_UK2_uniq_groups
    cat $CRN_UK2_uniq_groups | wc -l
    echo "The following CRNs were found in P.fragariae unique orthogroups:"
    CRN_Pf_uniq_groups=$CRN_Dir/Pf_CRN_Orthogroups_hits.txt
    cat $CRN_Orthogroup_UK2 > $CRN_Pf_uniq_groups
    cat $CRN_Pf_uniq_groups | wc -l
    echo "These orthogroups contain the following number of CRNs:"
    cat $CRN_Pf_uniq_groups | grep -w -o -f $CRN_ID_UK2 | wc -l
done
```

```
The number of CRNs searched for is:
231
Of these, the following number were found in orthogroups:
231
These were distributed through the following number of Orthogroups:
109
The following CRNs were found in Race 2 unique orthogroups:
0
The following CRNs were found in P.fragariae unique orthogroups:
109
These orthogroups contain the following number of CRNs:
231
```

## The Race 2 CRN genes not found in orthogroups were identified

```bash
for num in 1
do
    CRN_UK2_uniq=$CRN_Dir/UK2_unique_CRNs.txt
    cat $CRN_ID_UK2 | grep -v -w -f $CRN_Orthogroup_hits_UK2 > $CRN_UK2_uniq
    echo "The number of UK2 unique CRNs are:"
    cat $CRN_UK2_uniq | wc -l
    CRN_Seq_Bc16=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc16/Bc16_final_CRN_renamed.fa
    CRN_Seq_A4=analysis/CRN_effectors/hmmer_CRN/P.fragariae/A4/A4_final_CRN_renamed.fa
    Final_genes_Bc16=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors_renamed.pep.fasta
    Final_genes_A4=gene_pred/annotation/P.fragariae/A4/A4_genes_incl_ORFeffectors_renamed.pep.fasta
    Bc16_CRN_UK2_uniq_fa=$CRN_Dir/Bc16_UK2_unique_CRNs.fa
    A4_CRN_UK2_uniq_fa=$CRN_Dir/A4_UK2_unique_CRNs.fa
    Bc16_to_extract=$CRN_Dir/Bc16_to_extract.txt
    A4_to_extract=$CRN_Dir/A4_to_extract.txt
    cat $CRN_UK2_uniq | grep 'Bc16|' | cut -f2 -d "|" > $Bc16_to_extract
    cat $CRN_UK2_uniq | grep 'A4|' | cut -f2 -d "|" > $A4_to_extract
    cat $Final_genes_Bc16 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $CRN_UK2_uniq | grep -E -v '^--' > $Bc16_CRN_UK2_uniq_fa
    cat $Final_genes_A4 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $CRN_UK2_uniq | grep -E -v '^--' > $A4_CRN_UK2_uniq_fa
    echo "The number of BC-16 genes extracted is:"
    cat $Bc16_CRN_UK2_uniq_fa | grep '>' | wc -l
    echo "The number of A4 genes extracted is:"
    cat $A4_CRN_UK2_uniq_fa | grep '>' | wc -l
done
```

```
The number of UK2 unique CRNs are:
0
The number of BC-16 genes extracted is:
0
The number of A4 genes extracted is:
0
```

##Extracting fasta files for orthogroups containing Race 2 putative CRNs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_CRN/UK2_CRN_Orthogroups_hits.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_CRN/orthogroups_fasta_UK2_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Extracting fasta files for P. fragariae orthogroups containing Race 2 putative CRNs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_CRN/Pf_CRN_Orthogroups_hits.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_CRN/orthogroups_fasta_Pf_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Race 2 unique Apoplastic effector families

## Race 2 Apoplastic effectors were parsed to same format as used in analysis

```bash
for num in 1
do
    ApoP_Names_Bc16=analysis/ApoplastP/P.fragariae/Bc16/Bc16_Total_ApoplastP_renamed.txt
    ApoP_Names_A4=analysis/ApoplastP/P.fragariae/A4/A4_Total_ApoplastP_renamed.txt
    WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18
    ApoP_Dir=$WorkDir/UK2_ApoP
    Orthogroups=$WorkDir/Orthogroups.txt
    ApoP_ID_UK2=$ApoP_Dir/UK2_ApoP_IDs.txt
    mkdir -p $ApoP_Dir
    cat $ApoP_Names_Bc16 | sed -r 's/^/Bc16|/g' > $ApoP_ID_UK2
    cat $ApoP_Names_A4 | sed -r 's/^/A4|/g' >> $ApoP_ID_UK2
done
```

## Orthology groups containing apoplastic effectors were identified

```bash
for num in 1
do
    echo "The number of apoplastic effectors searched for is:"
    cat $ApoP_ID_UK2 | wc -l
    echo "Of these, the following number were found in orthogroups:"
    ApoP_Orthogroup_hits_UK2=$ApoP_Dir/UK2_ApoP_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $ApoP_ID_UK2 > $ApoP_Orthogroup_hits_UK2
    cat $ApoP_Orthogroup_hits_UK2 | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    ApoP_Orthogroup_UK2=$ApoP_Dir/UK2_ApoP_Orthogroups.txt
    cat $Orthogroups | grep -w -f $ApoP_ID_UK2 > $ApoP_Orthogroup_UK2
    cat $ApoP_Orthogroup_UK2 | wc -l
    echo "The following apoplastic effectors were found in Race 2 unique orthogroups:"
    ApoP_UK2_uniq_groups=$ApoP_Dir/UK2_uniq_ApoP_Orthogroups_hits.txt
    cat $ApoP_Orthogroup_UK2 | grep -v -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'Bc1|' -e 'Nov9|' | grep -e 'A4|' | grep -e 'Bc16|' > $ApoP_UK2_uniq_groups
    cat $ApoP_UK2_uniq_groups | wc -l
    echo "The following apoplastic effectors were found in P.fragariae unique orthogroups:"
    ApoP_Pf_uniq_groups=$ApoP_Dir/Pf_ApoP_Orthogroups_hits.txt
    cat $ApoP_Orthogroup_UK2 > $ApoP_Pf_uniq_groups
    cat $ApoP_Pf_uniq_groups | wc -l
    echo "These orthogroups contain the following number of apoplastic effectors:"
    cat $ApoP_Pf_uniq_groups | grep -w -o -f $ApoP_ID_UK2 | wc -l
done
```

```
The number of apoplastic effectors searched for is:
23,464
Of these, the following number were found in orthogroups:
3,201
These were distributed through the following number of Orthogroups:
1,667
The following apoplastic effectors were found in Race 2 unique orthogroups:
5
The following apoplastic effectors were found in P.fragariae unique orthogroups:
1,667
These orthogroups contain the following number of apoplastic effectors:
3,201
```

## The Race 2 apoplastic effectors not found in orthogroups were identified

```bash
for num in 1
do
    ApoP_UK2_uniq=$ApoP_Dir/UK2_unique_ApoP.txt
    cat $ApoP_ID_UK2 | grep -v -w -f $ApoP_Orthogroup_hits_UK2 > $ApoP_UK2_uniq
    echo "The number of UK2 unique apoplastic effectors are:"
    cat $ApoP_UK2_uniq | wc -l
    ApoP_Seq_Bc16=analysis/ApoplastP/P.fragariae/Bc16/Bc16_final_ApoplastP_renamed.fa
    ApoP_Seq_A4=analysis/ApoplastP/P.fragariae/A4/A4_final_ApoplastP_renamed.fa
    Final_genes_Bc16=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors_renamed.pep.fasta
    Final_genes_A4=gene_pred/annotation/P.fragariae/A4/A4_genes_incl_ORFeffectors_renamed.pep.fasta
    Bc16_ApoP_UK2_uniq_fa=$ApoP_Dir/Bc16_UK2_unique_ApoP.fa
    A4_ApoP_UK2_uniq_fa=$ApoP_Dir/A4_UK2_unique_ApoP.fa
    Bc16_to_extract=$ApoP_Dir/Bc16_to_extract.txt
    A4_to_extract=$ApoP_Dir/A4_to_extract.txt
    cat $ApoP_UK2_uniq | grep 'Bc16|' | cut -f2 -d "|" > $Bc16_to_extract
    cat $ApoP_UK2_uniq | grep 'A4|' | cut -f2 -d "|" > $A4_to_extract
    cat $Final_genes_Bc16 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Bc16_to_extract | grep -E -v '^--' > $Bc16_ApoP_UK2_uniq_fa
    cat $Final_genes_A4 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $A4_to_extract | grep -E -v '^--' > $A4_ApoP_UK2_uniq_fa
    echo "The number of BC-16 genes extracted is:"
    cat $Bc16_ApoP_UK2_uniq_fa | grep '>' | wc -l
    echo "The number of A4 genes extracted is:"
    cat $A4_ApoP_UK2_uniq_fa | grep '>' | wc -l
done
```

```
The number of UK2 unique apoplastic effectors are:
20,263
The number of BC-16 genes extracted is:
10,989
The number of A4 genes extracted is:
9,274
```

## Extract fasta files for orthogroups with Race 2 putative apoplastic effectors

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_ApoP/UK2_ApoP_Orthogroups.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_ApoP/orthogroups_fasta_UK2_ApoP
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Extracting fasta files for Pf orthogroups with Race 2 apoplastic effectors

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_ApoP/Pf_ApoP_Orthogroups_hits.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_ApoP/orthogroups_fasta_Pf_ApoP
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Race 2 unique secreted proteins

## Race 2 secreted protein genes parsed to the same format as analysis

```bash
for num in 1
do
    Sec_Names_Bc16=gene_pred/combined_sigP_CQ/P.fragariae/Bc16/Bc16_secreted_renamed.txt
    Sec_Names_A4=gene_pred/combined_sigP_CQ/P.fragariae/A4/A4_secreted_renamed.txt
    Sec_Names_Bc16_ORFs=gene_pred/combined_sigP_ORF/P.fragariae/Bc16/Bc16_all_secreted_merged_renamed.txt
    Sec_Names_A4_ORFs=gene_pred/combined_sigP_ORF/P.fragariae/A4/A4_all_secreted_merged_renamed.txt
    WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18
    Sec_Dir=$WorkDir/UK2_Secreted
    Orthogroups=$WorkDir/Orthogroups.txt
    Sec_ID=$Sec_Dir/UK2_aug_Sec_IDs.txt
    mkdir -p $Sec_Dir
    cat $Sec_Names_Bc16 | sed -r 's/^/Bc16|/g' > $Sec_ID
    cat $Sec_Names_A4 | sed -r 's/^/A4|/g' >> $Sec_ID
    cat $Sec_Names_Bc16_ORFs | sed -r 's/^/Bc16|/g' | sed -r 's/$/.t1/g' >> $Sec_ID
    cat $Sec_Names_A4_ORFs | sed -r 's/^/A4|/g' | sed -r 's/$/.t1/g' >> $Sec_ID
done
```

## Ortholog groups containing Secreted proteins were identified

```bash
for num in 1
do
    echo "The number of secreted proteins searched for is:"
    cat $Sec_ID | wc -l
    echo "Of these, the following number were found in orthogroups:"
    Sec_Orthogroup_hits=$Sec_Dir/UK2_Sec_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $Sec_ID > $Sec_Orthogroup_hits
    cat $Sec_Orthogroup_hits | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    Sec_Orthogroup=$Sec_Dir/UK2_Sec_Orthogroups.txt
    cat $Orthogroups | grep -w -f $Sec_ID > $Sec_Orthogroup
    cat $Sec_Orthogroup | wc -l
    echo "The following secreted proteins were found in Race 2 unique orthogroups:"
    Sec_UK2_uniq_groups=$Sec_Dir/UK2_uniq_Sec_Orthogroups_hits.txt
    cat $Sec_Orthogroup | grep -v -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'Bc1|' -e 'Nov9|' | grep -e 'A4|' | grep -e 'Bc16|' > $Sec_UK2_uniq_groups
    cat $Sec_UK2_uniq_groups | wc -l
    echo "These orthogroups contain the following number of secreted proteins:"
    cat $Sec_UK2_uniq_groups | grep -w -o -f $Sec_ID | wc -l
    echo "The following secreted proteins were found in P.fragariae unique orthogroups:"
    Sec_Pf_uniq_groups=$Sec_Dir/Pf_Sec_Orthogroups_hits.txt
    cat $Sec_Orthogroup > $Sec_Pf_uniq_groups
    cat $Sec_Pf_uniq_groups | wc -l
    echo "These orthogroups contain the following number of Secreted proteins:"
    cat $Sec_Pf_uniq_groups | grep -w -o -f $Sec_ID | wc -l
done
```

```
The number of secreted proteins searched for is:
72,134
Of these, the following number were found in orthogroups:
11,487
These were distributed through the following number of Orthogroups:
5,930
The following secreted proteins were found in Race 2 unique orthogroups:
11
These orthogroups contain the following number of secreted proteins:
22
The following secreted proteins were found in P.fragariae unique orthogroups:
5,930
These orthogroups contain the following number of Secreted proteins:
11,487
```

## Race 2 secreted protein genes that not in orthogroups were identified

```bash
for num in 1
do
    Sec_UK2_uniq=$Sec_Dir/UK2_unique_Sec.txt
    cat $Sec_ID | grep -v -w -f $Sec_Orthogroup_hits > $Sec_UK2_uniq
    echo "The number of UK2 unique secreted proteins are:"
    cat $Sec_UK2_uniq | wc -l
    Final_genes_Bc16=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors_renamed.pep.fasta
    Final_genes_A4=gene_pred/annotation/P.fragariae/A4/A4_genes_incl_ORFeffectors.pep_renamed.fasta
    Bc16_Sec_UK2_uniq_fa=$Sec_Dir/Bc16_UK2_unique_Secs.fa
    A4_Sec_UK2_uniq_fa=$Sec_Dir/A4_UK2_unique_Secs.fa
    Bc16_to_extract=$Sec_Dir/Bc16_to_extract.txt
    A4_to_extract=$Sec_Dir/A4_to_extract.txt
    cat $Sec_UK2_uniq | grep 'Bc16|' | cut -f2 -d "|" > $Bc16_to_extract
    cat $Sec_UK2_uniq | grep 'A4|' | cut -f2 -d "|" > $A4_to_extract
    cat $Final_genes_Bc16 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Bc16_to_extract | grep -E -v '^--' > $Bc16_Sec_UK2_uniq_fa
    cat $Final_genes_A4 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $A4_to_extract | grep -E -v '^--' > $A4_Sec_UK2_uniq_fa
    echo "The number of BC-16 genes extracted is:"
    cat $Bc16_Sec_UK2_uniq_fa | grep '>' | wc -l
    echo "The number of A4 genes extracted is:"
    cat $A4_Sec_UK2_uniq_fa | grep '>' | wc -l
done
```

```
The number of UK2 unique secreted proteins are:
60,647
The number of BC-16 genes extracted is:
10,198
The number of A4 genes extracted is:
8,597
```

## Extracting fastas for orthogroups containing Race 2 secreted proteins

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_Secreted/UK2_Sec_Orthogroups.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_Secreted/orthogroups_fasta_UK2_Sec
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Extracting fastas for Pf orthogroups containing Race 2 secreted proteins

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_Secreted/Pf_Sec_Orthogroups_hits.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_Secreted/orthogroups_fasta_Pf_Sec
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Race 2 unique transcription factors and transcriptional regulators

## Race 2 TF/TRs were parsed to the same format as used in the analysis

```bash
for num in 1
do
    TF_Names_Bc16=analysis/transcription_factors/P.fragariae/Bc16/greedy/Bc16_TF_TR_Headers.txt
    TF_Names_A4=analysis/transcription_factors/P.fragariae/A4/greedy/A4_TF_TR_Headers.txt
    WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18
    TF_Dir=$WorkDir/UK2_TFs
    Orthogroups=$WorkDir/Orthogroups.txt
    TF_ID=$TF_Dir/UK2_TF_IDs.txt
    mkdir -p $TF_Dir
    cat $TF_Names_Bc16 | sed -r 's/^/Bc16|/g' > $TF_ID
    cat $TF_Names_A4 | sed -r 's/^/A4|/g' >> $TF_ID
done
```

## Orthology groups containing TF/TRs were identified

```bash
for num in 1
do
    echo "The number of TF/TRs searched for is:"
    cat $TF_ID | wc -l
    echo "Of these, the following number were found in orthogroups:"
    TF_Orthogroup_hits=$TF_Dir/UK2_TF_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $TF_ID > $TF_Orthogroup_hits
    cat $TF_Orthogroup_hits | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    TF_Orthogroup=$TF_Dir/UK2_TF_Orthogroups.txt
    cat $Orthogroups | grep -w -f $TF_ID > $TF_Orthogroup
    cat $TF_Orthogroup | wc -l
    echo "The following TF/TRs were found in Race 2 unique orthogroups:"
    TF_UK2_uniq_groups=$TF_Dir/UK2_uniq_TF_Orthogroups_hits.txt
    cat $TF_Orthogroup | grep -v -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'Bc1|' -e 'Nov9|' | grep -e 'A4|' | grep -e 'Bc16|' > $TF_UK2_uniq_groups
    cat $TF_UK2_uniq_groups | wc -l
    echo "These orthogroups contain the following number of TF/TRs:"
    cat $TF_UK2_uniq_groups | grep -w -o -f $TF_ID | wc -l
    echo "The following TF/TRs were found in P.fragariae unique orthogroups:"
    TF_Pf_uniq_groups=$TF_Dir/Pf_TF_Orthogroups_hits.txt
    cat $TF_Orthogroup > $TF_Pf_uniq_groups
    cat $TF_Pf_uniq_groups | wc -l
    echo "These orthogroups contain the following number of TF/TRs:"
    cat $TF_Pf_uniq_groups | grep -w -o -f $TF_ID | wc -l
done
```

```
The number of TF/TRs searched for is:
516
Of these, the following number were found in orthogroups:
511
These were distributed through the following number of Orthogroups:
234
The following TF/TRs were found in Race 2 unique orthogroups:
0
These orthogroups contain the following number of TF/TRs:
0
The following TF/TRs were found in P.fragariae unique orthogroups:
234
These orthogroups contain the following number of TF/TRs:
511
```

## The Race 2 TF/TRs that were not found in orthogroups were identified

```bash
for num in 1
do
    TF_UK2_uniq=$TF_Dir/UK2_unique_TF.txt
    cat $TF_ID | grep -v -w -f $TF_Orthogroup_hits > $TF_UK2_uniq
    echo "The number of UK2 unique TF/TRs are:"
    cat $TF_UK2_uniq | wc -l
    Final_genes_Bc16=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors_renamed.pep.fasta
    Final_genes_A4=gene_pred/annotation/P.fragariae/A4/A4_genes_incl_ORFeffectors_renamed.pep.fasta
    Bc16_TF_UK2_uniq_fa=$TF_Dir/Bc16_UK2_unique_TFs.fa
    A4_TF_UK2_uniq_fa=$TF_Dir/A4_UK2_unique_TFs.fa
    Bc16_to_extract=$TF_Dir/Bc16_to_extract.txt
    A4_to_extract=$TF_Dir/A4_to_extract.txt
    cat $TF_UK2_uniq | grep 'Bc16|' | cut -f2 -d "|" > $Bc16_to_extract
    cat $TF_UK2_uniq | grep 'A4|' | cut -f2 -d "|" > $A4_to_extract
    cat $Final_genes_Bc16 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Bc16_to_extract | grep -E -v '^--' > $Bc16_TF_UK2_uniq_fa
    cat $Final_genes_A4 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $A4_to_extract | grep -E -v '^--' > $A4_TF_UK2_uniq_fa
    echo "The number of BC-16 genes extracted is:"
    cat $Bc16_TF_UK2_uniq_fa | grep '>' | wc -l
    echo "The number of A4 genes extracted is:"
    cat $A4_TF_UK2_uniq_fa | grep '>' | wc -l
done
```

```
The number of UK2 unique TF/TRs are:
5
The number of BC-16 genes extracted is:
3
The number of A4 genes extracted is:
2
```

## Extracting fastas for orthogroups containing Race 2 putative TF/TRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_TFs/UK2_TF_Orthogroups.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_TFs/orthogroups_fasta_UK2_TF
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Extracting fastas for Pf orthogroups containing Race 2 putative TF/TRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_TFs/Pf_TF_Orthogroups_hits.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK2_TFs/orthogroups_fasta_Pf_TF
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Analysis of orthogroups unique to UK race 1 (Strains BC-1 & NOV-5)

## The genes unique to Race 1 were identified within the orthology analysis

## First variables were set

```bash
WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/
UK1UniqDir=$WorkDir/UK1_unique
Orthogroups=$WorkDir/Orthogroups.txt
GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
Final_genes_Bc1=gene_pred/annotation/P.fragariae/Bc1/Bc1_genes_incl_ORFeffectors_renamed.pep.fasta
Final_genes_Nov5=gene_pred/annotation/P.fragariae/Nov5/Nov5_genes_incl_ORFeffectors_renamed.pep.fasta
Uniq_UK1_groups=$UK1UniqDir/UK1_uniq_orthogroups.txt
mkdir -p $UK1UniqDir
```

## Orthogroups only containing Race 1 genes were extracted

```bash
for num in 1
do
    cat $Orthogroups | grep -v -e 'A4|' -e 'Nov27|' -e 'Nov71|' -e 'Bc16|' -e 'Nov9|' | grep -e 'Nov5|' | grep -e 'Bc1|' > $Uniq_UK1_groups
    echo "The number of orthogroups unique to Race UK1 are:"
    cat $Uniq_UK1_groups | wc -l
    echo "The following number genes are contained in these orthogroups:"
    cat $Uniq_UK1_groups | grep -v -e 'A4|' -e 'Nov27|' -e 'Nov71|' -e 'Bc16|' -e 'Nov9|' | grep -e 'Nov5|' | grep -e 'Bc1|' | grep -o '|' | wc -l
done
```

```
The number of orthogroups unique to Race 1 are:
36
The following number genes are contained in these orthogroups:
164
```

## Race 1 unique RxLR families

### Race 1 RxLRs were parsed to the same format as used in the analysis

```bash
for num in 1
do
    RxLR_Names_Bc1=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc1/Bc1_Total_RxLR_motif_hmm_renamed.txt
    RxLR_Names_Nov5=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov5/Nov5_Total_RxLR_motif_hmm_renamed.txt
    WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18
    RxLR_Dir=$WorkDir/UK1_RxLR
    Orthogroups=$WorkDir/Orthogroups.txt
    RxLR_ID=$RxLR_Dir/UK1_aug_RxLR_IDs.txt
    mkdir -p $RxLR_Dir
    cat $RxLR_Names_Bc1 | sed -r 's/^/Bc1|/g' > $RxLR_ID
    cat $RxLR_Names_Nov5 | sed -r 's/^/Nov5|/g' >> $RxLR_ID
done
```

## Orthology groups containing RxLR proteins were identified

```bash
for num in 1
do
    echo "The number of RxLRs searched for is:"
    cat $RxLR_ID | wc -l
    echo "Of these, the following number were found in orthogroups:"
    RxLR_Orthogroup_hits=$RxLR_Dir/UK1_RxLR_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $RxLR_ID > $RxLR_Orthogroup_hits
    cat $RxLR_Orthogroup_hits | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    RxLR_Orthogroup=$RxLR_Dir/UK1_RxLR_Orthogroups.txt
    cat $Orthogroups | grep -w -f $RxLR_ID > $RxLR_Orthogroup
    cat $RxLR_Orthogroup | wc -l
    echo "The following RxLRs were found in Race 1 unique orthogroups:"
    RxLR_UK1_uniq_groups=$RxLR_Dir/UK1_uniq_RxLR_Orthogroups_hits.txt
    cat $RxLR_Orthogroup | grep -v -e 'A4|' -e 'Nov27|' -e 'Nov71|' -e 'Bc16|' -e 'Nov9|' | grep -e 'Nov5|' | grep -e 'Bc1|' > $RxLR_UK1_uniq_groups
    cat $RxLR_UK1_uniq_groups | wc -l
    echo "These orthogroups contain the following number of RxLRs:"
    cat $RxLR_UK1_uniq_groups | grep -w -o -f $RxLR_ID | wc -l
    echo "The following RxLRs were found in P.fragariae unique orthogroups:"
    RxLR_Pf_uniq_groups=$RxLR_Dir/Pf_RxLR_Orthogroups_hits.txt
    cat $RxLR_Orthogroup > $RxLR_Pf_uniq_groups
    cat $RxLR_Pf_uniq_groups | wc -l
    echo "These orthogroups contain the following number of RxLRs:"
    cat $RxLR_Pf_uniq_groups | grep -w -o -f $RxLR_ID | wc -l
done
```

```
The number of RxLRs searched for is:
4,571
Of these, the following number were found in orthogroups:
4,571
These were distributed through the following number of Orthogroups:
2,230
The following RxLRs were found in Race 1 unique orthogroups:
2
These orthogroups contain the following number of RxLRs:
4
The following RxLRs were found in P.fragariae unique orthogroups:
2,230
These orthogroups contain the following number of RxLRs:
4,571
```

## The Race 1 RxLR genes that were not found in orthogroups were identified

```bash
for num in 1
do
    RxLR_UK1_uniq=$RxLR_Dir/UK1_unique_RxLRs.txt
    cat $RxLR_ID | grep -v -w -f $RxLR_Orthogroup_hits > $RxLR_UK1_uniq
    echo "The number of UK1 unique RxLRs are:"
    cat $RxLR_UK1_uniq | wc -l
    RxLR_Seq_Bc1=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc1/Bc1_final_RxLR_renamed.fa
    RxLR_Seq_Nov5=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov5/Nov5_final_RxLR_renamed.fa
    Final_genes_Bc1=gene_pred/annotation/P.fragariae/Bc1/Bc1_genes_incl_ORFeffectors.pep_renamed.fasta
    Final_genes_Nov5=gene_pred/annotation/P.fragariae/Nov5/Nov5_genes_incl_ORFeffectors.pep_renamed.fasta
    Bc1_RxLR_UK1_uniq_fa=$RxLR_Dir/Bc1_UK1_unique_RxLRs.fa
    Nov5_RxLR_UK1_uniq_fa=$RxLR_Dir/Nov5_UK1_unique_RxLRs.fa
    Bc1_to_extract=$RxLR_Dir/Bc1_to_extract.txt
    Nov5_to_extract=$RxLR_Dir/Nov5_to_extract.txt
    cat $RxLR_UK1_uniq | grep 'Bc1|' | cut -f2 -d "|" > $Bc1_to_extract
    cat $RxLR_UK1_uniq | grep 'Nov5|' | cut -f2 -d "|" > $Nov5_to_extract
    cat $Final_genes_Bc1 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Bc1_to_extract | grep -E -v '^--' > $Bc1_RxLR_UK1_uniq_fa
    cat $Final_genes_Nov5 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Nov5_to_extract | grep -E -v '^--' > $Nov5_RxLR_UK1_uniq_fa
    echo "The number of BC-1 genes extracted is:"
    cat $Bc1_RxLR_UK1_uniq_fa | grep '>' | wc -l
    echo "The number of NOV-5 genes extracted is:"
    cat $Nov5_RxLR_UK1_uniq_fa | grep '>' | wc -l
done
```

```
The number of UK1 unique RxLRs are:
0
The number of BC-1 genes extracted is:
0
The number of NOV-5 genes extracted is:
0
```

## Extracting fasta files for orthogroups containing Race 1 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_RxLR/UK1_RxLR_Orthogroups.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_RxLR/orthogroups_fasta_UK1_RxLR
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Extracting fastas for Pf orthogroups containing Race 1 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_RxLR/Pf_RxLR_Orthogroups_hits.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_RxLR/orthogroups_fasta_Pf_RxLR
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Race 1 unique Crinkler families

### Race 1 CRNs were parsed to the same format as used in the analysis

```bash
for num in 1
do
    CRN_Names_Bc1=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc1/Bc1_final_CRN_renamed.txt
    CRN_Names_Nov5=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov5/Nov5_final_CRN_renamed.txt
    WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18
    CRN_Dir=$WorkDir/UK1_CRN
    Orthogroups=$WorkDir/Orthogroups.txt
    CRN_ID_UK1=$CRN_Dir/UK1_CRN_hmmer_IDs.txt
    mkdir -p $CRN_Dir
    cat $CRN_Names_Bc1 | sed -r 's/^/Bc1|/g' > $CRN_ID_UK1
    cat $CRN_Names_Nov5 | sed -r 's/^/Nov5|/g' >> $CRN_ID_UK1
done
```

## Ortholog groups containing CRN proteins were identified

```bash
for num in 1
do
    echo "The number of CRNs searched for is:"
    cat $CRN_ID_UK1 | wc -l
    echo "Of these, the following number were found in orthogroups:"
    CRN_Orthogroup_hits_UK1=$CRN_Dir/UK1_CRN_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $CRN_ID_UK1 > $CRN_Orthogroup_hits_UK1
    cat $CRN_Orthogroup_hits_UK1 | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    CRN_Orthogroup_UK1=$CRN_Dir/UK1_CRN_Orthogroups.txt
    cat $Orthogroups | grep -w -f $CRN_ID_UK1 > $CRN_Orthogroup_UK1
    cat $CRN_Orthogroup_UK1 | wc -l
    echo "The following CRNs were found in Race 1 unique orthogroups:"
    CRN_UK1_uniq_groups=$CRN_Dir/UK1_uniq_CRN_Orthogroups_hits.txt
    cat $CRN_Orthogroup_UK1 | grep -v -e 'A4|' -e 'Nov27|' -e 'Nov71|' -e 'Bc16|' -e 'Nov9|' | grep -e 'Nov5|' | grep -e 'Bc1|' > $CRN_UK1_uniq_groups
    cat $CRN_UK1_uniq_groups | wc -l
    echo "The following CRNs were found in P.fragariae unique orthogroups:"
    CRN_Pf_uniq_groups=$CRN_Dir/Pf_CRN_Orthogroups_hits.txt
    cat $CRN_Orthogroup_UK1 > $CRN_Pf_uniq_groups
    cat $CRN_Pf_uniq_groups | wc -l
    echo "These orthogroups contain the following number of CRNs:"
    cat $CRN_Pf_uniq_groups | grep -w -o -f $CRN_ID_UK1 | wc -l
done
```

```
The number of CRNs searched for is:
216
Of these, the following number were found in orthogroups:
216
These were distributed through the following number of Orthogroups:
102
The following CRNs were found in Race 1 unique orthogroups:
0
The following CRNs were found in P.fragariae unique orthogroups:
102
These orthogroups contain the following number of CRNs:
216
```

## The Race 1 CRN genes not found in orthogroups were identified

```bash
for num in 1
do
    CRN_UK1_uniq=$CRN_Dir/UK1_unique_CRNs.txt
    cat $CRN_ID_UK1 | grep -v -w -f $CRN_Orthogroup_hits_UK1 > $CRN_UK1_uniq
    echo "The number of Race 1 unique CRNs are:"
    cat $CRN_UK1_uniq | wc -l
    CRN_Seq_Bc1=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc1/Bc1_final_CRN_renamed.fa
    CRN_Seq_Nov5=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov5/Nov5_final_CRN_renamed.fa
    Final_genes_Bc1=gene_pred/annotation/P.fragariae/Bc1/Bc1_genes_incl_ORFeffectors_renamed.pep.fasta
    Final_genes_Nov5=gene_pred/annotation/P.fragariae/Nov5/Nov5_genes_incl_ORFeffectors_renamed.pep.fasta
    Bc1_CRN_UK1_uniq_fa=$CRN_Dir/Bc1_UK1_unique_CRNs.fa
    Nov5_CRN_UK1_uniq_fa=$CRN_Dir/Nov5_UK1_unique_CRNs.fa
    Bc1_to_extract=$CRN_Dir/Bc1_to_extract.txt
    Nov5_to_extract=$CRN_Dir/Nov5_to_extract.txt
    cat $CRN_UK1_uniq | grep 'Bc1|' | cut -f2 -d "|" > $Bc1_to_extract
    cat $CRN_UK1_uniq | grep 'Nov5|' | cut -f2 -d "|" > $Nov5_to_extract
    cat $Final_genes_Bc1 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Bc1_to_extract | grep -E -v '^--' > $Bc1_CRN_UK1_uniq_fa
    cat $Final_genes_Nov5 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Nov5_to_extract | grep -E -v '^--' > $Nov5_CRN_UK1_uniq_fa
    echo "The number of BC-1 genes extracted is:"
    cat $Bc1_CRN_UK1_uniq_fa | grep '>' | wc -l
    echo "The number of NOV-5 genes extracted is:"
    cat $Nov5_CRN_UK1_uniq_fa | grep '>' | wc -l
done
```

```
The number of Race 1 unique CRNs are:
0
The number of BC-1 genes extracted is:
0
The number of NOV-5 genes extracted is:
0
```

## Extracting fasta files for orthogroups containing Race 1 putative CRNs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_CRN/UK1_CRN_Orthogroups.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_CRN/orthogroups_fasta_UK1_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Extracting fasta files for Pf orthogroups containing Race 1 putative CRNs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_CRN/Pf_CRN_Orthogroups_hits.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_CRN/orthogroups_fasta_Pf_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Race 1 unique Apoplastic effector families

## Race 1 Apoplastic effectors were parsed to same format as used in the analysis

```bash
for num in 1
do
    ApoP_Names_Bc1=analysis/ApoplastP/P.fragariae/Bc1/Bc1_Total_ApoplastP_renamed.txt
    ApoP_Names_Nov5=analysis/ApoplastP/P.fragariae/Nov5/Nov5_Total_ApoplastP_renamed.txt
    WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18
    ApoP_Dir=$WorkDir/UK1_ApoP
    Orthogroups=$WorkDir/Orthogroups.txt
    ApoP_ID_UK1=$ApoP_Dir/UK1_ApoP_IDs.txt
    mkdir -p $ApoP_Dir
    cat $ApoP_Names_Bc1 | sed -r 's/^/Bc1|/g' > $ApoP_ID_UK1
    cat $ApoP_Names_Nov5 | sed -r 's/^/Nov5|/g' >> $ApoP_ID_UK1
done
```

## Ortholog groups containing apoplastic effectors were identified

```bash
for num in 1
do
    echo "The number of apoplastic effectors searched for is:"
    cat $ApoP_ID_UK1 | wc -l
    echo "Of these, the following number were found in orthogroups:"
    ApoP_Orthogroup_hits_UK1=$ApoP_Dir/UK1_ApoP_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $ApoP_ID_UK1 > $ApoP_Orthogroup_hits_UK1
    cat $ApoP_Orthogroup_hits_UK1 | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    ApoP_Orthogroup_UK1=$ApoP_Dir/UK1_ApoP_Orthogroups.txt
    cat $Orthogroups | grep -w -f $ApoP_ID_UK1 > $ApoP_Orthogroup_UK1
    cat $ApoP_Orthogroup_UK1 | wc -l
    echo "The following apoplastic effectors were found in Race 1 unique orthogroups:"
    ApoP_UK1_uniq_groups=$ApoP_Dir/UK1_uniq_ApoP_Orthogroups_hits.txt
    cat $ApoP_Orthogroup_UK1 | grep -v -e 'Bc16|' -e 'Nov27|' -e 'Nov71|' -e 'A4|' -e 'Nov9|' | grep -e 'Bc1|' | grep -e 'Nov5|' > $ApoP_UK1_uniq_groups
    cat $ApoP_UK1_uniq_groups | wc -l
    echo "The following apoplastic effectors were found in P.fragariae unique orthogroups:"
    ApoP_Pf_uniq_groups=$ApoP_Dir/Pf_ApoP_Orthogroups_hits.txt
    cat $ApoP_Orthogroup_UK1 > $ApoP_Pf_uniq_groups
    cat $ApoP_Pf_uniq_groups | wc -l
    echo "These orthogroups contain the following number of apoplastic effectors:"
    cat $ApoP_Pf_uniq_groups | grep -w -o -f $ApoP_ID_UK1 | wc -l
done
```

```
The number of apoplastic effectors searched for is:
21,393
Of these, the following number were found in orthogroups:
2,806
These were distributed through the following number of Orthogroups:
1,513
The following apoplastic effectors were found in Race 1 unique orthogroups:
0
The following apoplastic effectors were found in P.fragariae unique orthogroups:
1,513
These orthogroups contain the following number of apoplastic effectors:
2,806
```

## The Race 1 apoplastic effectors not found in orthogroups were identified

```bash
for num in 1
do
    ApoP_UK1_uniq=$ApoP_Dir/UK1_unique_ApoP.txt
    cat $ApoP_ID_UK1 | grep -v -w -f $ApoP_Orthogroup_hits_UK1 > $ApoP_UK1_uniq
    echo "The number of UK1 unique apoplastic effectors are:"
    cat $ApoP_UK1_uniq | wc -l
    ApoP_Seq_Bc1=analysis/ApoplastP/P.fragariae/Bc1/Bc1_final_ApoplastP_renamed.fa
    ApoP_Seq_Nov5=analysis/ApoplastP/P.fragariae/Nov5/Nov5_final_ApoplastP_renamed.fa
    Final_genes_Bc1=gene_pred/annotation/P.fragariae/Bc1/Bc1_genes_incl_ORFeffectors_renamed.pep.fasta
    Final_genes_Nov5=gene_pred/annotation/P.fragariae/Nov5/Nov5_genes_incl_ORFeffectors_renamed.pep.fasta
    Bc1_ApoP_UK1_uniq_fa=$ApoP_Dir/Bc1_UK1_unique_ApoP.fa
    Nov5_ApoP_UK1_uniq_fa=$ApoP_Dir/Nov5_UK1_unique_ApoP.fa
    Bc1_to_extract=$ApoP_Dir/Bc1_to_extract.txt
    Nov5_to_extract=$ApoP_Dir/Nov5_to_extract.txt
    cat $ApoP_UK1_uniq | grep 'Bc1|' | cut -f2 -d "|" > $Bc1_to_extract
    cat $ApoP_UK1_uniq | grep 'Nov5|' | cut -f2 -d "|" > $Nov5_to_extract
    cat $Final_genes_Bc1 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Bc1_to_extract | grep -E -v '^--' > $Bc1_ApoP_UK1_uniq_fa
    cat $Final_genes_Nov5 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Nov5_to_extract | grep -E -v '^--' > $Nov5_ApoP_UK1_uniq_fa
    echo "The number of BC-1 genes extracted is:"
    cat $Bc1_ApoP_UK1_uniq_fa | grep '>' | wc -l
    echo "The number of Nov5 genes extracted is:"
    cat $Nov5_ApoP_UK1_uniq_fa | grep '>' | wc -l
done
```

```
The number of UK1 unique apoplastic effectors are:
18,587
The number of BC-1 genes extracted is:
9,336
The number of Nov5 genes extracted is:
9,251
```

## Extracting fasta files for orthogroups containing Race 1 putative apoplastic effectors

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_ApoP/UK1_ApoP_Orthogroups.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_ApoP/orthogroups_fasta_UK1_ApoP
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Extracting fastas for Pf orthogroups containing Race 1 putative apoplastic effectors

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_ApoP/Pf_ApoP_Orthogroups_hits.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_ApoP/orthogroups_fasta_Pf_ApoP
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Race 1 unique secreted proteins

## Race 1 secreted protein genes were parsed to the same format as used in the analysis

```bash
for num in 1
do
    Sec_Names_Bc1=gene_pred/combined_sigP_CQ/P.fragariae/Bc1/Bc1_secreted_renamed.txt
    Sec_Names_Nov5=gene_pred/combined_sigP_CQ/P.fragariae/Nov5/Nov5_secreted_renamed.txt
    Sec_Names_Bc1_ORFs=gene_pred/combined_sigP_ORF/P.fragariae/Bc1/Bc1_all_secreted_merged_renamed.txt
    Sec_Names_Nov5_ORFs=gene_pred/combined_sigP_ORF/P.fragariae/Nov5/Nov5_all_secreted_merged_renamed.txt
    WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18
    Sec_Dir=$WorkDir/UK1_Secreted
    Orthogroups=$WorkDir/Orthogroups.txt
    Sec_ID=$Sec_Dir/UK1_aug_Sec_IDs.txt
    mkdir -p $Sec_Dir
    cat $Sec_Names_Bc1 | sed -r 's/^/Bc1|/g' > $Sec_ID
    cat $Sec_Names_Nov5 | sed -r 's/^/Nov5|/g' >> $Sec_ID
    cat $Sec_Names_Bc1_ORFs | sed -r 's/^/Bc1|/g' | sed -r 's/$/.t1/g' >> $Sec_ID
    cat $Sec_Names_Nov5_ORFs | sed -r 's/^/Nov5|/g' | sed -r 's/$/.t1/g' >> $Sec_ID
done
```

## Orthology groups containing Secreted proteins were identified

```bash
for num in 1
do
    echo "The number of secreted proteins searched for is:"
    cat $Sec_ID | wc -l
    echo "Of these, the following number were found in orthogroups:"
    Sec_Orthogroup_hits=$Sec_Dir/UK1_Sec_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $Sec_ID > $Sec_Orthogroup_hits
    cat $Sec_Orthogroup_hits | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    Sec_Orthogroup=$Sec_Dir/UK1_Sec_Orthogroups.txt
    cat $Orthogroups | grep -w -f $Sec_ID > $Sec_Orthogroup
    cat $Sec_Orthogroup | wc -l
    echo "The following secreted proteins were found in Race 1 unique orthogroups:"
    Sec_UK1_uniq_groups=$Sec_Dir/UK1_uniq_Sec_Orthogroups_hits.txt
    cat $Sec_Orthogroup | grep -v -e 'A4|' -e 'Nov27|' -e 'Nov71|' -e 'Bc16|' -e 'Nov9|' | grep -e 'Nov5|' | grep -e 'Bc1|' > $Sec_UK1_uniq_groups
    cat $Sec_UK1_uniq_groups | wc -l
    echo "These orthogroups contain the following number of secreted proteins:"
    cat $Sec_UK1_uniq_groups | grep -w -o -f $Sec_ID | wc -l
    echo "The following secreted proteins were found in P.fragariae unique orthogroups:"
    Sec_Pf_uniq_groups=$Sec_Dir/Pf_Sec_Orthogroups_hits.txt
    cat $Sec_Orthogroup > $Sec_Pf_uniq_groups
    cat $Sec_Pf_uniq_groups | wc -l
    echo "These orthogroups contain the following number of Secreted proteins:"
    cat $Sec_Pf_uniq_groups | grep -w -o -f $Sec_ID | wc -l
done
```

```
The number of secreted proteins searched for is:
66,470
Of these, the following number were found in orthogroups:
10,612
These were distributed through the following number of Orthogroups:
5,495
The following secreted proteins were found in Race 1 unique orthogroups:
1
These orthogroups contain the following number of secreted proteins:
2
The following secreted proteins were found in P.fragariae unique orthogroups:
5,495
These orthogroups contain the following number of Secreted proteins:
10,612
```

## The Race 1 secreted protein genes that were not found in orthogroups were identified

```bash
for num in 1
do
    Sec_UK1_uniq=$Sec_Dir/UK1_unique_Sec.txt
    cat $Sec_ID | grep -v -w -f $Sec_Orthogroup_hits > $Sec_UK1_uniq
    echo "The number of UK1 unique secreted proteins are:"
    cat $Sec_UK1_uniq | wc -l
    Final_genes_Bc1=gene_pred/annotation/P.fragariae/Bc1/Bc1_genes_incl_ORFeffectors_renamed.pep.fasta
    Final_genes_Nov5=gene_pred/annotation/P.fragariae/Nov5/Nov5_genes_incl_ORFeffectors_renamed.pep.fasta
    Bc1_Sec_UK1_uniq_fa=$Sec_Dir/Bc1_UK1_unique_Secs.fa
    Nov5_Sec_UK1_uniq_fa=$Sec_Dir/Nov5_UK1_unique_Secs.fa
    Bc1_to_extract=$Sec_Dir/Bc1_to_extract.txt
    Nov5_to_extract=$Sec_Dir/Nov5_to_extract.txt
    cat $Sec_UK1_uniq | grep 'Bc1|' | cut -f2 -d "|" > $Bc1_to_extract
    cat $Sec_UK1_uniq | grep 'Nov5|' | cut -f2 -d "|" > $Nov5_to_extract
    cat $Final_genes_Bc1 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Bc1_to_extract | grep -E -v '^--' > $Bc1_Sec_UK1_uniq_fa
    cat $Final_genes_Nov5 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Nov5_to_extract | grep -E -v '^--' > $Nov5_Sec_UK1_uniq_fa
    echo "The number of BC-1 genes extracted is:"
    cat $Bc1_Sec_UK1_uniq_fa | grep '>' | wc -l
    echo "The number of Nov5 genes extracted is:"
    cat $Nov5_Sec_UK1_uniq_fa | grep '>' | wc -l
done
```

```
The number of UK1 unique secreted proteins are:
55,858
The number of BC-1 genes extracted is:
8,645
The number of Nov5 genes extracted is:
8,576
```

## Extracting fastas for orthogroups containing Race 1 putative secreted proteins

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_Secreted/UK1_Sec_Orthogroups.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_Secreted/orthogroups_fasta_UK1_Sec
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Extracting fastas for Pf orthogroups containing Race 1 putative secreted proteins

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_Secreted/Pf_Sec_Orthogroups_hits.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_Secreted/orthogroups_fasta_Pf_Sec
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Race 1 unique transcription factor and transcriptional regulator orthogroups

## Race 1 TF/TRs were parsed to the same format as the gene names used in the analysis

```bash
for num in 1
do
    TF_Names_Bc1=analysis/transcription_factors/P.fragariae/Bc1/greedy/Bc1_TF_TR_Headers.txt
    TF_Names_Nov5=analysis/transcription_factors/P.fragariae/Nov5/greedy/Nov5_TF_TR_Headers.txt
    WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18
    TF_Dir=$WorkDir/UK1_TFs
    Orthogroups=$WorkDir/Orthogroups.txt
    TF_ID=$TF_Dir/UK1_TF_IDs.txt
    mkdir -p $TF_Dir
    cat $TF_Names_Bc1 | sed -r 's/^/Bc1|/g' > $TF_ID
    cat $TF_Names_Nov5 | sed -r 's/^/Nov5|/g' >> $TF_ID
done
```

## Orthology groups containing TF/TRs were identified using the following commands

```bash
for num in 1
do
    echo "The number of TFs searched for is:"
    cat $TF_ID | wc -l
    echo "Of these, the following number were found in orthogroups:"
    TF_Orthogroup_hits=$TF_Dir/UK1_TF_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $TF_ID > $TF_Orthogroup_hits
    cat $TF_Orthogroup_hits | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    TF_Orthogroup=$TF_Dir/UK1_TF_Orthogroups.txt
    cat $Orthogroups | grep -w -f $TF_ID > $TF_Orthogroup
    cat $TF_Orthogroup | wc -l
    echo "The following TFs were found in Race 1 unique orthogroups:"
    TF_UK1_uniq_groups=$TF_Dir/UK1_uniq_TF_Orthogroups_hits.txt
    cat $TF_Orthogroup | grep -v -e 'A4|' -e 'Nov27|' -e 'Nov71|' -e 'Bc16|' -e 'Nov9|' | grep -e 'Nov5|' | grep -e 'Bc1|' > $TF_UK1_uniq_groups
    cat $TF_UK1_uniq_groups | wc -l
    echo "These orthogroups contain the following number of TFs:"
    cat $TF_UK1_uniq_groups | grep -w -o -f $TF_ID | wc -l
    echo "The following TFs were found in P.fragariae unique orthogroups:"
    TF_Pf_uniq_groups=$TF_Dir/Pf_TF_Orthogroups_hits.txt
    cat $TF_Orthogroup > $TF_Pf_uniq_groups
    cat $TF_Pf_uniq_groups | wc -l
    echo "These orthogroups contain the following number of TFs:"
    cat $TF_Pf_uniq_groups | grep -w -o -f $TF_ID | wc -l
done
```

```
The number of TFs searched for is:
497
Of these, the following number were found in orthogroups:
493
These were distributed through the following number of Orthogroups:
233
The following TFs were found in Race 1 unique orthogroups:
0
These orthogroups contain the following number of TFs:
0
The following TFs were found in P.fragariae unique orthogroups:
233
These orthogroups contain the following number of TFs:
493
```

## The Race 1 TF/TRs that were not found in orthogroups were identified

```bash
for num in 1
do
    TF_UK1_uniq=$TF_Dir/UK1_unique_TFs.txt
    cat $TF_ID | grep -v -w -f $TF_Orthogroup_hits > $TF_UK1_uniq
    echo "The number of UK1 unique TFs are:"
    cat $TF_UK1_uniq | wc -l
    Final_genes_Bc1=gene_pred/annotation/P.fragariae/Bc1/Bc1_genes_incl_ORFeffectors_renamed.pep.fasta
    Final_genes_Nov5=gene_pred/annotation/P.fragariae/Nov5/Nov5_genes_incl_ORFeffectors_renamed.pep.fasta
    Bc1_TF_UK1_uniq_fa=$TF_Dir/Bc1_UK1_unique_TFs.fa
    Nov5_TF_UK1_uniq_fa=$TF_Dir/Nov5_UK1_unique_TFs.fa
    Bc1_to_extract=$TF_Dir/Bc1_to_extract.txt
    Nov5_to_extract=$TF_Dir/Nov5_to_extract.txt
    cat $TF_UK1_uniq | grep 'Bc1|' | cut -f2 -d "|" > $Bc1_to_extract
    cat $TF_UK1_uniq | grep 'Nov5|' | cut -f2 -d "|" > $Nov5_to_extract
    cat $Final_genes_Bc1 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Bc1_to_extract | grep -E -v '^--' > $Bc1_TF_UK1_uniq_fa
    cat $Final_genes_Nov5 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Nov5_to_extract | grep -E -v '^--' > $Nov5_TF_UK1_uniq_fa
    echo "The number of BC-1 genes extracted is:"
    cat $Bc1_TF_UK1_uniq_fa | grep '>' | wc -l
    echo "The number of NOV-5 genes extracted is:"
    cat $Nov5_TF_UK1_uniq_fa | grep '>' | wc -l
done
```

```
The number of UK1 unique TFs are:
4
The number of BC-1 genes extracted is:
2
The number of NOV-5 genes extracted is:
2
```

## Extracting fasta files for orthogroups containing Race 1 putative TF/TRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_TFs/UK1_TF_Orthogroups.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_TFs/orthogroups_fasta_UK1_TF
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Extracting fasta files for P. fragariae orthogroups containing Race 1 TF/TRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_TFs/Pf_TF_Orthogroups_hits.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK1_TFs/orthogroups_fasta_Pf_TF
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Analysis of orthogroups unique to UK race 3 (Strains NOV-27, NOV-71 & NOV-9)

## The genes unique to Race 3 were identified within the orthology analysis

## First variables were set for UK3

```bash
WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18
UK3UniqDir=$WorkDir/UK3_unique
Orthogroups=$WorkDir/Orthogroups.txt
GoodProts=$WorkDir/goodProteins/goodProteins.fasta
Final_genes_Nov27=gene_pred/annotation/P.fragariae/Nov27/Nov27_genes_incl_ORFeffectors_renamed.pep.fasta
Final_genes_Nov71=gene_pred/annotation/P.fragariae/Nov71/Nov71_genes_incl_ORFeffectors_renamed.pep.fasta
Final_genes_Nov9=gene_pred/annotation/P.fragariae/Nov9/Nov9_genes_incl_ORFeffectors_renamed.pep.fasta
Uniq_UK3_groups=$UK3UniqDir/UK3_uniq_orthogroups.txt
mkdir -p $UK3UniqDir
```

## Orthogroups only containing Race 3 genes were extracted

```bash
for num in 1
do
    cat $Orthogroups | grep -v -e 'A4|' -e 'Nov5|' -e 'Bc1|' -e 'Bc16|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov9|' > $Uniq_UK3_groups
    echo "The number of orthogroups unique to Race UK3 are:"
    cat $Uniq_UK3_groups | wc -l
    echo "The following number genes are contained in these orthogroups:"
    cat $Uniq_UK3_groups | grep -v -e 'A4|' -e 'Nov5|' -e 'Bc1|' -e 'Bc16|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov9|' | grep -o '|' | wc -l
done
```

```
The number of orthogroups unique to Race 3 are:
22
The following number genes are contained in these orthogroups:
121
```

## Race 3 unique RxLR families

## Race 3 RxLR genes were parsed to the same format as used in the analysis

```bash
for num in 1
do
    RxLR_Names_Nov27=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov27/Nov27_Total_RxLR_motif_hmm_renamed.txt
    RxLR_Names_Nov71=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov71/Nov71_Total_RxLR_motif_hmm_renamed.txt
    RxLR_Names_Nov9=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov9/Nov9_Total_RxLR_motif_hmm_renamed.txt
    WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18
    RxLR_Dir=$WorkDir/UK3_RxLR
    Orthogroups=$WorkDir/Orthogroups.txt
    RxLR_ID=$RxLR_Dir/UK3_aug_RxLR_EER_IDs.txt
    mkdir -p $RxLR_Dir
    cat $RxLR_Names_Nov27 | sed -r 's/^/Nov27|/g' > $RxLR_ID
    cat $RxLR_Names_Nov71 | sed -r 's/^/Nov71|/g' >> $RxLR_ID
    cat $RxLR_Names_Nov9 | sed -r 's/^/Nov9|/g' >> $RxLR_ID
done
```

## Orthology groups containing RxLR proteins were identified for UK3

```bash
for num in 1
do
    echo "The number of RxLRs searched for is:"
    cat $RxLR_ID | wc -l
    echo "Of these, the following number were found in orthogroups:"
    RxLR_Orthogroup_hits=$RxLR_Dir/UK3_RxLR_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $RxLR_ID > $RxLR_Orthogroup_hits
    cat $RxLR_Orthogroup_hits | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    RxLR_Orthogroup=$RxLR_Dir/UK3_RxLR_Orthogroups.txt
    cat $Orthogroups | grep -w -f $RxLR_ID > $RxLR_Orthogroup
    cat $RxLR_Orthogroup | wc -l
    echo "The following RxLRs were found in Race 3 unique orthogroups:"
    RxLR_UK3_uniq_groups=$RxLR_Dir/UK3_uniq_RxLR_Orthogroups_hits.txt
    cat $RxLR_Orthogroup | grep -v -e 'A4|' -e 'Nov5|' -e 'Bc1|' -e 'Bc16|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov9|' > $RxLR_UK3_uniq_groups
    cat $RxLR_UK3_uniq_groups | wc -l
    echo "These orthogroups contain the following number of RxLRs:"
    cat $RxLR_UK3_uniq_groups | grep -w -o -f $RxLR_ID | wc -l
    echo "The following RxLRs were found in P.fragariae unique orthogroups:"
    RxLR_Pf_uniq_groups=$RxLR_Dir/Pf_RxLR_Orthogroups_hits.txt
    cat $RxLR_Orthogroup > $RxLR_Pf_uniq_groups
    cat $RxLR_Pf_uniq_groups | wc -l
    echo "These orthogroups contain the following number of RxLRs:"
    cat $RxLR_Pf_uniq_groups | grep -w -o -f $RxLR_ID | wc -l
done
```

```
The number of RxLRs searched for is:
6,854
Of these, the following number were found in orthogroups:
6,739
These were distributed through the following number of Orthogroups:
2,261
The following RxLRs were found in Race 3 unique orthogroups:
2
These orthogroups contain the following number of RxLRs:
6
The following RxLRs were found in P.fragariae unique orthogroups:
2,261
These orthogroups contain the following number of RxLRs:
6,854
```

## The Race 3 RxLR genes that were not found in orthogroups were identified

```bash
for num in 1
do
    RxLR_UK3_uniq=$RxLR_Dir/UK3_unique_RxLRs.txt
    cat $RxLR_ID | grep -v -w -f $RxLR_Orthogroup_hits > $RxLR_UK3_uniq
    echo "The number of UK3 unique RxLRs are:"
    cat $RxLR_UK3_uniq | wc -l
    RxLR_Seq_Nov27=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov27/Nov27_final_RxLR_renamed.fa
    RxLR_Seq_Nov71=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov71/Nov71_final_RxLR_renamed.fa
    RxLR_Seq_Nov9=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov9/Nov9_final_RxLR_renamed.fa
    Final_genes_Nov27=gene_pred/annotation/P.fragariae/Nov27/Nov27_genes_incl_ORFeffectors_renamed.pep.fasta
    Final_genes_Nov71=gene_pred/annotation/P.fragariae/Nov71/Nov71_genes_incl_ORFeffectors_renamed.pep.fasta
    Final_genes_Nov9=gene_pred/annotation/P.fragariae/Nov9/Nov9_genes_incl_ORFeffectors_renamed.pep.fasta
    Nov27_RxLR_UK3_uniq_fa=$RxLR_Dir/Nov27_UK3_unique_RxLRs.fa
    Nov71_RxLR_UK3_uniq_fa=$RxLR_Dir/Nov71_UK3_unique_RxLRs.fa
    Nov9_RxLR_UK3_uniq_fa=$RxLR_Dir/Nov9_UK3_unique_RxLRs.fa
    Nov27_to_extract=$RxLR_Dir/Nov27_to_extract.txt
    Nov71_to_extract=$RxLR_Dir/Nov71_to_extract.txt
    Nov9_to_extract=$RxLR_Dir/Nov9_to_extract.txt
    cat $RxLR_UK3_uniq | grep 'Nov27|' | cut -f2 -d "|" > $Nov27_to_extract
    cat $RxLR_UK3_uniq | grep 'Nov71|' | cut -f2 -d "|" > $Nov71_to_extract
    cat $RxLR_UK3_uniq | grep 'Nov9|' | cut -f2 -d "|" > $Nov9_to_extract
    cat $Final_genes_Nov27 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Nov27_to_extract | grep -E -v '^--' > $Nov27_RxLR_UK3_uniq_fa
    cat $Final_genes_Nov71 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Nov71_to_extract | grep -E -v '^--' > $Nov71_RxLR_UK3_uniq_fa
    cat $Final_genes_Nov9 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Nov9_to_extract | grep -E -v '^--' > $Nov9_RxLR_UK3_uniq_fa
    echo "The number of NOV-27 genes extracted is:"
    cat $Nov27_RxLR_UK3_uniq_fa | grep '>' | wc -l
    echo "The number of NOV-71 genes extracted is:"
    cat $Nov71_RxLR_UK3_uniq_fa | grep '>' | wc -l
    echo "The number of NOV-9 genes extracted is:"
    cat $Nov9_RxLR_UK3_uniq_fa | grep '>' | wc -l
done
```

```
The number of UK3 unique RxLRs are:
0
The number of NOV-27 genes extracted is:
0
The number of NOV-71 genes extracted is:
0
The number of NOV-9 genes extracted is:
0
```

## Extracting fasta files for orthogroups containing Race 3 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_RxLR/UK3_RxLR_Orthogroups.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_RxLR/orthogroups_fasta_UK3_RxLR
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Extracting fasta files for Pf orthogroups containing Race 3 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_RxLR/Pf_RxLR_Orthogroups_hits.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_RxLR/orthogroups_fasta_Pf_RxLR
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

## Race 3 unique Crinkler families

### Race 3 crinkler genes were parsed to the same format as used in the analysis

```bash
for num in 1
do
    CRN_Names_Nov27=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov27/Nov27_final_CRN_renamed.txt
    CRN_Names_Nov71=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov71/Nov71_final_CRN_renamed.txt
    CRN_Names_Nov9=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov9/Nov9_final_CRN_renamed.txt
    WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18
    CRN_Dir=$WorkDir/UK3_CRN
    Orthogroups=$WorkDir/Orthogroups.txt
    CRN_ID_UK3=$CRN_Dir/UK3_CRN_hmmer_IDs.txt
    mkdir -p $CRN_Dir
    cat $CRN_Names_Nov27 | sed 's/^/Nov27|/g' > $CRN_ID_UK3
    cat $CRN_Names_Nov71 | sed 's/^/Nov71|/g' >> $CRN_ID_UK3
    cat $CRN_Names_Nov9 | sed 's/^/Nov9|/g' >> $CRN_ID_UK3
done
```

#Ortholog groups containing CRN proteins were identified using the following commands:

```bash
for num in 1
do
    echo "The number of CRNs searched for is:"
    cat $CRN_ID_UK3 | wc -l
    echo "Of these, the following number were found in orthogroups:"
    CRN_Orthogroup_hits_UK3=$CRN_Dir/UK3_CRN_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $CRN_ID_UK3 > $CRN_Orthogroup_hits_UK3
    cat $CRN_Orthogroup_hits_UK3 | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    CRN_Orthogroup_UK3=$CRN_Dir/UK3_CRN_Orthogroups.txt
    cat $Orthogroups | grep -w -f $CRN_ID_UK3 > $CRN_Orthogroup_UK3
    cat $CRN_Orthogroup_UK3 | wc -l
    echo "The following CRNs were found in Race 3 unique orthogroups:"
    CRN_UK3_uniq_groups=$CRN_Dir/UK3_uniq_CRN_Orthogroups_hits.txt
    cat $CRN_Orthogroup_UK3 | grep -v -e 'A4|' -e 'Nov5|' -e 'Bc1|' -e 'Bc16|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov9|' > $CRN_UK3_uniq_groups
    cat $CRN_UK3_uniq_groups | wc -l
    echo "The following CRNs were found in P.fragariae unique orthogroups:"
    CRN_Pf_uniq_groups=$CRN_Dir/Pf_CRN_Orthogroups_hits.txt
    cat $CRN_Orthogroup_UK3 > $CRN_Pf_uniq_groups
    cat $CRN_Pf_uniq_groups | wc -l
    echo "These orthogroups contain the following number of CRNs:"
    cat $CRN_Pf_uniq_groups | grep -w -o -f $CRN_ID_UK3 | wc -l
done
```

```
The number of CRNs searched for is:
326
Of these, the following number were found in orthogroups:
326
These were distributed through the following number of Orthogroups:
105
The following CRNs were found in Race 3 unique orthogroups:
0
The following CRNs were found in P.fragariae unique orthogroups:
105
These orthogroups contain the following number of CRNs:
326
```

#The Race 3 CRN genes not found in orthogroups were identified:

```bash
for num in 1
do
    CRN_UK3_uniq=$CRN_Dir/UK3_unique_CRNs.txt
    cat $CRN_ID_UK3 | grep -v -w -f $CRN_Orthogroup_hits_UK3 > $CRN_UK3_uniq
    echo "The number of Race 3 unique CRNs are:"
    cat $CRN_UK3_uniq | wc -l
    Final_genes_Nov27=gene_pred/annotation/P.fragariae/Nov27/Nov27_genes_incl_ORFeffectors.pep.fasta
    Final_genes_Nov71=gene_pred/annotation/P.fragariae/Nov71/Nov71_genes_incl_ORFeffectors.pep.fasta
    Final_genes_Nov9=gene_pred/annotation/P.fragariae/Nov9/Nov9_genes_incl_ORFeffectors.pep.fasta
    Nov27_CRN_UK3_uniq_fa=$CRN_Dir/Nov27_UK3_unique_CRNs.fa
    Nov71_CRN_UK3_uniq_fa=$CRN_Dir/Nov71_UK3_unique_CRNs.fa
    Nov9_CRN_UK3_uniq_fa=$CRN_Dir/Nov9_UK3_unique_CRNs.fa
    Nov27_to_extract=$CRN_Dir/Nov27_to_extract.txt
    Nov71_to_extract=$CRN_Dir/Nov71_to_extract.txt
    Nov9_to_extract=$CRN_Dir/Nov9_to_extract.txt
    cat $CRN_UK3_uniq | grep 'Nov27|' | cut -f2 -d "|" > $Nov27_to_extract
    cat $CRN_UK3_uniq | grep 'Nov71|' | cut -f2 -d "|" > $Nov71_to_extract
    cat $CRN_UK3_uniq | grep 'Nov9|' | cut -f2 -d "|" > $Nov9_to_extract
    cat $Final_genes_Nov27 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Nov27_to_extract | grep -E -v '^--' > $Nov27_CRN_UK3_uniq_fa
    cat $Final_genes_Nov71 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Nov71_to_extract | grep -E -v '^--' > $Nov71_CRN_UK3_uniq_fa
    cat $Final_genes_Nov9 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Nov9_to_extract | grep -E -v '^--' > $Nov9_CRN_UK3_uniq_fa
    echo "The number of NOV-27 genes extracted is:"
    cat $Nov27_CRN_UK3_uniq_fa | grep '>' | wc -l
    echo "The number of NOV-71 genes extracted is:"
    cat $Nov71_CRN_UK3_uniq_fa | grep '>' | wc -l
    echo "The number of NOV-9 genes extracted is:"
    cat $Nov9_CRN_UK3_uniq_fa | grep '>' | wc -l
done
```

```
The number of Race 3 unique CRNs are:
0
The number of NOV-27 genes extracted is:
0
The number of NOV-71 genes extracted is:
0
The number of NOV-9 genes extracted is:
0
```

##Extracting fasta files for orthogroups containing Race 3 putative CRNs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_CRN/UK3_CRN_Orthogroups.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_CRN/orthogroups_fasta_UK3_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

##Extracting fasta files for P. fragariae orthogroups containing Race 3 putative CRNs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_CRN/Pf_CRN_Orthogroups_hits.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_CRN/orthogroups_fasta_Pf_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

##Race 3 unique Apoplastic effector families

#Race 3 Apoplastic effectors were parsed to the same format as the gene names used in the analysis:

```bash
for num in 1
do
    ApoP_Names_Nov27=analysis/ApoplastP/P.fragariae/Nov27/Nov27_Total_ApoplastP.txt
    ApoP_Names_Nov71=analysis/ApoplastP/P.fragariae/Nov71/Nov71_Total_ApoplastP.txt
    ApoP_Names_Nov9=analysis/ApoplastP/P.fragariae/Nov9/Nov9_Total_ApoplastP.txt
    WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18
    ApoP_Dir=$WorkDir/UK3_ApoP
    Orthogroups=$WorkDir/Orthogroups.txt
    ApoP_ID_UK3=$ApoP_Dir/UK3_ApoP_IDs.txt
    mkdir -p $ApoP_Dir
    cat $ApoP_Names_Nov27 | sed -r 's/^/Nov27|/g' > $ApoP_ID_UK3
    cat $ApoP_Names_Nov71 | sed -r 's/^/Nov71|/g' >> $ApoP_ID_UK3
    cat $ApoP_Names_Nov9 | sed -r 's/^/Nov9|/g' >> $ApoP_ID_UK3
done
```

#Ortholog groups containing apoplastic effectors were identified using the following commands:

```bash
for num in 1
do
    echo "The number of apoplastic effectors searched for is:"
    cat $ApoP_ID_UK3 | wc -l
    echo "Of these, the following number were found in orthogroups:"
    ApoP_Orthogroup_hits_UK3=$ApoP_Dir/UK3_ApoP_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $ApoP_ID_UK3 > $ApoP_Orthogroup_hits_UK3
    cat $ApoP_Orthogroup_hits_UK3 | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    ApoP_Orthogroup_UK3=$ApoP_Dir/UK3_ApoP_Orthogroups.txt
    cat $Orthogroups | grep -w -f $ApoP_ID_UK3 > $ApoP_Orthogroup_UK3
    cat $ApoP_Orthogroup_UK3 | wc -l
    echo "The following apoplastic effectors were found in Race 3 unique orthogroups:"
    ApoP_UK3_uniq_groups=$ApoP_Dir/UK3_uniq_ApoP_Orthogroups_hits.txt
    cat $ApoP_Orthogroup_UK3 | grep -v -e 'Nov5|' -e 'A4|' -e 'Bc16|' -e 'Bc1|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov9|' > $ApoP_UK3_uniq_groups
    cat $ApoP_UK3_uniq_groups | wc -l
    echo "The following apoplastic effectors were found in P.fragariae unique orthogroups:"
    ApoP_Pf_uniq_groups=$ApoP_Dir/Pf_ApoP_Orthogroups_hits.txt
    cat $ApoP_Orthogroup_UK3 > $ApoP_Pf_uniq_groups
    cat $ApoP_Pf_uniq_groups | wc -l
    echo "These orthogroups contain the following number of apoplastic effectors:"
    cat $ApoP_Pf_uniq_groups | grep -w -o -f $ApoP_ID_UK3 | wc -l
done
```

```
The number of apoplastic effectors searched for is:
32,146
Of these, the following number were found in orthogroups:
4,266
These were distributed through the following number of Orthogroups:
1,560
The following apoplastic effectors were found in Race 3 unique orthogroups:
0
The following apoplastic effectors were found in P.fragariae unique orthogroups:
1,560
These orthogroups contain the following number of apoplastic effectors:
4,266
```


#The Race 3 apoplastic effectors not found in orthogroups were identified:

```bash
for num in 1
do
    ApoP_UK3_uniq=$ApoP_Dir/UK3_unique_ApoP.txt
    cat $ApoP_ID_UK3 | grep -v -w -f $ApoP_Orthogroup_hits_UK3 > $ApoP_UK3_uniq
    echo "The number of UK3 unique apoplastic effectors are:"
    cat $ApoP_UK3_uniq | wc -l
    ApoP_Seq_Nov27=analysis/ApoplastP/P.fragariae/Nov27/Nov27_final_ApoplastP.fa
    ApoP_Seq_Nov71=analysis/ApoplastP/P.fragariae/Nov71/Nov71_final_ApoplastP.fa
    ApoP_Seq_Nov9=analysis/ApoplastP/P.fragariae/Nov9/Nov9_final_ApoplastP.fa
    Final_genes_Nov27=gene_pred/annotation/P.fragariae/Nov27/Nov27_genes_incl_ORFeffectors.pep.fasta
    Final_genes_Nov71=gene_pred/annotation/P.fragariae/Nov71/Nov71_genes_incl_ORFeffectors.pep.fasta
    Final_genes_Nov9=gene_pred/annotation/P.fragariae/Nov9/Nov9_genes_incl_ORFeffectors.pep.fasta
    Nov27_ApoP_UK3_uniq_fa=$ApoP_Dir/Nov27_UK3_unique_ApoP.fa
    Nov71_ApoP_UK3_uniq_fa=$ApoP_Dir/Nov71_UK3_unique_ApoP.fa
    Nov9_ApoP_UK3_uniq_fa=$ApoP_Dir/Nov9_UK3_unique_ApoP.fa
    Nov27_to_extract=$ApoP_Dir/Nov27_to_extract.txt
    Nov71_to_extract=$ApoP_Dir/Nov71_to_extract.txt
    Nov9_to_extract=$ApoP_Dir/Nov9_to_extract.txt
    cat $ApoP_UK3_uniq | grep 'Nov27|' | cut -f2 -d "|" > $Nov27_to_extract
    cat $ApoP_UK3_uniq | grep 'Nov71|' | cut -f2 -d "|" > $Nov71_to_extract
    cat $ApoP_UK3_uniq | grep 'Nov9|' | cut -f2 -d "|" > $Nov9_to_extract
    cat $Final_genes_Nov27 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $ApoP_UK3_uniq | grep -E -v '^--' > $Nov27_ApoP_UK3_uniq_fa
    cat $Final_genes_Nov71 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $ApoP_UK3_uniq | grep -E -v '^--' > $Nov71_ApoP_UK3_uniq_fa
    cat $Final_genes_Nov9 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $ApoP_UK3_uniq | grep -E -v '^--' > $Nov9_ApoP_UK3_uniq_fa
    echo "The number of NOV-27 genes extracted is:"
    cat $Nov27_ApoP_UK3_uniq_fa | grep '>' | wc -l
    echo "The number of NOV-71 genes extracted is:"
    cat $Nov71_ApoP_UK3_uniq_fa | grep '>' | wc -l
    echo "The number of NOV-9 genes extracted is:"
    cat $Nov9_ApoP_UK3_uniq_fa | grep '>' | wc -l
done
```

```
The number of UK3 unique apoplastic effectors are:
27,880
The number of NOV-27 genes extracted is:
0
The number of NOV-71 genes extracted is:
0
The number of NOV-9 genes extracted is:
0
```

##Extracting fasta files for orthogroups containing Race 3 putative apoplastic effectors

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_ApoP/UK3_ApoP_Orthogroups.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_ApoP/orthogroups_fasta_UK3_ApoP
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

##Extracting fasta files for P. fragariae orthogroups containing Race 3 putative apoplastic effectors

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_ApoP/Pf_ApoP_Orthogroups_hits.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_ApoP/orthogroups_fasta_Pf_ApoP
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

#Race 3 unique secreted proteins

#Race 3 secreted protein genes were parsed to the same format as the gene names used in the analysis:

```bash
for num in 1
do
    Sec_Names_Nov27=gene_pred/combined_sigP_CQ/P.fragariae/Nov27/Nov27_secreted.txt
    Sec_Names_Nov71=gene_pred/combined_sigP_CQ/P.fragariae/Nov71/Nov71_secreted.txt
    Sec_Names_Nov9=gene_pred/combined_sigP_CQ/P.fragariae/Nov9/Nov9_secreted.txt
    Sec_Names_Nov27_ORFs=gene_pred/combined_sigP_ORF/P.fragariae/Nov27/Nov27_all_secreted_merged.txt
    Sec_Names_Nov71_ORFs=gene_pred/combined_sigP_ORF/P.fragariae/Nov71/Nov71_all_secreted_merged.txt
    Sec_Names_Nov9_ORFs=gene_pred/combined_sigP_ORF/P.fragariae/Nov9/Nov9_all_secreted_merged.txt
    WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18
    Sec_Dir=$WorkDir/UK3_Secreted
    Orthogroups=$WorkDir/Orthogroups.txt
    Sec_ID=$Sec_Dir/UK3_aug_Sec_IDs.txt
    mkdir -p $Sec_Dir
    cat $Sec_Names_Nov27 | sed -r 's/^/Nov27|/g' > $Sec_ID
    cat $Sec_Names_Nov71 | sed -r 's/^/Nov71|/g' >> $Sec_ID
    cat $Sec_Names_Nov9 | sed -r 's/^/Nov9|/g' >> $Sec_ID
    cat $Sec_Names_Nov27_ORFs | sed -r 's/^/Nov27|/g' | sed -r 's/$/.t1/g' >> $Sec_ID
    cat $Sec_Names_Nov71_ORFs | sed -r 's/^/Nov71|/g' | sed -r 's/$/.t1/g' >> $Sec_ID
    cat $Sec_Names_Nov9_ORFs | sed -r 's/^/Nov9|/g' | sed -r 's/$/.t1/g' >> $Sec_ID
done
```

#Ortholog groups containing Secreted proteins were identified using the following commands:

```bash
for num in 1
do
    echo "The number of secreted proteins searched for is:"
    cat $Sec_ID | wc -l
    echo "Of these, the following number were found in orthogroups:"
    Sec_Orthogroup_hits=$Sec_Dir/UK3_Sec_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $Sec_ID > $Sec_Orthogroup_hits
    cat $Sec_Orthogroup_hits | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    Sec_Orthogroup=$Sec_Dir/UK3_Sec_Orthogroups.txt
    cat $Orthogroups | grep -w -f $Sec_ID > $Sec_Orthogroup
    cat $Sec_Orthogroup | wc -l
    echo "The following secreted proteins were found in Race 3 unique orthogroups:"
    Sec_UK3_uniq_groups=$Sec_Dir/UK3_uniq_Sec_Orthogroups_hits.txt
    cat $Sec_Orthogroup | grep -v -e 'A4|' -e 'Bc1|' -e 'Nov5|' -e 'Bc16|' | grep -e 'Nov9|' | grep -e 'Nov27|' | grep -e 'Nov71|' > $Sec_UK3_uniq_groups
    cat $Sec_UK3_uniq_groups | wc -l
    echo "These orthogroups contain the following number of secreted proteins:"
    cat $Sec_UK3_uniq_groups | grep -w -o -f $Sec_ID | wc -l
    echo "The following secreted proteins were found in P.fragariae unique orthogroups:"
    Sec_Pf_uniq_groups=$Sec_Dir/Pf_Sec_Orthogroups_hits.txt
    cat $Sec_Orthogroup > $Sec_Pf_uniq_groups
    cat $Sec_Pf_uniq_groups | wc -l
    echo "These orthogroups contain the following number of Secreted proteins:"
    cat $Sec_Pf_uniq_groups | grep -w -o -f $Sec_ID | wc -l
done
```

```
The number of secreted proteins searched for is:
99,722
Of these, the following number were found in orthogroups:
16,056
These were distributed through the following number of Orthogroups:
5,749
The following secreted proteins were found in Race 3 unique orthogroups:
3
These orthogroups contain the following number of secreted proteins:
7
The following secreted proteins were found in P.fragariae unique orthogroups:
5,749
These orthogroups contain the following number of Secreted proteins:
16,056
```

#The Race 3 secreted protein genes that were not found in orthogroups were identified:

```bash
for num in 1
do
    Sec_UK3_uniq=$Sec_Dir/UK3_unique_Sec.txt
    cat $Sec_ID | grep -v -w -f $Sec_Orthogroup_hits > $Sec_UK3_uniq
    echo "The number of UK3 unique secreted proteins are:"
    cat $Sec_UK3_uniq | wc -l
    Final_genes_Nov27=gene_pred/annotation/P.fragariae/Nov27/Nov27_genes_incl_ORFeffectors.pep.fasta
    Final_genes_Nov71=gene_pred/annotation/P.fragariae/Nov71/Nov71_genes_incl_ORFeffectors.pep.fasta
    Final_genes_Nov9=gene_pred/annotation/P.fragariae/Nov9/Nov9_genes_incl_ORFeffectors.pep.fasta
    Nov27_Sec_UK3_uniq_fa=$Sec_Dir/Nov27_UK3_unique_Secs.fa
    Nov71_Sec_UK3_uniq_fa=$Sec_Dir/Nov71_UK3_unique_Secs.fa
    Nov9_Sec_UK3_uniq_fa=$Sec_Dir/Nov9_UK3_unique_Secs.fa
    Nov27_to_extract=$Sec_Dir/Nov27_to_extract.txt
    Nov71_to_extract=$Sec_Dir/Nov71_to_extract.txt
    Nov9_to_extract=$Sec_Dir/Nov9_to_extract.txt
    cat $Sec_UK3_uniq | grep 'Nov27|' | cut -f2 -d "|" > $Nov27_to_extract
    cat $Sec_UK3_uniq | grep 'Nov71|' | cut -f2 -d "|" > $Nov71_to_extract
    cat $Sec_UK3_uniq | grep 'Nov9|' | cut -f2 -d "|" > $Nov9_to_extract
    cat $Final_genes_Nov27 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Nov27_to_extract | grep -E -v '^--' > $Nov27_Sec_UK3_uniq_fa
    cat $Final_genes_Nov71 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Nov71_to_extract | grep -E -v '^--' > $Nov71_Sec_UK3_uniq_fa
    cat $Final_genes_Nov9 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Nov9_to_extract | grep -E -v '^--' > $Nov9_Sec_UK3_uniq_fa
    echo "The number of NOV-27 genes extracted is:"
    cat $Nov27_Sec_UK3_uniq_fa | grep '>' | wc -l
    echo "The number of NOV-71 genes extracted is:"
    cat $Nov71_Sec_UK3_uniq_fa | grep '>' | wc -l
    echo "The number of NOV-9 genes extracted is:"
    cat $Nov9_Sec_UK3_uniq_fa | grep '>' | wc -l
done
```

```
The number of UK3 unique secreted proteins are:
83,666
The number of NOV-27 genes extracted is:
8,539
The number of NOV-71 genes extracted is:
8,570
The number of NOV-9 genes extracted is:
8,713
```

##Extracting fasta files for orthogroups containing Race 3 putative secreted proteins

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_Secreted/UK3_Sec_Orthogroups.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_Secreted/orthogroups_fasta_UK3_Sec
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```


##Extracting fasta files for P. fragariae orthogroups containing Race 3 putative secreted proteins

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_Secreted/Pf_Sec_Orthogroups_hits.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_Secreted/orthogroups_fasta_Pf_Sec
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

# Race 3 unique transcription factors and transcriptional regulators

# Race 3 transcription factors and transcriptional regulators were parsed to the same format as the gene names used in the analysis

```bash
for num in 1
do
    TF_Names_Nov27=analysis/transcription_factors/P.fragariae/Nov27/greedy/Nov27_TF_TR_Headers.txt
    TF_Names_Nov71=analysis/transcription_factors/P.fragariae/Nov71/greedy/Nov71_TF_TR_Headers.txt
    TF_Names_Nov9=analysis/transcription_factors/P.fragariae/Nov9/greedy/Nov9_TF_TR_Headers.txt
    WorkDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18
    TF_Dir=$WorkDir/UK3_TFs
    Orthogroups=$WorkDir/Orthogroups.txt
    TF_ID=$TF_Dir/UK3_TF_IDs.txt
    mkdir -p $TF_Dir
    cat $TF_Names_Nov27 | sed -r 's/^/Nov27|/g' > $TF_ID
    cat $TF_Names_Nov71 | sed -r 's/^/Nov71|/g' >> $TF_ID
    cat $TF_Names_Nov9 | sed -r 's/^/Nov9|/g' >> $TF_ID
done
```

# Orthology groups containing transcription factors and transcriptional regulators were identified using the following commands

```bash
for num in 1
do
    echo "The number of TFs searched for is:"
    cat $TF_ID | wc -l
    echo "Of these, the following number were found in orthogroups:"
    TF_Orthogroup_hits=$TF_Dir/UK3_TF_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $TF_ID > $TF_Orthogroup_hits
    cat $TF_Orthogroup_hits | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    TF_Orthogroup=$TF_Dir/UK3_TF_Orthogroups.txt
    cat $Orthogroups | grep -w -f $TF_ID > $TF_Orthogroup
    cat $TF_Orthogroup | wc -l
    echo "The following secreted proteins were found in Race 3 unique orthogroups:"
    TF_UK3_uniq_groups=$TF_Dir/UK3_uniq_TF_Orthogroups_hits.txt
    cat $TF_Orthogroup | grep -v -e 'A4|' -e 'Bc1|' -e 'Nov5|' -e 'Bc16|' | grep -e 'Nov9|' | grep -e 'Nov27|' | grep -e 'Nov71|' > $TF_UK3_uniq_groups
    cat $TF_UK3_uniq_groups | wc -l
    echo "These orthogroups contain the following number of TFs:"
    cat $TF_UK3_uniq_groups | grep -w -o -f $TF_ID | wc -l
    echo "The following TFs were found in P.fragariae unique orthogroups:"
    TF_Pf_uniq_groups=$TF_Dir/Pf_TF_Orthogroups_hits.txt
    cat $TF_Orthogroup > $TF_Pf_uniq_groups
    cat $TF_Pf_uniq_groups | wc -l
    echo "These orthogroups contain the following number of TFs:"
    cat $TF_Pf_uniq_groups | grep -w -o -f $TF_ID | wc -l
done
```

```
The number of TFs searched for is:
726
Of these, the following number were found in orthogroups:
720
These were distributed through the following number of Orthogroups:
234
The following secreted proteins were found in Race 3 unique orthogroups:
0
These orthogroups contain the following number of TFs:
0
The following TFs were found in P.fragariae unique orthogroups:
234
These orthogroups contain the following number of TFs:
720
```

# The Race 3 transcription factors and transcriptional regulators that were not found in orthogroups were identified

```bash
for num in 1
do
    TF_UK3_uniq=$TF_Dir/UK3_unique_TFs.txt
    cat $TF_ID | grep -v -w -f $TF_Orthogroup_hits > $TF_UK3_uniq
    echo "The number of UK3 unique TFs are:"
    cat $TF_UK3_uniq | wc -l
    Final_genes_Nov27=gene_pred/annotation/P.fragariae/Nov27/Nov27_genes_incl_ORFeffectors.pep.fasta
    Final_genes_Nov71=gene_pred/annotation/P.fragariae/Nov71/Nov71_genes_incl_ORFeffectors.pep.fasta
    Final_genes_Nov9=gene_pred/annotation/P.fragariae/Nov9/Nov9_genes_incl_ORFeffectors.pep.fasta
    Nov27_TF_UK3_uniq_fa=$TF_Dir/Nov27_UK3_unique_TFs.fa
    Nov71_TF_UK3_uniq_fa=$TF_Dir/Nov71_UK3_unique_TFs.fa
    Nov9_TF_UK3_uniq_fa=$TF_Dir/Nov9_UK3_unique_TFs.fa
    Nov27_to_extract=$TF_Dir/Nov27_to_extract.txt
    Nov71_to_extract=$TF_Dir/Nov71_to_extract.txt
    Nov9_to_extract=$TF_Dir/Nov9_to_extract.txt
    cat $TF_UK3_uniq | grep 'Nov27|' | cut -f2 -d "|" > $Nov27_to_extract
    cat $TF_UK3_uniq | grep 'Nov71|' | cut -f2 -d "|" > $Nov71_to_extract
    cat $TF_UK3_uniq | grep 'Nov9|' | cut -f2 -d "|" > $Nov9_to_extract
    cat $Final_genes_Nov27 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Nov27_to_extract | grep -E -v '^--' > $Nov27_TF_UK3_uniq_fa
    cat $Final_genes_Nov71 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Nov71_to_extract | grep -E -v '^--' > $Nov71_TF_UK3_uniq_fa
    cat $Final_genes_Nov9 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Nov9_to_extract | grep -E -v '^--' > $Nov9_TF_UK3_uniq_fa
    echo "The number of NOV-27 genes extracted is:"
    cat $Nov27_TF_UK3_uniq_fa | grep '>' | wc -l
    echo "The number of NOV-71 genes extracted is:"
    cat $Nov71_TF_UK3_uniq_fa | grep '>' | wc -l
    echo "The number of NOV-9 genes extracted is:"
    cat $Nov9_TF_UK3_uniq_fa | grep '>' | wc -l
done
```

```
The number of UK3 unique TFs are:
6
The number of NOV-27 genes extracted is:
2
The number of NOV-71 genes extracted is:
2
The number of NOV-9 genes extracted is:
2
```

## Extracting fasta files for orthogroups containing Race 3 putative transcription factors and transcriptional regulators

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_TFs/UK3_TF_Orthogroups.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_TFs/orthogroups_fasta_UK3_TF
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```


## Extracting fasta files for P. fragariae orthogroups containing Race 3 putative transcription factors and transcriptional regulators

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_TFs/Pf_TF_Orthogroups_hits.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK3_TFs/orthogroups_fasta_Pf_TF
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

#Extract fasta files for all unique orthogroups, including non-effector groups

```bash
for OrthogroupTxt in $(ls analysis/orthology/OrthoFinder/formatted/Results_Aug18/UK*_unique/*)
do
    Race=$(echo $OrthogroupTxt | rev | cut -f2 -d '/' | rev)
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/group_fastas/$Race
    mkdir -p $OutDir
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    echo $Race
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

#Produce a count table of the number of genes for each strain in each groups

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
OrthoFinder_output=analysis/orthology/OrthoFinder/formatted/Results_Aug18/Orthogroups.txt
OutName=analysis/orthology/OrthoFinder/formatted/Results_Aug18/count_table.tsv
$ProgDir/parse_orthogroups.py --orthogroups $OrthoFinder_output --out_dir $OutName
```

##Analyse this count table for expanded groups and write orthogroups to a text file 'UKX_expanded.txt'

```bash
cd analysis/orthology/OrthoFinder/formatted/Results_Aug18
python /home/adamst/git_repos/scripts/phytophthora_fragariae/orthology_counts.py
```

###Reformat the lists and extract full orthogroup details

```bash
for file in $(ls UK*_expanded.txt)
do
    while IFS=' ' read -r line
    do
        echo $line | sed 's/ //g' >> tmp.txt
    done < "$file"
    Start=$(basename "$file" .txt)
    New_File="$Start"_modified.txt
    while IFS=' ' read -r line
    do
        cat Orthogroups.txt | grep "$line" >> $New_File
    done < tmp.txt
    rm tmp.txt
done
```

##Extract FASTA files of expanded orthogroups

```bash
cd  ../../../../../
for Race in UK1 UK2 UK3
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/"$Race"_expanded_modified.txt
    GoodProt=analysis/orthology/OrthoFinder/formatted/Results_Aug18/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/OrthoFinder/formatted/Results_Aug18/"$Race"_expanded
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```
