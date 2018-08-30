# Evaluation of population structure using fastStructure

This uses only biallelic SNP sites

## With *Phytophthora rubi* isolates

### Sets initial variables

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/fastStructure/with_rubi
scripts=/home/adamst/git_repos/scripts/popgen/snp
```

### Converts VCF files to Plink's PED format

```bash
mkdir -p $input
cd $input

vcf=../../SNP_calling/polished_contigs_unmasked_filtered.recode_annotated.vcf
input_file=polished_contigs_unmasked_filtered.recode_annotated.vcf
cp $vcf $input_file

plink --indep-pairwise 100000 1 0.5 --allow-extra-chr --const-fid 0 --vcf $input_file --make-bed --recode --out ${input_file%.vcf} > ${input_file%.vcf}.log
```

### Tests various values of K for iterations of fastStructure

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

### Choose model complexity (K) among all the K values tested

```bash
structure=/home/sobczm/bin/fastStructure
input_file=polished_contigs_unmasked_filtered.recode_annotated.vcf
input_vcf_file=${input_file%.vcf}
python $structure/chooseK.py --input $input_vcf_file > ${input_file%.vcf}_K_choice
```

### Visualise expected admixture proportions with Distruct plots

This uses the mean of variational posterior distribution
over admixture proportions

#### First generate sample labels

```bash
cut -f2 ${input_file%.vcf}.fam | cut -d " " -f2 > ${input_file%.vcf}.lab
```

#### Now draw plots

```bash
# X11 forwarding is required, set up on an OSX local machine running OSX v10.13.4 using:
# https://stackoverflow.com/questions/39622173/cant-run-ssh-x-on-macos-sierra
# -X option needed for ssh to allow X11 forwarding
input_file=polished_contigs_unmasked_filtered.recode_annotated.vcf
input_vcf_file=${input_file%.vcf}
Popfile=${input_file%.vcf}.lab
s=1
f=5
structure=/home/sobczm/bin/fastStructure
for i in $(seq $s $f)
do
    Output=${input_file%.vcf}_${i}.svg
    python $structure/distruct_mod.py -K $i --input $input_vcf_file --output $Output --title K$i --popfile $Popfile
done
```

Works, Throws error for being unable to load a Fontconfig file (non-critical)

## Without *Phytophthora rubi* isolates

### Sets initial variables

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/fastStructure/without_rubi
scripts=/home/adamst/git_repos/scripts/popgen/snp
```

### Converts VCF files to Plink's PED format

```bash
mkdir -p $input
cd $input

vcf_file=../../SNP_calling/Pfrag_only_polished_contigs_unmasked_filtered.recode_annotated.vcf
input_file=Pfrag_only_polished_contigs_unmasked_filtered.recode_annotated.vcf
cp $vcf_file $input_file

plink --indep-pairwise 100000 1 0.5 --allow-extra-chr --const-fid 0 --vcf $input_file --make-bed --recode --out ${input_file%.vcf} > ${input_file%.vcf}.log
```

### Tests various values of K for iterations of fastStructure

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

### Choose model complexity (K) among all the K values tested

```bash
structure=/home/sobczm/bin/fastStructure
input_file=Pfrag_only_polished_contigs_unmasked_filtered.recode_annotated.vcf
input_vcf_file=${input_file%.vcf}
python $structure/chooseK.py --input $input_vcf_file > ${input_file%.vcf}_K_choice
```

### Visualise expected admixture proportions with Distruct plots

This uses the mean of variational posterior distribution
over admixture proportions

#### First generate sample labels

```bash
cut -f2 ${input_file%.vcf}.fam | cut -d " " -f2 > ${input_file%.vcf}.lab
```

#### Now draw plots

```bash
# X11 forwarding is required, set up on an OSX local machine running OSX v10.13.4 using:
# https://stackoverflow.com/questions/39622173/cant-run-ssh-x-on-macos-sierra
# -X option needed for ssh to allow X11 forwarding
input_file=Pfrag_only_polished_contigs_unmasked_filtered.recode_annotated.vcf
input_vcf_file=${input_file%.vcf}
Popfile=${input_file%.vcf}.lab
s=1
f=5
structure=/home/sobczm/bin/fastStructure
for i in $(seq $s $f)
do
    Output=${input_file%.vcf}_${i}.svg
    python $structure/distruct_mod.py -K $i --input $input_vcf_file --output $Output --title K$i --popfile $Popfile
done
```

Throws an error for being unable to load a Fontconfig file (non-critical)

## For curiosities sake, keep only UK123 isolates

### Sets initial variables

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/fastStructure/UK123
scripts=/home/adamst/git_repos/scripts/popgen/snp
```

### Converts VCF files to Plink's PED format

```bash
mkdir -p $input
cd $input

vcf_file=../../SNP_calling/Pfrag_only_polished_contigs_unmasked_filtered.recode_annotated.vcf
input_file=UK123_only_polished_contigs_unmasked_filtered.recode_annotated.vcf
vcflib=/home/sobczm/bin/vcflib/bin
$vcflib/vcfremovesamples $vcf_file SCRP245_v2 Bc23 Nov77 ONT3 > $input_file

plink --indep-pairwise 100000 1 0.5 --allow-extra-chr --const-fid 0 --vcf $input_file --make-bed --recode --out ${input_file%.vcf} > ${input_file%.vcf}.log
```

### Tests various values of K for iterations of fastStructure

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

### Choose model complexity (K) among all the K values tested

```bash
structure=/home/sobczm/bin/fastStructure
input_file=UK123_only_polished_contigs_unmasked_filtered.recode_annotated.vcf
input_vcf_file=${input_file%.vcf}
python $structure/chooseK.py --input $input_vcf_file > ${input_file%.vcf}_K_choice
```

### Visualise expected admixture proportions with Distruct plots

This uses the mean of variational posterior distribution
over admixture proportions

#### First generate sample labels

```bash
cut -f2 ${input_file%.vcf}.fam | cut -d " " -f2 > ${input_file%.vcf}.lab
```

#### Now draw plots

```bash
# X11 forwarding is required, set up on an OSX local machine running OSX v10.13.4 using:
# https://stackoverflow.com/questions/39622173/cant-run-ssh-x-on-macos-sierra
# -X option needed for ssh to allow X11 forwarding
input_file=UK123_only_polished_contigs_unmasked_filtered.recode_annotated.vcf
input_vcf_file=${input_file%.vcf}
Popfile=${input_file%.vcf}.lab
s=1
f=5
structure=/home/sobczm/bin/fastStructure
for i in $(seq $s $f)
do
    Output=${input_file%.vcf}_${i}.svg
    python $structure/distruct_mod.py -K $i --input $input_vcf_file --output $Output --title K$i --popfile $Popfile
done
```

## Try only UK123 isolates again using logistic prior option

This should help detect any weak signals of population structure

### Sets initial variables

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/fastStructure/UK123_logistic
scripts=scripts=/home/adamst/git_repos/scripts/popgen/snp
```

### Converts VCF files to Plink's PED format

```bash
mkdir -p $input
cd $input

vcf_file=../../SNP_calling/Pfrag_only_polished_contigs_unmasked_filtered.recode_annotated.vcf
input_file=UK123_only_polished_contigs_unmasked_filtered.recode_annotated.vcf
vcflib=/home/sobczm/bin/vcflib/bin
$vcflib/vcfremovesamples $vcf_file SCRP245_v2 Bc23 Nov77 ONT3 > $input_file

plink --indep-pairwise 100000 1 0.5 --allow-extra-chr --const-fid 0 --vcf $input_file --make-bed --recode --out ${input_file%.vcf} > ${input_file%.vcf}.log
```

### Tests various values of K for iterations of fastStructure

```bash
# Set minimum number of considered clusters
s=1
# Set maximum number of considered clusters
f=5

for i in $(seq $s $f)
do
    qsub $scripts/sub_fast_structure.sh ${input_file%.vcf} $i logistic
done
```

### Choose model complexity (K) among all the K values tested

```bash
structure=/home/sobczm/bin/fastStructure
input_file=UK123_only_polished_contigs_unmasked_filtered.recode_annotated.vcf
input_vcf_file=${input_file%.vcf}
python $structure/chooseK.py --input $input_vcf_file > ${input_file%.vcf}_K_choice
```

### Visualise expected admixture proportions with Distruct plots

This uses the mean of variational posterior distribution
over admixture proportions

#### First generate sample labels

```bash
cut -f2 ${input_file%.vcf}.fam | cut -d " " -f2 > ${input_file%.vcf}.lab
```

#### Now draw plots

```bash
# X11 forwarding is required, set up on an OSX local machine running OSX v10.13.4 using:
# https://stackoverflow.com/questions/39622173/cant-run-ssh-x-on-macos-sierra
# -X option needed for ssh to allow X11 forwarding
input_file=UK123_only_polished_contigs_unmasked_filtered.recode_annotated.vcf
input_vcf_file=${input_file%.vcf}
Popfile=${input_file%.vcf}.lab
s=1
f=5
structure=/home/sobczm/bin/fastStructure
for i in $(seq $s $f)
do
    Output=${input_file%.vcf}_${i}.svg
    python $structure/distruct_mod.py -K $i --input $input_vcf_file --output $Output --title K$i --popfile $Popfile
done
```

```
Still no population structure detected
```
