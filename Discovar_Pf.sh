#!/bin/bash

#
# run discovar on P.fragariae genome, change for each strain
#

export PATH=${PATH}:/home/vicker/programs/discovardenovo-52488-install/bin/


Strain=Nov77
OUTDIR=discovar/P.fragariae/$Strain
FRAC=1

READS="/home/groups/harrisonlab/project_files/phytophthora_fragariae/raw_dna/paired/P.fragariae/$Strain/*/*.fastq.gz"

mkdir -p ${OUTDIR}

DiscovarDeNovo READS="frac:${FRAC} :: ${READS}" OUT_DIR=${OUTDIR} MEMORY_CHECK=True MAX_MEM_GB=370
