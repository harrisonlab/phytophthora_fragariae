#Analysis of private SNPs

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

#Maria has a (probably better) script to look at this.

##Set inital variables

```bash
scripts=/home/sobczm/bin/popgen/summary_stats
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/Polarising
```

##Create a cut-down vcf and filter it

```bash
mkdir $input
cd $input

cp ../SNP_calling/polished_contigs_unmasked.vcf .

vcflib=/home/sobczm/bin/vcflib/bin
$vcflib/vcfremovesamples polished_contigs_unmasked.vcf SCRP245_v2 ONT3 Nov77 Bc23 > polished_contigs_unmasked_bw.vcf

vcftools=/home/sobczm/bin/vcftools/bin
$vcftools/vcftools --vcf polished_contigs_unmasked_bw.vcf  --max-missing 0.95 --recode --out polished_contigs_unmasked_bw_filtered
```

##This requires editing every time, the python script is designed by Maria to find differences.
###For UK2, set UK2 isolates and P. rubi isolates

```bash
python $scripts/vcf_find_difference_pop.py --vcf polished_contigs_unmasked_bw_filtered.recode.vcf --out polished_contigs_unmasked_bw_filtered_fixed.vcf --ply 2 --pop1 Bc16,,A4,,SCRP249,,SCRP324,,SCRP333 --pop2 Nov5,,Bc1,,Nov9,,Nov27,,Nov71 --thr 0.95
```

```
Only one variant found, a G to A SNP on contig 14 at position 964,434. No gene present, but a possible promoter region, 1kb from gene models
```

###UK1 based analysis

```bash
python $scripts/vcf_find_difference_pop.py --vcf 95m_contigs_unmasked_bw_filtered.recode.vcf --out 95m_contigs_unmasked_bw_filtered_fixed_UK1.vcf --ply 2 --pop1 Bc1,,Nov5,,SCRP249,,SCRP324,,SCRP333 --pop2 A4,,Bc16,,Nov9,,Nov27,,Nov71 --thr 0.95
```

```
Nothing found
```

###UK3 based analysis

```bash
python $scripts/vcf_find_difference_pop.py --vcf 95m_contigs_unmasked_bw_filtered.recode.vcf --out 95m_contigs_unmasked_bw_filtered_fixed_UK3.vcf --ply 2 --pop1 Nov9,,Nov27,,Nov71,,SCRP249,,SCRP324,,SCRP333 --pop2 A4,,Bc16,,Nov5,,Bc1 --thr 0.95
```

```
Nothing found
```

#Polarising variants without rubi, just looking for polarised differences within UK123 strains

##Set inital variables

```bash
scripts=/home/sobczm/bin/popgen/summary_stats
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/Polarising
```

##Create a cut-down vcf and filter it

```bash
cd $input

vcflib=/home/sobczm/bin/vcflib/bin
$vcflib/vcfremovesamples 95m_contigs_unmasked.vcf SCRP245_v2 ONT3 Nov77 Bc23 SCRP249 SCRP324 SCRP333 > 95m_contigs_unmasked_pol.vcf

vcftools=/home/sobczm/bin/vcftools/bin
$vcftools/vcftools --vcf 95m_contigs_unmasked_bw.vcf  --max-missing 0.95 --recode --out 95m_contigs_unmasked_pol_filtered
```

##This requires editing every time, the python script is designed by Maria to find differences.
###For UK2, set UK2 isolates and P. rubi isolates

```bash
python $scripts/vcf_find_difference_pop.py --vcf 95m_contigs_unmasked_pol_filtered.recode.vcf --out 95m_contigs_unmasked_pol_filtered_fixed.vcf --ply 2 --pop1 Bc16,,A4 --pop2 Nov5,,Bc1,,Nov9,,Nov27,,Nov71 --thr 0.95
```

```
contig_2 2,193,093 G/T ~1kb upstream of TSS, g1639.
contig_2 2,193,105 C/T ~1kb upstream of TSS, g1639.
contig_3 1,536,609 T/C No nearby TSS, flanked by two genes going in the wrong direction, 22kb both ways to actually reach a gene! g2186 & NS_14830.
contig_12 164,098 A/C ~1.5 and 1kb upstream of TSS going either way, g6665 and g6664.
contig_32 467,075 T/C - In a CDS! But is silent, g12140.
contig_45 358,224 T/C ~2kb upstream of TSS, g14706. Nearest going other way is ~5.5kb away with other genes in the way, g14705.
contig_49 37,872 TG/T/TGG ~3kb upstream of TSS, g15246, ~8kb going the other way with other genes in the way, g15249.
contig_113 185,134 T/C ~2kb upstream of TSS, NS_02424, ~5kb the other way, with genes in the way, NS_02421.
contig_182 18,638 T/A 360bp upstream of TSS, g28602, ~20kb upstream the other way, with genes in the way, NS_08364.
contig_201 99,050 A/G In a CDS! Changes L11 to P! Bc16|g29528.t1 - neither an RxLR nor a CRN, not secreted by either SigP or Phobius.
contig_305 38,563 T/C ~1kb and 4kb upstream of TSS going either way, g32690 and g32689.

Of these genes neighbouring SNPs, the following are predicted as RxLRs, CRNs or secreted:
g12140 - secreted (Phobius), 13AA signal peptide, also predicted by SigP.
```

###UK1 based analysis

```bash
python $scripts/vcf_find_difference_pop.py --vcf 95m_contigs_unmasked_pol_filtered.recode.vcf --out 95m_contigs_unmasked_pol_filtered_fixed_UK1.vcf --ply 2 --pop1 Bc1,,Nov5 --pop2 A4,,Bc16,,Nov9,,Nov27,,Nov71 --thr 0.95
```

```
None found
```

###UK3 based analysis

```bash
python $scripts/vcf_find_difference_pop.py --vcf 95m_contigs_unmasked_pol_filtered.recode.vcf --out 95m_contigs_unmasked_pol_filtered_fixed_UK3.vcf --ply 2 --pop1 Nov9,,Nov27,,Nov71 --pop2 A4,,Bc16,,Nov5,,Bc1 --thr 0.95
```

```
Nothing found
```
