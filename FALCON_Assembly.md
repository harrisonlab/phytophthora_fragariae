#FALCON Assembly instructions
FALCON is an assembler designed by Pacific Biosciences to assemble long-read data. It is also 'diploid-aware'. This file contains an example set of commands for running FALCON on PacBio data for the BC-16 strain of *Phytophthora fragariae*. This is run on NIABs triticum computer.

##First, convert the shell interface to BASH for ease of used

```sh
/bin/bash
```

##Next, extract the concatenated pacio reads created in pacbio_assembly.md

```bash
cd /data/projects/vicker/tom_adams_pfrag/
gunzip concatenated_pacbio_1.fastq.gz
gunzip concatenated_pacbio_2.fastq.gz
```

##FALCON requires a config file and an input file to be created, these is written below and can be pasted into a document using nano

This will be called fc_run.cfg, comments are to explain the various options
```
[General]
# list of files of the initial subread fasta files
input_fofn = input.fofn

#FALCON can take either error corrected or raw reads
input_type = raw
#input_type = preads

# The length cutoff used for seed reads used for initial mapping
length_cutoff = 12000

# The length cutoff used for seed reads usef for pre-assembly
length_cutoff_pr = 12000

# Cluster queue setting
sge_option_da = -pe smp 8 -q jobqueue
sge_option_la = -pe smp 2 -q jobqueue
sge_option_pda = -pe smp 8 -q jobqueue
sge_option_pla = -pe smp 2 -q jobqueue
sge_option_fc = -pe smp 24 -q jobqueue
sge_option_cns = -pe smp 8 -q jobqueue

# concurrency settgin
pa_concurrent_jobs = 32
cns_concurrent_jobs = 32
ovlp_concurrent_jobs = 32

# overlapping options for Daligner
pa_HPCdaligner_option =  -v -dal4 -t16 -e.70 -l1000 -s1000
ovlp_HPCdaligner_option = -v -dal4 -t32 -h60 -e.96 -l500 -s1000

pa_DBsplit_option = -x500 -s50
ovlp_DBsplit_option = -x500 -s50

# error correction consensus optione
falcon_sense_option = --output_multi --min_idt 0.70 --min_cov 4 --local_match_count_threshold 2 --max_n_read 200 --n_core 6

# overlap filtering options
overlap_filtering_setting = --max_diff 100 --max_cov 100 --min_cov 20 --bestn 10
```

Going to need to make qsub print arguments so I can hack around the fact this written for a particular cluster. Not going to be easy!
