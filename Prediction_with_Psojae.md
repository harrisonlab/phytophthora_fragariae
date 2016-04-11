#Phytophthora fragariae
Commands used to predict genes in Phytophthora fragariae using published RNAseq data from Phytophthora sojae
====================

All commands run in the directory:
/home/groups/harrisonlab/project_files/phytophthora_fragariae

#Download RNAseq data from SRA

```bash
cd raw_rna/genbank
mkdir -p P.sojae/P6497
fastq-dump SRR243567
```
