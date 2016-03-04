##Beginning orthology analysis of: A4, Bc1, Bc16, Bc23, Nov27, Nov5, Nov71, Nov77, Nov9, ONT3, SCRP245_v2

##RxLR Regex orthologies

##Set up working directories

```bash
	ProjDir=/home/groups/harrisonlab/project_files/phytophthora_fragariae
	cd $ProjDir
	IsolateAbrv=A4_Bc1_Bc16_Bc23_Nov27_Nov5_Nov71_Nov77_Nov9_ONT3_SCRP245_v2
	WorkDir=analysis/orthology/orthomcl/$IsolateAbrv
	mkdir -p $WorkDir
	mkdir -p $WorkDir/formatted
	mkdir -p $WorkDir/goodProteins
	mkdir -p $WorkDir/badProteins
```

##Format fasta files

#for A4

```bash
	Taxon_code=A4
	Fasta_file=analysis/RxLR_effectors/RxLR_EER_regex_finder/P.fragariae/A4/A4_braker_RxLR_regex.fa
	Id_field=1
	orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
	mv "$Taxon_code".fasta $WorkDir/formated/"$Taxon_code".fasta
```

#for Bc1

```bash
	Taxon_code=Bc1
	Fasta_file=analysis/RxLR_effectors/RxLR_EER_regex_finder/P.fragariae/Bc1/Bc1_braker_RxLR_regex.fa
	Id_field=1
	orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
	mv "$Taxon_code".fasta $WorkDir/formated/"$Taxon_code".fasta
```

#for Bc16

```bash
	Taxon_code=Bc16
	Fasta_file=analysis/RxLR_effectors/RxLR_EER_regex_finder/P.fragariae/Bc16/Bc16_braker_RxLR_regex.fa
	Id_field=1
	orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
	mv "$Taxon_code".fasta $WorkDir/formated/"$Taxon_code".fasta
```

#for Bc23

```bash
	Taxon_code=Bc23
	Fasta_file=analysis/RxLR_effectors/RxLR_EER_regex_finder/P.fragariae/Bc23/Bc23_braker_RxLR_regex.fa
	Id_field=1
	orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
	mv "$Taxon_code".fasta $WorkDir/formated/"$Taxon_code".fasta
```

#for Nov27

```bash
	Taxon_code=Nov27
	Fasta_file=analysis/RxLR_effectors/RxLR_EER_regex_finder/P.fragariae/Nov27/Nov27_braker_RxLR_regex.fa
	Id_field=1
	orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
	mv "$Taxon_code".fasta $WorkDir/formated/"$Taxon_code".fasta
```

#for Nov5

```bash
	Taxon_code=Nov5
	Fasta_file=analysis/RxLR_effectors/RxLR_EER_regex_finder/P.fragariae/Nov5/Nov5_braker_RxLR_regex.fa
	Id_field=1
	orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
	mv "$Taxon_code".fasta $WorkDir/formated/"$Taxon_code".fasta
```

#for Nov71

```bash
	Taxon_code=Nov71
	Fasta_file=analysis/RxLR_effectors/RxLR_EER_regex_finder/P.fragariae/Nov71/Nov71_braker_RxLR_regex.fa
	Id_field=1
	orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
	mv "$Taxon_code".fasta $WorkDir/formated/"$Taxon_code".fasta
```

#for Nov77

```bash
	Taxon_code=Nov77
	Fasta_file=analysis/RxLR_effectors/RxLR_EER_regex_finder/P.fragariae/Nov77/Nov77_braker_RxLR_regex.fa
	Id_field=1
	orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
	mv "$Taxon_code".fasta $WorkDir/formated/"$Taxon_code".fasta
```

#for Nov9

```bash
	Taxon_code=Nov9
	Fasta_file=analysis/RxLR_effectors/RxLR_EER_regex_finder/P.fragariae/Nov9/Nov9_braker_RxLR_regex.fa
	Id_field=1
	orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
	mv "$Taxon_code".fasta $WorkDir/formated/"$Taxon_code".fasta
```

#for ONT3

```bash
	Taxon_code=ONT3
	Fasta_file=analysis/RxLR_effectors/RxLR_EER_regex_finder/P.fragariae/ONT3/ONT3_braker_RxLR_regex.fa
	Id_field=1
	orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
	mv "$Taxon_code".fasta $WorkDir/formated/"$Taxon_code".fasta
```

#for SCRP245_v2

```bash
	Taxon_code=SCRP245_v2
	Fasta_file=analysis/RxLR_effectors/RxLR_EER_regex_finder/P.fragariae/SCRP245_v2/SCRP245_v2_braker_RxLR_regex.fa
	Id_field=1
	orthomclAdjustFasta $Taxon_code $Fasta_file $Id_field
	mv "$Taxon_code".fasta $WorkDir/formated/"$Taxon_code".fasta
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
	for File in $(find $WorkDir/splitfiles); do
		Jobs=$(qstat | grep 'blast_500' | wc -l)
		while [ $Jobs -gt 32 ]; do
			sleep 10
			printf "."
			Jobs=$(qstat | grep 'blast_500' | wc -l)
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
	ProgDir=home/adamst/git_repos/tools/pathogen/orthology/orthoMCL
	MergeHits="$IsolateAbrv"_blast.tab
	GoodProtDir=$WorkDir/goodProteins
	$ProgDir/qsub_orthomcl.sh $MergeHits $GoodProtDir
```

##Plot venn diagrams - REQUIRES INPUT FOR R CODE

```bash
	ProgDir=/home/adamst/git_repos/tools/pathogen/orthology/venn_diagrams
	$ProgDir/venn_diag_4_way.r --inp $WorkDir/"$IsolateAbrv"_orthogroups.tab --out $WorkDir/"$IsolateAbrv"_orthogroups.pdf
```