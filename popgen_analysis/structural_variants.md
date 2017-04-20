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

####Before running, individuals with multiple libraries require concatenating

```bash
for sample in $(ls $input_dip | grep -v '62471' | grep -v 'A4' | grep -v 'Bc23' | grep -v 'Nov27' | grep -v 'Nov5' | grep -v 'Nov77' | grep -v 'ONT3' | grep -v 'SCRP245_v2')
do
    F1_Read=$(ls $sample/F/*.fq.gz | head -n1)
    Forward_out=$(basename "F1_Read")
    #Copy the forward reads to the working folder
    cp -r $sample/F/*.fq.gz ./
    #Uncompress and concatenate
    for a in *.fq.gz
    do
        gzip -d $a
        cat ${a%.gz} >> ${Forward_out%.fq.gz}_concat_F.fastq
    done
    #Copy the reverse reads to the working folder
    cp -r $sample/R/*.fq.gz ./
    #Uncompress and concatenate
    for b in *.fq.gz
    do
        gzip -d $b
        cat ${b%.gz} >> ${Forward_out%.fq.gz}_concat_R.fastq
    done
    #Compress the output
    gzip ${Forward_out%.fq.gz}_concat_F.fastq
    gzip ${Forward_out%.fq.gz}_concat_R.fastq
done
```

####Now run bwa-mem

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

##Run lumpy to call structural variants

```bash
qsub $scripts/sub_lumpy.sh pfrag_struc_variants
```
