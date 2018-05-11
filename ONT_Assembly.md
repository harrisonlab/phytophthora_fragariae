# New sequencing data was generated for the UK3 isolate NOV-9 using ONT

Raw data is deposited at the following location after running on a GridION

```bash
/data/seq_data/minion/2018/20180418_NOV9/
```

Code was all run from /home/groups/harrisonlab/project_files/phytophthora_fragariae

## Build directory structure and run base calling

Data was basecalled again using Albacore on the minion server

```bash
screen -a
ssh nanopore@nanopore

# upgrade albacore
wget https://mirror.oxfordnanoportal.com/software/analysis/ont_albacore-2.2.7-cp34-cp34m-manylinux1_x86_64.whl
/home/nanopore/.local/bin/read_fast5_basecaller.py --version
pip3 install --user ont_albacore-2.2.7-cp34-cp34m-manylinux1_x86_64.whl --upgrade
/home/nanopore/.local/bin/read_fast5_basecaller.py --version

mkdir Pfrag_NOV9_18-04-18
cd Pfrag_NOV9_18-04-18

Organism=P.fragariae
Date=24-04-18
FlowCell="FLO-MIN106"
Kit="SQK-LSK108"
RawDataDir=/data/seq_data/minion/2018/20180418_NOV9/NOV9/GA20000/
OutDir=/data/scratch/nanopore_tmp_data/P.fragariae/albacore_v2.2.7
mkdir -p $OutDir

mkdir -p /home/nanopore/Pfrag_NOV9_18-04-18/$Date
cd /home/nanopore/Pfrag_NOV9_18-04-18/$Date
/home/nanopore/.local/bin/read_fast5_basecaller.py \
--flowcell $FlowCell \
--kit $Kit \
--input $RawDataDir \
--recursive \
--worker_threads 24 \
--save_path Pfrag_albacore_v2.2.7 \
--output_format fastq,fast5 \
--reads_per_fastq_batch 4000
cat Pfrag_albacore_v2.2.7/workspace/pass/*.fastq | gzip -cf > Pfrag_albacore_v2.2.7.fastq.gz
chmod +w $OutDir
cp Pfrag_albacore_v2.2.7.fastq.gz $OutDir/.
chmod +rw $OutDir/Pfrag_albacore_v2.2.7.fastq.gz
tar -czf Pfrag_albacore_v2.2.7.tar.gz Pfrag_albacore_v2.2.7
mv Pfrag_albacore_v2.2.7.tar.gz $OutDir/.
chmod +rw $OutDir/Pfrag_albacore_v2.2.7.tar.gz
```

Build a directory structure on /data and /home

```bash
ProjDir=/home/groups/harrisonlab/project_files/phytophthora_fragariae
cd $ProjDir

Organism=P.fragariae
Strain=NOV-9
OutDir=raw_dna/minion/$Organism/$Strain
mkdir -p $OutDir
RawData=$(ls /data/scratch/nanopore_tmp_data/P.fragariae/albacore_v2.2.7/Pfrag_albacore_v2.2.7.fastq.gz)
cd $OutDir
cp -s $RawData .
cd $ProjDir
```

## Assemble a rough genome with SMARTdenovo

### Adapter removal with porechop

Line added to line 42 of sub_porechop.sh script, not pushed to github by
request of colleagues

```bash
unset PYTHONPATH
```

```bash
for RawReads in $(ls raw_dna/minion/*/*/*.fastq.gz)
do
    Organism=$(echo $RawReads | rev | cut -f3 -d '/' | rev)
    Strain=$(echo $RawReads | rev | cut -f2 -d '/' | rev)
    echo "$Organism - $Strain"
    OutDir=qc_dna/minion/$Organism/$Strain
    ProgDir=/home/adamst/git_repos/tools/seq_tools/dna_qc
    qsub $ProgDir/sub_porechop.sh $RawReads $OutDir
done
```

### Identify sequencing coverage

```bash
for RawData in $(ls qc_dna/minion/*/*/*.fastq.gz)
do
    echo $RawData
    ProgDir=/home/adamst/git_repos/tools/seq_tools/dna_qc
    GenomeSz=90
    OutDir=$(dirname $RawData)
    mkdir -p $OutDir
    qsub $ProgDir/sub_count_nuc.sh $GenomeSz $RawData $OutDir
done
```

```
Genome size: 90 Mb
Bases in file: 6,368,613,371
Number of sequences: 1,016,351
Coverage: 70.76x
```

### Read correction using Canu

```bash
for TrimReads in $(ls qc_dna/minion/*/*/*fastq.gz)
do
    Organism=$(echo $TrimReads | rev | cut -f3 -d '/' | rev)
    Strain=$(echo $TrimReads | rev | cut -f2 -d '/' | rev)
    OutDir=assembly/canu/$Organism/$Strain
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/canu
    GenomeSz=90m
    qsub $ProgDir/sub_canu_correction.sh $TrimReads $GenomeSz $Strain $OutDir
done
```

### Assembly using SMARTdenovo

```bash
for CorrectedReads in $(ls assembly/canu/*/*/*.trimmedReads.fasta.gz | grep -v Bc16)
do
    Organism=$(echo $CorrectedReads | rev | cut -f3 -d '/' | rev)
    Strain=$(echo $CorrectedReads | rev | cut -f2 -d '/' | rev)
    Prefix="$Strain"_SMARTdenovo
    OutDir=assembly/SMARTdenovo/$Organism/$Strain
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/SMARTdenovo
    qsub $ProgDir/sub_SMARTdenovo.sh $CorrectedReads $Prefix $OutDir
done
```

#### Quast and busco analyses were used to assess assembly quality

Quast

```bash
for Assembly in $(ls assembly/SMARTdenovo/*/*/*.dmo.lay.utg)
do
    Strain=$(echo $Assembly | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    OutDir=$(dirname $Assembly)
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/quast
    qsub $ProgDir/sub_quast.sh $Assembly $OutDir
done
```

BUSCO

```bash
for Assembly in $(ls assembly/SMARTdenovo/*/*/*.dmo.lay.utg)
do
    Strain=$(echo $Assembly | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    echo "$Organism - $Strain"
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/busco
    BuscoDB=Eukaryotic
    OutDir=gene_pred/busco/$Organism/$Strain/assembly
    qsub $ProgDir/sub_busco3.sh $Assembly $BuscoDB $OutDir
done
```

```
Assembly statistics:

Number of contigs: 124
N50: 1,250,697
Genome Size: 92,662,945
L50: 23
GC content: 53.48%

BUSCO statistics:

224 complete single copy
6 complete duplicated
40 fragmented
33 missing
```

### Error correction using racon

Before running, add the following line to my bash profile

```
PATH=${PATH}:/data/scratch/armita/minimap/minimap2
```

This polishes the assembly using the raw ONT reads

```bash
for Assembly in $(ls assembly/SMARTdenovo/*/*/*.dmo.lay.utg)
do
    Strain=$(echo $Assembly | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    ReadsFq=$(ls qc_dna/minion/*/$Strain/*fastq.gz)
    Iterations=10
    OutDir=$(dirname $Assembly)"/racon2_$Iterations"
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/racon
    qsub $ProgDir/sub_racon.sh $Assembly $ReadsFq $Iterations $OutDir
done
```

Remove contaminants using a python script

```bash
for Assembly in $(ls assembly/SMARTdenovo/*/*/racon2_10/*.fasta | grep 'round_10')
do
    OutDir=$(dirname $Assembly)
    echo "" > tmp.txt
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/remove_contaminants
    $ProgDir/remove_contaminants.py --keep_mitochondria --inp $Assembly --out $OutDir/racon_min_500bp_renamed.fasta --coord_file tmp.txt > $OutDir/log.txt
done
```

#### Quast and BUSCO were run to assess the effects of racon on assembly quality

Quast

```bash
for Assembly in $(ls assembly/SMARTdenovo/*/*/racon2_10/racon_min_500bp_renamed.fasta)
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    OutDir=$(dirname $Assembly)
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/quast
    qsub $ProgDir/sub_quast.sh $Assembly $OutDir
done
```

BUSCO

```bash
for Assembly in $(ls assembly/SMARTdenovo/*/*/racon2_10/racon_min_500bp_renamed.fasta)
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    echo "$Organism - $Strain"
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/busco
    BuscoDB=Eukaryotic
    OutDir=gene_pred/busco/$Organism/$Strain/assembly
    qsub $ProgDir/sub_busco3.sh $Assembly $BuscoDB $OutDir
done
```

```
Assembly statistics:

Number of contigs: 124
N50: 1,262,408
Genome Size: 93,610,772
L50: 23
GC content: 53.50%

BUSCO statistics:

256 complete single copy
9 complete duplicated
17 fragmented
21 missing
```

### Error correction using nanopolish

Fast5 files are very large and need to be stored as gzipped tarballs.
These need to be temporarily unpacked
They must be deleted after nanpolish has finished running.
This uses information from raw ONT data to polish assemblies

Copy raw reads onto the cluster scratch space for this step and unpack

```bash
Tar=/data/scratch/nanopore_tmp_data/P.fragariae/albacore_v2.2.7/Pfrag_albacore_v2.2.7.tar.gz
ScratchDir=/data/scratch/adamst/P.fragariae/albacore_v2.2.7
mkdir -p $ScratchDir
tar -zxvf $Tar -C $ScratchDir
```

### Run Nanopolish

```bash
for Assembly in $(ls assembly/SMARTdenovo/*/NOV-9/racon2_10/racon_min_500bp_renamed.fasta)
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    echo "$Organism - $Strain"
    # Extract reads as a .fq file
    ReadDir=raw_dna/nanopolish/$Organism/$Strain
    mkdir -p $ReadDir
    ReadsFq=$(ls raw_dna/minion/*/$Strain/*.fastq.gz)
    ScratchDir=/data/scratch/adamst/P.fragariae
    Fast5Dir=$ScratchDir/albacore_v2.2.7/Pfrag_albacore_v2.2.7/workspace/pass
    OutDir=$(dirname $Assembly)/nanopolish
    mkdir -p $OutDir
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/nanopolish
    qsub $ProgDir/sub_minimap2_nanopolish.sh $Assembly $ReadsFq $OutDir
done
```

#### Split assembly into 50Kb fragments and submit each separately for nanopolish

```bash
for Assembly in $(ls assembly/SMARTdenovo/*/NOV-9/racon2_10/racon_min_500bp_renamed.fasta)
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    echo "$Organism - $Strain"
    OutDir=$(dirname $Assembly)/nanopolish
    RawReads=$(ls raw_dna/minion/*/$Strain/*.fastq.gz)
    AlignedReads=$(ls $OutDir/reads.sorted.bam)

    NanopolishDir=/home/armita/prog/nanopolish/nanopolish/scripts
    python $NanopolishDir/nanopolish_makerange.py $Assembly --segment-length 50000 > $OutDir/nanopolish_range.txt

    Ploidy=2
    echo "nanopolish log:" > $OutDir/nanopolish_log.txt
    for Region in $(cat $OutDir/nanopolish_range.txt)
    do
        Jobs=$(qstat | grep 'sub_nanopo' | grep 'qw' | wc -l)
        while [ $Jobs -gt 1 ]
        do
            sleep 1m
            printf "."
            Jobs=$(qstat | grep 'sub_nanopo' | grep 'qw' | wc -l)
        done
        printf "\n"
        echo $Region
        echo $Region >> $OutDir/nanopolish_log.txt
        ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/nanopolish
        qsub $ProgDir/sub_nanopolish_variants.sh $Assembly $RawReads $AlignedReads $Ploidy $Region $OutDir/$Region
    done
done
```

Merge nanopolish results

```bash
for Assembly in $(ls assembly/SMARTdenovo/*/*/racon2_10/racon_min_500bp_renamed.fasta)
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    OutDir=assembly/SMARTdenovo/$Organism/$Strain/nanopolish
    mkdir -p $OutDir
    NanopolishDir=/home/armita/prog/nanopolish/nanopolish/scripts
    InDir=$(dirname $Assembly)
    python $NanopolishDir/nanopolish_merge.py $InDir/nanopolish/*/*.fa > $OutDir/"$Strain"_nanopolish.fa
    echo "" > tmp.txt
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/remove_contaminants
    $ProgDir/remove_contaminants.py --keep_mitochondria --inp $OutDir/"$Strain"_nanopolish.fa --out $OutDir/"$Strain"_nanopolish_min_500bp_renamed.fasta --coord_file tmp.txt > $OutDir/log.txt
done
```

#### Run quast and BUSCO to assess effects of nanopolish on quality

```bash
for Assembly in $(ls assembly/SMARTdenovo/*/*/nanopolish/*_nanopolish_min_500bp_renamed.fasta)
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    # Quast
    OutDir=$(dirname $Assembly)
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/quast
    qsub $ProgDir/sub_quast.sh $Assembly $OutDir
    # BUSCO
    BuscoDB=Eukaryotic
    OutDir=gene_pred/busco/$Organism/$Strain/assembly
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/busco
    qsub $ProgDir/sub_busco3.sh $Assembly $BuscoDB $OutDir
done
```

### Pilon error correction

Corrects assembly using Illumina reads, due to lower error rate
Strain name and illumina filenames need to be changed if code reused

```bash
for Assembly in $(ls assembly/SMARTdenovo/*/*/nanpolish/*_nanopolish_min_500bp_renamed.fasta)
do
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    echo "$Organism - $Strain"
    IlluminaDir=$(ls -d qc_dna/paired/$Organism/Nov9)
    TrimF1_Read=$(ls $IlluminaDir/F/*_160129_trim.fq.gz)
    TrimR1_Read=$(ls $IlluminaDir/R/*_160129_trim.fq.gz)
    TrimF2_Read=$(ls $IlluminaDir/F/Pfrag-*.fq.gz)
    TrimR2_Read=$(ls $IlluminaDir/R/Pfrag-*.fq.gz)
    TrimF3_Read=$(ls $IlluminaDir/F/PfragNov9*.fq.gz)
    TrimR3_Read=$(ls $IlluminaDir/R/PfragNov9*.fq.gz)
    OutDir=$(dirname $Assembly)/../pilon
    Iterations=10
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/pilon
    qsub $ProgDir/sub_pilon_3_libs.sh $Assembly $TrimF1_Read $TrimR1_Read $TrimF2_Read $TrimR2_Read $TrimF3_Read $TrimR3_Read $OutDir $Iterations
done
```

#### Rename contigs

```bash
for Assembly in $(ls assembly/SMARTdenovo/*/*/pilon/*.fasta | grep 'pilon_10')
do
    echo $Assembly
    echo "" > tmp.txt
    OutDir=$(dirname $Assembly)
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/remove_contaminants
    $ProgDir/remove_contaminants.py --keep_mitochondria --inp $Assembly --out $OutDir/pilon_min_500bp_renamed.fasta --coord_file tmp.txt > $OutDir/log.txt
done
```

#### Quast and BUSCO were run to assess the effects of Pilon on quality

```bash
for Assembly in $(ls assembly/SMARTdenovo/*/*/pilon/pilon_min_500bp_renamed.fasta)
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    OutDir=$(dirname $Assembly)
    echo "$Organism - $Strain"
    # Quast
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/quast
    qsub $ProgDir/sub_quast.sh $Assembly $OutDir
    # BUSCO
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/busco
    BuscoDB=Eukaryotic
    OutDir=gene_pred/busco/$Organism/$Strain/assembly
    qsub $ProgDir/sub_busco3.sh $Assembly $BuscoDB $OutDir
done
```

## Hybrid assembly

Some people report hybrid assemblies give higher quality.
I found the opposite for PacBio data, but test with ONT data.

### SPAdes assembly

```bash
for TrimReads in $(ls raw_dna/minion/*/*/*.fastq.gz)
do
    Organism=$(echo $TrimReads | rev | cut -f3 -d '/' | rev)
    Strain=$(echo $TrimReads | rev | cut -f2 -d '/' | rev)
    IlluminaDir=$(ls -d qc_dna/paired/$Organism/Nov9)
    TrimF1_Read=$(ls $IlluminaDir/F/*_160129_trim.fq.gz)
    TrimR1_Read=$(ls $IlluminaDir/R/*_160129_trim.fq.gz)
    TrimF2_Read=$(ls $IlluminaDir/F/Pfrag-*.fq.gz)
    TrimR2_Read=$(ls $IlluminaDir/R/Pfrag-*.fq.gz)
    TrimF3_Read=$(ls $IlluminaDir/F/PfragNov9*.fq.gz)
    TrimR3_Read=$(ls $IlluminaDir/R/PfragNov9*.fq.gz)
    OutDir=assembly/spades_minion/$Organism/$Strain
    echo $TrimF1_Read
    echo $TrimR1_Read
    echo $TrimF2_Read
    echo $TrimR2_Read
    echo $TrimF3_Read
    echo $TrimR3_Read
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/spades/multiple_libraries
    qsub $ProgDir/subSpades_3lib_minion.sh $TrimReads $TrimF1_Read $TrimR1_Read $TrimF2_Read $TrimR2_Read $TrimF3_Read $TrimR3_Read $OutDir
done
```

#### Remove contigs shorter than 500bp

```bash
for Contigs in $(ls assembly/spades_minion/*/*/contigs.fasta)
do
    AssemblyDir=$(dirname $Contigs)
    mkdir -p $AssemblyDir/filtered_contigs
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/abyss
    $ProgDir/filter_abyss_contigs.py $Contigs 500 > $AssemblyDir/filtered_contigs/contigs_min_500bp.fasta
done
```

#### Quast and BUSCO analyses run to assess quality of assemblies

```bash
for Assembly in $(ls assembly/spades_minion/*/*/filtered_contigs/contigs_min_500bp.fasta)
do
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    OutDir=$(dirname $Assembly)
    # Quast
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/quast
    qsub $ProgDir/sub_quast.sh $Assembly $OutDir
    # BUSCO
    BuscoDB=Eukaryotic
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/busco
    qsub $ProgDir/sub_busco3.sh $Assembly $BuscoDB $OutDir
done
```

```
Assembly Statistics:
Number of contigs: 2,824
N50: 124,780
Genome Size: 86,494,617
L50: 203
GC content: 53.34%

BUSCO statistics:

269 complete single copy
10 complete duplicated
7 fragmented
17 missing
```

## Merging SMARTdenovo and SPAdes assemblies

```bash
for MinionAssembly in $(ls assembly/SMARTdenovo/*/*/pilon/pilon_min_500bp_renamed.fasta)
do
    Organism=$(echo $MinionAssembly | rev | cut -f4 -d '/' | rev)
    Strain=$(echo $MinionAssembly | rev | cut -f3 -d '/' | rev)
    HybridAssembly=$(ls assembly/spades_minion/$Organism/$Strain/filtered_contigs/contigs_min_500bp.fasta)
    OutDir=assembly/merged_SMARTdenovo_spades/$Organism/$Strain
    AnchorLength=500000 # May need changing to N50 of Minion
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/quickmerge
    qsub $ProgDir/sub_quickmerge.sh $MinionAssembly $HybridAssembly $OutDir $AnchorLength
done
```

### Quast & BUSCO to assess merged assembly

```bash
for Assembly in $(ls assembly/merged_SMARTdenovo_spades/*/*/merged.fasta)
do
    Strain=$(echo $Assembly | rev | cut -f2 -d '/' | rev)
    Organism=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    OutDir=$(dirname $Assembly)
    # Quast
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/quast
    qsub $ProgDir/sub_quast.sh $Assembly $OutDir
    # BUSCO
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/busco
    BuscoDB=Eukaryotic
    OutDir=$(dirname $Assembly)
    qsub $ProgDir/sub_busco3.sh $Assembly $BuscoDB $OutDir
done
```

### Polish merged assembly with Pilon

```bash
for Assembly in $(ls assembly/merged_SMARTdenovo_spades/*/*/merged.fasta)
do
    Organism=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    Strain=$(echo $Assembly | rev | cut -f2 -d '/' | rev)
    echo "$Organism - $Strain"
    IlluminaDir=$(qc_dna/paired/*/$Strain)
    TrimF1_Read=$(ls $IlluminaDir/F/*_160129_trim.fq.gz)
    TrimR1_Read=$(ls $IlluminaDir/R/*_160129_trim.fq.gz)
    TrimF2_Read=$(ls $IlluminaDir/F/Pfrag-*.fq.gz)
    TrimR2_Read=$(ls $IlluminaDir/R/Pfrag-*.fq.gz)
    TrimF3_Read=$(ls $IlluminaDir/F/PfragNov9*.fq.gz)
    TrimR3_Read=$(ls $IlluminaDir/R/PfragNov9*.fq.gz)
    OutDir=$(dirname $Assembly)/pilon
    Iterations=10
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/pilon
    qsub $ProgDir/sub_pilon_3_libs.sh $Assembly $TrimF1_Read $TrimR1_Read $TrimF2_Read $TrimR2_Read $TrimF3_Read $TrimR3_Read $OutDir $Iterations
done
```

#### Rename contigs of merged assembly

```bash
for Assembly in $(ls assembly/merged_SMARTdenovo_spades/*/*/pilon/*.fasta | grep 'pilon_10')
do
    echo Assembly
    echo "" > tmp.txt
    OutDir=$(dirname $Assembly)
    ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/assembly_qc/remove_contaminants
    $ProgDir/remove_contaminants.py --keep_mitochondria --inp $Assembly --out $OutDir/pilon_min_500bp_renamed.fasta --coord_file tmp.txt > $OutDir/log.txt
done
```

## Repeat Masking

The <X> assembly was the highest quality and so carried forward for analysis

```bash
for Assembly in $(ls PATH/TO/ASSEMBLY)
do
    Organism=$(echo $Assembly | rev | cut -f4 -d '/' | rev)
    Strain=$(echo $Assembly | rev | cut -f3 -d '/' | rev)
    echo "$Organism - $Strain"
    OutDir=repeat_masked/$Organism/$Strain/filtered_contigs
    ProgDir=/home/adamst/git_repos/tools/seq_tools/repeat_masking
    qsub $ProgDir/rep_modeling.sh $Assembly $OutDir
    qsub $ProgDir/transposonPSI.sh $Assembly $OutDir
done
```

### Merge transposonPSI & repeatmasker/repeatmodeller results

```bash
# Softmasked
for File in $(ls PATH/TO/SOFT/MASKED/ASSEMBLY)
do
    OutDir=$(dirname $File)
    TPSI=$(ls $OutDir/*_contigs_unmasked.fa.TPSI.allHits.chains.gff3)
    OutFile=$(echo $File | sed 's/_contigs_softmasked.fa/_contigs_softmasked_repeatmasker_TPSI_appended.fa/g')
    echo "$OutFile"
    bedtools maskfasta -sof -fi $File -bed $TPSI -fo $OutFile
    echo "Number of masked bases:"
    cat $OutFile | grep -v '>' | tr -d '\n' | awk '{print $0, gsub("[a-z]", ".")}' | cut -f2 -d ' '
done

# Hardmasked
for File in $(ls PATH/TO/HARD/MASKED/ASSEMBLY)
do
    OutDir=$(dirname $File)
    TPSI=$(ls $OutDir/*_contigs_unmasked.fa.TPSI.allHits.chains.gff3)
    OutFile=$(echo $File | sed 's/_contigs_hardmasked.fa/_contigs_hardmasked_repeatmasker_TPSI_appended.fa/g')
    echo "$OutFile"
    bedtools maskfasta -fi $File -bed $TPSI -fo $OutFile
done
```
