# Second stage of summary_stats analysis

R scripts sourced from Maria's analyses

## Pf analysis

### Set initial variables

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats
scripts=/home/adamst/git_repos/scripts/popgen_analysis
```

```
In order to calculate different statistics in Popgenome, the input has to be
arranged in a particular way.
The input directory should contain two folders.
Folder No. 1: named "gff", contains GFF files for all the contigs output from
the split_gff_contig.sh script
Folder No. 2: named "contigs", contains subfolders, each subfolder named with
exact contig name and containing one individual contig FASTA file, also named
with exact contig name, as output from vcf_to_fasta.py
```

### Create this directory structure

```bash
cd $input/all_Pf
```

### This folder contains only contig FASTA files

So create a new "contigs" directory to hold those files:

```bash
mkdir contigs
mv *.fasta ./contigs
```

### Copy the "gff" folder containing gff files

```bash
cp -r \
/home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats/gff ./
```

### Create subfolders, each to hold one contig FASTA file

```bash
cd contigs
for f in *.fasta
do
    folder=${f%.fasta}
    mkdir $folder
    mv $f $folder
done
```

### Navigate to the input folder to proceed with Popgenome run

```bash
cd $input/all_Pf
```

### Lastly, test if all contigs have a matching gff and remove any which do not

```bash
for a in $PWD/contigs/*/*.fasta
do
    filename=$(basename "$a")
    expected_gff="$PWD/gff/${filename%.fa*}.gff"
    if [ ! -f "$expected_gff" ]
    then
       rm -rf $(dirname $a)
    fi
done
```

```
The R script used below is custom-made for each run (see first few lines of it).
It requires custom definition of populations, and individual assignment to them.
The example below calculates nucleotide diversity within (Pi) and between (Dxy) populations.
Other scripts (sub_calculate_neutrality_stats.sh) are used in analogous manner.
Vcf of all Pf strains, bar NOV-77 has been phased, run for haplotype-based stats.
```

```bash
scripts2=/home/adamst/git_repos/scripts/phytophthora_fragariae/popgen_analysis/popgenome_scripts
qsub $scripts2/sub_calculate_nucleotide_diversity.sh
qsub $scripts2/sub_calculate_neutrality_stats.sh
qsub $scripts2/sub_calculate_fst.sh
qsub $scripts2/sub_calculate_4_gamete_test.sh
```

This calculation was done over all sites. Now going to proceed for site subsets:
synonymous, non-synonymous and four-fold degenerate (silent)

### four_fold_degenerate (analogous to above, for all sites), called silent

```bash
cd $input/silent_Pf
mkdir contigs
mv *.fasta ./contigs
cp -r \
/home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats/gff ./
cd contigs
for f in *.fasta
do
    folder=${f%.fasta}
    mkdir $folder
    mv $f $folder
done
cd $input/silent_Pf

# Check all contigs have a matching gff and remove any that do not

for a in $PWD/contigs/*/*.fasta
do
    filename=$(basename "$a")
    expected_gff="$PWD/gff/${filename%.fa*}.gff"
    if [ ! -f "$expected_gff" ]
    then
       rm -rf $(dirname $a)
    fi
done

qsub $scripts2/sub_calculate_nucleotide_diversity.sh
qsub $scripts2/sub_calculate_neutrality_stats.sh
qsub $scripts2/sub_calculate_fst.sh
qsub $scripts2/sub_calculate_4_gamete_test.sh
```

## For synonymous and non-synonymous have to create FASTA input first

### Synonymous sites

```bash
cd $input
ref_genome=/home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa
ProgDir=/home/adamst/git_repos/scripts/popgen/summary_stats
python $ProgDir/vcf_to_fasta.py \
polished_contigs_unmasked_two_pops_filtered.recode_syn.vcf $ref_genome 2
mkdir syn_Pf
mv *.fasta ./syn_Pf
```

### Non-synonymous sites

```bash
cd $input
ref_genome=/home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa
ProgDir=/home/adamst/git_repos/scripts/popgen/summary_stats
python $ProgDir/vcf_to_fasta.py \
polished_contigs_unmasked_two_pops_filtered.recode_nonsyn.vcf $ref_genome 2
mkdir nonsyn_Pf
mv *.fasta ./nonsyn_Pf
```

## Create directory structure and carry out Popgenome analysis

```bash
cd $input/syn_Pf
mkdir contigs
mv *.fasta ./contigs
cp -r \
/home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats/gff ./
cd contigs
for f in *.fasta
do
    folder=${f%.fasta}
    mkdir $folder
    mv $f $folder
done

cd $input/syn_Pf

# Check all contigs have a matching gff and remove any that do not

for a in $PWD/contigs/*/*.fasta
do
    filename=$(basename "$a")
    expected_gff="$PWD/gff/${filename%.fa*}.gff"
    if [ ! -f "$expected_gff" ]
    then
       rm -rf $(dirname $a)
    fi
done

qsub $scripts2/sub_calculate_nucleotide_diversity.sh
qsub $scripts2/sub_calculate_neutrality_stats.sh
qsub $scripts2/sub_calculate_fst.sh
qsub $scripts2/sub_calculate_4_gamete_test.sh

cd $input/nonsyn_Pf
mkdir contigs
mv *.fasta ./contigs
cp -r \
/home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats/gff ./
cd contigs
for f in *.fasta
do
    folder=${f%.fasta}
    mkdir $folder
    mv $f $folder
done

# Check all contigs have a matching gff and remove any that do not

cd $input/nonsyn_Pf

for a in $PWD/contigs/*/*.fasta
do
    filename=$(basename "$a")
    expected_gff="$PWD/gff/${filename%.fa*}.gff"
    if [ ! -f "$expected_gff" ]
    then
       rm -rf $(dirname $a)
    fi
done

qsub $scripts2/sub_calculate_nucleotide_diversity.sh
qsub $scripts2/sub_calculate_neutrality_stats.sh
qsub $scripts2/sub_calculate_fst.sh
qsub $scripts2/sub_calculate_4_gamete_test.sh
```

## 4 Gametes test for Pf vs Pr

### Create this directory structure

```bash
cd $input/all
```

### This folder contains only contig FASTA files

So create a new "contigs" directory to hold those files:

```bash
mkdir contigs
mv *.fasta ./contigs
```

### Copy the "gff" folder containing gff files

```bash
cp -r \
/home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats/gff ./
```

### Create subfolders, each to hold one contig FASTA file

```bash
cd contigs
for f in *.fasta
do
    folder=${f%.fasta}
    mkdir $folder
    mv $f $folder
done
```

### Navigate to the input folder to proceed with Popgenome run

```bash
cd $input/all
```

### Lastly, test if all contigs have a matching gff and remove any which do not

```bash
for a in $PWD/contigs/*/*.fasta
do
    filename=$(basename "$a")
    expected_gff="$PWD/gff/${filename%.fa*}.gff"
    if [ ! -f "$expected_gff" ]
    then
       rm -rf $(dirname $a)
    fi
done
```

Run R script

```bash
scripts2=/home/adamst/git_repos/scripts/phytophthora_fragariae/popgen_analysis/popgenome_scripts
qsub $scripts2/sub_calculate_4_gamete_test_Pf_Pr.sh
```

This calculation was done over all sites. Now going to proceed for site subsets:
synonymous, non-synonymous and four-fold degenerate (silent)

### four_fold_degenerate (analogous to above, for all sites), called silent

```bash
cd $input/silent
mkdir contigs
mv *.fasta ./contigs
cp -r \
/home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats/gff ./
cd contigs
for f in *.fasta
do
    folder=${f%.fasta}
    mkdir $folder
    mv $f $folder
done
cd $input/silent

# Check all contigs have a matching gff and remove any that do not

for a in $PWD/contigs/*/*.fasta
do
    filename=$(basename "$a")
    expected_gff="$PWD/gff/${filename%.fa*}.gff"
    if [ ! -f "$expected_gff" ]
    then
       rm -rf $(dirname $a)
    fi
done

qsub $scripts2/sub_calculate_4_gamete_test_Pf_Pr.sh
```

## For synonymous and non-synonymous have to create FASTA input first

### Synonymous sites

```bash
cd $input
ref_genome=/home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa
ProgDir=/home/adamst/git_repos/scripts/popgen/summary_stats
python $ProgDir/vcf_to_fasta.py \
polished_contigs_unmasked_filtered.recode_syn.vcf $ref_genome 2
mkdir syn
mv *.fasta ./syn
```

### Non-synonymous sites

```bash
cd $input
ref_genome=/home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa
ProgDir=/home/adamst/git_repos/scripts/popgen/summary_stats
python $ProgDir/vcf_to_fasta.py \
polished_contigs_unmasked_filtered.recode_nonsyn.vcf $ref_genome 2
mkdir nonsyn
mv *.fasta ./nonsyn
```

## Create directory structure and carry out Popgenome analysis

```bash
cd $input/syn
mkdir contigs
mv *.fasta ./contigs
cp -r \
/home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats/gff ./
cd contigs
for f in *.fasta
do
    folder=${f%.fasta}
    mkdir $folder
    mv $f $folder
done

cd $input/syn

# Check all contigs have a matching gff and remove any that do not

for a in $PWD/contigs/*/*.fasta
do
    filename=$(basename "$a")
    expected_gff="$PWD/gff/${filename%.fa*}.gff"
    if [ ! -f "$expected_gff" ]
    then
       rm -rf $(dirname $a)
    fi
done

qsub $scripts2/sub_calculate_4_gamete_test_Pf_Pr.sh

cd $input/nonsyn
mkdir contigs
mv *.fasta ./contigs
cp -r \
/home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats/gff ./
cd contigs
for f in *.fasta
do
    folder=${f%.fasta}
    mkdir $folder
    mv $f $folder
done

# Check all contigs have a matching gff and remove any that do not

cd $input/nonsyn

for a in $PWD/contigs/*/*.fasta
do
    filename=$(basename "$a")
    expected_gff="$PWD/gff/${filename%.fa*}.gff"
    if [ ! -f "$expected_gff" ]
    then
       rm -rf $(dirname $a)
    fi
done

qsub $scripts2/sub_calculate_4_gamete_test_Pf_Pr.sh
```

## Analysis of population separation

Fst, Kst & Dxy measure the separation of the two populations, extract genes
showing high separation and investigate their function

```bash
cd /home/groups/harrisonlab/project_files/phytophthora_fragariae
Out_Dir=summary_stats/all_Pf
Fst_File=$Out_Dir/genome_pairwise_FST_per_gene_pop1_vs_pop2.txt
Kst_File=$Out_Dir/genome_Hudson_KST_per_gene_all.txt
Dxy_File=$Out_Dir/genome_pop1_vs_pop2_dxy_per_gene.txt
Fst_Threshold=0.5
Kst_Threshold=0.5
Dxy_Threshold=0.005
Out_Prefix=Population_Separated_Genes
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae/popgen_analysis
$ProgDir/ID_population_separated_genes.py --Fst_File $Fst_File --Kst_File $Kst_File --Dxy_File $Dxy_File --Fst_Threshold $Fst_Threshold --Kst_Threshold $Kst_Threshold --Dxy_Threshold $Dxy_Threshold --Out_Dir $Out_Dir --Out_Prefix $Out_Prefix
```

### Summarise these results

```bash
RxLRs=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_Total_RxLR_motif_hmm_renamed.txt
CRNs=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc16/Bc16_final_CRN_renamed.txt
ApoPs=analysis/ApoplastP/P.fragariae/Bc16/Bc16_Total_ApoplastP_renamed.txt
Secs=gene_pred/combined_sigP_CQ/P.fragariae/Bc16/Bc16_all_secreted_Aug_ORF.txt
WorkDir=summary_stats/all_Pf

for file in $(ls $WorkDir/Population_Separated_Genes*)
do
    echo $file
    echo "The number of population separated genes is:"
    cat $file | wc -l
    echo "The number of RxLRs showing population separation is:"
    cat $RxLRs | grep -w -f $file | wc -l
    echo "The number of CRNs showing population separation is:"
    cat $CRNs | grep -w -f $file | wc -l
    echo "The number of Apoplastic Effectors showing population separation is:"
    cat $ApoPs | grep -w -f $file | wc -l
    echo "The number of Secreted Proteins showing population separation is:"
    cat $Secs | grep -w -f $file | wc -l
done
```

```
summary_stats/all_Pf/Population_Separated_Genes_High_Conf.txt
The number of population separated genes is:
49
The number of RxLRs showing population separation is:
1
The number of CRNs showing population separation is:
0
The number of Apoplastic Effectors showing population separation is:
11
The number of Secreted Proteins showing population separation is:
12
summary_stats/all_Pf/Population_Separated_Genes_Low_Conf.txt
The number of population separated genes is:
4,554
The number of RxLRs showing population separation is:
80
The number of CRNs showing population separation is:
11
The number of Apoplastic Effectors showing population separation is:
575
The number of Secreted Proteins showing population separation is:
906
```

### Functional enrichment analysis - using interpro terms

Create lists of gene IDs including all possible transcripts

```bash
WorkDir=summary_stats/all_Pf
for Set in High_Conf Low_Conf
do
    AnnotTable=gene_pred/annotation/P.fragariae/Bc16/Bc16_gene_table_incl_exp.tsv
    Target_Genes=$WorkDir/Population_Separated_Genes_"$Set".txt
    All_Genes=$WorkDir/Bc16_all_genes.txt
    cat $AnnotTable | tail -n+2 | cut -f1 > $All_Genes
    Set1_Genes=$WorkDir/Bc16_Separated_"$Set".txt
    Set2_Genes=$WorkDir/Bc16_not_Separated_"$Set".txt
    cat $All_Genes | grep -w -f $Target_Genes > $Set1_Genes
    cat $All_Genes | grep -w -v -f $Target_Genes > $Set2_Genes
done
```

Conduct enrichment analyses

```bash
WorkDir=summary_stats/all_Pf
Interpro=gene_pred/annotation/P.fragariae/Bc16/Bc16_gene_table_incl_exp.tsv
for Set in High_Conf Low_Conf
do
    Out_Dir=analysis/enrichment/P.fragariae/Bc16/$Set
    mkdir -p $Out_Dir/tables
    Set1_Genes=$WorkDir/Bc16_Separated_"$Set".txt
    Set2_Genes=$WorkDir/Bc16_not_Separated_"$Set".txt
    ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
    $ProgDir/IPR_prep_tables.py --Interpro $Interpro --Set1_Genes $Set1_Genes --Set2_Genes $Set2_Genes --Out_Dir $Out_Dir/tables
    ProgDir=/home/armita/git_repos/emr_repos/scripts/fusarium/analysis/gene_enrichment
    $ProgDir/fisherstest.r --in_dir $Out_Dir/tables --out_file $Out_Dir/results.tsv
    SigIPR=$(cat $Out_Dir/significant_terms.txt | cut -f1)
    for IPR in $(ls $Out_Dir/tables/*_fischertable.txt | rev | cut -f1 -d '/' | rev | sed 's/_fischertable.txt//g')
    do
      cat $Out_Dir/tables/"$IPR"_fischertable.txt | grep "$IPR"
    done
done
```
