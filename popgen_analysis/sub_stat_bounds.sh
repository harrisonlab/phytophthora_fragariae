#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -pe smp 1
#$ -l h_vmem=2G
#$ -l h=blacklace05.blacklace|blacklace06.blacklace|blacklace07.blacklace|blacklace08.blacklace|blacklace09.blacklace|blacklace10.blacklace

input=$1
burn=$2
loc=$3

stat -input $input -burn $burn -loc $loc
mv res.txt res_bounds.txt
