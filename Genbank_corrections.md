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

Results were summarised using the following commands

Illumina fragariae genomes

```bash
# for File in $(ls assembly/spades/P.*/*/deconseq/log.txt); do
for File in $(ls assembly/spades/P.*/*/deconseq_Paen/log.txt)
do
    Name=$(echo $File | rev | cut -f3 -d '/' | rev)
    Good=$(cat $File |cut -f2 | head -n1 | tail -n1)
    Both=$(cat $File |cut -f2 | head -n2 | tail -n1)
    Bad=$(cat $File |cut -f2 | head -n3 | tail -n1)
    printf "$Name\t$Good\t$Both\t$Bad\n"
done
```

Pacbio fragariae genomes

```bash
# for File in $(ls assembly/spades/P.*/*/deconseq/log.txt); do
File=assembly/FALCON_Trial/quiver_results/polished/deconseq_Paen/log.txt
Name=Bc16
Good=$(cat $File |cut -f2 | head -n1 | tail -n1)
Both=$(cat $File |cut -f2 | head -n2 | tail -n1)
Bad=$(cat $File |cut -f2 | head -n3 | tail -n1)
printf "$Name\t$Good\t$Both\t$Bad\n"
```

```
A4	13445	0	1
Bc1	11554	1	1
Bc23	13189	2	0
Nov27	12487	1	1
Nov5	13526	2	0
Nov71	12209	3	1
Nov77	13320	1	0
Nov9	11801	0	1
ONT3	13291	1	0
SCRP245_v2	13239	1	9
Bc16	180	0	0
```

Contaminant organisms identified by NCBI BLAST

```
A lot of these contaminant contigs hit phytophthora's when BLASTed. Do not keep this. A few contigs in SCRP245 have bacillus hits, these have been noted and will be removed along with genbanks flagged sequences. Too high a false positive rate.
```

##Manually download report files from NCBI for correction

Phytophthora fragariae

```bash
for Assembly in $(ls assembly/spades/P.*/*/deconseq_Paen/contigs_min_500bp_filtered_renamed.fasta | grep -e 'A4' -e 'Bc1' -e 'Nov5' -e 'Nov71' -e 'Nov9' -e 'SCRP245_v2')
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)  
    NCBI_report_dir=genome_submission/$Organism/$Strain/initial_submission
    mkdir -p $NCBI_report_dir
done
```

Phytophthora rubi

```bash
for Assembly in $(ls assembly/spades/P.*/*/deconseq_Paen/contigs_min_500bp_filtered_renamed.fasta | grep -e 'SCRP324')
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)  
    NCBI_report_dir=genome_submission/$Organism/$Strain/initial_submission
    mkdir -p $NCBI_report_dir
done
```

##These files were used to correct assemblies

```bash
for Assembly in $(ls assembly/spades/P.*/*/deconseq_Paen/contigs_min_500bp_renamed.fasta | grep -e 'A4' -e 'Bc1' -e 'Nov5' -e 'Nov71' -e 'Nov9' -e 'SCRP245_v2')
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    echo "$Organism - $Strain"
    NCBI_report=$(ls genome_submission/$Organism/$Strain/initial_submission/Contamination*.txt)
    if [[ $NCBI_report ]]
    then
        echo "Contamination report found"
    else
        NCBI_report=genome_submission/$Organism/$Strain/initial_submission/no_edits.txt
        printf "Exclude:\nSequence name, length, apparent source\n" > $NCBI_report
    fi
    OutDir=assembly/spades/$Organism/$Strain/ncbi_edits
    mkdir -p $OutDir
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/remove_contaminants
    $ProgDir/remove_contaminants.py --inp $Assembly --out $OutDir/contigs_min_500bp_renamed.fasta --coord_file $NCBI_report > $OutDir/log.txt
    # $ProgDir/remove_contaminants.py --keep_mitochondria --inp $Assembly --out $OutDir/contigs_min_500bp_renamed.fasta --coord_file $NCBI_report > $OutDir/log.txt
done
```
