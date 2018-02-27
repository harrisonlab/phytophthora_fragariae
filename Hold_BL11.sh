#!/bin/bash
#$ -S /bin/bash
#$ -l h_vmem=376.0G
###$ -l mem_free=1.0G
###$ -l virtual_free=1.0G
#$ -l h_rt=9999:00:00
###$ -pe smp 24
###$ -l h=blacklace11.blacklace

# hold node11 for discovar running directly on the node

while true
do
    sleep 10
done
