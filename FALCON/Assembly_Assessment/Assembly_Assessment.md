Several FALCON assembly attempts have been trialled, it is now important to see how they compare, using the published Phytophthora sojae genome as a potential comparison.

#Download P. sojae genome

```bash
mkdir -p assembly/downloaded/P.sojae/P6497
cd assembly/downloaded/P.sojae/P6497
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/149/755/GCA_000149755.2_P.sojae_V3.0/GCA_000149755.2_P.sojae_V3.0_genomic.fna.gz
gunzip GCA_000149755.2_P.sojae_V3.0_genomic.fna.gz
cd ../../../../
```

#Copy files from triticum - each folder name is different for each file
dec_lengthcut dec_max_cov dec_max_diff inc_lengthcut inc_max_cov

example for inc_max_cov

```bash
mkdir -p assembly/FALCON_Trial/inc_max_cov
scp -r vicker@10.1.10.170:/data/projects/adamst/P.fragariae/inc_max_cov/2*/p_ctg.fa /home/groups/harrisonlab/project_files/phytophthora_fragariae/assembly/FALCON_Trial/inc_max_cov/.
scp -r vicker@10.1.10.170:/data/projects/adamst/P.fragariae/inc_max_cov/2*/a_ctg.fa /home/groups/harrisonlab/project_files/phytophthora_fragariae/assembly/FALCON_Trial/inc_max_cov/.
```
