#! /bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -pe smp 1
#$ -l h_vmem=1G
#$ -l h=blacklace01.blacklace|blacklace02.blacklace|blacklace03.blacklace|blacklace04.blacklace|blacklace05.blacklace|blacklace06.blacklace|blacklace07.blacklace|blacklace08.blacklace|blacklace09.blacklace|blacklace10.blacklace

#Input:
#Fasta file to be subsampled - 1st argument
#Number of random sequences to be printed - 2nd argument
#example usage: qsub sub_fasta_subsample.sh test.fasta 100
#Output: Fasta file with "random_<number of subsampled sequences>" suffix

fasta=$1
number=$2
rep=$3
OutDir=$4

ffilename=$(basename "$fasta")

RANDOM=`date +%N|sed s/...$//`

meme=/home/sobczm/bin/meme_4.11.2/bin/

$meme/fasta-subsample -seed $RANDOM $fasta $number > $OutDir/${ffilename%.*}_random_"$number"_"$rep".fasta

echo "Finished with no errors" > /dev/stdout
