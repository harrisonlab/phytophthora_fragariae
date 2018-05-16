# Evaluation of population structure using fastStructure

## With *Phytophthora rubi* isolates

### Sets initial variables

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/fastStructure/with_rubi
scripts=/home/sobczm/bin/popgen/snp
```

### Concatenates vcf files from multiple sources into one

In this case, variant calls from GATK and indels & SVs from svaba

```bash
mkdir -p $input
cd $input

GATK_vcf=../../SNP_calling/polished_contigs_unmasked_filtered.recode_annotated.vcf
indel_vcf=../../sv_calling/Pfrag_svaba_sv.svaba.indel.vcf
indel_vcf_corrected=Pfrag_svaba_sv.svaba.indel_corrected.vcf
indel_vcf_corrected_sorted=Pfrag_svaba_sv.svaba.indel_corrected_sorted.vcf
SV_vcf=../../sv_calling/Pfrag_svaba_sv.svaba.sv.vcf
sv_vcf_corrected=Pfrag_svaba_sv.svaba.sv_corrected.vcf
sv_vcf_corrected_sorted=Pfrag_svaba_sv.svaba.sv_corrected_sorted.vcf
final_vcf=concatenated_Pfrag_SNP_indel_SV.vcf
vcftools=/home/sobczm/bin/vcftools/bin

cp $indel_vcf $indel_vcf_corrected
cp $SV_vcf $sv_vcf_corrected

# Use nano to remove _sorted.bam from ends of sample names & add _v2 to SCRP245
# Remove at BOTH metafields & column headers
nano $indel_vcf_corrected
nano $sv_vcf_corrected

# Had to uncomment vcflib & vcftools perl variables in my profile for this to run
$vcftools/vcf-shuffle-cols -t $GATK_vcf $indel_vcf_corrected > $indel_vcf_corrected_sorted
$vcftools/vcf-shuffle-cols -t $GATK_vcf $sv_vcf_corrected > $sv_vcf_corrected_sorted
$vcftools/vcf-concat $GATK_vcf $indel_vcf_corrected_sorted $sv_vcf_corrected_sorted > $final_vcf
```

### Converts VCF files to Plink's PED format

```bash
input_file=concatenated_Pfrag_SNP_indel_SV.vcf

plink --allow-extra-chr --const-fid 0 --vcf $input_file --make-bed --out ${input_file%.vcf} > ${input_file%.vcf}.log
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
input_file=concatenated_Pfrag_SNP_indel_SV.vcf
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
input_file=concatenated_Pfrag_SNP_indel_SV.vcf
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

## Without *Phytophthora rubi* isolates

### Concatenates vcf files from multiple sources into one

In this case, variant calls from GATK and indels & SVs from svaba

### Sets initial variables

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/fastStructure/without_rubi
scripts=/home/sobczm/bin/popgen/snp
```

```bash
mkdir -p $input
cd $input

GATK_vcf=../../SNP_calling/Pfrag_only_polished_contigs_unmasked_filtered.recode_annotated.vcf
indel_vcf=../../sv_calling/Pfrag_svaba_sv.svaba.indel.vcf
indel_vcf_corrected=Pfrag_svaba_sv.svaba.indel_corrected.vcf
indel_vcf_corrected_sorted=Pfrag_svaba_sv.svaba.indel_corrected_sorted.vcf
SV_vcf=../../sv_calling/Pfrag_svaba_sv.svaba.sv.vcf
sv_vcf_corrected=Pfrag_svaba_sv.svaba.sv_corrected.vcf
sv_vcf_corrected_sorted=Pfrag_svaba_sv.svaba.sv_corrected_sorted.vcf
final_vcf=concatenated_Pfrag_SNP_indel_SV.vcf
vcftools=/home/sobczm/bin/vcftools/bin
vcflib=/home/sobczm/bin/vcflib/bin

$vcflib/vcfremovesamples $indel_vcf SCRP324_sorted.bam SCRP333_sorted.bam SCRP249_sorted.bam > $indel_vcf_corrected
$vcflib/vcfremovesamples $SV_vcf SCRP324_sorted.bam SCRP333_sorted.bam SCRP249_sorted.bam > $sv_vcf_corrected

# Use nano to remove _sorted.bam from ends of sample names & add _v2 to SCRP245
# Remove at BOTH metafields & column headers
nano $indel_vcf_corrected
nano $sv_vcf_corrected

# Had to uncomment vcflib & vcftools perl variables in my profile for this to run
$vcftools/vcf-shuffle-cols -t $GATK_vcf $indel_vcf_corrected > $indel_vcf_corrected_sorted
$vcftools/vcf-shuffle-cols -t $GATK_vcf $sv_vcf_corrected > $sv_vcf_corrected_sorted
$vcftools/vcf-concat $GATK_vcf $indel_vcf_corrected_sorted $sv_vcf_corrected_sorted > $final_vcf
```

### Converts VCF files to Plink's PED format

```bash
input_file=concatenated_Pfrag_SNP_indel_SV.vcf

plink --allow-extra-chr --const-fid 0 --vcf $input_file --make-bed --out ${input_file%.vcf} > ${input_file%.vcf}.log
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
input_file=concatenated_Pfrag_SNP_indel_SV.vcf
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
