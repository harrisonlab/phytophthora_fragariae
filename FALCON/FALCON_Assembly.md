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

## Next, extract the concatenated pacio reads created in pacbio_assembly.md

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
export PYTHONUSERBASE=/path/to/FALCON-integrate/fc_env
export PATH=$PYTHONUSERBASE/bin:$PATH
fc_run.py fc_run.cfg
```
