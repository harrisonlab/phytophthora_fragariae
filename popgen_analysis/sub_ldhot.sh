#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -pe smp 1
#$ -l h_vmem=2G
#$ -l h=blacklace05.blacklace|blacklace06.blacklace|blacklace07.blacklace|blacklace08.blacklace|blacklace09.blacklace|blacklace10.blacklace

seq=$1
loc=$2
lk=$3
res=$4
nsim=$5
out=$6

ldhot --seq $seq --loc $loc --lk $lk --res $res --nsim $nsim --out $out
