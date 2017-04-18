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

##Parse vcf file to a table for easier working

```bash
java -jar GenomeAnalysisTK.jar \
-R /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/P.fragariae/Bc16/filtered_contigs_repmask/Bc16_contigs_unmasked.fa \
-T VariantsToTable \
-V Polarising_95m_contigs_unmasked.vcf \
-F CHROM -F POS -F ID -F QUAL \
-GF A4 -GF Bc1 -GF Bc16 -GF Nov27 -GF Nov5 -GF Nov71 -GF Nov9 -GF SCRP249 -GF SCRP324 -GF SCRP333 \
-AMD \
-o Parsed_Polarising_95m_contigs_unmasked.tbl
```
