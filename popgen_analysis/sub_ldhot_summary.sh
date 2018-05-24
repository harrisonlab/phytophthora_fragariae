#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -pe smp 1
#$ -l h_vmem=2G
#$ -l h=blacklace05.blacklace|blacklace06.blacklace|blacklace07.blacklace|blacklace08.blacklace|blacklace09.blacklace|blacklace10.blacklace

res=$1
hot=$2
out=$3

ldhot_summary --res $res --hot $hot --out $out
