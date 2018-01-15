#Looks for structural variations between the genomes
##Structural variants can include: duplications, deletions, inversions & translocations. Uses read-pair configuration, split-reads & read-depth

###Sets inital variables

```bash
input_dip=/home/groups/harrisonlab/project_files/phytophthora_fragariae/qc_dna/paired/P.fragariae
input_dip_assembly=/home/groups/harrisonlab/project_files/phytophthora_fragariae/summary_stats/polished_contigs_unmasked.fa
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
for isolate in $(ls $input_dip | grep -v '62471' | grep -v 'A4' | grep -v 'Bc23' | grep -v 'Nov27' | grep -v 'Nov5' | grep -v 'Nov77' | grep -v 'ONT3' | grep -v 'SCRP245_v2')
do
    sample=$input_dip/$isolate
    F1_Read=$(ls $sample/F/*.fq.gz | head -n1)
    Forward_out=$(basename "$F1_Read")
    mkdir -p $input/$isolate
    cd $input/$isolate
    #Copy the forward reads to the working folder
    cp -r $sample/F/*.fq.gz ./
    #Uncompress and concatenate
    for a in *.fq.gz
    do
        gzip -d $a
        cat ${a%.gz} >> ${Forward_out%.fq.gz}_concat_F.fq
    done
    #Copy the reverse reads to the working folder
    cp -r $sample/R/*.fq.gz ./
    #Uncompress and concatenate
    for b in *.fq.gz
    do
        gzip -d $b
        cat ${b%.gz} >> ${Forward_out%.fq.gz}_concat_R.fq
    done
    #Compress the output
    gzip ${Forward_out%.fq.gz}_concat_F.fq
    gzip ${Forward_out%.fq.gz}_concat_R.fq
    mkdir F
    mkdir R
    mv *_concat_F* F/./
    mv *_concat_R* R/./
    cd $input
done
```

####Now copy over reads for isolates with only a single library

```bash
for isolate in $(ls $input_dip | grep -v '62471' | grep -v 'Bc1' | grep -v 'Bc16' | grep -v 'Nov9' | grep -v 'Nov71')
do
    sample=$input_dip/$isolate
    mkdir -p $input/$isolate
    cd $input/$isolate
    mkdir F
    mkdir R
    cp -r $sample/F/*.fq.gz F/./
    cp -r $sample/R/*.fq.gz R/./
    cd $input
done
```

####Now run bwa-mem

```bash
for sample in $input/*
do
    reads_forward=$sample/F/*fq.gz
    reads_reverse=$sample/R/*fq.gz
    sname=$(echo $(basename "$reads_forward") | cut -d"_" -f1)
    qsub $scripts/sub_bwa_mem.sh Illumina $sname $input_dip_assembly $reads_forward $reads_reverse
done
```

In some cases, the forward and reverse read files are corrupted (reads do not match in the two files) and this crashes bwa-mem. These need to be fixed with $scripts/sub_pairfq.sh

##Run lumpy to call structural variants

```bash
scripts=/home/adamst/git_repos/scripts/phytophthora_fragariae
qsub $scripts/sub_lumpy.sh pfrag_struc_variants
```

###Analysis of output of lumpy - PRELIMINARY DATA, only goes up to contig_92

####Set variables

```bash
scripts=/home/sobczm/bin/popgen/summary_stats
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/sv_calling
```

####Cut down and filter vcf for analysis including P. rubi as an ancestral grouping

```bash
cd $input

vcflib=/home/sobczm/bin/vcflib/bin
$vcflib/vcfremovesamples pfrag.vcf Pfrag-SCRP245 Pfrag-ONT-3 Pfrag-Nov-77 Pfrag-Bc23 62471  > pfrag_struc_variants_plus_pr.vcf

vcftools=/home/sobczm/bin/vcftools/bin
$vcftools/vcftools --vcf pfrag_struc_variants_plus_pr.vcf  --max-missing 0.95 --recode --out pfrag_struc_variants_plus_pr_filtered
```

####UK2 focused analysis

```bash
python $scripts/vcf_find_difference_pop.py --vcf pfrag_struc_variants_plus_pr_filtered.recode.vcf --out pfrag_struc_variants_UK2.vcf --ply 2 --pop1 Bc16,,PfragariaeA4 --pop2 Pfrag-Nov-5,,Bc1,,Nov9,,Nov27,,Pfrag-Nov71 --thr 0.95
```

```
No variants found
```

####UK1 focused analysis

```bash
python $scripts/vcf_find_difference_pop.py --vcf pfrag_struc_variants_plus_pr_filtered.recode.vcf --out pfrag_struc_variants_UK1.vcf --ply 2 --pop1 Bc1,,Pfrag-Nov-5 --pop2 PfragariaeA4,,Bc16,,Nov9,,Nov27,,Pfrag-Nov71 --thr 0.95
```

```
No variants found
```

####UK3 focused analysis

```bash
python $scripts/vcf_find_difference_pop.py --vcf pfrag_struc_variants_plus_pr_filtered.recode.vcf --out pfrag_struc_variants_UK3.vcf --ply 2 --pop1 Nov9,,Nov27,,Pfrag-Nov71 --pop2 Bc1,,Pfrag-Nov-5,,PfragariaeA4,,Bc16 --thr 0.95
```

```
No variants found
```

##fastSTRUCTURE analysis - potentially a better caller than lumpy
This allows a quicker evaluation of population structure in diploid organisms (and is less problematic to run than lumpy)
