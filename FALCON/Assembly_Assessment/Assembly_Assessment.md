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

#For an idea of how the genomes compare even at this stage, run BUSCO on all of them

```bash
for Assembly in $(ls assembly/FALCON_Trial/*/p_ctg.fa)
do
    Name=$(echo $Assembly | rev |cut -d '/' -f2 | rev)
    echo "$Name"
    ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/busco
    BuscoDB=Eukaryotic
    OutDir=assembly/FALCON_Trial/$Name
    qsub $ProgDir/sub_busco2.sh $Assembly $BuscoDB $OutDir
done

for Assembly in $(ls assembly/downloaded/P.sojae/*/*.fna)
do
    Name=P.sojae
    ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/busco
    BuscoDB=Eukaryotic
    OutDir=assembly/FALCON_Trial/$Name
    qsub $ProgDir/sub_busco2.sh $Assembly $BuscoDB $OutDir
done
```

Output files from BUSCO are used to create a spreadsheet for ease of comparison, spreadsheet stored on my local machine.
*P. sojae* genome is of good quality, so assess for colinearity with inc_max_cov.

```bash
/home/adamst/git_repos/scripts/phytophthora_fragariae/Robs_scripts/plot_compare_kmers.py 31 assembly/downloaded/P.sojae/P6497/GCA_000149755.2_P.sojae_V3.0_genomic.fna assembly/FALCON_Trial/inc_max_cov/p_ctg.fa colinearity_assessement.png
```
