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
$vcflib/vcfremovesamples 95m_contigs_unmasked.vcf SCRP245 ONT3 Nov77 Bc23 > Polarising_95m_contigs_unmasked.vcf
```
