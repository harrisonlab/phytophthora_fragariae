# Looks for structural variations between the genomes
## Structural variants can include: duplications, deletions, inversions & translocations. Uses read-pair configuration, split-reads & read-depth

### First, run BWA-mem to align reads to FALCON assembly before SV calling

#### Copy files and concatenate multiple reads into forward and reverse files

```bash
mkdir sv_calling
cd sv_calling

#Copy single library *P. fragariae* isolates
for Strain in A4 Bc23 Nov27 Nov5 Nov77 ONT3 SCRP245_v2
do
    Output_name=$(echo $Strain | sed 's/_.*//g')
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

#### Run BWA-mem

```bash
Reference=../repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa
for Strain in $(ls -d */ | sed 's/[/]//g')
do
    Organism=P.fragariae
    echo "$Organism - $Strain"
    FRead=$Strain/F/*.fq.gz
    RRead=$Strain/R/*.fq.gz
    OutDir=alignment
    mkdir -p $OutDir
    ProgDir=/home/adamst/git_repos/tools/seq_tools/genome_alignment/bwa
    qsub $ProgDir/sub_bwa.sh $Strain $Reference $FRead $RRead $OutDir
done
```

#### Run svaba

```bash
Prefix=Pfrag_svaba
Reference=../repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa
AlignDir=alignment
OutDir=.
ProgDir=/home/adamst/git_repos/scripts/phytophthora/Pcac_popgen
qsub $ProgDir/sub_svaba.sh $Prefix $Reference $AlignDir $OutDir
```

### Analysis of files produced by svaba

#### Analysis of indel file

This file contains smaller indels

##### Set initial variables

```bash
scripts=/home/sobczm/bin/popgen/summary_stats
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/sv_calling
```

##### Create a cut-down VCF and filter it

```bash
cd $input

vcflib=/home/sobczm/bin/vcflib/bin
$vcflib/vcfremovesamples Pfrag_svaba_sv.svaba.indel.vcf SCRP245_sorted.bam ONT3_sorted.bam Nov77_sorted.bam Bc23_sorted.bam > Pfrag_svaba_sv.svaba.indel_cut.vcf

vcftools=/home/sobczm/bin/vcftools/bin
$vcftools/vcftools --vcf Pfrag_svaba_sv.svaba.indel_cut.vcf  --max-missing 0.95 --recode --out Pfrag_svaba_sv.svaba.indel_cut_filtered
```

No sites removed by filtering

#### Ancestral variants

##### For UK2, set UK2 isolates and P. rubi isolates as pop1

```bash
python $scripts/vcf_find_difference_pop.py --vcf Pfrag_svaba_sv.svaba.indel_cut_filtered.recode.vcf --out Pfrag_svaba_sv.svaba.indel_cut_filtered_fixed_UK2.vcf --ply 2 --pop1 Bc16,,A4,,SCRP249,,SCRP324,,SCRP333 --pop2 Nov5,,Bc1,,Nov9,,Nov27,,Nov71 --thr 0.95
```

```
Nothing found
```

##### UK1 based analysis, set UK1 isolates and P. rubi isolates as pop1

```bash
python $scripts/vcf_find_difference_pop.py --vcf Pfrag_svaba_sv.svaba.indel_cut_filtered.recode.vcf --out Pfrag_svaba_sv.svaba.indel_cut_filtered_fixed_UK1.vcf --ply 2 --pop1 Bc1,,Nov5,,SCRP249,,SCRP324,,SCRP333 --pop2 A4,,Bc16,,Nov9,,Nov27,,Nov71 --thr 0.95
```

```
Nothing found
```

##### UK3 based analysis, set UK3 isolates and P. rubi isolates as pop1

```bash
python $scripts/vcf_find_difference_pop.py --vcf Pfrag_svaba_sv.svaba.indel_cut_filtered.recode.vcf --out Pfrag_svaba_sv.svaba.indel_cut_filtered_fixed_UK3.vcf --ply 2 --pop1 Nov9,,Nov27,,Nov71,,SCRP249,,SCRP324,,SCRP333 --pop2 A4,,Bc16,,Nov5,,Bc1 --thr 0.95
```

```
Nothing found
```

#### Just private variants, without addressing ancestral state

##### Create cut down VCF and filter it

```bash
vcflib=/home/sobczm/bin/vcflib/bin
$vcflib/vcfremovesamples Pfrag_svaba_sv.svaba.indel.vcf SCRP245_sorted.bam ONT3_sorted.bam Nov77_sorted.bam Bc23_sorted.bam SCRP249_sorted.bam SCRP324_sorted.bam SCRP333_sorted.bam > Pfrag_svaba_sv.svaba.indel_cut_UK123.vcf

vcftools=/home/sobczm/bin/vcftools/bin
$vcftools/vcftools --vcf Pfrag_svaba_sv.svaba.indel_cut_UK123.vcf  --max-missing 0.95 --recode --out Pfrag_svaba_sv.svaba.indel_cut_UK123_filtered
```

##### For UK2, set UK2 isolates as pop1

```bash
python $scripts/vcf_find_difference_pop.py --vcf Pfrag_svaba_sv.svaba.indel_cut_UK123_filtered.recode.vcf --out Pfrag_svaba_sv.svaba.indel_cut_filtered_fixed_UK2.vcf --ply 2 --pop1 Bc16,,A4 --pop2 Nov5,,Bc1,,Nov9,,Nov27,,Nov71 --thr 0.95
```

```
Nothing found
```

##### UK1 based analysis, set UK1 isolates as pop1

```bash
python $scripts/vcf_find_difference_pop.py --vcf Pfrag_svaba_sv.svaba.indel_cut_UK123_filtered.recode.vcf --out Pfrag_svaba_sv.svaba.indel_cut_filtered_fixed_UK1.vcf --ply 2 --pop1 Bc1,,Nov5 --pop2 A4,,Bc16,,Nov9,,Nov27,,Nov71 --thr 0.95
```

```
Nothing found
```

##### UK3 based analysis, set UK3 isolates as pop1

```bash
python $scripts/vcf_find_difference_pop.py --vcf Pfrag_svaba_sv.svaba.indel_cut_UK123_filtered.recode.vcf --out Pfrag_svaba_sv.svaba.indel_cut_filtered_fixed_UK3.vcf --ply 2 --pop1 Nov9,,Nov27,,Nov71 --pop2 A4,,Bc16,,Nov5,,Bc1 --thr 0.95
```

```
Nothing found
```

### Analysis of files produced by svaba

#### Analysis of sv file

This file contains larger indels

##### Set initial variables

```bash
scripts=/home/sobczm/bin/popgen/summary_stats
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/sv_calling
```

##### Create a cut-down VCF and filter it

```bash
cd $input

vcflib=/home/sobczm/bin/vcflib/bin
$vcflib/vcfremovesamples Pfrag_svaba_sv.svaba.sv.vcf SCRP245_sorted.bam ONT3_sorted.bam Nov77_sorted.bam Bc23_sorted.bam > Pfrag_svaba_sv.svaba.sv_cut.vcf

vcftools=/home/sobczm/bin/vcftools/bin
$vcftools/vcftools --vcf Pfrag_svaba_sv.svaba.sv_cut.vcf  --max-missing 0.95 --recode --out Pfrag_svaba_sv.svaba.sv_cut_filtered
```

#### Ancestral variants

##### For UK2, set UK2 isolates and P. rubi isolates as pop1

```bash
python $scripts/vcf_find_difference_pop.py --vcf Pfrag_svaba_sv.svaba.sv_cut_filtered.recode.vcf --out Pfrag_svaba_sv.svaba.sv_cut_filtered_fixed_UK2.vcf --ply 2 --pop1 Bc16,,A4,,SCRP249,,SCRP324,,SCRP333 --pop2 Nov5,,Bc1,,Nov9,,Nov27,,Nov71 --thr 0.95
```

```
Nothing found
```

##### UK1 based analysis, set UK1 isolates and P. rubi isolates as pop1

```bash
python $scripts/vcf_find_difference_pop.py --vcf Pfrag_svaba_sv.svaba.sv_cut_filtered.recode.vcf --out Pfrag_svaba_sv.svaba.sv_cut_filtered_fixed_UK1.vcf --ply 2 --pop1 Bc1,,Nov5,,SCRP249,,SCRP324,,SCRP333 --pop2 A4,,Bc16,,Nov9,,Nov27,,Nov71 --thr 0.95
```

```
Nothing found
```

##### UK3 based analysis, set UK3 isolates and P. rubi isolates as pop1

```bash
python $scripts/vcf_find_difference_pop.py --vcf Pfrag_svaba_sv.svaba.sv_cut_filtered.recode.vcf --out Pfrag_svaba_sv.svaba.sv_cut_filtered_fixed_UK3.vcf --ply 2 --pop1 Nov9,,Nov27,,Nov71,,SCRP249,,SCRP324,,SCRP333 --pop2 A4,,Bc16,,Nov5,,Bc1 --thr 0.95
```

```
Nothing found
```

#### Just private variants, without assessing ancestral state

##### Create cut down VCF and filter it

```bash
vcflib=/home/sobczm/bin/vcflib/bin
$vcflib/vcfremovesamples Pfrag_svaba_sv.svaba.sv.vcf SCRP245_sorted.bam ONT3_sorted.bam Nov77_sorted.bam Bc23_sorted.bam SCRP249_sorted.bam SCRP324_sorted.bam SCRP333_sorted.bam > Pfrag_svaba_sv.svaba.sv_cut_UK123.vcf

vcftools=/home/sobczm/bin/vcftools/bin
$vcftools/vcftools --vcf Pfrag_svaba_sv.svaba.sv_cut_UK123.vcf  --max-missing 0.95 --recode --out Pfrag_svaba_sv.svaba.sv_cut_UK123_filtered
```

##### For UK2, set UK2 isolates as pop1

```bash
python $scripts/vcf_find_difference_pop.py --vcf Pfrag_svaba_sv.svaba.sv_cut_filtered.recode.vcf --out Pfrag_svaba_sv.svaba.sv_cut_filtered_fixed_UK2.vcf --ply 2 --pop1 Bc16,,A4 --pop2 Nov5,,Bc1,,Nov9,,Nov27,,Nov71 --thr 0.95
```

```
Nothing found
```

##### UK1 based analysis, set UK1 isolates as pop1

```bash
python $scripts/vcf_find_difference_pop.py --vcf Pfrag_svaba_sv.svaba.sv_cut_filtered.recode.vcf --out Pfrag_svaba_sv.svaba.sv_cut_filtered_fixed_UK1.vcf --ply 2 --pop1 Bc1,,Nov5 --pop2 A4,,Bc16,,Nov9,,Nov27,,Nov71 --thr 0.95
```

```
Nothing found
```

##### UK3 based analysis, set UK3 isolates as pop1

```bash
python $scripts/vcf_find_difference_pop.py --vcf Pfrag_svaba_sv.svaba.sv_cut_filtered.recode.vcf --out Pfrag_svaba_sv.svaba.sv_cut_filtered_fixed_UK3.vcf --ply 2 --pop1 Nov9,,Nov27,,Nov71 --pop2 A4,,Bc16,,Nov5,,Bc1 --thr 0.95
```

```
Nothing found
```
