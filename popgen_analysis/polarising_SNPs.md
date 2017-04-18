#SNPs will be polarised to identify those ancestral in UK2 & P. rubi, but differs in UK1 and UK3

##First, filter vcf to remove SCRP245, ONT-3, NOV-77 & BC-23

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
-F CHROM -F POS -F ID -F QUAL -F REF -F ALT \
-GF A4 -GF Bc1 -GF Bc16 -GF Nov27 -GF Nov5 -GF Nov71 -GF Nov9 -GF SCRP249 -GF SCRP324 -GF SCRP333 \
-AMD \
-o Parsed_Polarising_95m_contigs_unmasked.tbl
```
