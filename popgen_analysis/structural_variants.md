#Looks for structural variations between the genomes
##Structural variants can include: duplications, deletions, inversions & translocations. Uses read-pair configuration, split-reads & read-depth

###First, run BWA-mem to align reads to FALCON assembly before SV calling

####Copy files and concatenate multiple reads into forward and reverse files

```bash
mkdir sv_calling
cd sv_calling

#Copy single library *P. fragariae* isolates
for Strain in A4 Bc23 Nov27 Nov5 Nov77 ONT3 SCRP245_v2
do
    Output_name=$(echo $Strain | sed 's/_.*//g')
    mkdir -p $Output_name/F
    mkdir -p $Output_name/R
    cp ../qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz $Output_name/F/.
    cp ../qc_dna/paired/P.fragariae/$Strain/R/*.fq.gz $Output_name/R/.
done

#Copy single library *P. rubi* isolates
for Strain in SCRP249 SCRP324 SCRP333
do
    mkdir -p $Strain/F
    mkdir -p $Strain/R
    cp ../../phytophthora_rubi/qc_dna/paired/P.rubi/$Strain/F/*.fq.gz $Strain/F/.
    cp ../../phytophthora_rubi/qc_dna/paired/P.rubi/$Strain/R/*.fq.gz $Strain/R/.
done

#Concatenate and copy *P.fragariae* isolates with multiple libraries
for Strain in Bc1 Bc16 Nov71 Nov9
do
    mkdir -p $Strain/F
    mkdir -p $Strain/R
    gunzip ../qc_dna/paired/P.fragariae/$Strain/F/*.fq.gz
    for File in $(ls ../qc_dna/paired/P.fragariae/$Strain/F/*.fq)
    do
        cat $File >> ../qc_dna/paired/P.fragariae/$Strain/F/"$Strain"_concatenated_F.fq
    done
    gzip ../qc_dna/paired/P.fragariae/$Strain/F/*.fq
    gunzip ../qc_dna/paired/P.fragariae/$Strain/R/*.fq.gz
    for File in $(ls ../qc_dna/paired/P.fragariae/$Strain/R/*.fq)
    do
        cat $File >> ../qc_dna/paired/P.fragariae/$Strain/R/"$Strain"_concatenated_R.fq
    done
    gzip ../qc_dna/paired/P.fragariae/$Strain/R/*.fq
    mv ../qc_dna/paired/P.fragariae/$Strain/F/*_concatenated* $Strain/F/.
    mv ../qc_dna/paired/P.fragariae/$Strain/R/*_concatenated* $Strain/R/.
done
```

####Run BWA-mem

```bash
Reference=../repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa
for Strain in $(ls -d */ | sed 's/[/]//g')
do
    Organism=P.fragariae
    echo "$Organism - $Strain"
    FRead=$Strain/F/*.fq.gz
    RRead=$Strain/R/*.fq.gz
    OutDir=alignment
    mkdir -p $OutDir
    ProgDir=/home/adamst/git_repos/tools/seq_tools/genome_alignment/bwa
    qsub $ProgDir/sub_bwa.sh $Strain $Reference $FRead $RRead $OutDir
done
```

####Run svaba

```bash
Prefix=Pfrag_svaba
Reference=../repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa
AlignDir=alignment
OutDir=./
ProgDir=/home/adamst/git_repos/scripts/phytophthora/Pcac_popgen
qsub $ProgDir/sub_svaba.sh $Prefix $Reference $AlignDir $OutDir
```
