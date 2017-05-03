# FALCON Assembly instructions
FALCON is an assembler designed by Pacific Biosciences to assemble long-read data. It is also 'diploid-aware'. This file contains an example set of commands for running FALCON on PacBio data for the BC-16 strain of *Phytophthora fragariae*. This is run on NIABs triticum computer.

## Log in to NIABs cluster

```bash
ssh vicker@10.1.10.170
```

## First, convert the shell interface to BASH for ease of used

```sh
/bin/bash
```

## Next, extract the concatenated pacbio reads created in pacbio_assembly.md

```bash
cd /data/projects/vicker/tom_adams_pfrag/
gunzip concatenated_pacbio_1.fastq.gz
gunzip concatenated_pacbio_2.fastq.gz
```

In order to run, FALCON needs two files to be available. One that tells it where the fasta files of reads are and one that specifies parameters to run with. These need to be stored in the run directory. Create these files with touch, then use nano to copy and paste in the body text.

```bash
touch input.fofn
nano input.fofn
touch fc_run_Bc16_local.cfg
nano fc_run_Bc16_local.cfg
```

## Run falcon job itself in a screen session

```bash
screen -a
export PYTHONUSERBASE=/data/software/FALCON-integrate/fc_env
export PATH=$PYTHONUSERBASE/bin:$PATH
fc_run.py fc_run.cfg
```

#My script was immediately crashing, Maria managed to get it working and put together a config file for this assembly.
Because FALCON is not a plug-and-play assembler, the initial run provides information that can be used for improving the assembly. Following is a summary of the statistics it is suggested to generate in the FALCON tutorial documentation: https://pb-falcon.readthedocs.io/en/latest/tutorial.html#raw-and-pread-coverage-and-quality

```
From countFasta.pl:

primary contigs:

Total length of sequence:       94100515 bp
Total number of sequences:      287
N25 stats:                      25% of total sequence length is contained in the 12 sequences >= 1648251
bp
N50 stats:                      50% of total sequence length is contained in the 31 sequences >= 922668
bp
N75 stats:                      75% of total sequence length is contained in the 66 sequences >= 495519
bp
Total GC count:                 50198336 bp
GC %:                           53.35 %

This is about 2kb smaller than the canu assembly, but has a larger N50 and the GC content is about the same.

associate contigs:

Total length of sequence:       472036 bp
Total number of sequences:      34
N25 stats:                      25% of total sequence length is contained in the 3 sequences >= 20138
bp
N50 stats:                      50% of total sequence length is contained in the 10 sequences >= 15101
bp
N75 stats:                      75% of total sequence length is contained in the 18 sequences >= 13255
bp
Total GC count:                 260149 bp
GC %:                           55.11 %

-----

From DBstats on raw reads:

Statistics for all wells of length 500 bases or more

        775,791 reads        out of         797,702  ( 97.3%)
  5,877,358,088 base pairs   out of   5,883,645,299  ( 99.9%)

          7,575 average read length
          5,024 standard deviation

  Base composition: 0.243(A) 0.249(C) 0.261(G) 0.247(T)

This shows an extremely small amount of reads and bases were discarded.

From DBstats on preads:

Statistics for all reads of length 70 bases or more

        167,207 reads        out of         167,207  (100.0%)
  1,781,207,300 base pairs   out of   1,781,207,300  (100.0%)

         10,652 average read length
          3,797 standard deviation

  Base composition: 0.240(A) 0.260(C) 0.260(G) 0.240(T)

This shows a much lower number of base pairs than in the raw reads, but this is fine.

-----

From pre_assembly_stats.json

"genome_length": 100000000,
"length_cutoff": 10262,
"preassembled_bases": 1781207300,
"preassembled_coverage": 17.812,
"preassembled_mean": 10652.708,
"preassembled_n50": 11749,
"preassembled_p95": 16895,
"preassembled_reads": 167207,
"preassembled_seed_fragmentation": 1.128,
"preassembled_seed_truncation": 1758.356,
"preassembled_yield": 0.594,
"raw_bases": 5877358088,
"raw_coverage": 58.774,
"raw_mean": 7575.955,
"raw_n50": 10395,
"raw_p95": 16514,
"raw_reads": 775791,
"seed_bases": 3000126538,
"seed_coverage": 30.001,
"seed_mean": 14047.772,
"seed_n50": 13735,
"seed_p95": 21140,
"seed_reads": 213566

The preassembled coverage here is very low, at only 17x, but a drop between raw and preassembled is normal, yield is okay as > 50. Seed truncation is nice and low.
```

An assembly graph will also be created, asked Maria to run the following commands as I cannot due to permissions:

```bash
cd 2-asm-falcon
fc_ovlp_stats.py --fofn ../1-preads_ovl/merge-gather/las.fofn > ovlp.stats
```

This is plotted using the R script Plot_ovlp_stats.R

This has a cluster at the far left of the graph, this will inform coverage cut off values


#Run commands from Maria

```bash
screen -a

/bin/bash
export PYTHONPATH="$PYTHONPATH:/home/sobczm/usr/local/lib/python2.7/site-packages"
export PYTHONPATH="$PYTHONPATH:/home/sobczm/bin/FALCON-integrate/fc_env/lib/python2.7/site-packages"
export PYTHONUSERBASE=/home/sobczm/bin/FALCON-integrate/fc_env
export PATH=$PYTHONUSERBASE/bin:${PATH}
export PATH=/home/sobczm/usr/local/bin:${PATH}
source /home/sobczm/bin/FALCON-integrate/env.sh
/home/sobczm/bin/FALCON-integrate/fc_env/bin/fc_run.py fc_run.cfg
```

After running

```
cd 2-asm-falcon
perl ../../../sobczm/pfrag/2-asm-falcon/countFasta.pl p_ctg.fa
```

#Second attempt run with the following parameters changed:

```
max_cov = 100
min_cov = 2
```

#Third attempt increased max_cov as decreasing made it worse

```
max_cov = 150
```

This seems to be balancing act of contiguity vs assembly size - increasing it increases size but decreases contiguity

#Fourth trial, see what changing max_diff does - this looks like less of the repetitive regions have assembled, so the genome size is smaller, but the contiguity is worse

```
max_diff = 35
```

#Trial 5, increase length_cutoff, it made it horrible, 20Mb smaller, 4 times as many contigs!

```
length_cutoff=15000
```

#Trial 6, lower it, which was my inital intention

```
length_cutoff=5000
```
