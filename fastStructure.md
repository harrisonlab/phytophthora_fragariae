##fastStructure analysis - potentially a better caller than lumpy
This allows a quicker evaluation of population structure in diploid organisms (and is less problematic to run than lumpy)

###Set up initial variables

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/sv_calling
scripts=/home/adamst/git_repos/scripts/popgen/snp
```

###Convert from VCF to Plink's PED format

```bash
cd sv_calling
cp ../SNP_calling/polished_contigs_unmasked_filtered.vcf .
input_file=polished_contigs_unmasked_filtered.vcf
plink --allow-extra-chr --const-fid 0 --vcf $input_file --recode --make-bed --out ${input_file%.vcf} > ${input_file%.vcf}.log
```

###Run fastStructure

####Test various K values (K represents model complexity)

```bash
s=1
f=5
for i in $(seq $s $f)
do
    qsub $scripts/sub_fast_structure.sh ${input_file%.vcf} $i
done
```

####Choosing model complexity (K) among all the K values tested

```bash
structure=/home/sobczm/bin/fastStructure
python $structure/chooseK.py --input=${input_file%.vcf} > ${input_file%.vcf}_K_choice
```

####Visualise output of fastStructure

```bash
#Generate sample lables
cut -f2 ${input_file%.vcf}.fam | cut -d " " -f2 > ${input_file%.vcf}.lab

#Draw output - errors here
for i in $(seq $s $f)
do
    python $structure/distruct_mod.py -K $i --input=${input_file%.vcf} --output=${input_file%.vcf}_${i}.svg --title K$i --popfile=${input_file%.vcf}.lab
done
```
