#Maria has suggested a new tool to try for orthology analysis, run it in parallel with orthomcl as a comparison.

##Setting of variables

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/analysis/orthology/OrthoFinder
scripts=/home/adamst/git_repos/scripts/popgen/clock/motif_discovery
```

##Copy files of all protein sequences to one directory

```bash
fasta_directory=$input/protein_sequences
mkdir -p $fasta_directory
for Isolate in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    FastaFile=gene_pred/annotation/P.fragariae/$Isolate/"$Isolate"_genes_incl_ORFeffectors.pep.fasta
    cp $FastaFile $fasta_directory/"$Isolate".pep.fa
done

for Isolate in SCRP249 SCRP324 SCRP333
do
    FastaFile=../phytophthora_rubi/gene_pred/annotation/P.rubi/$Isolate/"$Isolate"_genes_incl_ORFeffectors.pep.fasta
    cp $FastaFile $fasta_directory/"$Isolate".pep.fa
done
```

###Runs orthofinder

```bash
screen -a
qlogin -l h=blacklace01.blacklace
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/analysis/orthology/OrthoFinder
scripts=/home/adamst/git_repos/scripts/popgen/clock/motif_discovery
cd $input
sh $scripts/run_orthofinder.sh $fasta_directory
```

This throws an error about packages when run on a worker node. Maria's only solution is for her to run it.
