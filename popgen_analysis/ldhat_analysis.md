# Further analysis of linkage disequilibrium using the LDhat suite

Caveat - the model for recombination hotspots is based on human data

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
Treat each contig as a separate "chromosome"

```bash
input=LDhat/UK123
mkdir -p $input
cd $input

vcftools=/home/sobczm/bin/vcftools/bin
input_vcf=../../summary_stats/polished_contigs_unmasked_UK123_filtered.recode_haplo.vcf
Out_prefix=polished_contigs_unmasked_UK123_haplo

contigs=$(cat $input_vcf | grep -v "#" | cut -f1 | cut -f2 -d "_" | sort -n | uniq)
for num in $(echo $contigs)
do
    contig_name=$(echo contig_"$num")
    Out_prefix=$(echo ldhat_"$contig_name")
    mkdir -p $contig_name
    $vcftools/vcftools --vcf $input_vcf --out $Out_prefix --chr $contig_name --phased --ldhat
    mv ldhat_"$contig_name".log $contig_name/.
    mv ldhat_"$contig_name".ldhat.locs $contig_name/.
    mv ldhat_"$contig_name".ldhat.sites $contig_name/.
done
```

## Use pairwise to build a lookup table and calculate some statistics

The following commands must be run in a screen session running a qlogin job
Requires some user input on the command line

My recommendations:

```
Unless another source of evidence available, use the suggested value of theta
Minor changes in theta do not seem to have an effect
4Ner should range between 20 - 100
No. of points on grid should range between 21 - 201
Larger values of 4Ner & No. of points take longer, but are more accurate

After generation of the table, use default grid value for recombination rate
If estimates at extreme of grid, change the defaults - can exceed above limits

Ignore sliding window analyses - interval is better

Use option 2 for rmin to write output to a file not just screen

Allow estimation of 4Ner by moment method

Test for recombination
```

The main thing needed from pairwise is the lookup table
The rest are mostly improved upon by interval & rhomap

```bash
for input_dir in $(ls -d contig_*)
do
    cd $input_dir
    seq_file=*.ldhat.sites
    loc_file=*.ldhat.locs
    pairwise -seq $seq_file -loc $loc_file
    cd ../
done
```

Manually copy and paste all output written to screen to a log.txt file

## Use complete to refine the lookup table

Use the same 4Ner_max, no of points and theta as in pairwise, stored in log file

```bash
input_dir=contig_1
cd $input_dir
n=14
4Ner_max=500
no_points=201
theta=0.00479
complete -n $n -rhomax $4Ner_max -n_pts $n_pts -theta $theta
```
