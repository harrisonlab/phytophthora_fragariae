#Looks for structural variations between the genomes
##Structural variants can include: duplications, deletions, inversions & translocations. Uses read-pair configuration, split-reads & read-depth

###Sets inital variables

```bash
input_dip=/home/groups/harrisonlab/project_files/phytophthora_fragariae/qc_dna/paired/P.fragariae
input_dip_assembly=/home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats/95m_contigs_unmasked.fa
scripts=/home/sobczm/bin/popgen/snp
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/sv_calling
```

####Move to correct directory

```bash
mkdir -p $input
cd $input
```

###Set up bwa-mem for illumina reads aligning to SMRT sequenced *P. fragariae* genome

```bash
for sample in $input_dip/*
do
    reads_forward=$sample/F/*trim.fq.gz
    reads_reverse=$sample/R/*trim.fq.gz
    sname=$(echo $(basename "$reads_forward") | cut -d"_" -f1)
    qsub $scripts/sub_bwa_mem.sh Illumina $sname $input_dip_assembly $reads_forward $reads_reverse
done
```

In some cases, the forward and reverse read files are corrupted (reads do not match in the two files) and this crashes bwa-mem. These need to be fixed with $scripts/sub_pairfq.sh
