#Methodology 4 from Andy's files - run on A4, BC-1, BC-16, BC-23, NOV-27, NOV-5, NOV-71, NOV-77, NOV-9, ONT-3, SCRP245_v2

##Analysis 1: No removal of BC-16 ORF effectors without expression before analysis

```bash
ProjDir=/home/groups/harrisonlab/project_files/phytophthora_fragariae
cd $ProjDir
IsolateAbrv=All_Strains_plus_rubi_no_removal
WorkDir=analysis/orthology/orthomcl/$IsolateAbrv
mkdir -p $WorkDir
mkdir -p $WorkDir/formatted
mkdir -p $WorkDir/goodProteins
mkdir -p $WorkDir/badProteins
```

##4.1 Format fasta files


###for A4

```bash
Taxon_code=A4
Fasta_file=gene_pred/annotation/P.fragariae/A4/A4_genes_incl_ORFeffectors.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for BC-1

```bash
Taxon_code=Bc1
Fasta_file=gene_pred/annotation/P.fragariae/Bc1/Bc1_genes_incl_ORFeffectors.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for BC-16

```bash
Taxon_code=Bc16
Fasta_file=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for BC-23

```bash
Taxon_code=Bc23
Fasta_file=gene_pred/annotation/P.fragariae/Bc23/Bc23_genes_incl_ORFeffectors.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for NOV-27

```bash
Taxon_code=Nov27
Fasta_file=gene_pred/annotation/P.fragariae/Nov27/Nov27_genes_incl_ORFeffectors.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for NOV-5

```bash
Taxon_code=Nov5
Fasta_file=gene_pred/annotation/P.fragariae/Nov5/Nov5_genes_incl_ORFeffectors.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for NOV-71

```bash
Taxon_code=Nov71
Fasta_file=gene_pred/annotation/P.fragariae/Nov71/Nov71_genes_incl_ORFeffectors.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for NOV-77

```bash
Taxon_code=Nov77
Fasta_file=gene_pred/annotation/P.fragariae/Nov77/Nov77_genes_incl_ORFeffectors.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for NOV-9

```bash
Taxon_code=Nov9
Fasta_file=gene_pred/annotation/P.fragariae/Nov9/Nov9_genes_incl_ORFeffectors.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for ONT-3

```bash
Taxon_code=ONT3
Fasta_file=gene_pred/annotation/P.fragariae/ONT3/ONT3_genes_incl_ORFeffectors.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for SCRP245_v2

```bash
Taxon_code=SCRP245_v2
Fasta_file=gene_pred/annotation/P.fragariae/SCRP245_v2/SCRP245_v2_genes_incl_ORFeffectors.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for SCRP249

```bash
Taxon_code=SCRP249
Fasta_file=../phytophthora_rubi/gene_pred/annotation/P.rubi/SCRP249/SCRP249_genes_incl_ORFeffectors.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for SCRP324

```bash
Taxon_code=SCRP324
Fasta_file=../phytophthora_rubi/gene_pred/annotation/P.rubi/SCRP324/SCRP324_genes_incl_ORFeffectors.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for SCRP333

```bash
Taxon_code=SCRP333
Fasta_file=../phytophthora_rubi/gene_pred/annotation/P.rubi/SCRP333/SCRP333_genes_incl_ORFeffectors.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

##4.2 Filter proteins into good and poor sets.

```bash
Input_dir=$WorkDir/formatted
Min_length=10
Max_percent_stops=20
Good_proteins_file=$WorkDir/goodProteins/goodProteins.fasta
Poor_proteins_file=$WorkDir/badProteins/poorProteins.fasta
orthomclFilterFasta $Input_dir $Min_length $Max_percent_stops $Good_proteins_file $Poor_proteins_file
```

##4.3.a Perform an all-vs-all blast of the proteins

```bash
BlastDB=$WorkDir/blastall/$IsolateAbrv.db

makeblastdb -in $Good_proteins_file -dbtype prot -out $BlastDB
BlastOut=$WorkDir/all-vs-all_results.tsv
mkdir -p $WorkDir/splitfiles

SplitDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/signal_peptides
$SplitDir/splitfile_500.py --inp_fasta $Good_proteins_file --out_dir $WorkDir/splitfiles --out_base goodProteins

ProgDir=/home/adamst/git_repos/scripts/phytophthora/pathogen/orthology  
for File in $(find $WorkDir/splitfiles)
do
    Jobs=$(qstat | grep 'blast_500' | grep 'qw' | wc -l)
    while [ $Jobs -gt 1 ]
    do
        sleep 3
        printf "."
        Jobs=$(qstat | grep 'blast_500' | grep 'qw' | wc -l)
    done
    printf "\n"
    echo $File
    BlastOut=$(echo $File | sed 's/.fa/.tab/g')
    qsub $ProgDir/blast_500.sh $BlastDB $File $BlastOut
done
```

##4.3.b Merge the all-vs-all blast results

```bash
MergeHits="$IsolateAbrv"_blast.tab
printf "" > $MergeHits
for Num in $(ls $WorkDir/splitfiles/*.tab | rev | cut -f1 -d '_' | rev | sort -n)
do
    File=$(ls $WorkDir/splitfiles/*_$Num)
    cat $File
done > $MergeHits
```

##4.4 Perform ortholog identification

```bash
ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
MergeHits="$IsolateAbrv"_blast.tab
GoodProts=$WorkDir/goodProteins/goodProteins.fasta
qsub $ProgDir/qsub_orthomcl.sh $MergeHits $GoodProts 5
```

##4.5.a Manual identification of numbers of orthologous and unique genes

```bash
for num in 1
do
    echo "The total number of orthogroups is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | wc -l
    echo "The total number of genes in orthogroups is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -o '|' | wc -l
    echo "The number of orthogroups common to P. rubi is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -e 'SCRP249|' | grep -e 'SCRP324|' | grep -e 'SCRP333|' | grep -v -e 'A4|' -e 'Bc1|' -e 'Bc16|' -e 'Bc23|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -e 'SCRP249|' | grep -e 'SCRP324|' | grep -e 'SCRP333|' | grep -v -e 'A4|' -e 'Bc1|' -e 'Bc16|' -e 'Bc23|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to P. fragariae is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'A4|' | grep -e 'Bc1|' | grep -e 'Bc16|' | grep -e 'Bc23|' | grep -e 'Nov5|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov77|' | grep -e 'Nov9|' | grep -e 'ONT3|' | grep -e 'SCRP245_v2|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'A4|' | grep -e 'Bc1|' | grep -e 'Bc16|' | grep -e 'Bc23|' | grep -e 'Nov5|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov77|' | grep -e 'Nov9|' | grep -e 'ONT3|' | grep -e 'SCRP245_v2|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to UK1 isolates is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc1|' | grep -e 'Nov5|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc1|' | grep -e 'Nov5|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to UK2 isolates is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'Bc1|' -e 'Bc23|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'Nov5|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc16|' | grep -e 'A4|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'Bc1|' -e 'Bc23|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'Nov5|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc16|' | grep -e 'A4|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to UK3 isolates is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov9|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov9|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to CA4 isolates is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'Nov9|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'ONT3|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'Nov9|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'ONT3|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to CA5 isolates is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'ONT3|' -e 'Nov9|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc23|' | grep -e 'Nov77|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'ONT3|' -e 'Nov9|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc23|' | grep -e 'Nov77|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to Unknown race isolates is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'Nov9|' -e 'A4|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'SCRP245_v2|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'Nov9|' -e 'A4|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'SCRP245_v2|' | grep -o '|' | wc -l
    echo "The number of orthogroups with only seven highly conserved target isolates is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc23|' -e 'Nov77|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' -e 'SCRP245_v2|' | grep -e 'Nov5|' | grep -e 'Nov27' | grep -e 'Nov71' | grep -e 'Bc16' | grep -e 'Nov9' | grep -e 'Bc1' | grep -e 'A4' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc23|' -e 'Nov77|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' -e 'SCRP245_v2|' | grep -e 'Nov5|' | grep -e 'Nov27' | grep -e 'Nov71' | grep -e 'Bc16' | grep -e 'Nov9' | grep -e 'Bc1' | grep -e 'A4' | grep -o '|' | wc -l
    echo "The number of orthogroups containing all seven highly conserved target isolates is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -e 'Nov5|' | grep -e 'Nov27' | grep -e 'Nov71' | grep -e 'Bc16' | grep -e 'Nov9' | grep -e 'Bc1' | grep -e 'A4' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -e 'Nov5|' | grep -e 'Nov27' | grep -e 'Nov71' | grep -e 'Bc16' | grep -e 'Nov9' | grep -e 'Bc1' | grep -e 'A4' | grep -o '|' | wc -l
done
```

```
The total number of orthogroups is:
23,072
The total number of genes in orthogroups is:
479,549
The number of orthogroups common to P. rubi is:
1,365
This represents the following number of genes:
4,296
The number of orthogroups common to P. fragariae is:
1,013
This represents the following number of genes:
12,177
The number of orthogroups common to UK1 isolates is:
8
This represents the following number of genes:
16
The number of orthogroups common to UK2 isolates is:
20
This represents the following number of genes:
40
The number of orthogroups common to UK3 isolates is:
7
This represents the following number of genes:
21
The number of orthogroups common to CA4 isolates is:
225
This represents the following number of genes:
548
The number of orthogroups common to CA5 isolates is:
8
This represents the following number of genes:
16
The number of orthogroups common to Unknown race isolates is:
180
This represents the following number of genes:
480
The number of orthogroups with only seven highly conserved target isolates is:
30
This represents the following number of genes:
209
The number of orthogroups containing all seven highly conserved target isolates is:
15,355
This represents the following number of genes:
438,816
```

Identification of orthogroups of closely related isolates for further analysis

```bash
for num in 1
do
    echo "The total number of shared orthogroups is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -e 'A4|' | grep -e 'Nov5|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Bc16|' | grep -e 'Nov9|' | grep -e 'Bc1|' | wc -l
    echo "The total number of genes in shared orthogroups is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -e 'A4|' | grep -e 'Nov5|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Bc16|' | grep -e 'Nov9|' | grep -e 'Bc1|' | grep -o '|' | wc -l
    echo "The total number of orthogroups is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc23|' -e 'SCRP245_v2' -e 'Nov77|' -e 'SCRP249' -e 'SCRP324' -e 'SCRP333' | wc -l
    echo "The total number of genes in orthogroups is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc23|' -e 'SCRP245_v2' -e 'Nov77|' -e 'SCRP249' -e 'SCRP324' -e 'SCRP333' | grep -o '|' | wc -l
    echo "The total number of UK1 orthogroups is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Nov27|' -e 'Nov71|' -e 'Bc16|' -e 'Nov9|' | grep -e 'Nov5|' | grep -e 'Bc1|' | wc -l
    echo "The total number of genes in UK1 orthogroups is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Nov27|' -e 'Nov71|' -e 'Bc16|' -e 'Nov9|' | grep -e 'Nov5|' | grep -e 'Bc1|' | grep -o '|' | wc -l
    echo "The total number of UK2 orthogroups is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'Bc1|' -e 'Nov9|' | grep -e 'A4|' | grep -e 'Bc16|' | wc -l
    echo "The total number of genes in UK2 orthogroups is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'Bc1|' -e 'Nov9|' | grep -e 'A4|' | grep -e 'Bc16|' | grep -o '|' | wc -l
    echo "The total number of UK3 orthogroups is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'Nov5|' -e 'A4|' -e 'Bc16|' -e 'Bc1|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov9|' | wc -l
    echo "The total number of genes in UK3 orthogroups is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'Nov5|' -e 'A4|' -e 'Bc16|' -e 'Bc1|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov9|' | grep -o '|' | wc -l
done
```

```
The total number of shared orthogroups is:
15,267
The total number of genes in shared orthogroups is:
437,756
The total number of orthogroups is:
487
The total number of genes in orthogroups is:
1,427
The total number of UK1 orthogroups is:
36
The total number of genes in UK1 orthogroups is:
144
The total number of UK2 orthogroups is:
58
The total number of genes in UK2 orthogroups is:
220
The total number of UK3 orthogroups is:
15
The total number of genes in UK3 orthogroups is:
73
```

##4.5.b Plot venn diagrams:

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
$ProgDir/UK1_Pf_venn_diag.r --inp $WorkDir/"$IsolateAbrv"_orthogroups.tab --out $WorkDir/"$IsolateAbrv"_UK1_orthogroups.pdf
$ProgDir/UK2_Pf_venn_diag.r --inp $WorkDir/"$IsolateAbrv"_orthogroups.tab --out $WorkDir/"$IsolateAbrv"_UK2_orthogroups.pdf
$ProgDir/UK3_Pf_venn_diag.r --inp $WorkDir/"$IsolateAbrv"_orthogroups.tab --out $WorkDir/"$IsolateAbrv"_UK3_orthogroups.pdf
```

Output was a pdf file of the venn diagram.

The following additional information was also provided. The format of the following lines is as follows:

Isolate name (total number of orthogroups) number of unique singleton genes number of unique groups of inparalogs

###UK race 1 focused analysis

```
A4
The total number of orthogroups and singleton genes in this isolate:  18,521
The total number of orthogroups and singleton genes not in the venn diagram:  3,015
The total number of singleton genes not in the venn diagram:  1,079
NOV-5
The total number of orthogroups and singleton genes in this isolate:  18,503
The total number of orthogroups and singleton genes not in the venn diagram:  1,894
The total number of singleton genes not in the venn diagram:  1,125
NOV-27
The total number of orthogroups and singleton genes in this isolate:  18,495
The total number of orthogroups and singleton genes not in the venn diagram:  2,989
The total number of singleton genes not in the venn diagram:  1,075
NOV-71
The total number of orthogroups and singleton genes in this isolate:  18,432
The total number of orthogroups and singleton genes not in the venn diagram:  2,926
The total number of singleton genes not in the venn diagram:  1,013
BC-16
The total number of orthogroups and singleton genes in this isolate:  19,270
The total number of orthogroups and singleton genes not in the venn diagram:  3,764
The total number of singleton genes not in the venn diagram:  2,007
NOV-9
The total number of orthogroups and singleton genes in this isolate:  18,417
The total number of orthogroups and singleton genes not in the venn diagram:  2,911
The total number of singleton genes not in the venn diagram:  1,048
BC-1
The total number of orthogroups and singleton genes in this isolate:  18,466
The total number of orthogroups and singleton genes not in the venn diagram:  1,834
The total number of singleton genes not in the venn diagram:  1,078
```

###UK race 2 focused analysis

```
A4
The total number of orthogroups and singleton genes in this isolate:  18,486
The total number of orthogroups and singleton genes not in the venn diagram:  1,407
The total number of singleton genes not in the venn diagram:  1,060
NOV-5
The total number of orthogroups and singleton genes in this isolate:  18,528
The total number of orthogroups and singleton genes not in the venn diagram:  2,520
The total number of singleton genes not in the venn diagram:  1,109
NOV-27
The total number of orthogroups and singleton genes in this isolate:  18,503
The total number of orthogroups and singleton genes not in the venn diagram:  2,495
The total number of singleton genes not in the venn diagram:  1,083
NOV-71
The total number of orthogroups and singleton genes in this isolate:  18,363
The total number of orthogroups and singleton genes not in the venn diagram:  2,355
The total number of singleton genes not in the venn diagram:  1,020
BC-16
The total number of orthogroups and singleton genes in this isolate:  19,278
The total number of orthogroups and singleton genes not in the venn diagram:  1,492
The total number of singleton genes not in the venn diagram:  2,006
NOV-9
The total number of orthogroups and singleton genes in this isolate:  18,326
The total number of orthogroups and singleton genes not in the venn diagram:  2,318
The total number of singleton genes not in the venn diagram:  1,033
BC-1
The total number of orthogroups and singleton genes in this isolate:  18,531
The total number of orthogroups and singleton genes not in the venn diagram:  2,318
The total number of singleton genes not in the venn diagram:  1,062
```

###UK race 3 focused analysis

```
A4
The total number of orthogroups and singleton genes in this isolate:  18,486
The total number of orthogroups and singleton genes not in the venn diagram:  2,768
The total number of singleton genes not in the venn diagram:  1,060
NOV-5
The total number of orthogroups and singleton genes in this isolate:  18,528
The total number of orthogroups and singleton genes not in the venn diagram:  2,810
The total number of singleton genes not in the venn diagram:  1,109
NOV-27
The total number of orthogroups and singleton genes in this isolate:  18,503
The total number of orthogroups and singleton genes not in the venn diagram:  1,730
The total number of singleton genes not in the venn diagram:  1,083
NOV-71
The total number of orthogroups and singleton genes in this isolate:  18,363
The total number of orthogroups and singleton genes not in the venn diagram:  1,650
The total number of singleton genes not in the venn diagram:  1,020
BC-16
The total number of orthogroups and singleton genes in this isolate:  19,278
The total number of orthogroups and singleton genes not in the venn diagram:  3,560
The total number of singleton genes not in the venn diagram:  2,006
NOV-9
The total number of orthogroups and singleton genes in this isolate:  18,326
The total number of orthogroups and singleton genes not in the venn diagram:  1,639
The total number of singleton genes not in the venn diagram:  1,033
BC-1
The total number of orthogroups and singleton genes in this isolate:  18,531
The total number of orthogroups and singleton genes not in the venn diagram:  2,608
The total number of singleton genes not in the venn diagram:  1,062
```

#Analysis of orthogroups unique to UK race 2 (Strains BC-16 & A4)

##The genes unique to Race 2 were identified within the orthology analysis

##First variables were set:

```bash
WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal
UK2UniqDir=$WorkDir/UK2_unique
Orthogroups=$WorkDir/All_Strains_plus_rubi_no_removal_orthogroups.txt
GoodProts=$WorkDir/goodProteins/goodProteins.fasta
Final_genes_Bc16=gene_pred/codingquary/P.fragariae/Bc16/final/final_genes_combined.pep.fasta
Final_genes_A4=gene_pred/codingquary/P.fragariae/A4/final/final_genes_combined.pep.fasta
Uniq_UK2_groups=$UK2UniqDir/UK2_uniq_orthogroups.txt
mkdir -p $UK2UniqDir
```

#Orthogroups only containing Race 2 genes were extracted:

##Bars are to prevent incorrect filtering

```bash
cat $Orthogroups | grep -v -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'Bc1|' -e 'Nov9|' | grep -e 'A4|' | grep -e 'Bc16|' > $Uniq_UK2_groups
echo "The number of orthogroups unique to Race UK2 are:"
cat $Uniq_UK2_groups | wc -l
echo "The following number genes are contained in these orthogroups:"
cat $Uniq_UK2_groups | grep -v -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'Bc1|' -e 'Nov9|' | grep -e 'A4|' | grep -e 'Bc16|' | grep -o '|' | wc -l
```

```
The number of orthogroups unique to Race 2 are:
47
The following number genes are contained in these orthogroups:
201
```

#Race 2 unique RxLR families

#Race 2 RxLR genes were parsed to the same format as the gene names used in the analysis:

```bash
for num in 1
do
    RxLR_Names_Bc16=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_Total_RxLR_motif_hmm.txt
    RxLR_Names_A4=analysis/RxLR_effectors/combined_evidence/P.fragariae/A4/A4_Total_RxLR_motif_hmm.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal
    RxLR_Dir=$WorkDir/UKR2_RxLR
    Orthogroups=$WorkDir/All_Strains_plus_rubi_no_removal_orthogroups.txt
    RxLR_ID=$RxLR_Dir/UKR2_aug_RxLR_EER_IDs.txt
    mkdir -p $RxLR_Dir
    cat $RxLR_Names_Bc16 | sed -r 's/^/Bc16|/g' > $RxLR_ID
    cat $RxLR_Names_A4 | sed -r 's/^/A4|/g' >> $RxLR_ID
done
```

#Ortholog groups containing RxLR proteins were identified using the following commands:

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
4,854
Of these, the following number were found in orthogroups:
4,757
These were distributed through the following number of Orthogroups:
2,053
The following RxLRs were found in Race 2 unique orthogroups:
8
These orthogroups contain the following number of RxLRs:
17
The following RxLRs were found in P.fragariae unique orthogroups:
2,053
These orthogroups contain the following number of RxLRs:
4,757
```

#The Race 2 RxLR genes that were not found in orthogroups were identified:

```bash
for num in 1
do
    RxLR_UK2_uniq=$RxLR_Dir/UK2_unique_RxLRs.txt
    cat $RxLR_ID | grep -v -w -f $RxLR_Orthogroup_hits > $RxLR_UK2_uniq
    echo "The number of UK2 unique RxLRs are:"
    cat $RxLR_UK2_uniq | wc -l
    RxLR_Seq_Bc16=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_final_RxLR.fa
    RxLR_Seq_A4=analysis/RxLR_effectors/combined_evidence/P.fragariae/A4/A4_final_RxLR.fa
    Final_genes_Bc16=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors.pep.fasta
    Final_genes_A4=gene_pred/annotation/P.fragariae/A4/A4_genes_incl_ORFeffectors.pep.fasta
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
97
The number of BC-16 genes extracted is:
59
The number of A4 genes extracted is:
38
```

##Extracting fasta files for orthogroups containing Race 2 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UKR2_RxLR/UK2_RxLR_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UKR2_RxLR/orthogroups_fasta_UK2_RxLR
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```


##Extracting fasta files for P. fragariae orthogroups containing Race 2 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UKR2_RxLR/Pf_RxLR_Orthogroups_hits.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UKR2_RxLR/orthogroups_fasta_Pf_RxLR
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

#Race 2 unique secreted proteins

#Race 2 secreted protein genes were parsed to the same format as the gene names used in the analysis:

```bash
for num in 1
do
    Sec_Names_Bc16=gene_pred/combined_sigP_CQ/P.fragariae/Bc16/Bc16_secreted.txt
    Sec_Names_A4=gene_pred/combined_sigP_CQ/P.fragariae/A4/A4_secreted.txt
    Sec_Names_Bc16_ORFs=gene_pred/combined_sigP_ORF/P.fragariae/Bc16/Bc16_all_secreted_merged.txt
    Sec_Names_A4_ORFs=gene_pred/combined_sigP_ORF/P.fragariae/A4/A4_all_secreted_merged.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal
    Sec_Dir=$WorkDir/UKR2_Secreted
    Orthogroups=$WorkDir/All_Strains_plus_rubi_no_removal_orthogroups.txt
    Sec_ID=$Sec_Dir/UKR2_aug_Sec_IDs.txt
    mkdir -p $Sec_Dir
    cat $Sec_Names_Bc16 | sed -r 's/^/Bc16|/g' > $Sec_ID
    cat $Sec_Names_A4 | sed -r 's/^/A4|/g' >> $Sec_ID
    cat $Sec_Names_Bc16_ORFs | sed -r 's/^/Bc16|/g' | sed -r 's/$/.t1/g' >> $Sec_ID
    cat $Sec_Names_A4_ORFs | sed -r 's/^/A4|/g' | sed -r 's/$/.t1/g' >> $Sec_ID
done
```

#Ortholog groups containing Secreted proteins were identified using the following commands:

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
72,304
Of these, the following number were found in orthogroups:
11,103
These were distributed through the following number of Orthogroups:
4,396
The following secreted proteins were found in Race 2 unique orthogroups:
10
These orthogroups contain the following number of secreted proteins:
18
The following secreted proteins were found in P.fragariae unique orthogroups:
4,396
These orthogroups contain the following number of Secreted proteins:
11,103
```

#The Race 2 secreted protein genes that were not found in orthogroups were identified:

```bash
for num in 1
do
    Sec_UK2_uniq=$Sec_Dir/UK2_unique_Sec.txt
    cat $Sec_ID | grep -v -w -f $Sec_Orthogroup_hits > $Sec_UK2_uniq
    echo "The number of UK2 unique secreted proteins are:"
    cat $Sec_UK2_uniq | wc -l
    Final_genes_Bc16=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors.pep.fasta
    Final_genes_A4=gene_pred/annotation/P.fragariae/A4/A4_genes_incl_ORFeffectors.pep.fasta
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
332
The number of BC-16 genes extracted is:
209
The number of A4 genes extracted is:
123
```

##Extracting fasta files for orthogroups containing Race 2 putative secreted proteins

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UKR2_Secreted/UK2_Sec_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UKR2_Secreted/orthogroups_fasta_UK2_Sec
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```


##Extracting fasta files for P. fragariae orthogroups containing Race 2 putative secreted proteins

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UKR2_Secreted/Pf_Sec_Orthogroups_hits.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UKR2_Secreted/orthogroups_fasta_Pf_Sec
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

##Race 2 unique Crinkler families

#Race 2 crinkler genes were parsed to the same format as the gene names used in the analysis:

```bash
for num in 1
do
    CRN_Names_Bc16=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc16/Bc16_final_CRN.txt
    CRN_Names_A4=analysis/CRN_effectors/hmmer_CRN/P.fragariae/A4/A4_final_CRN.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal
    CRN_Dir=$WorkDir/UK2_CRN
    Orthogroups=$WorkDir/All_Strains_plus_rubi_no_removal_orthogroups.txt
    CRN_ID_UK2=$CRN_Dir/UK2_CRN_hmmer_IDs.txt
    mkdir -p $CRN_Dir
    cat $CRN_Names_Bc16 | sed -r 's/^/Bc16|/g' > $CRN_ID_UK2
    cat $CRN_Names_A4 | sed -r 's/^/A4|/g' >> $CRN_ID_UK2
done
```

#Ortholog groups containing CRN proteins were identified using the following commands:

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
243
Of these, the following number were found in orthogroups:
243
These were distributed through the following number of Orthogroups:
73
The following CRNs were found in Race 2 unique orthogroups:
0
The following CRNs were found in P.fragariae unique orthogroups:
73
These orthogroups contain the following number of CRNs:
243
```


#The Race 2 CRN genes not found in orthogroups were identified:

```bash
for num in 1
do
    CRN_UK2_uniq=$CRN_Dir/UK2_unique_CRNs.txt
    cat $CRN_ID_UK2 | grep -v -w -f $CRN_Orthogroup_hits_UK2 > $CRN_UK2_uniq
    echo "The number of UK2 unique CRNs are:"
    cat $CRN_UK2_uniq | wc -l
    CRN_Seq_Bc16=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc16/Bc16_final_CRN.fa
    CRN_Seq_A4=analysis/CRN_effectors/hmmer_CRN/P.fragariae/A4/A4_final_CRN.fa
    Final_genes_Bc16=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors.pep.fasta
    Final_genes_A4=gene_pred/annotation/P.fragariae/A4/A4_genes_incl_ORFeffectors.pep.fasta
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
The number of Race 2 unique CRNs are:
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
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK2_CRN/UK2_CRN_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK2_CRN/orthogroups_fasta_UK2_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

##Extracting fasta files for P. fragariae orthogroups containing Race 2 putative CRNs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK2_CRN/Pf_CRN_Orthogroups_hits.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK2_CRN/orthogroups_fasta_Pf_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

#Analysis of orthogroups unique to UK race 1 (Strains BC-1 & NOV-5)

##The genes unique to Race 1 were identified within the orthology analysis

##First variables were set:

```bash
WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal
UK1UniqDir=$WorkDir/UK1_unique
Orthogroups=$WorkDir/All_Strains_plus_rubi_no_removal_orthogroups.txt
GoodProts=$WorkDir/goodProteins/goodProteins.fasta
Final_genes_Bc1=gene_pred/codingquary/P.fragariae/Bc1/final/final_genes_combined.pep.fasta
Final_genes_Nov5=gene_pred/codingquary/P.fragariae/Nov5/final/final_genes_combined.pep.fasta
Uniq_UK1_groups=$UK1UniqDir/UK1_uniq_orthogroups.txt
mkdir -p $UK1UniqDir
```

#Orthogroups only containing Race 1 genes were extracted:

##Bars are to prevent incorrect filtering

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
15
The following number genes are contained in these orthogroups:
48
```

#Race 1 unique RxLR families

#Race 1 RxLR genes were parsed to the same format as the gene names used in the analysis:

```bash
for num in 1
do
    RxLR_Names_Bc1=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc1/Bc1_Total_RxLR_motif_hmm.txt
    RxLR_Names_Nov5=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov5/Nov5_Total_RxLR_motif_hmm.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal
    RxLR_Dir=$WorkDir/UK1_RxLR
    Orthogroups=$WorkDir/All_Strains_plus_rubi_no_removal_orthogroups.txt
    RxLR_ID=$RxLR_Dir/UK1_aug_RxLR_IDs.txt
    mkdir -p $RxLR_Dir
    cat $RxLR_Names_Bc1 | sed -r 's/^/Bc1|/g' > $RxLR_ID
    cat $RxLR_Names_Nov5 | sed -r 's/^/Nov5|/g' >> $RxLR_ID
done
```

#Ortholog groups containing RxLR proteins were identified using the following commands:

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
4,556
Of these, the following number were found in orthogroups:
4,474
These were distributed through the following number of Orthogroups:
2,001
The following RxLRs were found in Race 1 unique orthogroups:
1
These orthogroups contain the following number of RxLRs:
2
The following RxLRs were found in P.fragariae unique orthogroups:
2,001
These orthogroups contain the following number of RxLRs:
4,474
```

#The Race 1 RxLR genes that were not found in orthogroups were identified:

```bash
for num in 1
do
    RxLR_UK1_uniq=$RxLR_Dir/UK1_unique_RxLRs.txt
    cat $RxLR_ID | grep -v -w -f $RxLR_Orthogroup_hits > $RxLR_UK1_uniq
    echo "The number of UK1 unique RxLRs are:"
    cat $RxLR_UK1_uniq | wc -l
    RxLR_Seq_Bc1=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc1/Bc1_final_RxLR.fa
    RxLR_Seq_Nov5=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov5/Nov5_final_RxLR.fa
    Final_genes_Bc1=gene_pred/annotation/P.fragariae/Bc1/Bc1_genes_incl_ORFeffectors.pep.fasta
    Final_genes_Nov5=gene_pred/annotation/P.fragariae/Nov5/Nov5_genes_incl_ORFeffectors.pep.fasta
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
82
The number of BC-1 genes extracted is:
42
The number of NOV-5 genes extracted is:
40
```

##Extracting fasta files for orthogroups containing Race 1 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK1_RxLR/UK1_RxLR_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK1_RxLR/orthogroups_fasta_UK1_RxLR
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```


##Extracting fasta files for P. fragariae orthogroups containing Race 1 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK1_RxLR/Pf_RxLR_Orthogroups_hits.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK1_RxLR/orthogroups_fasta_Pf_RxLR
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

#Race 1 unique secreted proteins

#Race 1 secreted protein genes were parsed to the same format as the gene names used in the analysis:

```bash
for num in 1
do
    Sec_Names_Bc1=gene_pred/combined_sigP_CQ/P.fragariae/Bc1/Bc1_secreted.txt
    Sec_Names_Nov5=gene_pred/combined_sigP_CQ/P.fragariae/Nov5/Nov5_secreted.txt
    Sec_Names_Bc1_ORFs=gene_pred/combined_sigP_ORF/P.fragariae/Bc1/Bc1_all_secreted_merged.txt
    Sec_Names_Nov5_ORFs=gene_pred/combined_sigP_ORF/P.fragariae/Nov5/Nov5_all_secreted_merged.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal
    Sec_Dir=$WorkDir/UKR1_Secreted
    Orthogroups=$WorkDir/All_Strains_plus_rubi_no_removal_orthogroups.txt
    Sec_ID=$Sec_Dir/UKR1_aug_Sec_IDs.txt
    mkdir -p $Sec_Dir
    cat $Sec_Names_Bc1 | sed -r 's/^/Bc1|/g' > $Sec_ID
    cat $Sec_Names_Nov5 | sed -r 's/^/Nov5|/g' >> $Sec_ID
    cat $Sec_Names_Bc1_ORFs | sed -r 's/^/Bc1|/g' | sed -r 's/$/.t1/g' >> $Sec_ID
    cat $Sec_Names_Nov5_ORFs | sed -r 's/^/Nov5|/g' | sed -r 's/$/.t1/g' >> $Sec_ID
done
```

#Ortholog groups containing Secreted proteins were identified using the following commands:

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
66,716
Of these, the following number were found in orthogroups:
10,475
These were distributed through the following number of Orthogroups:
4,259
The following secreted proteins were found in Race 1 unique orthogroups:
4
These orthogroups contain the following number of secreted proteins:
7
The following secreted proteins were found in P.fragariae unique orthogroups:
4,259
These orthogroups contain the following number of Secreted proteins:
10,475
```

#The Race 1 secreted protein genes that were not found in orthogroups were identified:

```bash
for num in 1
do
    Sec_UK1_uniq=$Sec_Dir/UK1_unique_Sec.txt
    cat $Sec_ID | grep -v -w -f $Sec_Orthogroup_hits | tr -d 'Bc1|' | tr -d 'Nov5|' > $Sec_UK1_uniq
    echo "The number of UK1 unique secreted proteins are:"
    cat $Sec_UK1_uniq | wc -l
    Sec_Seq_Bc1=gene_pred/combined_sigP_CQ/P.fragariae/Bc1/Bc1_all_secreted.fa
    Sec_Seq_Nov5=gene_pred/combined_sigP_CQ/P.fragariae/Nov5/Nov5_all_secreted.fa
    Final_genes_Bc1=gene_pred/codingquary/P.fragariae/Bc1/final/final_genes_combined.pep.fasta
    Final_genes_Nov5=gene_pred/codingquary/P.fragariae/Nov5/final/final_genes_combined.pep.fasta
    Sec_UK1_uniq_fa=$Sec_Dir/UK1_unique_Sec.fa
    cat $Final_genes_Bc1 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Sec_UK1_uniq | grep -E -v '^--' > $Sec_UK1_uniq_fa
    cat $Final_genes_Nov5 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Sec_UK1_uniq | grep -E -v '^--' >> $Sec_UK1_uniq_fa
done
```

```
The number of UK1 unique secreted proteins are:
242
```

##Extracting fasta files for orthogroups containing Race 1 putative secreted proteins

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UKR1_Secreted/UK1_Sec_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UKR1_Secreted/orthogroups_fasta_UK1_Sec
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

##Extracting fasta files for P. fragariae orthogroups containing Race 1 putative secreted proteins

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UKR1_Secreted/Pf_Sec_Orthogroups_hits.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UKR1_Secreted/orthogroups_fasta_Pf_Sec
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

##Race 1 unique Crinkler families

#Race 1 crinkler genes were parsed to the same format as the gene names used in the analysis:

```bash
for num in 1
do
    CRN_Names_Bc1=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc1/Bc1_final_CRN.txt
    CRN_Names_Nov5=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov5/Nov5_final_CRN.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal
    CRN_Dir=$WorkDir/UK1_CRN
    Orthogroups=$WorkDir/All_Strains_plus_rubi_no_removal_orthogroups.txt
    CRN_ID_UK1=$CRN_Dir/UK1_CRN_hmmer_IDs.txt
    mkdir -p $CRN_Dir
    cat $CRN_Names_Bc1 | sed -r 's/^/Bc1|/g' > $CRN_ID_UK1
    cat $CRN_Names_Nov5 | sed -r 's/^/Nov5|/g' >> $CRN_ID_UK1
done
```

#Ortholog groups containing CRN proteins were identified using the following commands:

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
234
Of these, the following number were found in orthogroups:
234
These were distributed through the following number of Orthogroups:
71
The following CRNs were found in Race 1 unique orthogroups:
0
The following CRNs were found in P.fragariae unique orthogroups:
71
These orthogroups contain the following number of CRNs:
234
```

#The Race 1 CRN genes not found in orthogroups were identified:

```bash
for num in 1
do
    CRN_UK1_uniq=$CRN_Dir/UK1_unique_CRNs.txt
    cat $CRN_ID_UK1 | grep -v -w -f $CRN_Orthogroup_hits_UK1 > $CRN_UK1_uniq
    echo "The number of Race 1 unique CRNs are:"
    cat $CRN_UK1_uniq | wc -l
    CRN_Seq_Bc1=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc1/Bc1_final_CRN.fa
    CRN_Seq_Nov5=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov5/Nov5_final_CRN.fa
    Final_genes_Bc1=gene_pred/annotation/P.fragariae/Bc1/Bc1_genes_incl_ORFeffectors.pep.fasta
    Final_genes_Nov5=gene_pred/annotation/P.fragariae/Nov5/Nov5_genes_incl_ORFeffectors.pep.fasta
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

##Extracting fasta files for orthogroups containing Race 1 putative CRNs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK1_CRN/UK1_CRN_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK1_CRN/orthogroups_fasta_UK1_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

##Extracting fasta files for P. fragariae orthogroups containing Race 1 putative CRNs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK1_CRN/Pf_CRN_Orthogroups_hits.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK1_CRN/orthogroups_fasta_Pf_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

#Analysis of orthogroups unique to UK race 3 (Strains NOV-27, NOV-71 & NOV-9)

##The genes unique to Race 3 were identified within the orthology analysis

##First variables were set:

```bash
WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal
UK3UniqDir=$WorkDir/UK3_unique
Orthogroups=$WorkDir/All_Strains_plus_rubi_no_removal_orthogroups.txt
GoodProts=$WorkDir/goodProteins/goodProteins.fasta
Final_genes_Nov27=gene_pred/annotation/P.fragariae/Nov27/Nov27_genes_incl_ORFeffectors.pep.fasta
Final_genes_Nov71=gene_pred/annotation/P.fragariae/Nov71/Nov71_genes_incl_ORFeffectors.pep.fasta
Final_genes_Nov9=gene_pred/annotation/P.fragariae/Nov9/Nov9_genes_incl_ORFeffectors.pep.fasta
Uniq_UK3_groups=$UK3UniqDir/UK3_uniq_orthogroups.txt
mkdir -p $UK3UniqDir
```

#Orthogroups only containing Race 3 genes were extracted:

##Bars are to prevent incorrect filtering

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
11
The following number genes are contained in these orthogroups:
46
```

#Race 3 unique RxLR families

#Race 3 RxLR genes were parsed to the same format as the gene names used in the analysis:

```bash
for num in 1
do
    RxLR_Names_Nov27=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov27/Nov27_Total_RxLR_motif_hmm.txt
    RxLR_Names_Nov71=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov71/Nov71_Total_RxLR_motif_hmm.txt
    RxLR_Names_Nov9=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov9/Nov9_Total_RxLR_motif_hmm.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal
    RxLR_Dir=$WorkDir/UK3_RxLR
    Orthogroups=$WorkDir/All_Strains_plus_rubi_no_removal_orthogroups.txt
    RxLR_ID=$RxLR_Dir/UK3_aug_RxLR_EER_IDs.txt
    mkdir -p $RxLR_Dir
    cat $RxLR_Names_Nov27 | sed -r 's/^/Nov27|/g' > $RxLR_ID
    cat $RxLR_Names_Nov71 | sed -r 's/^/Nov71|/g' >> $RxLR_ID
    cat $RxLR_Names_Nov9 | sed -r 's/^/Nov9|/g' >> $RxLR_ID
done
```

#Ortholog groups containing RxLR proteins were identified using the following commands:

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
6,823
Of these, the following number were found in orthogroups:
6,710
These were distributed through the following number of Orthogroups:
2,023
The following RxLRs were found in Race 3 unique orthogroups:
1
These orthogroups contain the following number of RxLRs:
3
The following RxLRs were found in P.fragariae unique orthogroups:
2,023
These orthogroups contain the following number of RxLRs:
6,710
```

#The Race 3 RxLR genes that were not found in orthogroups were identified:

```bash
for num in 1
do
    RxLR_UK3_uniq=$RxLR_Dir/UK3_unique_RxLRs.txt
    cat $RxLR_ID | grep -v -w -f $RxLR_Orthogroup_hits > $RxLR_UK3_uniq
    echo "The number of UK3 unique RxLRs are:"
    cat $RxLR_UK3_uniq | wc -l
    RxLR_Seq_Nov27=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov27/Nov27_final_RxLR.fa
    RxLR_Seq_Nov71=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov71/Nov71_final_RxLR.fa
    RxLR_Seq_Nov9=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov9/Nov9_final_RxLR.fa
    Final_genes_Nov27=gene_pred/annotation/P.fragariae/Nov27/Nov27_genes_incl_ORFeffectors.pep.fasta
    Final_genes_Nov71=gene_pred/annotation/P.fragariae/Nov71/Nov71_genes_incl_ORFeffectors.pep.fasta
    Final_genes_Nov9=gene_pred/annotation/P.fragariae/Nov9/Nov9_genes_incl_ORFeffectors.pep.fasta
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
113
The number of NOV-27 genes extracted is:
35
The number of NOV-71 genes extracted is:
39
The number of NOV-9 genes extracted is:
39
```

##Extracting fasta files for orthogroups containing Race 3 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK3_RxLR/UK3_RxLR_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK3_RxLR/orthogroups_fasta_UK1_RxLR
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```


##Extracting fasta files for P. fragariae orthogroups containing Race 3 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK3_RxLR/Pf_RxLR_Orthogroups_hits.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK3_RxLR/orthogroups_fasta_Pf_RxLR
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
    WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal
    Sec_Dir=$WorkDir/UKR3_Secreted
    Orthogroups=$WorkDir/All_Strains_plus_rubi_no_removal_orthogroups.txt
    Sec_ID=$Sec_Dir/UKR3_aug_Sec_IDs.txt
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
100,025
Of these, the following number were found in orthogroups:
15,738
These were distributed through the following number of Orthogroups:
4,405
The following secreted proteins were found in Race 3 unique orthogroups:
4
These orthogroups contain the following number of secreted proteins:
8
The following secreted proteins were found in P.fragariae unique orthogroups:
4,405
These orthogroups contain the following number of Secreted proteins:
15,738
```

#The Race 3 secreted protein genes that were not found in orthogroups were identified:

```bash
for num in 1
do
    Sec_UK3_uniq=$Sec_Dir/UK3_unique_Sec.txt
    cat $Sec_ID | grep -v -w -f $Sec_Orthogroup_hits > $Sec_UK3_uniq
    echo "The number of UK3 unique secreted proteins are:"
    cat $Sec_UK3_uniq | wc -l
    Sec_Seq_Nov9=gene_pred/combined_sigP_CQ/P.fragariae/Nov9/Nov9_all_secreted.fa
    Sec_Seq_Nov27=gene_pred/combined_sigP_CQ/P.fragariae/Nov27/Nov27_all_secreted.fa
    Sec_Seq_Nov71=gene_pred/combined_sigP_CQ/P.fragariae/Nov71/Nov71_all_secreted.fa
    Sec_Seq_Nov9_ORF=gene_pred/combined_sigP_ORF/P.fragariae/Nov9/Nov9_all_secreted_merged.aa
    Sec_Seq_Nov27_ORF=gene_pred/combined_sigP_ORF/P.fragariae/Nov27/Nov27_all_secreted_merged.aa
    Sec_Seq_Nov71_ORF=gene_pred/combined_sigP_ORF/P.fragariae/Nov71/Nov71_all_secreted_merged.aa
    Final_genes_Nov9=gene_pred/annotation/P.fragariae/Nov9/Nov9_genes_incl_ORFeffectors.pep.fasta
    Final_genes_Nov27=gene_pred/annotation/P.fragariae/Nov27/Nov27_genes_incl_ORFeffectors.pep.fasta
    Final_genes_Nov71=gene_pred/annotation/P.fragariae/Nov71/Nov71_genes_incl_ORFeffectors.pep.fasta
    Sec_UK3_uniq_fa=$Sec_Dir/UK3_unique_Sec.fa
    cat $Final_genes_Nov9 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Sec_UK3_uniq | grep -E -v '^--' > $Sec_UK3_uniq_fa
    cat $Final_genes_Nov27 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Sec_UK3_uniq | grep -E -v '^--' >> $Sec_UK3_uniq_fa
    cat $Final_genes_Nov71 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Sec_UK3_uniq | grep -E -v '^--' >> $Sec_UK3_uniq_fa
done
```

```
The number of UK3 unique secreted proteins are:
378
```

##Extracting fasta files for orthogroups containing Race 3 putative secreted proteins

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UKR3_Secreted/UK3_Sec_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UKR3_Secreted/orthogroups_fasta_UK3_Sec
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```


##Extracting fasta files for P. fragariae orthogroups containing Race 3 putative secreted proteins

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UKR3_Secreted/Pf_Sec_Orthogroups_hits.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UKR3_Secreted/orthogroups_fasta_Pf_Sec
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

##Race 3 unique Crinkler families

#Race 3 crinkler genes were parsed to the same format as the gene names used in the analysis:

```bash
for num in 1
do
    CRN_Names_Nov27=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov27/Nov27_final_CRN.txt
    CRN_Names_Nov71=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov71/Nov71_final_CRN.txt
    CRN_Names_Nov9=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov9/Nov9_final_CRN.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal
    CRN_Dir=$WorkDir/UK3_CRN
    Orthogroups=$WorkDir/All_Strains_plus_rubi_no_removal_orthogroups.txt
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
355
Of these, the following number were found in orthogroups:
355
These were distributed through the following number of Orthogroups:
75
The following CRNs were found in Race 3 unique orthogroups:
0
The following CRNs were found in P.fragariae unique orthogroups:
75
These orthogroups contain the following number of CRNs:
355
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
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK3_CRN/UK3_CRN_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK3_CRN/orthogroups_fasta_UK3_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

##Extracting fasta files for P. fragariae orthogroups containing Race 3 putative CRNs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK3_CRN/Pf_CRN_Orthogroups_hits.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/UK1_CRN/orthogroups_fasta_Pf_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

#Extract fasta files for all unique orthogroups, including non-effector groups

```bash
for OrthogroupTxt in $(ls analysis/orthology/orthomcl/All_Strains_plus_rubi/UK*_unique/*)
do
    Race=$(echo $OrthogroupTxt | rev | cut -f2 -d '/' | rev)
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/group_fastas/$Race
    mkdir -p $OutDir
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    echo $Race
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

#Run fasta files through interproscan to identify function of genes in UK2 unique orthogroups

```bash
ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation/interproscan/
for Genes in $(ls analysis/orthology/orthomcl/All_Strains_plus_rubi/group_fastas/UK2_unique/*.fa)
do
    Jobs=$(qstat | grep 'adamst' | grep 'qw' | wc -l)
    while [ $Jobs -gt 1 ]
    do
        sleep 10
        printf "."
        Jobs=$(qstat | grep 'adamst' | grep 'qw' | wc -l)
    done
    printf "\n"
    $ProgDir/sub_interproscan.sh $Genes
done
```

#Produce a count table of the number of genes for each strain in each groups

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
Taxon_code=All_Strains
OrthoMCL_output=analysis/orthology/orthomcl/$Taxon_code/"$Taxon_code"_orthogroups.txt
OutName=analysis/orthology/orthomcl/$Taxon_code/"$Taxon_code"_count_table.tsv
$ProgDir/parse_orthogroups.py --orthogroups $OrthoMCL_output --out_dir $OutName
```

##Analyse this count table for expanded groups and write orthogroups to a text file 'UKX_expanded.txt'

```bash
cd analysis/orthology/orthomcl/All_Strains
python /home/adamst/git_repos/scripts/phytophthora_fragariae/orthology_counts.py
```

###Reformat the lists and extract full orthogroup details

```bash
for file in $(ls UK*_expanded.txt)
do
    while IFS=' ' read -r line
    do
        echo $line | sed 's/O/o/g' | sed 's/ //g' >> tmp.txt
    done < "$file"
    Start=$(basename "$file" .txt)
    New_File="$Start"_modified.txt
    while IFS=' ' read -r line
    do
        grep -w "$line" All_Strains_orthogroups.txt >> $New_File
    done < tmp.txt
    rm tmp.txt
done
```

###Look for RxLRs in each race

##UK1

###Create a list of RxLRs

```bash
for num in 1
do
    RxLR_Names_Bc1=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc1/Bc1_Total_RxLR_EER_motif_hmm.txt
    RxLR_Names_Nov5=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov5/Nov5_Total_RxLR_EER_motif_hmm.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains
    RxLR_Dir=$WorkDir/UKR1_RxLR
    Orthogroups=$WorkDir/UK1_expanded_modified.txt
    RxLR_ID=$RxLR_Dir/UKR1_aug_RxLR_EER_IDs.txt
    mkdir -p $RxLR_Dir
    cat $RxLR_Names_Bc1 | sed -r 's/^/Bc1|/g' > $RxLR_ID
    cat $RxLR_Names_Nov5 | sed -r 's/^/Nov5|/g' >> $RxLR_ID
done
```

#Ortholog groups containing RxLR proteins were identified using the following commands:

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
done
```

```
The number of RxLRs searched for is:
629
Of these, the following number were found in orthogroups:
0
These were distributed through the following number of Orthogroups:
0
```

##UK2

###Create a list of RxLRs

```bash
for num in 1
do
    RxLR_Names_Bc16=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_Total_RxLR_EER_motif_hmm.txt
    RxLR_Names_A4=analysis/RxLR_effectors/combined_evidence/P.fragariae/A4/A4_Total_RxLR_EER_motif_hmm.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains
    RxLR_Dir=$WorkDir/UKR2_RxLR
    Orthogroups=$WorkDir/UK2_expanded_modified.txt
    RxLR_ID=$RxLR_Dir/UKR2_aug_RxLR_EER_IDs.txt
    mkdir -p $RxLR_Dir
    cat $RxLR_Names_Bc16 | sed -r 's/^/Bc16|/g' > $RxLR_ID
    cat $RxLR_Names_A4 | sed -r 's/^/A4|/g' >> $RxLR_ID
done
```

#Ortholog groups containing RxLR proteins were identified using the following commands:

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
done
```

```
The number of RxLRs searched for is:
674
Of these, the following number were found in orthogroups:
3
These were distributed through the following number of Orthogroups:
1
This is orthogroup 37, containing:
Bc16|g33201.t1
A4|g9316.t1
A4|g26518.t1
The genes from A4 do not align well with the gene from BC-16, so this is a false positive.
```

##Extract the fasta files for selected orthogroups

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains/UKR2_RxLR/UK2_RxLR_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains/UKR2_RxLR/orthogroups_fasta_UK2_RxLR
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

##UK3

###Create a list of RxLRs

```bash
for num in 1
do
    RxLR_Names_Nov27=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov27/Nov27_Total_RxLR_EER_motif_hmm.txt
    RxLR_Names_Nov71=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov71/Nov71_Total_RxLR_EER_motif_hmm.txt
    RxLR_Names_Nov9=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov9/Nov9_Total_RxLR_EER_motif_hmm.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains
    RxLR_Dir=$WorkDir/UKR3_RxLR
    Orthogroups=$WorkDir/UK3_expanded_modified.txt
    RxLR_ID=$RxLR_Dir/UKR3_aug_RxLR_EER_IDs.txt
    mkdir -p $RxLR_Dir
    cat $RxLR_Names_Nov27 | sed -r 's/^/Nov27|/g' > $RxLR_ID
    cat $RxLR_Names_Nov71 | sed -r 's/^/Nov71|/g' >> $RxLR_ID
    cat $RxLR_Names_Nov9 | sed -r 's/^/Nov9|/g' >> $RxLR_ID
done
```

#Ortholog groups containing RxLR proteins were identified using the following commands:

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
done
```

```
The number of RxLRs searched for is:
938
Of these, the following number were found in orthogroups:
3
These were distributed through the following number of Orthogroups:
1
This is orthogroup 16649, containing:
Nov27|PGN_07235.t1
Nov9|PGN_05230.t1
Nov71|PGN_04367.t1
These genes are all identical, but there is also a identical gene in ONT-3, and one with a 4AA insertion in NOV-77 - These two are not the same race either
```

##Extract the fasta files for selected orthogroups

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains/UKR3_RxLR/UK3_RxLR_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains/UKR3_RxLR/orthogroups_fasta_UK3_RxLR
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

###Look for CRNs in each race

##UK1

###Create a list of CRNs

```bash
for num in 1
do
    CRN_Names_Bc1=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc1/Bc1_final_CRN.txt
    CRN_Names_Nov5=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov5/Nov5_final_CRN.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains
    CRN_Dir=$WorkDir/UKR1_CRN
    Orthogroups=$WorkDir/UK1_expanded_modified.txt
    CRN_ID=$CRN_Dir/UKR1_CRN_hmmer_IDs.txt
    mkdir -p $CRN_Dir
    cat $CRN_Names_Bc1 | sed -r 's/^/Bc1|/g' > $CRN_ID
    cat $CRN_Names_Nov5 | sed -r 's/^/Nov5|/g' >> $CRN_ID
done
```

#Ortholog groups containing CRN proteins were identified using the following commands:

```bash
for num in 1
do
    echo "The number of CRNs searched for is:"
    cat $CRN_ID | wc -l
    echo "Of these, the following number were found in orthogroups:"
    CRN_Orthogroup_hits=$CRN_Dir/UK1_CRN_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $CRN_ID > $CRN_Orthogroup_hits
    cat $CRN_Orthogroup_hits | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    CRN_Orthogroup=$CRN_Dir/UK1_CRN_Orthogroups.txt
    cat $Orthogroups | grep -w -f $CRN_ID > $CRN_Orthogroup
    cat $CRN_Orthogroup | wc -l
done
```

```
The number of CRNs searched for is:
222
Of these, the following number were found in orthogroups:
0
These were distributed through the following number of Orthogroups:
0
```

##UK2

###Create a list of CRNs

```bash
for num in 1
do
    CRN_Names_Bc16=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc16/Bc16_final_CRN.txt
    CRN_Names_A4=analysis/CRN_effectors/hmmer_CRN/P.fragariae/A4/A4_final_CRN.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains
    CRN_Dir=$WorkDir/UKR2_CRN
    Orthogroups=$WorkDir/UK2_expanded_modified.txt
    CRN_ID=$CRN_Dir/UKR2_CRN_hmmer_IDs.txt
    mkdir -p $CRN_Dir
    cat $CRN_Names_Bc16 | sed -r 's/^/Bc16|/g' > $CRN_ID
    cat $CRN_Names_A4 | sed -r 's/^/A4|/g' >> $CRN_ID
done
```

#Ortholog groups containing CRN proteins were identified using the following commands:

```bash
for num in 1
do
    echo "The number of CRNs searched for is:"
    cat $CRN_ID | wc -l
    echo "Of these, the following number were found in orthogroups:"
    CRN_Orthogroup_hits=$CRN_Dir/UK2_CRN_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $CRN_ID > $CRN_Orthogroup_hits
    cat $CRN_Orthogroup_hits | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    CRN_Orthogroup=$CRN_Dir/UK2_CRN_Orthogroups.txt
    cat $Orthogroups | grep -w -f $CRN_ID > $CRN_Orthogroup
    cat $CRN_Orthogroup | wc -l
done
```

```
The number of CRNs searched for is:
236
Of these, the following number were found in orthogroups:
0
These were distributed through the following number of Orthogroups:
0
```

##UK3

###Create a list of CRNs

```bash
for num in 1
do
    CRN_Names_Nov27=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov27/Nov27_final_CRN.txt
    CRN_Names_Nov71=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov71/Nov71_final_CRN.txt
    CRN_Names_Nov9=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov9/Nov9_final_CRN.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains
    CRN_Dir=$WorkDir/UKR3_CRN
    Orthogroups=$WorkDir/UK3_expanded_modified.txt
    CRN_ID=$CRN_Dir/UKR3_CRN_hmmer_IDs.txt
    mkdir -p $CRN_Dir
    cat $CRN_Names_Nov27 | sed -r 's/^/Nov27|/g' > $CRN_ID
    cat $CRN_Names_Nov71 | sed -r 's/^/Nov71|/g' >> $CRN_ID
    cat $CRN_Names_Nov9 | sed -r 's/^/Nov9|/g' >> $CRN_ID
done
```

#Ortholog groups containing CRN proteins were identified using the following commands:

```bash
for num in 1
do
    echo "The number of CRNs searched for is:"
    cat $CRN_ID | wc -l
    echo "Of these, the following number were found in orthogroups:"
    CRN_Orthogroup_hits=$CRN_Dir/UK3_CRN_Orthogroups_hits.txt
    cat $Orthogroups | grep -o -w -f $CRN_ID > $CRN_Orthogroup_hits
    cat $CRN_Orthogroup_hits | wc -l
    echo "These were distributed through the following number of Orthogroups:"
    CRN_Orthogroup=$CRN_Dir/UK3_CRN_Orthogroups.txt
    cat $Orthogroups | grep -w -f $CRN_ID > $CRN_Orthogroup
    cat $CRN_Orthogroup | wc -l
done
```

```
The number of CRNs searched for is:
338
Of these, the following number were found in orthogroups:
3
These were distributed through the following number of Orthogroups:
1
This is orthogroup 1557, which contains the following UK3 CRNs:
Nov9|g20292.t1
Nov71|g19146.t1
Nov27|g19382.t1
Nov71|g19147.t1
Nov27|g19383.t1
Nov9|g20293.t1
Nov9|g4254.t1
Nov71|g3854.t1
Nov27|g3856.t1
These group into three sets:
A = Nov9|g4254.t1, Nov27|g3856.t1 and Nov71|g3854.t1 - also have exact matches in BC-23 and SCRP245
B = Nov9|g20292.t1, Nov27|g19382.t1 and Nov71|g19146.t1 - has a large number of exact homologues
C = Nov9|g20293.t1, Nov27|g19383.t1 and Nov71|g19147.t1 - Exact match in ONT-3 of extended version, shortened version has many UK1 and 2 homologues.
```

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains/UKR3_CRN/UK3_CRN_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains/UKR3_CRN/orthogroups_fasta_UK3_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

###Look for secreted proteins in each race

##UK1

###Create a list of secreted proteins

```bash
for num in 1
do
    Sec_Names_Bc1=gene_pred/combined_sigP_CQ/P.fragariae/Bc1/Bc1_secreted.txt
    Sec_Names_Nov5=gene_pred/combined_sigP_CQ/P.fragariae/Nov5/Nov5_secreted.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains
    Sec_Dir=$WorkDir/UKR1_Secreted
    Orthogroups=$WorkDir/UK1_expanded_modified.txt
    Sec_ID=$Sec_Dir/UKR1_secreted_proteins.txt
    mkdir -p $Sec_Dir
    cat $Sec_Names_Bc1 | sed -r 's/^/Bc1|/g' > $Sec_ID
    cat $Sec_Names_Nov5 | sed -r 's/^/Nov5|/g' >> $Sec_ID
done
```

#Ortholog groups containing secreted proteins were identified using the following commands:

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
done
```

```
The number of secreted proteins searched for is:
7277
Of these, the following number were found in orthogroups:
30
These were distributed through the following number of Orthogroups:
5
```

##Extract the fasta files for selected orthogroups

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains/UKR1_Secreted/UK1_Sec_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains/UKR1_Secreted/orthogroups_fasta_UK1_Sec
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

###Overview of results

```
Orthogroup33 - no unqiue sequences, except one BC-1 secreted protein (g27192) which has no equivalent in NOV-5
Orthogroup71 only contains two BC-1 secreted proteins
Orthogroup249 - BC-1|g20529.t1 has 5AA extra at start but NOV-5 exactly matches others. BC-1|g20531.t1 is truncated, full length NOV-5 matches others. BC-1|g26283.t1 has 5AAs extra at start, but NOV-5 matches others. NOV-5|g26419.t1 is different at the end, but BC-1 matches exactly.
Orthogroup824 only contains one BC-1 protein
Orthogroup3289 no unique sequences
```

##UK2

###Create a list of secreted proteins

```bash
for num in 1
do
    Sec_Names_Bc16=gene_pred/combined_sigP_CQ/P.fragariae/Bc16/Bc16_secreted.txt
    Sec_Names_A4=gene_pred/combined_sigP_CQ/P.fragariae/A4/A4_secreted.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains
    Sec_Dir=$WorkDir/UKR2_Sec
    Orthogroups=$WorkDir/UK2_expanded_modified.txt
    Sec_ID=$Sec_Dir/UKR2_secreted_proteins.txt
    mkdir -p $Sec_Dir
    cat $Sec_Names_Bc16 | sed -r 's/^/Bc16|/g' > $Sec_ID
    cat $Sec_Names_A4 | sed -r 's/^/A4|/g' >> $Sec_ID
done
```

#Ortholog groups containing secreted proteins were identified using the following commands:

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
done
```

```
The number of secreted proteins searched for is:
7835
Of these, the following number were found in orthogroups:
51
These were distributed through the following number of Orthogroups:
18

Orthogroup 6 - 3 BC-16 proteins have no match in A4, the one that does is truncated in A4 and is different A4|g23055.t1 and Bc16|g21815.t1, may be a candidate, though genes are very similar.
Orthogroup 13 - A4 and BC-16 proteins do not match
Orthogroup 26 - No BC-16 secreted proteins
Orthogroup 32 - No match between A4 and BC-16 proteins
Orthogroup 61 - A4 & BC-16 do not match
Orthogroup 301 - Proteins match many other isolates
Orthogroup 302 - Bc16|g9197 is oddly truncated, full length A4 matches other isolates, other proteins either do not match in UK2 or match other isolates exactly.
Orthogroup 518 - Only one BC-16 protein
Orthogroup 542 - Only one BC-16 protein
Orthogroup 568 - Only one BC-16 protein
Orthogroup 570 - Proteins match other isolates
Orthogroup 3040 - Only one A4 protein
Orthogroup 16861 - Only one A4 protein
Orthogroup 16902 - Proteins match other isolates
Orthogroup 17353 - BC-16 truncated and matches NOV-77
Orthogroup 17398 - BC-16 truncated, A4 matches NOV-77
Orthogroup 17427 - BC-16 only
Orthogroup 18204 - BC-16 only
```

##Extract the fasta files for selected orthogroups

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains/UKR2_Sec/UK2_Sec_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains/UKR2_Sec/orthogroups_fasta_UK2_Sec
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

##UK3

###Create a list of secreted proteins

```bash
for num in 1
do
    Sec_Names_Nov27=gene_pred/combined_sigP_CQ/P.fragariae/Nov27/Nov27_secreted.txt
    Sec_Names_Nov71=gene_pred/combined_sigP_CQ/P.fragariae/Nov71/Nov71_secreted.txt
    Sec_Names_Nov9=gene_pred/combined_sigP_CQ/P.fragariae/Nov9/Nov9_secreted.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains
    Sec_Dir=$WorkDir/UKR3_Sec
    Orthogroups=$WorkDir/UK3_expanded_modified.txt
    Sec_ID=$Sec_Dir/UKR3_secreted_proteins.txt
    mkdir -p $Sec_Dir
    cat $Sec_Names_Nov27 | sed -r 's/^/Nov27|/g' > $Sec_ID
    cat $Sec_Names_Nov71 | sed -r 's/^/Nov71|/g' >> $Sec_ID
    cat $Sec_Names_Nov9 | sed -r 's/^/Nov9|/g' >> $Sec_ID
done
```

#Ortholog groups containing secreted proteins were identified using the following commands:

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
done
```

```
The number of secreted proteins searched for is:
11037
Of these, the following number were found in orthogroups:
46
These were distributed through the following number of Orthogroups:
9

Orthogroup 16 - NOV-71 is truncated and matches NOV-5, other two isolates match BC-23
Orthogroup 372 - All proteins match other isolates
Orthogroup 1422 - All proteins match other isolates
Orthogroup 2888 - single insertion in NOV-71 (matches BC-16), other two match two other strains. t2 does not have a NOV-71 example
Orthogroup 2917 - NOV-27 is truncated, matches two other isolates. NOV-9 and NOV-71 are unique at the end of the protein - probably not informative
Orthogroup 15696 - UK3 identical to each other, single AA subs in other isolates - Nov9|g14735.t1 (no interproscan hits), Nov71|CUFF_14914_1_1.t1 (no interproscan hits) & Nov27|g13517.t1 (no interproscan hits) - BLAST gives dpy30 motif, closest is H3 methyltransferase or flag associated - not very good hits
Orthogroup 16606 - all proteins match BC-23
Orthogroup 16649 - All proteins match ONT-3
Orthogroup 17755 - Only contains UK3 proteins - Nov27|g3633.t1, Nov9|g4077.t1 & Nov71|g3548.t1 - no interproscan hits, it's the damned green turtle things!
```

##Extract the fasta files for selected orthogroups

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains/UKR3_Sec/UK3_Sec_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains/UKR3_Sec/orthogroups_fasta_UK3_Sec
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```
