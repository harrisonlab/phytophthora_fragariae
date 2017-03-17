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
