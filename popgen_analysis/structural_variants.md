#Looks for structural variations between the genomes
##Structural variants can include: duplications, deletions, inversions & translocations. Uses read-pair configuration, split-reads & read-depth

###First, run BWA-mem to align reads to FALCON assembly before SV calling

####Copy files and concatenate multiple reads into forward and reverse files

```bash
mkdir sv_calling
cd sv_calling

#Copy single library *P. fragariae* isolates
for Strain in A4 Bc23 Nov27 Nov5 Nov77 ONT3 SCRP245_v2
do
    Output_name=$(echo $Strain | sed 's/_*//g')
    mkdir -p $Output_name/F
    mkdir -p $Output_name/R
    cp ../qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz $Output_name/F/.
    cp ../qc_dna/paired/P.fragariae/$Strain/R/*.fq.gz $Output_name/R/.
done

#Copy single library *P. rubi* isolates
for Strain in SCRP249 SCRP324 SCRP333
do
    mkdir -p $Strain/F
    mkdir -p $Strain/R
    cp ../../phytophthora_rubi/qc_dna/paired/P.rubi/$Strain/F/*.fq.gz $Strain/F/.
    cp ../../phytophthora_rubi/qc_dna/paired/P.rubi/$Strain/R/*.fq.gz $Strain/R/.
done

#Concatenate and copy *P.fragariae* isolates with multiple libraries
for Strain in Bc1 Bc16 Nov71 Nov9
do
    mkdir -p $Strain/F
    mkdir -p $Strain/R
    gunzip ../qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz
    for File in $(ls ../qc_dna/paired/P.fragariae/$Strain/F/*.fq)
    do
        cat $File >> ../qc_dna/paired/P.fragariae/$Strain/F/"$Strain"_concatenated_F.fq
    done
    gzip ../qc_dna/paired/P.fragariae/$Strain/F/*.fq
    gunzip ../qc_dna/paired/P.fragariae/$Strain/R/*.fq.gz
    for File in $(ls ../qc_dna/paired/P.fragariae/$Strain/R/*.fq)
    do
        cat $File >> ../qc_dna/paired/P.fragariae/$Strain/R/"$Strain"_concatenated_R.fq
    done
    gzip ../qc_dna/paired/P.fragariae/$Strain/R/*.fq
    mv ../qc_dna/paired/P.fragariae/$Strain/F/*_concatenated* $Strain/F/.
    mv ../qc_dna/paired/P.fragariae/$Strain/R/*_concatenated* $Strain/R/.
done
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

###Set up initial variables

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/sv_calling
scripts=/home/sobczm/bin/popgen/snp
```

###Convert from VCF to Plink's PED format

```bash
cd sv_calling
cp ../SNP_calling/polished_contigs_unmasked_filtered.vcf .
input_file=polished_contigs_unmasked_filtered.vcf
plink --allow-extra-chr --const-fid 0 --vcf $input_file --recode --make-bed --out ${input_file%.vcf} > ${input_file%.vcf}.log
```
