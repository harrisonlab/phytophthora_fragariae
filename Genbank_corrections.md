#After being run through the Genbank contamination screen, seven of thirteen genomes have had contaminants identified from various sources.

The identity of the contaminants has been passed to Andy to allow tweaking of Deconseq for screening assemblies pre-submission.

##One of the assemblies had a number of hits to Bacillus spp., run my isolates through to see if there are any hits in the other isolates.

###Contigs were identified that had BLAST hits to non-phytophthora genomes

Illumina fragariae genomes

```bash
for Assembly in $(ls assembly/spades/*/*/deconseq_Paen/contigs_min_500bp_filtered_renamed.fasta | grep -v 'Bc16')
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    echo "$Organism - $Strain"
    # Exclude_db="bact,virus,hsref"
    Exclude_db="bacillus"
    Good_db="phytoph"
    AssemblyDir=$(dirname $Assembly)
    # OutDir=$AssemblyDir/../deconseq
    OutDir=$AssemblyDir/../deconseq_Paen
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/remove_contaminants
    qsub $ProgDir/sub_deconseq.sh $Assembly $Exclude_db $Good_db $OutDir
done
```

Pacbio fragariae genomes

```bash
Assembly=assembly/FALCON_Trial/quiver_results/polished/deconseq_Paen/contigs_min_500bp_filtered_renamed.fasta
Strain=Bc16
Organism=P.fragariae
echo "$Organism - $Strain"
# Exclude_db="bact,virus,hsref"
Exclude_db="bacillus"
Good_db="phytoph"
AssemblyDir=$(dirname $Assembly)
# OutDir=$AssemblyDir/../deconseq
OutDir=$AssemblyDir/../deconseq_Paen
ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/remove_contaminants
qsub $ProgDir/sub_deconseq.sh $Assembly $Exclude_db $Good_db $OutDir
```

Illumina rubi genomes

```bash
for Assembly in $(ls ../phytophthora_rubi/assembly/spades/*/*/deconseq_Paen/contigs_min_500bp_filtered_renamed.fasta)
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    echo "$Organism - $Strain"
    # Exclude_db="bact,virus,hsref"
    Exclude_db="bacillus"
    Good_db="phytoph"
    AssemblyDir=$(dirname $Assembly)
    # OutDir=$AssemblyDir/../deconseq
    OutDir=$AssemblyDir/../deconseq_Paen
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/remove_contaminants
    qsub $ProgDir/sub_deconseq.sh $Assembly $Exclude_db $Good_db $OutDir
done
```
