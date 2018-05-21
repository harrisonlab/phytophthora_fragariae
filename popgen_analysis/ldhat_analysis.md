# Further analysis of linkage disequilibrium using the LDhat suite

## Installation and profile modifications

Not required for other users

```bash
cd  /home/adamst/prog
git clone https://github.com/auton1/LDhat.git

cd LDhat
make
make clean
```

A manual is included for usage of LDhat:

```bash
/home/adamst/prog/LDhat/manual.pdf
```

In order to use LDhat, add the following line to your profile
Prepending is necessary as convert is also the name of a part of core unix

```bash
PATH=/home/adamst/prog/LDhat:${PATH}
```

## Convert vcf file to correct format for LDhat

Requires a phased vcf (see Pf_linkage_disequilibrium.md) for diploids
Haploids do not require phasing

```bash
input=LDhat/UK123
mkdir -p $input
cd $input

vcftools=/home/sobczm/bin/vcftools/bin
input_vcf=../../summary_stats/polished_contigs_unmasked_UK123_filtered.recode_haplo.vcf
Out_prefix=polished_contigs_unmasked_UK123_haplo

```
