##Beginning orthology analysis of: A4, Bc1, Bc16, Bc23, Nov27, Nov5, Nov71, Nov77, Nov9, ONT3, SCRP245_v2

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
Taxon_code=A4
Fasta_file=analysis/RxLR_effectors/combined_evidence/P.fragariae/A4/A4_Total_RxLR_EER_motif_hmm_headers.fa
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta

Taxon_code=Bc1
Fasta_file=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc1/Bc1_Total_RxLR_EER_motif_hmm_headers.fa
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta

Taxon_code=Bc16
Fasta_file=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_Total_RxLR_EER_motif_hmm_headers.fa
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta

Taxon_code=Bc23
Fasta_file=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc23/Bc23_Total_RxLR_EER_motif_hmm_headers.fa
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta

Taxon_code=Nov27
Fasta_file=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov27/Nov27_Total_RxLR_EER_motif_hmm_headers.fa
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta

Taxon_code=Nov5
Fasta_file=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov5/Nov5_Total_RxLR_EER_motif_hmm_headers.fa
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta

Taxon_code=Nov71
Fasta_file=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov71/Nov71_Total_RxLR_EER_motif_hmm_headers.fa
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta

Taxon_code=Nov77
Fasta_file=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov77/Nov77_Total_RxLR_EER_motif_hmm_headers.fa
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta

Taxon_code=Nov9
Fasta_file=analysis/RxLR_effectors/combined_evidence/P.fragariae/Nov9/Nov9_Total_RxLR_EER_motif_hmm_headers.fa
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta

Taxon_code=ONT3
Fasta_file=analysis/RxLR_effectors/combined_evidence/P.fragariae/ONT3/ONT3_Total_RxLR_EER_motif_hmm_headers.fa
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta

Taxon_code=SCRP245_v2
Fasta_file=analysis/RxLR_effectors/combined_evidence/P.fragariae/SCRP245_v2/SCRP245_v2_Total_RxLR_EER_motif_hmm_headers.fa
Id_field=1
orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
mv "$Taxon_code".fasta $WorkDir/formatted/"$Taxon_code".fasta
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
MergeHits="$IsolateAbrv"_blast.tab
printf "" > $MergeHits
for Num in $(ls $WorkDir/splitfiles/*.tab | rev | cut -f1 -d '_' | rev | sort -n); do
    File=$(ls $WorkDir/splitfiles/*_$Num)
    cat $File
done > $MergeHits
```

##Perform ortholog identification

```bash
ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
MergeHits="$IsolateAbrv"_blast.tab
GoodProts=$WorkDir/goodProteins/goodProteins.fasta
$ProgDir/qsub_orthomcl.sh $MergeHits $GoodProts 5
```
