# Second stage of summary_stats analysis

## UK123 analysis

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
qsub $scripts2/sub_calculate_haplotype_based_stats.sh
```

This calculation was done over all sites. Now going to proceed for site subsets:
synonymous, non-synonymous and four-fold degenerate (silent)

### four_fold_degenerate (analogous to above, for all sites)

```bash
cd $input/ffd
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

qsub $scripts2/sub_calculate_nucleotide_diversity.sh
qsub $scripts2/sub_calculate_neutrality_stats.sh
qsub $scripts2/sub_calculate_fst.sh
qsub $scripts2/sub_calculate_haplotype_based_stats.sh
```

## For synonymous and non-synonymous have to create FASTA input first

### Synonymous sites

```bash
cd $input
ref_genome=/home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa
python $scripts/vcf_to_fasta.py \
polished_contigs_unmasked_filtered.recode_annotated_syn.vcf $ref_genome 2
mkdir syn
mv *.fasta ./syn
```

### Non-synonymous sites

```bash
cd $input
ref_genome=/home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa
python $scripts/vcf_to_fasta.py \
polished_contigs_unmasked_filtered.recode_annotated_nonsyn.vcf $ref_genome 2
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
qsub $scripts2/sub_calculate_nucleotide_diversity.sh
qsub $scripts2/sub_calculate_neutrality_stats.sh
qsub $scripts2/sub_calculate_fst.sh
qsub $scripts2/sub_calculate_haplotype_based_stats.sh

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

cd $input/nonsyn
qsub $scripts2/sub_calculate_nucleotide_diversity.sh
qsub $scripts2/sub_calculate_neutrality_stats.sh
qsub $scripts2/sub_calculate_fst.sh
qsub $scripts2/sub_calculate_haplotype_based_stats.sh
```

## Pf analysis

### Set initial variables for Pf

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

### Create directory structure

```bash
mkdir -p $input/all_Pf
cd $input/all_Pf
```

### This folder contains only contig FASTA files for Pf

So create a new "contigs" directory to hold those files

```bash
mkdir contigs
mv *.fasta ./contigs
```

### Copy the "gff" folder containing gff files for Pf

```bash
cp -r /
/home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats/gff ./
```

### In the folder "contigs" create subfolders, each to hold one FASTA file

```bash
cd contigs
for f in *.fasta
do
    folder=${f%.fasta}
    mkdir $folder
    mv $f $folder
done
```

## Navigate to the input folder and proceed with Popgenome run

```bash
cd $input/all_Pf
```

### Test if all contigs have a matching gff and remove any which do not

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
cd ../
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
qsub $scripts2/sub_calculate_haplotype_based_stats.sh
```

## This calculation was done over all sites. Proceed for site subsets

### synonymous, non-synonymous and four-fold degenerate (silent)

#### four_fold_degenerate (analogous to above, for all sites) for Pf

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

qsub $scripts2/sub_calculate_nucleotide_diversity.sh
qsub $scripts2/sub_calculate_neutrality_stats.sh
qsub $scripts2/sub_calculate_fst.sh
qsub $scripts2/sub_calculate_haplotype_based_stats.sh
```

## For synonymous and non-synonymous have to create FASTA input first for Pf

### Synonymous sites for Pf

```bash
cd $input
ref_genome=/home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa
python $scripts/vcf_to_fasta.py \
Pfrag_only_polished_contigs_unmasked_filtered.recode_annotated_syn.vcf \
$ref_genome 2
#Moving each subset of FASTA files into a separate dir.
mkdir syn
mv *.fasta ./syn
```

### Non-synonymous

```bash
cd $input
ref_genome=/home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa
python $scripts/vcf_to_fasta.py \
Pfrag_only_polished_contigs_unmasked_filtered.recode_annotated_nonsyn.vcf \
$ref_genome 2
# Moving each subset of FASTA files into a separate dir.
mkdir nonsyn
mv *.fasta ./nonsyn
```

## Create directory structure and carry out Popgenome analysis for Pf

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
qsub $scripts2/sub_calculate_nucleotide_diversity.sh
qsub $scripts2/sub_calculate_neutrality_stats.sh
qsub $scripts2/sub_calculate_fst.sh
qsub $scripts2/sub_calculate_haplotype_based_stats.sh

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

cd $input/nonsyn
qsub $scripts2/sub_calculate_nucleotide_diversity.sh
qsub $scripts2/sub_calculate_neutrality_stats.sh
qsub $scripts2/sub_calculate_fst.sh
qsub $scripts2/sub_calculate_haplotype_based_stats.sh
```
