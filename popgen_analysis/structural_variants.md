#Looks for structural variations between the genomes
##Structural variants can include: duplications, deletions, inversions & translocations. Uses read-pair configuration, split-reads & read-depth

###First, run BWA-mem to align reads to FALCON assembly before SV calling

####Copy files and concatenate multiple reads into forward and reverse files

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

###Set up initial variables

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/sv_calling
scripts=/home/sobczm/bin/popgen/snp
```

###Convert from VCF to Plink's PED format
