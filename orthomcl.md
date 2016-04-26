#Beginning orthology analysis of: A4, Bc1, Bc16, Bc23, Nov27, Nov5, Nov71, Nov77, Nov9, ONT3, SCRP245_v2

#RxLR Regex orthologies

##Set up working directories

```bash
ProjDir=/home/groups/harrisonlab/project_files/phytophthora_fragariae
cd $ProjDir
IsolateAbrv=phytophthora_fragariae
WorkDir=analysis/orthology/orthomcl/$IsolateAbrv
mkdir -p $WorkDir
mkdir -p $WorkDir/formatted
mkdir -p $WorkDir/goodProteins
mkdir -p $WorkDir/badProteins
```

##Format fasta files

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    Taxon_code=$Strain
    Fasta_file=analysis/RxLR_effectors/combined_evidence/P.fragariae/$Strain/"$Strain"_Total_RxLR_EER_motif_hmm_headers.fa
    Id_field=1
    orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
    mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
done
```

##Filter proteins into good and poor sets.

```bash
Input_dir=$WorkDir/formatted
Min_length=10
Max_percent_stops=20
Good_proteins_file=$WorkDir/goodProteins/goodProteins.fasta
Poor_proteins_file=$WorkDir/badProteins/poorProteins.fasta
orthomclFilterFasta $Input_dir $Min_length $Max_percent_stops $Good_proteins_file $Poor_proteins_file
```

##Perform an all-vs-all blast of the proteins

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
        sleep 10
        printf "."
        Jobs=$(qstat | grep 'blast_500' | grep 'qw' | wc -l)
    done
    printf "\n"
    echo $File
    BlastOut=$(echo $File | sed 's/.fa/.tab/g')
    qsub $ProgDir/blast_500.sh $BlastDB $File $BlastOut
done
```

##Merge the all-vs-all blast results

```bash
MergeHits=$WorkDir/"$IsolateAbrv"_blast.tab
printf "" > $MergeHits
for Num in $(ls $WorkDir/splitfiles/*.tab | rev | cut -f1 -d '_' | rev | sort -n)
do
    File=$(ls $WorkDir/splitfiles/*_$Num)
    cat $File
done > $MergeHits
```

##Perform ortholog identification
#Have to create alternative qsub script to deal with difference in file architecture

```bash
ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
MergeHits=$WorkDir/"$IsolateAbrv"_blast.tab
GoodProts=$WorkDir/goodProteins/goodProteins.fasta
qsub $ProgDir/qsub_orthomcl.sh $MergeHits $GoodProts 5
```

```
239 orthogroups were identified
```

#Analysis of orthogroups unique to UK race 2 (Strains BC-16)

##The genes unique to Race 2 were identified within the orthology analysis

##First variables were set:

```bash
WorkDir=analysis/orthology/orthomcl/phytophthora_fragariae
Bc16UniqDir=$WorkDir/Bc16_unique
Orthogroups=$WorkDir/phytophthora_fragariae_orthogroups.txt
GoodProts=$WorkDir/goodProteins/goodProteins.fasta
Braker_genes=gene_pred/braker/P.fragariae/Bc16/P.fragariae_Bc16_braker/augustus.aa
Uniq_Bc16_groups=$Bc16UniqDir/Bc16_uniq_orthogroups.txt
mkdir -p $Bc16UniqDir
```

#Orthogroups only containing Race 2 genes were extracted:

##Bars are to prevent incorrect filtering

```bash
cat $Orthogroups | grep -v 'A4|' | grep -v 'Bc1|' | grep -v 'Bc23|' | grep -v 'Nov27|' | grep -v 'Nov5|' | grep -v 'Nov71|' | grep -v 'Nov77|' | grep -v 'Nov9|' | grep -v 'ONT3|' | grep -v 'SCRP245_v2|' > $Uniq_Bc16_groups
echo "The number of orthogroups unique to Race 2 are:"
cat $Uniq_Bc16_groups | wc -l
echo "The following number genes are contained in these orthogroups:"
cat $Uniq_Bc16_groups | grep -o 'Bc16|' | wc -l
```

```
The number of orthogroups unique to Race 2 are:
0
The following number genes are contained in these orthogroups:
0
```

#Race 2 unique RxLR families

#Race 2 RxLR genes were parsed to the same format as the gene names used in the analysis:

```bash
RxLR_Names_Bc16=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_Total_RxLR_EER_motif_hmm.txt
WorkDir=analysis/orthology/orthomcl/phytophthora_fragariae
RxLR_Dir=$WorkDir/Bc16_RxLR
Orthogroups=$WorkDir/phytophthora_fragariae_orthogroups.txt
RxLR_ID_Bc16=$RxLR_Dir/Bc16_aug_RxLR_EER_IDs.txt
mkdir -p $RxLR_Dir
cat $RxLR_Names_Bc16 | sed -r 's/^/Bc16|/g' > $RxLR_ID_Bc16
```

#Ortholog groups containing RxLR proteins were identified using the following commands:

```bash
echo "The number of RxLRs searched for is:"
cat $RxLR_ID_Bc16 | wc -l
echo "Of these, the following number were found in orthogroups:"
RxLR_Orthogroup_hits_Bc16=$RxLR_Dir/Bc16_RxLR_Orthogroups_hits.txt
cat $Orthogroups | grep -o -w -f $RxLR_ID_Bc16 > $RxLR_Orthogroup_hits_Bc16
cat $RxLR_Orthogroup_hits_Bc16 | wc -l
echo "These were distributed through the following number of Orthogroups:"
RxLR_Orthogroup_Bc16=$RxLR_Dir/Bc16_RxLR_Orthogroups.txt
cat $Orthogroups | grep -w -f $RxLR_ID_Bc16 > $RxLR_Orthogroup_Bc16
cat $RxLR_Orthogroup_Bc16 | wc -l
echo "The following RxLRs were found in Race 2 unique orthogroups:"
RxLR_Bc16_uniq_groups=$RxLR_Dir/Bc16_uniq_RxLR_Orthogroups_hits.txt
cat $RxLR_Orthogroup_Bc16 | grep -v 'A4|' | grep -v 'Bc1|' | grep -v 'Bc23|' | grep -v 'Nov27|' | grep -v 'Nov5|' | grep -v 'Nov71|' | grep -v 'Nov77|' | grep -v 'Nov9|' | grep -v 'ONT3|' | grep -v 'SCRP245_v2|' > $RxLR_Bc16_uniq_groups
cat $RxLR_Bc16_uniq_groups | wc -l
echo "These orthogroups contain the following number of RxLRs:"
cat $RxLR_Bc16_uniq_groups | grep -w -o -f $RxLR_ID_Bc16 | wc -l
echo "The following RxLRs were found in P.fragariae unique orthogroups:"
RxLR_Pf_uniq_groups=$RxLR_Dir/Pf_RxLR_Orthogroups_hits.txt
cat $RxLR_Orthogroup_Bc16 > $RxLR_Pf_uniq_groups
cat $RxLR_Pf_uniq_groups | wc -l
echo "These orthogroups contain the following number of RxLRs:"
cat $RxLR_Pf_uniq_groups | grep -w -o -f $RxLR_ID_Bc16 | wc -l
```

```
The number of RxLRs searched for is:
237
Of these, the following number were found in orthogroups:
237
These were distributed through the following number of Orthogroups:
178
The following RxLRs were found in Race 2 unique orthogroups:
0
These orthogroups contain the following number of RxLRs:
0
The following RxLRs were found in P.fragariae unique orthogroups:
178
These orthogroups contain the following number of RxLRs:
237
```

#The Race 2 RxLR genes that were not found in orthogroups were identified:

```bash
RxLR_Bc16_uniq=$RxLR_Dir/Bc16_unique_RxLRs.txt
cat $RxLR_ID_Bc16 | grep -v -w -f $RxLR_Orthogroup_hits_Bc16 | tr -d 'Bc16|' > $RxLR_Bc16_uniq
echo "The number of BC-16 unique RxLRs are:"
cat $RxLR_Bc16_uniq | wc -l
RxLR_Seq_Bc16=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_Braker1_RxLR_EER_motif_hmm.fa
Braker_genes=gene_pred/braker/P.fragariae/Bc16/P.fragariae_Bc16_braker/augustus.aa
RxLR_Bc16_uniq_fa=$RxLR_Dir/Bc16_unique_RxLRs.fa
cat $Braker_genes | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $RxLR_Bc16_uniq | grep -E -v '^--' > $RxLR_Bc16_uniq_fa
```

```
The number of BC-16 unique RxLRs are:
0
```

##Extracting fasta files for orthogroups containing Race 2 putative RxLRs

```bash
ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
OrthogroupTxt=analysis/orthology/orthomcl/phytophthora_fragariae/Bc16_RxLR/Bc16_RxLR_Orthogroups.txt
GoodProt=analysis/orthology/orthomcl/phytophthora_fragariae/goodProteins/goodProteins.fasta
OutDir=analysis/orthology/orthomcl/phytophthora_fragariae/Bc16_RxLR/orthogroups_fasta_Bc16_RxLR
mkdir -p $OutDir
$ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
```

##Extracting fasta files for P. fragariae orthogroups containing Race 2 putative RxLRs

```bash
ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
OrthogroupTxt=analysis/orthology/orthomcl/phytophthora_fragariae/Bc16_RxLR/Pf_RxLR_Orthogroups_hits.txt
GoodProt=analysis/orthology/orthomcl/phytophthora_fragariae/goodProteins/goodProteins.fasta
OutDir=analysis/orthology/orthomcl/phytophthora_fragariae/Bc16_RxLR/orthogroups_fasta_Pf_RxLR
mkdir -p $OutDir
$ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
```

<!-- ##Race 2 unique Crinkler families

#Race 2 crinkler genes were parsed to the same format as the gene names used in the analysis:

```bash
CRN_Names_Bc16=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc16/Bc16_Braker1_CRN_hmmer_headers.txt
WorkDir=analysis/orthology/orthomcl/phytophthora_fragariae
CRN_Dir=$WorkDir/Bc16_CRN
Orthogroups=$WorkDir/phytophthora_fragariae_orthogroups.txt
CRN_ID_Bc16=$CRN_Dir/Bc16_CRN_hmmer_IDs.txt
mkdir -p $CRN_Dir
cat $CRN_Names_Bc16 | sed 's/g/Bc16|g/g' > $CRN_ID_Bc16
```

#Ortholog groups containing CRN proteins were identified using the following commands:

```bash
echo "The number of CRNs searched for is:"
cat $CRN_ID_Bc16 | wc -l
echo "Of these, the following number were found in orthogroups:"
CRN_Orthogroup_hits_Bc16=$CRN_Dir/Bc16_CRN_Orthogroups_hits.txt
cat $Orthogroups | grep -o -w -f $CRN_ID_Bc16 > $CRN_Orthogroup_hits_Bc16
cat $CRN_Orthogroup_hits_Bc16 | wc -l
echo "These were distributed through the following number of Orthogroups:"
CRN_Orthogroup_Bc16=$CRN_Dir/Bc16_CRN_Orthogroups.txt
cat $Orthogroups | grep -w -f $CRN_ID_Bc16 > $CRN_Orthogroup_Bc16
cat $CRN_Orthogroup_Bc16 | wc -l
echo "The following CRNs were found in Race 2 unique orthogroups:"
CRN_Bc16_uniq_groups=$CRN_Dir/Bc16_uniq_CRN_Orthogroups_hits.txt
cat $CRN_Orthogroup_Bc16 | grep -v 'A4' | grep -v 'Bc1' | grep -v 'Bc23' | grep -v 'Nov27' | grep -v 'Nov5' | grep -v 'Nov71' | grep -v 'Nov77' | grep -v 'Nov9' | grep -v 'ONT3' | grep -v 'SCRP245_v2' > $CRN_Bc16_uniq_groups
cat $CRN_Bc16_uniq_groups | wc -l
echo "The following CRNs were found in P.fragariae unique orthogroups:"
CRN_Pf_uniq_groups=$CRN_Dir/Pf_CRN_Orthogroups_hits.txt
cat $CRN_Orthogroup_Bc16 > $CRN_Pf_uniq_groups
cat $CRN_Pf_uniq_groups | wc -l
```

```
```

#The Race 2 CRN genes not found in orthogroups were identified:

```bash
CRN_Bc16_uniq=$CRN_Dir/Bc16_unique_CRNs.txt
cat $CRN_ID_Bc16 | grep -v -w -f $CRN_Orthogroup_hits_Bc16 | tr -d 'Bc16|' > $CRN_Bc16_uniq
echo "The number of Race 2 unique CRNs are:"
cat $CRN_Bc16_uniq | wc -l
CRN_Seq_Bc16=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc16/Bc16_pub_CRN_hmmer_out.fa
Braker_genes=gene_pred/braker/P.fragariae/Bc16/P.fragariae_Bc16_braker/augustus.aa
CRN_Bc16_uniq_fa=$CRN_Dir/Bc16_unique_CRNs.fa
cat $Braker_genes | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $CRN_Bc16_uniq | grep -E -v '^--' > $CRN_Bc16_uniq_fa
```

```
```

##Extracting fasta files for orthogroups containing Race 2 putative CRNs

```bash
ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
OrthogroupTxt=analysis/orthology/orthomcl/phytophthora_fragariae/Bc16_CRN/Bc16_CRN_Orthogroups.txt
GoodProt=analysis/orthology/orthomcl/phytophthora_fragariae/goodProteins/goodProteins.fasta
OutDir=analysis/orthology/orthomcl/phytophthora_fragariae/Bc16_CRN/orthogroups_fasta_Bc16_CRN
mkdir -p $OutDir
$ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
``` -->

<!-- ##Determining function of orthogroups (6.3 is the start here, all not relevant)

#Lists of genes from Race 2 unique genes, P. fragariae orthogroups and the largest shared gene families were identified

#Unclear on interproscan here, it doesn't match my output

```bash
WorkDir=analysis/orthology/orthomcl/phytophthora_fragariae
InterProFile=gene_pred/interproscan/Bc16/P.fragariae_Bc16_braker/10300_interproscan.tsv
``` -->

#Analysis of orthogroups unique to UK race 1 (Strains BC-1 and NOV-5)

##The genes unique to Race 1 were identified within the orthology analysis

##First variables were set:

```bash
WorkDir=analysis/orthology/orthomcl/phytophthora_fragariae
UKR1UniqDir=$WorkDir/UKR1_unique
Orthogroups=$WorkDir/phytophthora_fragariae_orthogroups.txt
GoodProts=$WorkDir/goodProteins/goodProteins.fasta
Braker_genes_Bc1=gene_pred/braker/P.fragariae/Bc1/P.fragariae_Bc1_braker/augustus.aa
Braker_genes_Nov5=gene_pred/braker/P.fragariae/Nov5/P.fragariae_Nov5_braker/augustus.aa
Uniq_UKR1_groups=$UKR1UniqDir/UKR1_uniq_orthogroups.txt
mkdir -p $UKR1UniqDir
```

#Orthogroups only containing Race 2 genes were extracted:

##Bars are to prevent incorrect filtering

```bash
cat $Orthogroups | grep -v 'A4|' | grep -v 'Bc1|' | grep -v 'Bc23|' | grep -v 'Nov27|' | grep -v 'Nov5|' | grep -v 'Nov71|' | grep -v 'Nov77|' | grep -v 'Nov9|' | grep -v 'ONT3|' | grep -v 'SCRP245_v2|' > $Uniq_Bc16_groups
echo "The number of orthogroups unique to Race 2 are:"
cat $Uniq_Bc16_groups | wc -l
echo "The following number genes are contained in these orthogroups:"
cat $Uniq_Bc16_groups | grep -o 'Bc16|' | wc -l
```

```
The number of orthogroups unique to Race 2 are:
0
The following number genes are contained in these orthogroups:
0
```

#Race 2 unique RxLR families

#Race 2 RxLR genes were parsed to the same format as the gene names used in the analysis:

```bash
RxLR_Names_Bc16=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_Total_RxLR_EER_motif_hmm.txt
WorkDir=analysis/orthology/orthomcl/phytophthora_fragariae
RxLR_Dir=$WorkDir/Bc16_RxLR
Orthogroups=$WorkDir/phytophthora_fragariae_orthogroups.txt
RxLR_ID_Bc16=$RxLR_Dir/Bc16_aug_RxLR_EER_IDs.txt
mkdir -p $RxLR_Dir
cat $RxLR_Names_Bc16 | sed -r 's/^/Bc16|/g' > $RxLR_ID_Bc16
```

#Ortholog groups containing RxLR proteins were identified using the following commands:

```bash
echo "The number of RxLRs searched for is:"
cat $RxLR_ID_Bc16 | wc -l
echo "Of these, the following number were found in orthogroups:"
RxLR_Orthogroup_hits_Bc16=$RxLR_Dir/Bc16_RxLR_Orthogroups_hits.txt
cat $Orthogroups | grep -o -w -f $RxLR_ID_Bc16 > $RxLR_Orthogroup_hits_Bc16
cat $RxLR_Orthogroup_hits_Bc16 | wc -l
echo "These were distributed through the following number of Orthogroups:"
RxLR_Orthogroup_Bc16=$RxLR_Dir/Bc16_RxLR_Orthogroups.txt
cat $Orthogroups | grep -w -f $RxLR_ID_Bc16 > $RxLR_Orthogroup_Bc16
cat $RxLR_Orthogroup_Bc16 | wc -l
echo "The following RxLRs were found in Race 2 unique orthogroups:"
RxLR_Bc16_uniq_groups=$RxLR_Dir/Bc16_uniq_RxLR_Orthogroups_hits.txt
cat $RxLR_Orthogroup_Bc16 | grep -v 'A4|' | grep -v 'Bc1|' | grep -v 'Bc23|' | grep -v 'Nov27|' | grep -v 'Nov5|' | grep -v 'Nov71|' | grep -v 'Nov77|' | grep -v 'Nov9|' | grep -v 'ONT3|' | grep -v 'SCRP245_v2|' > $RxLR_Bc16_uniq_groups
cat $RxLR_Bc16_uniq_groups | wc -l
echo "These orthogroups contain the following number of RxLRs:"
cat $RxLR_Bc16_uniq_groups | grep -w -o -f $RxLR_ID_Bc16 | wc -l
echo "The following RxLRs were found in P.fragariae unique orthogroups:"
RxLR_Pf_uniq_groups=$RxLR_Dir/Pf_RxLR_Orthogroups_hits.txt
cat $RxLR_Orthogroup_Bc16 > $RxLR_Pf_uniq_groups
cat $RxLR_Pf_uniq_groups | wc -l
echo "These orthogroups contain the following number of RxLRs:"
cat $RxLR_Pf_uniq_groups | grep -w -o -f $RxLR_ID_Bc16 | wc -l
```

```
The number of RxLRs searched for is:
237
Of these, the following number were found in orthogroups:
237
These were distributed through the following number of Orthogroups:
178
The following RxLRs were found in Race 2 unique orthogroups:
0
These orthogroups contain the following number of RxLRs:
0
The following RxLRs were found in P.fragariae unique orthogroups:
178
These orthogroups contain the following number of RxLRs:
237
```

#The Race 2 RxLR genes that were not found in orthogroups were identified:

```bash
RxLR_Bc16_uniq=$RxLR_Dir/Bc16_unique_RxLRs.txt
cat $RxLR_ID_Bc16 | grep -v -w -f $RxLR_Orthogroup_hits_Bc16 | tr -d 'Bc16|' > $RxLR_Bc16_uniq
echo "The number of BC-16 unique RxLRs are:"
cat $RxLR_Bc16_uniq | wc -l
RxLR_Seq_Bc16=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_Braker1_RxLR_EER_motif_hmm.fa
Braker_genes=gene_pred/braker/P.fragariae/Bc16/P.fragariae_Bc16_braker/augustus.aa
RxLR_Bc16_uniq_fa=$RxLR_Dir/Bc16_unique_RxLRs.fa
cat $Braker_genes | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $RxLR_Bc16_uniq | grep -E -v '^--' > $RxLR_Bc16_uniq_fa
```

```
The number of BC-16 unique RxLRs are:
0
```

##Extracting fasta files for orthogroups containing Race 2 putative RxLRs

```bash
ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
OrthogroupTxt=analysis/orthology/orthomcl/phytophthora_fragariae/Bc16_RxLR/Bc16_RxLR_Orthogroups.txt
GoodProt=analysis/orthology/orthomcl/phytophthora_fragariae/goodProteins/goodProteins.fasta
OutDir=analysis/orthology/orthomcl/phytophthora_fragariae/Bc16_RxLR/orthogroups_fasta_Bc16_RxLR
mkdir -p $OutDir
$ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
```

##Extracting fasta files for P. fragariae orthogroups containing Race 2 putative RxLRs

```bash
ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
OrthogroupTxt=analysis/orthology/orthomcl/phytophthora_fragariae/Bc16_RxLR/Pf_RxLR_Orthogroups_hits.txt
GoodProt=analysis/orthology/orthomcl/phytophthora_fragariae/goodProteins/goodProteins.fasta
OutDir=analysis/orthology/orthomcl/phytophthora_fragariae/Bc16_RxLR/orthogroups_fasta_Pf_RxLR
mkdir -p $OutDir
$ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
```

<!-- ##Race 2 unique Crinkler families

#Race 2 crinkler genes were parsed to the same format as the gene names used in the analysis:

```bash
CRN_Names_Bc16=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc16/Bc16_Braker1_CRN_hmmer_headers.txt
WorkDir=analysis/orthology/orthomcl/phytophthora_fragariae
CRN_Dir=$WorkDir/Bc16_CRN
Orthogroups=$WorkDir/phytophthora_fragariae_orthogroups.txt
CRN_ID_Bc16=$CRN_Dir/Bc16_CRN_hmmer_IDs.txt
mkdir -p $CRN_Dir
cat $CRN_Names_Bc16 | sed 's/g/Bc16|g/g' > $CRN_ID_Bc16
```

#Ortholog groups containing CRN proteins were identified using the following commands:

```bash
echo "The number of CRNs searched for is:"
cat $CRN_ID_Bc16 | wc -l
echo "Of these, the following number were found in orthogroups:"
CRN_Orthogroup_hits_Bc16=$CRN_Dir/Bc16_CRN_Orthogroups_hits.txt
cat $Orthogroups | grep -o -w -f $CRN_ID_Bc16 > $CRN_Orthogroup_hits_Bc16
cat $CRN_Orthogroup_hits_Bc16 | wc -l
echo "These were distributed through the following number of Orthogroups:"
CRN_Orthogroup_Bc16=$CRN_Dir/Bc16_CRN_Orthogroups.txt
cat $Orthogroups | grep -w -f $CRN_ID_Bc16 > $CRN_Orthogroup_Bc16
cat $CRN_Orthogroup_Bc16 | wc -l
echo "The following CRNs were found in Race 2 unique orthogroups:"
CRN_Bc16_uniq_groups=$CRN_Dir/Bc16_uniq_CRN_Orthogroups_hits.txt
cat $CRN_Orthogroup_Bc16 | grep -v 'A4' | grep -v 'Bc1' | grep -v 'Bc23' | grep -v 'Nov27' | grep -v 'Nov5' | grep -v 'Nov71' | grep -v 'Nov77' | grep -v 'Nov9' | grep -v 'ONT3' | grep -v 'SCRP245_v2' > $CRN_Bc16_uniq_groups
cat $CRN_Bc16_uniq_groups | wc -l
echo "The following CRNs were found in P.fragariae unique orthogroups:"
CRN_Pf_uniq_groups=$CRN_Dir/Pf_CRN_Orthogroups_hits.txt
cat $CRN_Orthogroup_Bc16 > $CRN_Pf_uniq_groups
cat $CRN_Pf_uniq_groups | wc -l
```

```
```

#The Race 2 CRN genes not found in orthogroups were identified:

```bash
CRN_Bc16_uniq=$CRN_Dir/Bc16_unique_CRNs.txt
cat $CRN_ID_Bc16 | grep -v -w -f $CRN_Orthogroup_hits_Bc16 | tr -d 'Bc16|' > $CRN_Bc16_uniq
echo "The number of Race 2 unique CRNs are:"
cat $CRN_Bc16_uniq | wc -l
CRN_Seq_Bc16=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc16/Bc16_pub_CRN_hmmer_out.fa
Braker_genes=gene_pred/braker/P.fragariae/Bc16/P.fragariae_Bc16_braker/augustus.aa
CRN_Bc16_uniq_fa=$CRN_Dir/Bc16_unique_CRNs.fa
cat $Braker_genes | sed -e 's/\(^>.*$\)/#\1#/' | tr -d "\r" | tr -d "\n" | sed -e 's/$/#/' | tr "#" "\n" | sed -e '/^$/d' | grep -w -A1 -f $CRN_Bc16_uniq | grep -E -v '^--' > $CRN_Bc16_uniq_fa
```

```
```

##Extracting fasta files for orthogroups containing Race 2 putative CRNs

```bash
ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
OrthogroupTxt=analysis/orthology/orthomcl/phytophthora_fragariae/Bc16_CRN/Bc16_CRN_Orthogroups.txt
GoodProt=analysis/orthology/orthomcl/phytophthora_fragariae/goodProteins/goodProteins.fasta
OutDir=analysis/orthology/orthomcl/phytophthora_fragariae/Bc16_CRN/orthogroups_fasta_Bc16_CRN
mkdir -p $OutDir
$ProgDir/orthoMCLgroups2fasta.py --orthogroups $OrthogroupTxt --fasta $GoodProt --out_dir $OutDir
``` -->

<!-- ##Determining function of orthogroups (6.3 is the start here, all not relevant)

#Lists of genes from Race 2 unique genes, P. fragariae orthogroups and the largest shared gene families were identified

#Unclear on interproscan here, it doesn't match my output

```bash
WorkDir=analysis/orthology/orthomcl/phytophthora_fragariae
InterProFile=gene_pred/interproscan/Bc16/P.fragariae_Bc16_braker/10300_interproscan.tsv
``` -->
