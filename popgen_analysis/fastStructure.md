# Evaluation of population structure using fastStructure

## Sets initial variables

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/fastStructure
scripts=/home/sobczm/bin/popgen/snp
```

## Converts VCF files to Plink's PED format

```bash
mkdir -p $input
cd $input

cp ../SNP_calling/polished_contigs_unmasked_filtered.recode_annotated.vcf .
input_file=polished_contigs_unmasked_filtered.recode_annotated.vcf

plink --allow-extra-chr --const-fid 0 --vcf $input_file --recode --make-bed --out ${input_file%.vcf} > ${input_file%.vcf}.log
```

## Tests various values of K for iterations of fastStructure

```bash
# Set minimum number of considered clusters
s=1
# Set maximum number of considered clusters
f=5

for i in $(seq $s $f)
do
    qsub $scripts/sub_fast_structure.sh ${input_file%.vcf} $i
done
```

## Choose model complexity (K) among all the K values tested

```bash
structure=/home/sobczm/bin/fastStructure
input_vcf_file=${input_file%.vcf}
python $structure/chooseK.py --input $input_vcf_file > ${input_file%.vcf}_K_choice
```
