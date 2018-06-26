# Runs analysis of *P. fragariae* and *P. rubi* genomes by McDonald-Kreitman test

Commands copied from Maria's directory

Scripts set up currently for UK123

## Set initial variables

```bash
scripts=/home/adamst/git_repos/scripts/popgen/summary_stats
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae
```

## A)

```
Establish ancestral allele using genotype(s) from select outgroup species:

1)
*P. rubi* - used as outgroup (incorrectly, as derived from *P. fragariae*)
in order to test the ancestral allele annotation procedure using VCF
polymorphism data stemming from alignment of genome outgroup reads to the focal
species genome.

2)
Outgroups: *P. sojae*, *P. ramorum*
(*P. ramorum* is quite distantly related to the other two species)
in order to test the ancestral allele annotation procedure using Mauve-based
whole-genome alignment.

3)
Lastly, the results of ancestral allele annotation using VCF-based annotation
(#1) will be compared to the whole genome alignment annotation (#2).

Choice of the analysis to follow: 1, 2, 3 depends on the available resources
and researcher preferences.
Annotation with ancestral alleles can be used just to polarise the mutation
status of SNPs of interest or can be used in the formal tests for selection
(e.g. McDonald-Kreitman Test and Fay & Wu's H described below)
```

### Set variables for locations of *P. fragariae* and *P. rubi* genomes

```bash
#*P. fragariae*
Pf=/home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_hardmasked.fa
#*P. rubi* SCRP249
Pra=/home/groups/harrisonlab/project_files/phytophthora_rubi/repeat_masked/P.rubi/SCRP249/deconseq_Paen_repmask/SCRP249_contigs_hardmasked.fa
#*P. rubi* SCRP324
Prb=/home/groups/harrisonlab/project_files/phytophthora_rubi/repeat_masked/P.rubi/SCRP324/ncbi_edits_repmask/SCRP324_contigs_hardmasked.fa
#*P. rubi* SCRP333
Prc=/home/groups/harrisonlab/project_files/phytophthora_rubi/repeat_masked/P.rubi/SCRP333/deconseq_Paen_repmask/SCRP333_contigs_hardmasked.fa
```

#### 1) Annotate vcf file

```bash
python $scripts/annotate_vcf_aa.py \
$input/SNP_calling/polished_contigs_unmasked_filtered.vcf 2 SCRP249,,SCRP324,,SCRP333
```

```
Out of 402,939 variants in the file, 402,094 were annotated with (an) ancestral allele(s)
```

#### 2) Run progressiveMauve

```bash
cd $input/summary_stats
cp $Pf ./
cp $Pra ./
cp $Prb ./
cp $Prc ./
qsub $scripts/run_progressive_mauve.sh $input/progressiveMauve \
"polished_contigs_hardmasked.fa SCRP249_contigs_hardmasked.fa \
SCRP324_contigs_hardmasked.fa SCRP333_contigs_hardmasked.fa"

# Only run this command once progressiveMauve finishes

rm polished_contigs_hardmasked.fa SCRP249_contigs_hardmasked.fa \
SCRP324_contigs_hardmasked.fa SCRP333_contigs_hardmasked.fa
```

##### Parse Mauve output

```bash
perl /home/sobczm/bin/popoolation_1.2.2/mauve-parser.pl --ref $Pf \
--input $input/summary_stats/progressiveMauve/aligned_genomes.xmfa --output \
$input/summary_stats/progressiveMauve/mel-guided-alignment.txt
```

```
Option 'Y' specifies to print fake genotype into the VCF file encoding the
identified ancestral alleles.
Use this option when proceeding to use Popgenome in order to calculate
outgroup-based statistics: Fay & Wu's H and McDonald-Kreitman test
```

##### Carry out analysis with fake genotype

```bash
python $scripts/annotate_gen_aa.py \
$input/summary_stats/progressiveMauve/mel-guided-alignment.txt \
$input/summary_stats/polished_contigs_unmasked_filtered.vcf 2 Y
```

```
Out of 402,939 variants in the file, 267,475 were annotated with (an) ancestral allele(s)
```

##### Carry out analysis above without printing fake genotypes

```bash
python $scripts/annotate_gen_aa.py \
$input/summary_stats/progressiveMauve/mel-guided-alignment.txt \
$input/summary_stats/polished_contigs_unmasked_filtered.vcf 2 N
```

```
Out of 402,939 variants in the file, 267,475 were annotated with (an) ancestral allele(s)
```

#### 3) Compare results of ancestral annotation

##### print AA field and fake genotype with the ancestral allele

```bash
python $scripts/compare_outgroup_results.py \
$input/summary_stats/polished_contigs_unmasked_filtered_gen_aa.vcf \
$input/summary_stats/polished_contigs_unmasked_filtered_gen_aa.vcf 2 N
```

```
In total, 267,475 variants were annotated with consensus ancestral allele, out
of 402,094 variants in the file. 0 annotations were found to differ between the
two input annotation sources, and were rejected, while 0 and 0 ancestral allele
annotations were present only in the input annotation source 1 or 2,
respectively, and were included.
```

## B) McDonald-Kreitman test calculated by PopGenome

```bash
mkdir -p $input/mkt
cd $input/mkt
ref_genome=$Pf
vcf_file=$input/SNP_calling/polished_contigs_unmasked_filtered_vcf_aa.vcf
python $scripts/vcf_to_fasta.py $vcf_file $ref_genome 2
```

### Prepare Popgenome input

```bash
function Popgenome {
mkdir contigs && mv *.fasta ./contigs
cd contigs
for f in *.fasta
do
    folder=${f%.fasta}
    mkdir $folder
    mv $f $folder
done

# Gff files

cd ..
gff=/home/groups/harrisonlab/project_files/phytophthora_fragariae/gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors.gff3
$scripts/split_gff_contig.sh $gff
mkdir gff && mv *.gff ./gff

# Check for orphan contigs with no matching gff file
# which need to be removed prior to the run.
for a in $PWD/contigs/*/*.fasta
do
    filename=$(basename "$a")
    expected_gff="$PWD/gff/${filename%.fa*}.gff"
    if [ ! -f "$expected_gff" ]
    then
       rm -rf $(dirname $a)
    fi
done
}
Popgenome
```

#### Requires adjustment of the script called below to include the samples

```bash
scripts2=/home/adamst/git_repos/scripts/phytophthora_fragariae/popgen_analysis
qsub $scripts2/sub_calculate_mkt.sh
```

## Outgroup-based tests for selection

### Fay & Wu's H (at least one outgroup needed) calculated by PopGenome

```bash
mkdir -p $input/faywuh
cd $input/faywuh
ref_genome=/home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_hardmasked.fa
vcf_file=$input/summary_stats/polished_contigs_unmasked_filtered_gen_aa.vcf
python $scripts/vcf_to_fasta.py $vcf_file $ref_genome 2
##Prepare Popgenome input
Popgenome
# Requires adjustment of the script called below to include the samples
qsub $scripts2/sub_calculate_faywu.sh
```

## Analyse using UK123 as the focal population

### Create cut down vcf file

```bash
vcflib=/home/sobczm/bin/vcflib/bin
$vcflib/vcfremovesamples $input/SNP_calling/polished_contigs_unmasked.vcf SCRP245_v2 Bc23 ONT3 Nov77 > $input/SNP_calling/polished_contigs_UK123_plus_ancestral_unmasked.vcf
```

### Filter vcf

```bash
vcf=$input/SNP_calling/polished_contigs_UK123_plus_ancestral_unmasked.vcf
echo $vcf
script=/home/adamst/git_repos/scripts/popgen/snp/sub_vcf_parser.sh
qsub $script $vcf
```

### 1) Annotate UK123 vcf file

```bash
mv polished_contigs_UK123_plus_ancestral_unmasked_filtered.vcf $input/summary_stats/.
python $scripts/annotate_vcf_aa.py \
$input/summary_stats/polished_contigs_UK123_plus_ancestral_unmasked_filtered.vcf \
2 SCRP249,,SCRP324,,SCRP333
```

```
Out of 359,325 variants in the file, 358,599 were annotated with (an) ancestral allele(s)
```

```
Option 'Y' specifies to print fake genotype into the VCF file encoding the
identified ancestral alleles.
Use this option when proceeding to use Popgenome in order to calculate
outgroup-based statistics: Fay & Wu's H and McDonald-Kreitman test
```

#### Carry out analysis with fake genotype for UK123

```bash
python $scripts/annotate_gen_aa.py \
$input/summary_stats/progressiveMauve/mel-guided-alignment.txt \
$input/summary_stats/polished_contigs_UK123_plus_ancestral_unmasked_filtered.vcf \
2 Y
```

```
Out of 819,736 variants in the file, 438,894 were annotated with (an) ancestral allele(s)
```

#### Carry out analysis above without printing fake genotypes for UK123

```bash
python $scripts/annotate_gen_aa.py \
$input/summary_stats/progressiveMauve/mel-guided-alignment.txt \
$input/SNP_calling/polished_contigs_UK123_plus_ancestral_unmasked.vcf 2 N
```

```
Out of 819,736  variants in the file, 438,894 were annotated with (an) ancestral allele(s)
```

### 3) Compare results of ancestral annotation for UK123

#### print AA field and fake genotype with the ancestral allele for UK123

```bash
python $scripts/compare_outgroup_results.py \
$input/summary_stats/polished_contigs_unmasked_UK123_filtered_gen_aa.vcf \
$input/summary_stats/polished_contigs_unmasked_UK123_filtered_gen_aa.vcf 2 N
```

```
In total, 342,303 variants were annotated with consensus ancestral allele,
out of 540,513 variants in the file. 0 annotations were found to differ between
the two input annotation sources, and were rejected, while 0 and 0 ancestral
allele annotations were present only in the input annotation source 1 or 2,
respectively, and were included.
```

## B) McDonald-Kreitman test calculated by PopGenome for UK123

```bash
mkdir -p $input/mkt/UK123
cd $input/mkt/UK123
ref_genome=$Pf
vcf_file=$input/summary_stats/polished_contigs_unmasked_UK123_filtered_vcf_aa.vcf
python $scripts/vcf_to_fasta.py $vcf_file $ref_genome 2
```

### Prepare Popgenome input for UK123

```bash
function Popgenome {
mkdir contigs && mv *.fasta ./contigs
cd contigs
for f in *.fasta
do
    folder=${f%.fasta}
    mkdir $folder
    mv $f $folder
done

# Gff files

cd ..
gff=/home/groups/harrisonlab/project_files/phytophthora_fragariae/gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors.gff3
$scripts/split_gff_contig.sh $gff
mkdir gff && mv *.gff ./gff

# Check for orphan contigs with no matching gff file
# which need to be removed prior to the run.
for a in $PWD/contigs/*/*.fasta
do
    filename=$(basename "$a")
    expected_gff="$PWD/gff/${filename%.fa*}.gff"
    if [ ! -f "$expected_gff" ]
    then
       rm -rf $(dirname $a)
    fi
done
}
Popgenome
```

#### Requires adjustment of the script called below to include the samples for UK123

```bash
scripts2=/home/adamst/git_repos/scripts/phytophthora_fragariae/popgen_analysis
qsub $scripts2/sub_calculate_mkt.sh
```

## Outgroup-based tests for selection for UK123

### Fay & Wu's H (at least one outgroup needed) calculated by PopGenome for UK123

```bash
mkdir -p $input/faywuh/UK123
cd $input/faywuh/UK123
ref_genome=/home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_hardmasked.fa
vcf_file=$input/summary_stats/polished_contigs_unmasked_UK123_filtered_vcf_aa.vcf
python $scripts/vcf_to_fasta.py $vcf_file $ref_genome 2
##Prepare Popgenome input
Popgenome
# Requires adjustment of the script called below to include the samples
qsub $scripts2/sub_calculate_faywu.sh
```
