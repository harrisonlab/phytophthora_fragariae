Several FALCON assembly attempts have been trialled, it is now important to see how they compare, using the published Phytophthora sojae genome as a potential comparison.

#Download P. sojae genome

```bash
mkdir -p assembly/downloaded/P.sojae/P6497
cd assembly/downloaded/P.sojae/P6497
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/149/755/GCA_000149755.2_P.sojae_V3.0/GCA_000149755.2_P.sojae_V3.0_genomic.fna.gz
gunzip GCA_000149755.2_P.sojae_V3.0_genomic.fna.gz
cd ../../../../
```

#Copy files from triticum

```bash
mkdir -p assembly/FALCON_Trial
scp -r /home/groups/harrisonlab/project_files/phytophthora_fragariae/assembly/FALCON_Trial vicker@10.1.10.170:/data/projects/adamst/P.fragariae/
```

Excess files manually removed just to leave primary and associate contig files for analysis.
