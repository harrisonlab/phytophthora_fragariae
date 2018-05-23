#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -pe smp 1
#$ -l h_vmem=2G
#$ -l h=blacklace05.blacklace|blacklace06.blacklace|blacklace07.blacklace|blacklace08.blacklace|blacklace09.blacklace|blacklace10.blacklace

input_dir=$1
seq=$2
loc=$3
lk=$4
its=$5
bpen=$6
samp=$7

cd $input_dir

interval -seq $seq -loc $loc -lk $lk -its $its -bpen $bpen -samp $samp -exact
