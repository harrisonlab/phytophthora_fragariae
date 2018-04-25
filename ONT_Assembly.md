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
mv Pfrag_albacore_v2.2.7.fastq.tar.gz $OutDir/.
chmod +rw $OutDir/Pfrag_albacore_v2.2.7.tar.gz
```

Build a directory structure on /data

```bash
ProjDir=/home/groups/harrisonlab/project_files/phytophthora_fragariae
cd $ProjDir

Organism=P.fragariae
Strain=NOV-9
OutDir=raw_dna/minion/$Organism/$Strain
mkdir -p $OutDir
RawData=$(ls /data/scratch/nanopore_tmp_data/P.fragariae/albacore_v2.2.7/Pfrag_albacore_v2.2.7.fastq.gz)
cd $OutDir
cp -s $RawDat .
cd $ProjDir
```

## Assemble a rough genome with canu

### Adapter removal with porechop

```bash
for RawReads in $(ls raw_dna/minion/*/*/*.fastq.gz)
do
    Organism=$(echo $RawReads | rev | cut -f3 -d '/' | rev)
    Strain=$(echo $RawReads | rev | cut -f2 -d '/' | rev)
    echo "$Organism - $Strain"
    OutDir=qc_dna/minion/$Organism/$Strain
    ProgDir=/home/adast/git_repos/tools/seq_tools/dna_qc
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
    OutDir=$(echo $RawData | cut -f11,12,13,14 -d '/')
    mkdir -p $OutDir
    qsub $ProgDir/sub_count_nuc.sh $GenomeSz $RawData $OutDir
done
```

```
Coverage:

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
for CorrectedReads in $(ls assembly/canu/*/*/*.trimmedReads.fasta.gz)
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

### Error correction using racon

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

Quast and BUSCO were run to assess the effects of racon on assembly quality

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
