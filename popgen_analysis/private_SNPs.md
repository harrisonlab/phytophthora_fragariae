# Analysis of private SNPs

Commented commands were my attempt, after discussions with Maria she found several faults and suggested I use her script instead. This begins after commented out commands, which are kept for reference.

<!-- ##First, filter vcf to remove SCRP245, ONT-3, NOV-77 & BC-23

Set key variables

```bash
vcftools=/home/sobczm/bin/vcftools/bin
vcflib=/home/sobczm/bin/vcflib/bin
```

Perform filtering

```bash
cd SNP_calling
$vcflib/vcfremovesamples 95m_contigs_unmasked.vcf SCRP245_v2 ONT3 Nov77 Bc23 > Polarising_95m_contigs_unmasked.vcf
```

##Filter vcf for quality, but keep multi-allelic variants and indels

All options except indel choice kept at default

```bash
vcf=Polarising_95m_contigs_unmasked.vcf
script=/home/adamst/git_repos/scripts/popgen/snp/sub_vcf_parser.sh
qsub $script $vcf 40 30 10 30 0.95 N
```

##Parse vcf file to a table for easier working

Copy over fasta file and create an index file and an index file for GATK

```bash
mkdir -p Polarising
cd Polarising
cp ../SNP_calling/Polarising* .
cp /home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats/95m_contigs_unmasked.fa Bc16_contigs_unmasked.fa

#Create .dict file
java -jar /home/sobczm/bin/picard-tools-2.5.0/picard.jar CreateSequenceDictionary \
R= Bc16_contigs_unmasked.fa \
O= Bc16_contigs_unmasked.dict

#Create .fai file
samtools faidx Bc16_contigs_unmasked.fa
```

```bash
java -jar /home/sobczm/bin/GenomeAnalysisTK-3.6/GenomeAnalysisTK.jar \
-T VariantsToTable \
-R Bc16_contigs_unmasked.fa \
-V Polarising_95m_contigs_unmasked_filtered.vcf \
-F CHROM -F POS -F REF -F ALT \
-GF GT \
-o Parsed_Polarising_95m_contigs_unmasked.tbl
```

In this table, GT indicates the genotype of the sample, AD is the unfiltered allele depth, DP is the filtered depth, GQ is the quality of the assigned genotype and PL is the the normalised likelihood of the possible genotypes (smaller the better). For more detail on vcf files see: http://gatkforums.broadinstitute.org/gatk/discussion/1268/what-is-a-vcf-and-how-should-i-interpret-it

```bash
python /home/adamst/git_repos/scripts/phytophthora_fragariae/popgen_analysis/UK1_polarisation.py
python /home/adamst/git_repos/scripts/phytophthora_fragariae/popgen_analysis/UK2_polarisation.py
python /home/adamst/git_repos/scripts/phytophthora_fragariae/popgen_analysis/UK3_polarisation.py
```

```
UK1:
None found
UK2:
None are in genes
UK3:
None found
``` -->

## Maria has a (probably better) script to look at this.

### Set inital variables

```bash
scripts=/home/sobczm/bin/popgen/summary_stats
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/Polarising
```

### Create a cut-down vcf and filter it

```bash
mkdir $input
cd $input

cp ../SNP_calling/polished_contigs_unmasked.vcf .

vcflib=/home/sobczm/bin/vcflib/bin
$vcflib/vcfremovesamples polished_contigs_unmasked.vcf SCRP245_v2 ONT3 Nov77 Bc23 > polished_contigs_unmasked_bw.vcf

vcftools=/home/sobczm/bin/vcftools/bin
$vcftools/vcftools --vcf polished_contigs_unmasked_bw.vcf  --max-missing 0.95 --recode --out polished_contigs_unmasked_bw_filtered
```

### This requires editing every time, the python script is designed by Maria to find differences

#### For UK2, set UK2 isolates and P. rubi isolates

```bash
python $scripts/vcf_find_difference_pop.py --vcf polished_contigs_unmasked_bw_filtered.recode.vcf --out polished_contigs_unmasked_bw_filtered_fixed.vcf --ply 2 --pop1 Bc16,,A4,,SCRP249,,SCRP324,,SCRP333 --pop2 Nov5,,Bc1,,Nov9,,Nov27,,Nov71 --thr 0.95
```

```
Only one variant found, a G to A SNP on contig 14 at position 964,434. No gene present, but a possible promoter region, 1kb from gene models
g11265 nearest - no annotations found, no expression evidence in any of UK123
```

#### UK1 based analysis

```bash
python $scripts/vcf_find_difference_pop.py --vcf polished_contigs_unmasked_bw_filtered.recode.vcf --out polished_contigs_unmasked_bw_filtered_fixed_UK1.vcf --ply 2 --pop1 Bc1,,Nov5,,SCRP249,,SCRP324,,SCRP333 --pop2 A4,,Bc16,,Nov9,,Nov27,,Nov71 --thr 0.95
```

```
Nothing found.
```

#### UK3 based analysis

```bash
python $scripts/vcf_find_difference_pop.py --vcf polished_contigs_unmasked_bw_filtered.recode.vcf --out polished_contigs_unmasked_bw_filtered_fixed_UK3.vcf --ply 2 --pop1 Nov9,,Nov27,,Nov71,,SCRP249,,SCRP324,,SCRP333 --pop2 A4,,Bc16,,Nov5,,Bc1 --thr 0.95
```

```
Nothing found.
```

## Private variants without rubi, just looking for private differences within UK123 strains

### Set inital variables

```bash
scripts=/home/sobczm/bin/popgen/summary_stats
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/Polarising
```

### Create a cut-down vcf and filter it

```bash
cd $input

vcflib=/home/sobczm/bin/vcflib/bin
$vcflib/vcfremovesamples polished_contigs_unmasked.vcf SCRP245_v2 ONT3 Nov77 Bc23 SCRP249 SCRP324 SCRP333 > polished_contigs_unmasked_pol.vcf

vcftools=/home/sobczm/bin/vcftools/bin
$vcftools/vcftools --vcf polished_contigs_unmasked_bw.vcf  --max-missing 0.95 --recode --out polished_contigs_unmasked_pol_filtered
```

### This requires editing every time, the python script is designed by Maria to find differences

#### For UK2, set UK2 isolates and P. rubi isolates

```bash
python $scripts/vcf_find_difference_pop.py --vcf polished_contigs_unmasked_pol_filtered.recode.vcf --out polished_contigs_unmasked_pol_filtered_fixed.vcf --ply 2 --pop1 Bc16,,A4 --pop2 Nov5,,Bc1,,Nov9,,Nov27,,Nov71 --thr 0.95
```

```
11 private variant sites identified. Format on allele is reference/variant(s)
1. contig_1 217,370 A/C - ~600bp upstream of g65 (beta helix repeat) [very little expression, no difference between UK123], ~2kb upstream of g66 (coil) [very little expression, not reliable difference between UK123]
2. contig_2 1,219,725 T/C - ~7kb upstream of g1731 (ApoplastP hit) [no expression]
3. contig_13 673,883 T/A - In CDS of g10482 (ApoplastP hit), silent SNP, no expression
4. contig_14 964,434 G/A - ~1kb upstream of g11265 (no annotation) [no expression]
5. contig_14 964,446 C/A - ~1kb upstream of g11265 (no annotation) [no expression]
6. contig_14 1,308,196 A/G - ~2kb upstream of g11447 (no annotation), ~5kb upstream of g11453 (no annotation) [no expression in either]
7. contig_19 961,636 T/C - Within CDS of g14158 (Zinc finger domains), but is silent, only expressed in NOV-9
8. contig_40 631,727 AC/A,ACC,AGC,AGCC - ~3kb upstream of g23432 (no annotation), ~5kb upstream of g23429 (no annotation) [no expression]
9. contig_48 312,824 T/C - 38bp upstream of g25960 (ApoplastP hit), ~2kb upstream of g25961 (homeodomain-like) [no expression]
10. contig_51 571,287 A/G - g27056 (GTPase & PDZ domain), changes a Leucine to a Proline at position 11 - isn't predicted as secreted, [expressed in all UK123 about evenly]
11. contig_76 248,619 T/C - ~1kb upstream of g33391 (no annotation), ~4.5kb upstream of g33392 [no expression in 33391, equal expression in g33392]
```

#### UK1 based analysis

```bash
python $scripts/vcf_find_difference_pop.py --vcf polished_contigs_unmasked_pol_filtered.recode.vcf --out polished_contigs_unmasked_pol_filtered_fixed_UK1.vcf --ply 2 --pop1 Bc1,,Nov5 --pop2 A4,,Bc16,,Nov9,,Nov27,,Nov71 --thr 0.95
```

```
None found.
```

#### UK3 based analysis

```bash
python $scripts/vcf_find_difference_pop.py --vcf polished_contigs_unmasked_pol_filtered.recode.vcf --out polished_contigs_unmasked_pol_filtered_fixed_UK3.vcf --ply 2 --pop1 Nov9,,Nov27,,Nov71 --pop2 A4,,Bc16,,Nov5,,Bc1 --thr 0.95
```

```
Nothing found.
```
