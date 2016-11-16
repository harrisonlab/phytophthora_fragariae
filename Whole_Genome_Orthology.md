#Methodology 4 from Andy's files - run on A4, BC-1, BC-16, BC-23, NOV-27, NOV-5, NOV-71, NOV-77, NOV-9, ONT-3, SCRP245_v2

```bash
ProjDir=/home/groups/harrisonlab/project_files/phytophthora_fragariae
cd $ProjDir
IsolateAbrv=All_Strains_plus_rubi
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
Fasta_file=gene_pred/codingquary/P.fragariae/A4/final/final_genes_combined.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for BC-1

```bash
Taxon_code=Bc1
Fasta_file=gene_pred/codingquary/P.fragariae/Bc1/final/final_genes_combined.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for BC-16

```bash
Taxon_code=Bc16
Fasta_file=gene_pred/codingquary/P.fragariae/Bc16/final/final_genes_combined.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for BC-23

```bash
Taxon_code=Bc23
Fasta_file=gene_pred/codingquary/P.fragariae/Bc23/final/final_genes_combined.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for NOV-27

```bash
Taxon_code=Nov27
Fasta_file=gene_pred/codingquary/P.fragariae/Nov27/final/final_genes_combined.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for NOV-5

```bash
Taxon_code=Nov5
Fasta_file=gene_pred/codingquary/P.fragariae/Nov5/final/final_genes_combined.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for NOV-71

```bash
Taxon_code=Nov71
Fasta_file=gene_pred/codingquary/P.fragariae/Nov71/final/final_genes_combined.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for NOV-77

```bash
Taxon_code=Nov77
Fasta_file=gene_pred/codingquary/P.fragariae/Nov77/final/final_genes_combined.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for NOV-9

```bash
Taxon_code=Nov9
Fasta_file=gene_pred/codingquary/P.fragariae/Nov9/final/final_genes_combined.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for ONT-3

```bash
Taxon_code=ONT3
Fasta_file=gene_pred/codingquary/P.fragariae/ONT3/final/final_genes_combined.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for SCRP245_v2

```bash
Taxon_code=SCRP245_v2
Fasta_file=gene_pred/codingquary/P.fragariae/SCRP245_v2/final/final_genes_combined.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for SCRP249

```bash
Taxon_code=SCRP249
Fasta_file=../phytophthora_rubi/gene_pred/codingquary/discovar/P.rubi/SCRP249/final/final_genes_combined.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for SCRP324

```bash
Taxon_code=SCRP324
Fasta_file=../phytophthora_rubi/gene_pred/codingquary/discovar/P.rubi/SCRP324/final/final_genes_combined.pep.fasta
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
```

###for SCRP333

```bash
Taxon_code=SCRP333
Fasta_file=../phytophthora_rubi/gene_pred/codingquary/discovar/P.rubi/SCRP333/final/final_genes_combined.pep.fasta
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
    echo "The number of orthogroups common to UK1 strains is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc1|' | grep -e 'Nov5|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc1|' | grep -e 'Nov5|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to UK2 strains is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc1|' -e 'Bc23|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'Nov5|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc16|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc1|' -e 'Bc23|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'Nov5|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc16|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to UK3 strains is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov9|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Nov27|' | grep -e 'Nov71|' | grep -e 'Nov9|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to CA4 strains is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'Nov9|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'ONT3|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'Nov9|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'ONT3|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to CA5 strains is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'ONT3|' -e 'Nov9|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc23|' | grep -e 'Nov77|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A4|' -e 'Bc16|' -e 'ONT3|' -e 'Nov9|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc23|' | grep -e 'Nov77|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to US4 strains is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'Nov9|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'A4|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'Nov9|' -e 'SCRP245_v2|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'A4|' | grep -o '|' | wc -l
    echo "The number of orthogroups common to Unknown race strains is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'Nov9|' -e 'A4|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'SCRP245_v2|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc16|' -e 'Bc23|' -e 'Nov77|' -e 'Nov9|' -e 'A4|' -e 'Bc1|' -e 'Nov5|' -e 'Nov27|' -e 'Nov71|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'SCRP245_v2|' | grep -o '|' | wc -l
    echo "The number of orthogroups with only six highly conserved target strains is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc23|' -e 'Nov77|' -e 'A4|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' -e 'SCRP245_v2|' | grep -e 'Nov5|' | grep -e 'Nov27' | grep -e 'Nov71' | grep -e 'Bc16' | grep -e 'Nov9' | grep -e 'Bc1' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'ONT3|' -e 'Bc23|' -e 'Nov77|' -e 'A4|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' -e 'SCRP245_v2|' | grep -e 'Nov5|' | grep -e 'Nov27' | grep -e 'Nov71' | grep -e 'Bc16' | grep -e 'Nov9' | grep -e 'Bc1' | grep -o '|' | wc -l
    echo "The number of orthogroups containing all six highly conserved target strains is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -e 'Nov5|' | grep -e 'Nov27' | grep -e 'Nov71' | grep -e 'Bc16' | grep -e 'Nov9' | grep -e 'Bc1' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -e 'Nov5|' | grep -e 'Nov27' | grep -e 'Nov71' | grep -e 'Bc16' | grep -e 'Nov9' | grep -e 'Bc1' | grep -o '|' | wc -l
done
```

```
The total number of orthogroups is:
19952
The total number of genes in orthogroups is:
356680
The number of orthogroups common to all strains is:
13436
This represents the following number of genes:
318253
The number of orthogroups common to UK1 strains is:
4
This represents the following number of genes:
8
The number of orthogroups common to UK2 strains is:
35
This represents the following number of genes:
76
The number of orthogroups common to UK3 strains is:
5
This represents the following number of genes:
15
The number of orthogroups common to CA4 strains is:
494
This represents the following number of genes:
1380
The number of orthogroups common to CA5 strains is:
12
This represents the following number of genes:
25
The number of orthogroups common to US4 strains is:
3
This represents the following number of genes:
3
The number of orthogroups common to Unknown race strains is:
169
This represents the following number of genes:
467
The number of orthogroups with only six highly conserved target strains is:
5
This represents the following number of genes:
39
The number of orthogroups containing all six highly conserved target strains is:
14275
This represents the following number of genes:
428573
```

Identification of orthogroups of closely related strains for further analysis

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
14052
The total number of genes in shared orthogroups is:
425856
The total number of orthogroups is:
583
The total number of genes in orthogroups is:
1808
The total number of UK1 orthogroups is:
16
The total number of genes in UK1 orthogroups is:
74
The total number of UK2 orthogroups is:
29
The total number of genes in UK2 orthogroups is:
127
The total number of UK3 orthogroups is:
39
The total number of genes in UK3 orthogroups is:
220
```

##4.5.b Plot venn diagrams:

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
$ProgDir/UK1_Pf_venn_diag.r --inp $WorkDir/"$IsolateAbrv"_orthogroups.tab --out $WorkDir/"$IsolateAbrv"_UK1_orthogroups.pdf
```

Output was a pdf file of the venn diagram.

The following additional information was also provided. The format of the following lines is as follows:

Isolate name (total number of orthogroups) number of unique singleton genes number of unique groups of inparalogs

  [1]  <- non-pathogen orthogroups (5 non-pathogens)
  [1]  <- pathogen orthogroups (3 pathogens)
  [1] "Fus2"
  [1] "The total number of orthogroups and singleton genes in this isolate:  13846"
  [1] "The total number of orthogroups and singleton genes not in the venn diagram:  2412"
  [1] "The total number of singleton genes not in the venn diagram:  293"
  [1] "125"
  [1] "The total number of orthogroups and singleton genes in this isolate:  13975"
  [1] "The total number of orthogroups and singleton genes not in the venn diagram:  2541"
  [1] "The total number of singleton genes not in the venn diagram:  342"
  [1] "A23"
  [1] "The total number of orthogroups and singleton genes in this isolate:  13616"
  [1] "The total number of orthogroups and singleton genes not in the venn diagram:  2182"
  [1] "The total number of singleton genes not in the venn diagram:  256"
  [1] "A13"
  [1] "The total number of orthogroups and singleton genes in this isolate:  13333"
  [1] "The total number of orthogroups and singleton genes not in the venn diagram:  1705"
  [1] "The total number of singleton genes not in the venn diagram:  647"
  [1] "fo47"
  [1] "The total number of orthogroups and singleton genes in this isolate:  14272"
  [1] "The total number of orthogroups and singleton genes not in the venn diagram:  2644"
  [1] "The total number of singleton genes not in the venn diagram:  1363"
  NULL
4.6.a Extracting fasta files orthogroups

  ProgDir=~/git_repos/emr_repos/tools/pathogen/orthology/orthoMCL
  OrthogroupTxt=analysis/orthology/orthomcl/$IsolateAbrv/"$IsolateAbrv"_orthogroups.txt
  GoodProt=analysis/orthology/orthomcl/$IsolateAbrv/goodProteins/goodProteins.fasta
  OutDir=analysis/orthology/orthomcl/$IsolateAbrv/fasta/all_orthogroups
  mkdir -p $OutDir
  $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir > $OutDir/extractionlog.txt
A combined dataset for nucleotide data was made for all gene models:

for nuc_file in $(ls gene_pred/final_genes/F.*/*/final/final_genes_combined.gene.fasta | grep -e 'Fus2' -e '125' -e 'A23' -e 'PG' -e 'A28' -e 'CB3' -e 'A13' -e 'PG'); do
  Strain=$(echo $nuc_file | rev | cut -f3 -d '/' | rev)
  cat analysis/orthology/orthomcl/FoC_vs_Fo_vs_FoL_publication/FoC_vs_Fo_vs_FoL_publication_orthogroups.txt | grep -e 'Fus2|g16859.t' -e 'Fus2|g10474.t' | sed 's/ /\n/g' | grep -v 'orthogroup' | sed 's/\.t*//g' | sed 's/T0//g' | grep "$Strain" | cut -f2 -d '|' > tmp.txt
  ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/ORF_finder
  $ProgDir/extract_from_fasta.py --fasta $nuc_file  --headers tmp.txt > $WorkDir/FTF/"$Strain"_FTF.nuc
done

nuc_file=assembly/external_group/F.oxysporum/fo47/broad/fusarium_oxysporum_fo47_1_genes.fasta
cat $nuc_file | sed "s/FOZG/fo47|FOZG/g" >> $WorkDir/goodProteins/nucleotide_seq.fa
nuc_file=assembly/external_group/F.oxysporum_fsp_lycopersici/4287/Fusox1/Fusox1_GeneCatalog_transcripts_20110522.nt.fasta
cat $nuc_file | sed "s/FOXG/4287|FOXG/g" >> $WorkDir/goodProteins/nucleotide_seq.fa
The FTF ortholog group was extracted from the main table. Constituant genes were extracted from the nucleotide file:

  mkdir -p $WorkDir/FTF
    cat analysis/orthology/orthomcl/FoC_vs_Fo_vs_FoL_publication/FoC_vs_Fo_vs_FoL_publication_orthogroups.txt | grep -e 'Fus2|g16859.t' -e 'Fus2|g10474.t' | sed 's/ /\n/g' | grep -v 'orthogroup' | sed 's/\.t*//g' | sed 's/T0//g' > $WorkDir/FTF/FTF_list.txt
  ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/ORF_finder
  $ProgDir/extract_from_fasta.py --fasta $WorkDir/goodProteins/nucleotide_seq.fa --headers $WorkDir/FTF/FTF_list.txt > $WorkDir/FTF/orthogroup506_nuc.fa
