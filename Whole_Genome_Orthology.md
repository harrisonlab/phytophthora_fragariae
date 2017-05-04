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
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'Bc1|' -e 'Bc23|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'Nov5|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc16|' | grep -e 'A4|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'Bc1|' -e 'Bc23|' -e 'Nov27|' -e 'Nov71|' -e 'Nov77|' -e 'Nov9|' -e 'ONT3|' -e 'SCRP245_v2|' -e 'Nov5|' -e 'SCRP249|' -e 'SCRP324|' -e 'SCRP333|' | grep -e 'Bc16|' | grep -e 'A4|' | grep -o '|' | wc -l
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
8
This represents the following number of genes:
16
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
$ProgDir/UK2_Pf_venn_diag.r --inp $WorkDir/"$IsolateAbrv"_orthogroups.tab --out $WorkDir/"$IsolateAbrv"_UK2_orthogroups.pdf
$ProgDir/UK3_Pf_venn_diag.r --inp $WorkDir/"$IsolateAbrv"_orthogroups.tab --out $WorkDir/"$IsolateAbrv"_UK3_orthogroups.pdf
```

Output was a pdf file of the venn diagram.

The following additional information was also provided. The format of the following lines is as follows:

Isolate name (total number of orthogroups) number of unique singleton genes number of unique groups of inparalogs

###UK race 1 focused analysis

```
[1] "A4"
[1] "The total number of orthogroups and singleton genes in this isolate:  16638"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  2427"
[1] "The total number of singleton genes not in the venn diagram:  1013"
[1] "NOV-5"
[1] "The total number of orthogroups and singleton genes in this isolate:  16762"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  1539"
[1] "The total number of singleton genes not in the venn diagram:  1024"
[1] "NOV-27"
[1] "The total number of orthogroups and singleton genes in this isolate:  17613"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  3402"
[1] "The total number of singleton genes not in the venn diagram:  1373"
[1] "NOV-71"
[1] "The total number of orthogroups and singleton genes in this isolate:  16645"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  2434"
[1] "The total number of singleton genes not in the venn diagram:  962"
[1] "BC-16"
[1] "The total number of orthogroups and singleton genes in this isolate:  17356"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  3145"
[1] "The total number of singleton genes not in the venn diagram:  1530"
[1] "NOV-9"
[1] "The total number of orthogroups and singleton genes in this isolate:  17602"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  3391"
[1] "The total number of singleton genes not in the venn diagram:  1369"
[1] "BC-1"
[1] "The total number of orthogroups and singleton genes in this isolate:  17518"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  2049"
[1] "The total number of singleton genes not in the venn diagram:  1330"
```

###UK race 2 focused analysis

```
[1] "A4"
[1] "The total number of orthogroups and singleton genes in this isolate:  16638"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  1186"
[1] "The total number of singleton genes not in the venn diagram:  1013"
[1] "NOV-5"
[1] "The total number of orthogroups and singleton genes in this isolate:  16762"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  2246"
[1] "The total number of singleton genes not in the venn diagram:  1024"
[1] "NOV-27"
[1] "The total number of orthogroups and singleton genes in this isolate:  17613"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  3097"
[1] "The total number of singleton genes not in the venn diagram:  1373"
[1] "NOV-71"
[1] "The total number of orthogroups and singleton genes in this isolate:  16645"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  2129"
[1] "The total number of singleton genes not in the venn diagram:  962"
[1] "BC-16"
[1] "The total number of orthogroups and singleton genes in this isolate:  17356"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  1478"
[1] "The total number of singleton genes not in the venn diagram:  1530"
[1] "NOV-9"
[1] "The total number of orthogroups and singleton genes in this isolate:  17602"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  3086"
[1] "The total number of singleton genes not in the venn diagram:  1369"
[1] "BC-1"
[1] "The total number of orthogroups and singleton genes in this isolate:  17518"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  3086"
[1] "The total number of singleton genes not in the venn diagram:  1330"
```

###UK race 3 focused analysis

```
[1] "A4"
[1] "The total number of orthogroups and singleton genes in this isolate:  16638"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  2244"
[1] "The total number of singleton genes not in the venn diagram:  1013"
[1] "NOV-5"
[1] "The total number of orthogroups and singleton genes in this isolate:  16762"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  2368"
[1] "The total number of singleton genes not in the venn diagram:  1024"
[1] "NOV-27"
[1] "The total number of orthogroups and singleton genes in this isolate:  17613"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  1754"
[1] "The total number of singleton genes not in the venn diagram:  1373"
[1] "NOV-71"
[1] "The total number of orthogroups and singleton genes in this isolate:  16645"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  1331"
[1] "The total number of singleton genes not in the venn diagram:  962"
[1] "BC-16"
[1] "The total number of orthogroups and singleton genes in this isolate:  17356"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  2962"
[1] "The total number of singleton genes not in the venn diagram:  1530"
[1] "NOV-9"
[1] "The total number of orthogroups and singleton genes in this isolate:  17602"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  1757"
[1] "The total number of singleton genes not in the venn diagram:  1369"
[1] "BC-1"
[1] "The total number of orthogroups and singleton genes in this isolate:  17518"
[1] "The total number of orthogroups and singleton genes not in the venn diagram:  3208"
[1] "The total number of singleton genes not in the venn diagram:  1330"
```

#Analysis of orthogroups unique to UK race 2 (Strains BC-16 & A4)

##The genes unique to Race 2 were identified within the orthology analysis

##First variables were set:

```bash
WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi
UK2UniqDir=$WorkDir/UK2_unique
Orthogroups=$WorkDir/All_Strains_plus_rubi_orthogroups.txt
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
29
The following number genes are contained in these orthogroups:
127
```

#Race 2 unique RxLR families

#Race 2 RxLR genes were parsed to the same format as the gene names used in the analysis:

```bash
for num in 1
do
    RxLR_Names_Bc16=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_Total_RxLR_EER_motif_hmm.txt
    RxLR_Names_A4=analysis/RxLR_effectors/combined_evidence/P.fragariae/A4/A4_Total_RxLR_EER_motif_hmm.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi
    RxLR_Dir=$WorkDir/UKR2_RxLR
    Orthogroups=$WorkDir/All_Strains_plus_rubi_orthogroups.txt
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
674
Of these, the following number were found in orthogroups:
485
These were distributed through the following number of Orthogroups:
185
The following RxLRs were found in Race 2 unique orthogroups:
0
These orthogroups contain the following number of RxLRs:
0
The following RxLRs were found in P.fragariae unique orthogroups:
185
These orthogroups contain the following number of RxLRs:
485
```

#The Race 2 RxLR genes that were not found in orthogroups were identified:

```bash
for num in 1
do
    RxLR_UK2_uniq=$RxLR_Dir/UK2_unique_RxLRs.txt
    cat $RxLR_ID | grep -v -w -f $RxLR_Orthogroup_hits | tr -d 'Bc16|' | tr -d 'A4|' > $RxLR_UK2_uniq
    echo "The number of UK2 unique RxLRs are:"
    cat $RxLR_UK2_uniq | wc -l
    RxLR_Seq_Bc16=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_final_RxLR_EER.fa
    RxLR_Seq_A4=analysis/RxLR_effectors/combined_evidence/P.fragariae/A4/A4_final_RxLR_EER.fa
    Final_genes_Bc16=gene_pred/codingquary/P.fragariae/Bc16/final/final_genes_combined.pep.fasta
    Final_genes_A4=gene_pred/codingquary/P.fragariae/A4/final/final_genes_combined.pep.fasta
    RxLR_UK2_uniq_fa=$RxLR_Dir/UK2_unique_RxLRs.fa
    cat $Final_genes_Bc16 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $RxLR_UK2_uniq | grep -E -v '^--' > $RxLR_UK2_uniq_fa
    cat $Final_genes_A4 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $RxLR_UK2_uniq | grep -E -v '^--' >> $RxLR_UK2_uniq_fa
done
```

```
The number of UK2 unique RxLRs are:
189
```

##Extracting fasta files for orthogroups containing Race 2 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UKR2_RxLR/UK2_RxLR_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UKR2_RxLR/orthogroups_fasta_UK2_RxLR
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```


##Extracting fasta files for P. fragariae orthogroups containing Race 2 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UKR2_RxLR/Pf_RxLR_Orthogroups_hits.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UKR2_RxLR/orthogroups_fasta_Pf_RxLR
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
    WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi
    Sec_Dir=$WorkDir/UKR2_Secreted
    Orthogroups=$WorkDir/All_Strains_plus_rubi_orthogroups.txt
    Sec_ID=$Sec_Dir/UKR2_aug_Sec_IDs.txt
    mkdir -p $Sec_Dir
    cat $Sec_Names_Bc16 | sed -r 's/^/Bc16|/g' > $Sec_ID
    cat $Sec_Names_A4 | sed -r 's/^/A4|/g' >> $Sec_ID
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
    Sec_Pf_uniq_groups=$RxLR_Dir/Sec_RxLR_Orthogroups_hits.txt
    cat $Sec_Orthogroup > $Sec_Pf_uniq_groups
    cat $Sec_Pf_uniq_groups | wc -l
    echo "These orthogroups contain the following number of Secreted proteins:"
    cat $Sec_Pf_uniq_groups | grep -w -o -f $Sec_ID | wc -l
done
```

```
The number of RxLRs searched for is:
674
Of these, the following number were found in orthogroups:
485
These were distributed through the following number of Orthogroups:
185
The following RxLRs were found in Race 2 unique orthogroups:
0
These orthogroups contain the following number of RxLRs:
0
The following RxLRs were found in P.fragariae unique orthogroups:
185
These orthogroups contain the following number of RxLRs:
485
```

#The Race 2 secreted protein genes that were not found in orthogroups were identified:

```bash
for num in 1
do
    Sec_UK2_uniq=$Sec_Dir/UK2_unique_Sec.txt
    cat $Sec_ID | grep -v -w -f $Sec_Orthogroup_hits | tr -d 'Bc16|' | tr -d 'A4|' > $Sec_UK2_uniq
    echo "The number of UK2 unique secreted proteins are:"
    cat $Sec_UK2_uniq | wc -l
    Sec_Seq_Bc16=gene_pred/combined_sigP_CQ/P.fragariae/Bc16/Bc16_all_secreted.fa
    Sec_Seq_A4=gene_pred/combined_sigP_CQ/P.fragariae/A4/A4_all_secreted.fa
    Final_genes_Bc16=gene_pred/codingquary/P.fragariae/Bc16/final/final_genes_combined.pep.fasta
    Final_genes_A4=gene_pred/codingquary/P.fragariae/A4/final/final_genes_combined.pep.fasta
    Sec_UK2_uniq_fa=$Sec_Dir/UK2_unique_Sec.fa
    cat $Final_genes_Bc16 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Sec_UK2_uniq | grep -E -v '^--' > $Sec_UK2_uniq_fa
    cat $Final_genes_A4 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $Sec_UK2_uniq | grep -E -v '^--' >> $Sec_UK2_uniq_fa
done
```

```
The number of UK2 unique RxLRs are:
189
```

##Extracting fasta files for orthogroups containing Race 2 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UKR2_RxLR/UK2_RxLR_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UKR2_RxLR/orthogroups_fasta_UK2_RxLR
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```


##Extracting fasta files for P. fragariae orthogroups containing Race 2 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UKR2_RxLR/Pf_RxLR_Orthogroups_hits.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UKR2_RxLR/orthogroups_fasta_Pf_RxLR
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
    WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi
    CRN_Dir=$WorkDir/UK2_CRN
    Orthogroups=$WorkDir/All_Strains_plus_rubi_orthogroups.txt
    CRN_ID_UK2=$CRN_Dir/UK2_CRN_hmmer_IDs.txt
    mkdir -p $CRN_Dir
    cat $CRN_Names_Bc16 | sed 's/g/Bc16|g/g' > $CRN_ID_UK2
    cat $CRN_Names_A4 | sed 's/g/A4|g/g' >> $CRN_ID_UK2
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
done
```

```
The number of CRNs searched for is:
236
Of these, the following number were found in orthogroups:
225
These were distributed through the following number of Orthogroups:
69
The following CRNs were found in Race 2 unique orthogroups:
0
The following CRNs were found in P.fragariae unique orthogroups:
69
```

#The Race 2 CRN genes not found in orthogroups were identified:

```bash
for num in 1
do
    CRN_UK2_uniq=$CRN_Dir/UK2_unique_CRNs.txt
    cat $CRN_ID_UK2 | grep -v -w -f $CRN_Orthogroup_hits_UK2 | tr -d 'Bc16|' | tr -d 'A4|' > $CRN_UK2_uniq
    echo "The number of Race 2 unique CRNs are:"
    cat $CRN_UK2_uniq | wc -l
    CRN_Seq_Bc16=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc16/Bc16_final_CRN.fa
    CRN_Seq_A4=analysis/CRN_effectors/hmmer_CRN/P.fragariae/A4/A4_final_CRN.fa
    Final_genes_Bc16=gene_pred/codingquary/P.fragariae/Bc16/final/final_genes_combined.pep.fasta
    Final_genes_A4=gene_pred/codingquary/P.fragariae/A4/final/final_genes_combined.pep.fasta
    CRN_UK2_uniq_fa=$CRN_Dir/UK2_unique_CRNs.fa
    cat $Final_genes_Bc16 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $CRN_UK2_uniq | grep -E -v '^--' > $CRN_UK2_uniq_fa
    cat $Final_genes_A4 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $CRN_UK2_uniq | grep -E -v '^--' >> $CRN_UK2_uniq_fa
done
```

```
The number of Race 2 unique CRNs are:
12
```

##Extracting fasta files for orthogroups containing Race 2 putative CRNs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK2_CRN/UK2_CRN_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK2_CRN/orthogroups_fasta_UK2_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

##Extracting fasta files for P. fragariae orthogroups containing Race 2 putative CRNs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK2_CRN/Pf_CRN_Orthogroups_hits.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK2_CRN/orthogroups_fasta_Pf_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

#Analysis of orthogroups unique to UK race 1 (Strains BC-1 & NOV-5)

##The genes unique to Race 1 were identified within the orthology analysis

##First variables were set:

```bash
WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi
UK1UniqDir=$WorkDir/UK1_unique
Orthogroups=$WorkDir/All_Strains_plus_rubi_orthogroups.txt
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
16
The following number genes are contained in these orthogroups:
74
```

#Race 1 unique RxLR families

#Race 1 RxLR genes were parsed to the same format as the gene names used in the analysis:

```bash
for num in 1
do
    RxLR_Names_Bc1=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc1/Bc1_Total_RxLR_EER_motif_hmm.txt
    RxLR_Names_Nov5=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov5/Nov5_Total_RxLR_EER_motif_hmm.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi
    RxLR_Dir=$WorkDir/UK1_RxLR
    Orthogroups=$WorkDir/All_Strains_plus_rubi_orthogroups.txt
    RxLR_ID=$RxLR_Dir/UK1_aug_RxLR_EER_IDs.txt
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
629
Of these, the following number were found in orthogroups:
462
These were distributed through the following number of Orthogroups:
184
The following RxLRs were found in Race 1 unique orthogroups:
0
These orthogroups contain the following number of RxLRs:
0
The following RxLRs were found in P.fragariae unique orthogroups:
184
These orthogroups contain the following number of RxLRs:
462
```

#The Race 1 RxLR genes that were not found in orthogroups were identified:

```bash
for num in 1
do
    RxLR_UK1_uniq=$RxLR_Dir/UK1_unique_RxLRs.txt
    cat $RxLR_ID | grep -v -w -f $RxLR_Orthogroup_hits | tr -d 'Bc1|' | tr -d 'Nov5|' > $RxLR_UK1_uniq
    echo "The number of UK1 unique RxLRs are:"
    cat $RxLR_UK1_uniq | wc -l
    RxLR_Seq_Bc1=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc1/Bc1_final_RxLR_EER.fa
    RxLR_Seq_Nov5=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov5/Nov5_final_RxLR_EER.fa
    Final_genes_Bc1=gene_pred/codingquary/P.fragariae/Bc1/final/final_genes_combined.pep.fasta
    Final_genes_Nov5=gene_pred/codingquary/P.fragariae/Nov5/final/final_genes_combined.pep.fasta
    RxLR_UK1_uniq_fa=$RxLR_Dir/UK1_unique_RxLRs.fa
    cat $Final_genes_Bc1 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $RxLR_UK1_uniq | grep -E -v '^--' > $RxLR_UK1_uniq_fa
    cat $Final_genes_Nov5 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $RxLR_UK1_uniq | grep -E -v '^--' >> $RxLR_UK1_uniq_fa
done
```

```
The number of UK2 unique RxLRs are:
167
```

##Extracting fasta files for orthogroups containing Race 1 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK1_RxLR/UK1_RxLR_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK1_RxLR/orthogroups_fasta_UK1_RxLR
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```


##Extracting fasta files for P. fragariae orthogroups containing Race 1 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK1_RxLR/Pf_RxLR_Orthogroups_hits.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK1_RxLR/orthogroups_fasta_Pf_RxLR
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
    WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi
    CRN_Dir=$WorkDir/UK1_CRN
    Orthogroups=$WorkDir/All_Strains_plus_rubi_orthogroups.txt
    CRN_ID_UK1=$CRN_Dir/UK1_CRN_hmmer_IDs.txt
    mkdir -p $CRN_Dir
    cat $CRN_Names_Bc1 | sed 's/g/Bc1|g/g' > $CRN_ID_UK1
    cat $CRN_Names_Nov5 | sed 's/g/Nov5|g/g' >> $CRN_ID_UK1
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
done
```

```
The number of CRNs searched for is:
222
Of these, the following number were found in orthogroups:
210
These were distributed through the following number of Orthogroups:
68
The following CRNs were found in Race 1 unique orthogroups:
0
The following CRNs were found in P.fragariae unique orthogroups:
68
```

#The Race 1 CRN genes not found in orthogroups were identified:

```bash
for num in 1
do
    CRN_UK1_uniq=$CRN_Dir/UK1_unique_CRNs.txt
    cat $CRN_ID_UK1 | grep -v -w -f $CRN_Orthogroup_hits_UK1 | tr -d 'Bc1|' | tr -d 'Nov5|' > $CRN_UK1_uniq
    echo "The number of Race 1 unique CRNs are:"
    cat $CRN_UK1_uniq | wc -l
    CRN_Seq_Bc1=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc1/Bc1_final_CRN.fa
    CRN_Seq_Nov5=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov5/Nov5_final_CRN.fa
    Final_genes_Bc1=gene_pred/codingquary/P.fragariae/Bc1/final/final_genes_combined.pep.fasta
    Final_genes_Nov5=gene_pred/codingquary/P.fragariae/Nov5/final/final_genes_combined.pep.fasta
    CRN_UK1_uniq_fa=$CRN_Dir/UK1_unique_CRNs.fa
    cat $Final_genes_Bc1 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $CRN_UK1_uniq | grep -E -v '^--' > $CRN_UK1_uniq_fa
    cat $Final_genes_Nov5 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $CRN_UK1_uniq | grep -E -v '^--' >> $CRN_UK1_uniq_fa
done
```

```
The number of Race 1 unique CRNs are:
12
```

##Extracting fasta files for orthogroups containing Race 1 putative CRNs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK1_CRN/UK1_CRN_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK1_CRN/orthogroups_fasta_UK1_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

##Extracting fasta files for P. fragariae orthogroups containing Race 1 putative CRNs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK1_CRN/Pf_CRN_Orthogroups_hits.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK1_CRN/orthogroups_fasta_Pf_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

#Analysis of orthogroups unique to UK race 3 (Strains NOV-27, NOV-71 & NOV-9)

##The genes unique to Race 3 were identified within the orthology analysis

##First variables were set:

```bash
WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi
UK3UniqDir=$WorkDir/UK3_unique
Orthogroups=$WorkDir/All_Strains_plus_rubi_orthogroups.txt
GoodProts=$WorkDir/goodProteins/goodProteins.fasta
Final_genes_Nov27=gene_pred/codingquary/P.fragariae/Nov27/final/final_genes_combined.pep.fasta
Final_genes_Nov71=gene_pred/codingquary/P.fragariae/Nov71/final/final_genes_combined.pep.fasta
Final_genes_Nov9=gene_pred/codingquary/P.fragariae/Nov9/final/final_genes_combined.pep.fasta
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
39
The following number genes are contained in these orthogroups:
220
```

#Race 3 unique RxLR families

#Race 3 RxLR genes were parsed to the same format as the gene names used in the analysis:

```bash
for num in 1
do
    RxLR_Names_Nov27=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov27/Nov27_Total_RxLR_EER_motif_hmm.txt
    RxLR_Names_Nov71=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov71/Nov71_Total_RxLR_EER_motif_hmm.txt
    RxLR_Names_Nov9=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov9/Nov9_Total_RxLR_EER_motif_hmm.txt
    WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi
    RxLR_Dir=$WorkDir/UK3_RxLR
    Orthogroups=$WorkDir/All_Strains_plus_rubi_orthogroups.txt
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
938
Of these, the following number were found in orthogroups:
690
These were distributed through the following number of Orthogroups:
187
The following RxLRs were found in Race 3 unique orthogroups:
1
These orthogroups contain the following number of RxLRs:
3
The following RxLRs were found in P.fragariae unique orthogroups:
187
These orthogroups contain the following number of RxLRs:
690
```

#The Race 3 RxLR genes that were not found in orthogroups were identified:

```bash
for num in 1
do
    RxLR_UK3_uniq=$RxLR_Dir/UK3_unique_RxLRs.txt
    cat $RxLR_ID | grep -v -w -f $RxLR_Orthogroup_hits | tr -d 'Nov27|' | tr -d 'Nov71|' | tr -d 'Nov9|' > $RxLR_UK3_uniq
    echo "The number of UK3 unique RxLRs are:"
    cat $RxLR_UK3_uniq | wc -l
    RxLR_Seq_Nov27=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov27/Nov27_final_RxLR_EER.fa
    RxLR_Seq_Nov71=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov71/Nov71_final_RxLR_EER.fa
    RxLR_Seq_Nov9=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov9/Nov9_final_RxLR_EER.fa
    Final_genes_Nov27=gene_pred/codingquary/P.fragariae/Nov27/final/final_genes_combined.pep.fasta
    Final_genes_Nov71=gene_pred/codingquary/P.fragariae/Nov71/final/final_genes_combined.pep.fasta
    Final_genes_Nov9=gene_pred/codingquary/P.fragariae/Nov9/final/final_genes_combined.pep.fasta
    RxLR_UK3_uniq_fa=$RxLR_Dir/UK3_unique_RxLRs.fa
    cat $Final_genes_Nov27 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $RxLR_UK3_uniq | grep -E -v '^--' > $RxLR_UK3_uniq_fa
    cat $Final_genes_Nov71 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $RxLR_UK3_uniq | grep -E -v '^--' >> $RxLR_UK3_uniq_fa
    cat $Final_genes_Nov9 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $RxLR_UK3_uniq | grep -E -v '^--' >> $RxLR_UK3_uniq_fa
done
```

```
The number of UK3 unique RxLRs are:
248
```

##Extracting fasta files for orthogroups containing Race 3 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK3_RxLR/UK3_RxLR_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK3_RxLR/orthogroups_fasta_UK1_RxLR
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```


##Extracting fasta files for P. fragariae orthogroups containing Race 3 putative RxLRs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK3_RxLR/Pf_RxLR_Orthogroups_hits.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK3_RxLR/orthogroups_fasta_Pf_RxLR
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
    WorkDir=analysis/orthology/orthomcl/All_Strains_plus_rubi
    CRN_Dir=$WorkDir/UK3_CRN
    Orthogroups=$WorkDir/All_Strains_plus_rubi_orthogroups.txt
    CRN_ID_UK3=$CRN_Dir/UK3_CRN_hmmer_IDs.txt
    mkdir -p $CRN_Dir
    cat $CRN_Names_Nov27 | sed 's/g/Nov27|g/g' > $CRN_ID_UK3
    cat $CRN_Names_Nov71 | sed 's/g/Nov71|g/g' >> $CRN_ID_UK3
    cat $CRN_Names_Nov9 | sed 's/g/Nov9|g/g' >> $CRN_ID_UK3
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
done
```

```
The number of CRNs searched for is:
338
Of these, the following number were found in orthogroups:
321
These were distributed through the following number of Orthogroups:
72
The following CRNs were found in Race 3 unique orthogroups:
0
The following CRNs were found in P.fragariae unique orthogroups:
72
```

#The Race 3 CRN genes not found in orthogroups were identified:

```bash
for num in 1
do
    CRN_UK3_uniq=$CRN_Dir/UK3_unique_CRNs.txt
    cat $CRN_ID_UK3 | grep -v -w -f $CRN_Orthogroup_hits_UK3 | tr -d 'Nov27|' | tr -d 'Nov71|' | tr -d 'Nov9|' > $CRN_UK3_uniq
    echo "The number of Race 3 unique CRNs are:"
    cat $CRN_UK3_uniq | wc -l
    CRN_Seq_Nov27=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov27/Nov27_final_CRN.fa
    CRN_Seq_Nov71=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov71/Nov71_final_CRN.fa
    CRN_Seq_Nov9=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Nov9/Nov9_final_CRN.fa
    Final_genes_Nov27=gene_pred/codingquary/P.fragariae/Nov27/final/final_genes_combined.pep.fasta
    Final_genes_Nov71=gene_pred/codingquary/P.fragariae/Nov71/final/final_genes_combined.pep.fasta
    Final_genes_Nov9=gene_pred/codingquary/P.fragariae/Nov9/final/final_genes_combined.pep.fasta
    CRN_UK3_uniq_fa=$CRN_Dir/UK3_unique_CRNs.fa
    cat $Final_genes_Nov27 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $CRN_UK3_uniq | grep -E -v '^--' > $CRN_UK3_uniq_fa
    cat $Final_genes_Nov71 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $CRN_UK3_uniq | grep -E -v '^--' >> $CRN_UK3_uniq_fa
    cat $Final_genes_Nov9 | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $CRN_UK3_uniq | grep -E -v '^--' >> $CRN_UK3_uniq_fa
done
```

```
The number of Race 3 unique CRNs are:
20
```

##Extracting fasta files for orthogroups containing Race 3 putative CRNs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK3_CRN/UK3_CRN_Orthogroups.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK3_CRN/orthogroups_fasta_UK3_CRN
    mkdir -p $OutDir
    $ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
done
```

##Extracting fasta files for P. fragariae orthogroups containing Race 3 putative CRNs

```bash
for num in 1
do
    ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
    OrthogroupTxt=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK3_CRN/Pf_CRN_Orthogroups_hits.txt
    GoodProt=analysis/orthology/orthomcl/All_Strains_plus_rubi/goodProteins/goodProteins.fasta
    OutDir=analysis/orthology/orthomcl/All_Strains_plus_rubi/UK1_CRN/orthogroups_fasta_Pf_CRN
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
