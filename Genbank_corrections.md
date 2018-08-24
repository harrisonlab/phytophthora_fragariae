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

ONT fragariae genomes

```bash
Assembly=assembly/SMARTdenovo/P.fragariae/NOV-9/pilon/pilon_repeats/pilon_min_500bp_renamed.fasta
Strain=Nov9
Organism=P.fragariae
echo "$Organism - $Strain"
Exclude_db="bacillus"
Good_db="phytoph"
AssemblyDir=$(dirname $Assembly)
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
Good=$(cat $File | cut -f2 | head -n1 | tail -n1)
Both=$(cat $File | cut -f2 | head -n2 | tail -n1)
Bad=$(cat $File | cut -f2 | head -n3 | tail -n1)
printf "$Name\t$Good\t$Both\t$Bad\n"
```

ONT fragariae genomes

```bash
File=assembly/SMARTdenovo/P.fragariae/NOV-9/pilon/deconseq_Paen/log.txt
Name=Nov9
Good=$(cat $File | cut -f2 | head -n1 | tail -n1)
Both=$(cat $File | cut -f2 | head -n2 | tail -n1)
Bad=$(cat $File | cut -f2 | head -n3 | tail -n1)
printf "$Name\t$Good\t$Both\t$Bad"
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
Nov9 (MinION)   124 0   0
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

##These files were used to correct assemblies

```bash
for Assembly in $(ls assembly/spades/P.*/*/deconseq_Paen/contigs_min_500bp_filtered_renamed.fasta | grep -e 'A4' -e 'Bc1' -e 'Nov5' -e 'Nov71' -e 'Nov9' -e 'SCRP245_v2')
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

###Summarise assemblies using QUAST

```bash
for Assembly in $(ls assembly/spades/*/*/ncbi_edits/contigs_min_500bp_renamed.fasta)
do
    Kmer=$(echo $Assembly | rev | cut -f2 -d '/' | rev)
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    # OutDir=assembly/spades/$Organism/$Strain/filtered_contigs
    OutDir=$(dirname $Assembly)
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/quast
    qsub $ProgDir/sub_quast.sh $Assembly $OutDir
done
```

Summary statistics

```
Number of contigs > 1kb:
A4: 8,659 (Decreased by 1)
Bc1: 7,504 (No change)
Nov5: 8,762 (Decreased by 2)
Nov71: 7,884 (Decreased by 1)
Nov9: 7,654 (Decreased by 1)
SCRP245_v2: 8,577 (Decreased by 7)

N50:
A4: 18,245 (No change)
Bc1: 21,842 (Increased by 8)
Nov5: 17,887 (No change)
Nov71: 20,226 (No change)
Nov9: 21,522 (No change)
SCRP245_v2: 20,056 (Decreased by 49)

L50:
A4: 1,116 (No change)
Bc1: 953 (Decreased by 1)
Nov5: 1,134 (No change)
Nov71: 1,016 (No change)
Nov9: 978 (No change)
SCRP245_v2: 995 (Increased by 1)
```

##The python script used above does not yet have the capacity to deal with duplications. Trick it into thinking it's an exclude request by mocking up a text file.

```bash
for Assembly in $(ls assembly/spades/P.*/*/deconseq_Paen/contigs_min_500bp_filtered_renamed.fasta | grep -e 'Nov71')
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    echo "$Organism - $Strain"
    NCBI_report=assembly/spades/P.fragariae/Nov71/ncbi_edits/duplication_trick.txt
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

###Summarise assemblies using QUAST

```bash
for Assembly in $(ls assembly/spades/*/*/ncbi_edits/contigs_min_500bp_renamed.fasta | grep -e 'Nov71')
do
    Kmer=$(echo $Assembly | rev | cut -f2 -d '/' | rev)
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    # OutDir=assembly/spades/$Organism/$Strain/filtered_contigs
    OutDir=$(dirname $Assembly)
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/quast
    qsub $ProgDir/sub_quast.sh $Assembly $OutDir
done
```

```
Number of contigs > 1kb:
NOV-71: 7,884 (No change)

N50:
NOV-71: 20,226 (No change)

L50:
NOV-71: 1,016 (No change)
```

## Re-run SCRP245 against bacillus database to re-identify problem contigs to remove

```bash
for Assembly in $(ls assembly/spades/*/*/ncbi_edits/contigs_min_500bp_renamed.fasta | grep -e 'SCRP245_v2')
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    echo "$Organism - $Strain"
    # Exclude_db="bact,virus,hsref"
    Exclude_db="bacillus"
    Good_db="phytoph"
    AssemblyDir=$(dirname $Assembly)
    # OutDir=$AssemblyDir/../deconseq
    OutDir=$AssemblyDir/../deconseq_Bac
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/remove_contaminants
    qsub $ProgDir/sub_deconseq.sh $Assembly $Exclude_db $Good_db $OutDir
done
```

Assess results

```bash
# for File in $(ls assembly/spades/P.*/*/deconseq/log.txt); do
for File in $(ls assembly/spades/P.*/*/deconseq_Bac/log.txt)
do
    Name=$(echo $File | rev | cut -f3 -d '/' | rev)
    Good=$(cat $File |cut -f2 | head -n1 | tail -n1)
    Both=$(cat $File |cut -f2 | head -n2 | tail -n1)
    Bad=$(cat $File |cut -f2 | head -n3 | tail -n1)
    printf "$Name\t$Good\t$Both\t$Bad\n"
done
```

```
SCRP245_v2      13151   84      16
```

Check these contigs via BLAST and create a list of those that are genuine contaminants

From BLAST, none of them look like it, so ignore these results

## Additional contaminant contigs were identified manually and removed

```bash
for Assembly in $(ls assembly/spades/P.*/*/deconseq_Paen/contigs_min_500bp_filtered_renamed.fasta | grep -e 'ONT3')
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    echo "$Organism - $Strain"
    NCBI_report=assembly/spades/P.fragariae/ONT3/deconseq_Paen/Manual_ID.txt
    if [[ $NCBI_report ]]
    then
        echo "Contamination report found"
    else
        NCBI_report=genome_submission/$Organism/$Strain/initial_submission/no_edits.txt
        printf "Exclude:\nSequence name, length, apparent source\n" > $NCBI_report
    fi
    OutDir=assembly/spades/$Organism/$Strain/manual_edits
    mkdir -p $OutDir
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/remove_contaminants
    $ProgDir/remove_contaminants.py --inp $Assembly --out $OutDir/contigs_min_500bp_renamed.fasta --coord_file $NCBI_report > $OutDir/log.txt
    # $ProgDir/remove_contaminants.py --keep_mitochondria --inp $Assembly --out $OutDir/contigs_min_500bp_renamed.fasta --coord_file $NCBI_report > $OutDir/log.txt
done

for Assembly in $(ls assembly/spades/P.*/*/ncbi_edits/contigs_min_500bp_renamed.fasta | grep -e 'SCRP245_v2')
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    echo "$Organism - $Strain"
    NCBI_report=assembly/spades/P.fragariae/SCRP245_v2/ncbi_edits/Manual_ID.txt
    if [[ $NCBI_report ]]
    then
        echo "Contamination report found"
    else
        NCBI_report=genome_submission/$Organism/$Strain/initial_submission/no_edits.txt
        printf "Exclude:\nSequence name, length, apparent source\n" > $NCBI_report
    fi
    OutDir=assembly/spades/$Organism/$Strain/manual_edits
    mkdir -p $OutDir
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/remove_contaminants
    $ProgDir/remove_contaminants.py --inp $Assembly --out $OutDir/contigs_min_500bp_renamed.fasta --coord_file $NCBI_report > $OutDir/log.txt
    # $ProgDir/remove_contaminants.py --keep_mitochondria --inp $Assembly --out $OutDir/contigs_min_500bp_renamed.fasta --coord_file $NCBI_report > $OutDir/log.txt
done
```

### Run QUAST on edited genomes

```bash
for Assembly in $(ls assembly/spades/*/*/manual_edits/contigs_min_500bp_renamed.fasta)
do
    Kmer=$(echo $Assembly | rev | cut -f2 -d '/' | rev)
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    # OutDir=assembly/spades/$Organism/$Strain/filtered_contigs
    OutDir=$(dirname $Assembly)
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/quast
    qsub $ProgDir/sub_quast.sh $Assembly $OutDir
done
```
