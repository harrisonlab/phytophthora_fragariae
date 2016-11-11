An assembly has been published by a Chinese group and is available on Genbank, but the assembly looks of low quality and he paper is poorly written so confirming that it definitely is _Phytophthora fragariae_. BLAST analysis has shown β-tubulin to have the _P. fragariae_ type SNP, and ITS was not found by BLAST.

#Assembly downloaded from Genbank

```bash
mkdir -p assembly/downloaded/P.fragariae/309.62
cd assembly/downloaded/P.fragariae/309.62
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/686/205/GCA_000686205.3_ASM68620v3/GCA_000686205.3_ASM68620v3_genomic.fna.gz
gunzip GCA_000686205.3_ASM68620v3_genomic.fna.gz
```
