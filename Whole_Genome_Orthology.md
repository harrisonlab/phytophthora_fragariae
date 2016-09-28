#Methodology 4 from Andy's files - run on A4, BC-1, BC-16, BC-23, NOV-27, NOV-5, NOV-71, NOV-77, NOV-9, ONT-3, SCRP245_v2

```bash
ProjDir=/home/groups/harrisonlab/project_files/phytophthora_fragariae
cd $ProjDir
IsolateAbrv=All_Strains
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

##4.2 Filter proteins into good and poor sets.

```bash
Input_dir=$WorkDir/formatted
Min_length=10
Max_percent_stops=20
Good_proteins_file=$WorkDir/goodProteins/goodProteins.fasta
Poor_proteins_file=$WorkDir/badProteins/poorProteins.fasta
orthomclFilterFasta $Input_dir $Min_length $Max_percent_stops $Good_proteins_file $Poor_proteins_file
```

4.3.a Perform an all-vs-all blast of the proteins

  BlastDB=$WorkDir/blastall/$IsolateAbrv.db

  makeblastdb -in $Good_proteins_file -dbtype prot -out $BlastDB
  BlastOut=$WorkDir/all-vs-all_results.tsv
  mkdir -p $WorkDir/splitfiles

  SplitDir=/home/armita/git_repos/emr_repos/tools/seq_tools/feature_annotation/signal_peptides
  $SplitDir/splitfile_500.py --inp_fasta $Good_proteins_file --out_dir $WorkDir/splitfiles --out_base goodProteins

  ProgDir=/home/armita/git_repos/emr_repos/scripts/phytophthora/pathogen/orthology  
  for File in $(find $WorkDir/splitfiles); do
    Jobs=$(qstat | grep 'blast_500' | grep 'qw' | wc -l)
    while [ $Jobs -gt 1 ]; do
      sleep 3
      printf "."
      Jobs=$(qstat | grep 'blast_500' | grep 'qw' | wc -l)
    done
    printf "\n"
    echo $File
    BlastOut=$(echo $File | sed 's/.fa/.tab/g')
    qsub $ProgDir/blast_500.sh $BlastDB $File $BlastOut
  done
4.3.b Merge the all-vs-all blast results

  MergeHits="$IsolateAbrv"_blast.tab
  printf "" > $MergeHits
  for Num in $(ls $WorkDir/splitfiles/*.tab | rev | cut -f1 -d '_' | rev | sort -n); do
    File=$(ls $WorkDir/splitfiles/*_$Num)
    cat $File
  done > $MergeHits
4.4 Perform ortholog identification

  ProgDir=~/git_repos/emr_repos/tools/pathogen/orthology/orthoMCL
  MergeHits="$IsolateAbrv"_blast.tab
  GoodProts=$WorkDir/goodProteins/goodProteins.fasta
  qsub $ProgDir/qsub_orthomcl.sh $MergeHits $GoodProts 5
4.5.a Manual identification of numbers of orthologous and unique genes

  for num in 1; do
    echo "The number of ortholog groups found in pathogen but absent in non-pathogens is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A28|' -e 'PG|' -e 'A13|' -e 'fo47|' -e 'CB3|' | grep 'Fus2|' | grep '125|' | grep 'A23|' |  wc -l
    echo "The number of ortholog groups unique to pathogens are:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A28|' -e 'PG|' -e 'A13|' -e 'fo47|' -e 'CB3|' | grep 'Fus2|' | grep '125|' | grep 'A23|' | wc -l
    echo "This represents the following number of genes:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A28|' -e 'PG|' -e 'A13|' -e 'fo47|' -e 'CB3|' | grep 'Fus2|' | grep '125|' | grep 'A23|' | grep -o '|' | wc -l
    echo "This represents the following number of genes from Fus2:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A28|' -e 'PG|' -e 'A13|' -e 'fo47|' -e 'CB3|' | grep 'Fus2|' | grep '125|' | grep 'A23|' | grep -o 'Fus2|' | wc -l
    echo "The number of genes in the largest orthogroup is:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A28|' -e 'PG|' -e 'A13|' -e 'fo47|' -e 'CB3|' | grep 'Fus2|' | grep '125|' | grep 'A23|' | head -n1 | grep -o '|' | wc -l
    echo "The number of ortholog groups unique to non-pathogens are:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'Fus2|' -e '125|' -e 'A23|' | grep 'A13|' | grep 'A28|' | grep 'PG|' | grep 'fo47|' | grep 'CB3|' | wc -l
    echo "The number of ortholog groups common to all F. oxysporum isolates are:"
    cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep 'Fus2|' | grep '125|' | grep 'A23|' | grep 'A28|' | grep 'PG|' | grep 'A13|' | grep 'fo47|' | grep 'CB3|' | grep '4287|' |wc -l
  done
The number of ortholog groups found in pathogen but absent in non-pathogens is:
255
The number of ortholog groups unique to pathogens are:
255
The number of ortholog groups unique to non-pathogens are:
61
The number of ortholog groups common to all F. oxysporum isolates are:
10391
The number of ortholog groups shared between FoC and FoL was identified:

  echo "The number of ortholog groups common to FoC and FoL are:"
  cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep 'Fus2|' | grep '125|' | grep 'A23|' | grep '4287|' | wc -l
  cat $WorkDir/"$IsolateAbrv"_orthogroups.txt | grep -v -e 'A28|' -e 'PG|' -e 'A13|' -e 'fo47|' -e 'CB3' | grep 'Fus2|' | grep '125|' | grep 'A23|' | grep '4287|' |  wc -l
  The number of ortholog groups common to FoC and FoL are:
  10916
  43
4.5.b Plot venn diagrams:

  ProgDir=~/git_repos/emr_repos/scripts/fusarium/pathogen/orthology
  $ProgDir/FoC_path_vs_non_path_venn_diag.r --inp $WorkDir/"$IsolateAbrv"_orthogroups.tab --out $WorkDir/"$IsolateAbrv"_orthogroups.pdf
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
