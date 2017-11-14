# FALCON Assembly instructions
FALCON is an assembler designed by Pacific Biosciences to assemble long-read data. It is also 'diploid-aware'. This file contains an example set of commands for running FALCON on PacBio data for the BC-16 strain of *Phytophthora fragariae*. This is run on NIABs triticum computer.

## Log in to NIABs cluster

```bash
ssh vicker@10.1.10.170
```

## First, convert the shell interface to BASH for ease of used

```sh
/bin/bash
```

The following lines must be in your bash profile

```bash
export PATH=/home/sobczm/bin/cmake-3.8.0/bin:${PATH}
export PATH=/home/sobczm/bin/gawk-4.1.4:${PATH}
export PYTHONPATH=/data/software/smrtanalysis/install/smrtanalysis_2.3.0.140936/analysis/bin
export PYTHONPATH="$PYTHONPATH:/data/software/smrtanalysis/install/smrtanalysis_2.3.0.140936/common/lib"
export PYTHONPATH="$PYTHONPATH:/data/software/smrtanalysis/install/smrtanalysis_2.3.0.140936/analysis/lib/python2.7"
export PYTHONPATH="$PYTHONPATH:/home/sobczm/usr/local/lib/python2.7/site-packages"
export PYTHONPATH="$PYTHONPATH:/home/sobczm/bin/FALCON-integrate/fc_env/lib/python2.7/site-packages"
export PYTHONPATH="$PYTHONPATH:/data/software/smrtanalysis/install/smrtanalysis_2.3.0.140936/analysis/lib"
export PYTHONUSERBASE=/home/sobczm/bin/FALCON-integrate/fc_env
export PATH=$PYTHONUSERBASE/bin:${PATH}
export PATH=/home/sobczm/usr/local/bin:${PATH}
export PATH=/home/sobczm/bin/pbh5tools/bin:${PATH}
export PATH=/data/software/smrtanalysis/install/smrtanalysis_2.3.0.140936/analysis/bin:${PATH}
```

## Next, extract the concatenated pacbio reads created in pacbio_assembly.md

```bash
cd /data/projects/vicker/tom_adams_pfrag/
gunzip concatenated_pacbio_1.fastq.gz
gunzip concatenated_pacbio_2.fastq.gz
```

In order to run, FALCON needs two files to be available. One that tells it where the fasta files of reads are and one that specifies parameters to run with. These need to be stored in the run directory. Create these files with touch, then use nano to copy and paste in the body text.

```bash
touch input.fofn
nano input.fofn
touch fc_run_Bc16_local.cfg
nano fc_run_Bc16_local.cfg
```

## Run falcon job itself in a screen session

```bash
screen -a
export PYTHONUSERBASE=/data/software/FALCON-integrate/fc_env
export PATH=$PYTHONUSERBASE/bin:$PATH
# fc_run.py fc_run.cfg
```
These commands failed, see below for correct commands

#My script was immediately crashing, Maria managed to get it working and put together a config file for this assembly.
Because FALCON is not a plug-and-play assembler, the initial run provides information that can be used for improving the assembly. Following is a summary of the statistics it is suggested to generate in the FALCON tutorial documentation: https://pb-falcon.readthedocs.io/en/latest/tutorial.html#raw-and-pread-coverage-and-quality

Ways of assessing each step of the assembly is detailed in Assembly_Assessment.md

```
From countFasta.pl:

primary contigs:

Total length of sequence:       94100515 bp
Total number of sequences:      287
N25 stats:                      25% of total sequence length is contained in the 12 sequences >= 1648251
bp
N50 stats:                      50% of total sequence length is contained in the 31 sequences >= 922668
bp
N75 stats:                      75% of total sequence length is contained in the 66 sequences >= 495519
bp
Total GC count:                 50198336 bp
GC %:                           53.35 %

This is about 2kb smaller than the canu assembly, but has a larger N50 and the GC content is about the same.

associate contigs:

Total length of sequence:       472036 bp
Total number of sequences:      34
N25 stats:                      25% of total sequence length is contained in the 3 sequences >= 20138
bp
N50 stats:                      50% of total sequence length is contained in the 10 sequences >= 15101
bp
N75 stats:                      75% of total sequence length is contained in the 18 sequences >= 13255
bp
Total GC count:                 260149 bp
GC %:                           55.11 %

-----

From DBstats on raw reads:

Statistics for all wells of length 500 bases or more

        775,791 reads        out of         797,702  ( 97.3%)
  5,877,358,088 base pairs   out of   5,883,645,299  ( 99.9%)

          7,575 average read length
          5,024 standard deviation

  Base composition: 0.243(A) 0.249(C) 0.261(G) 0.247(T)

This shows an extremely small amount of reads and bases were discarded.

From DBstats on preads:

Statistics for all reads of length 70 bases or more

        167,207 reads        out of         167,207  (100.0%)
  1,781,207,300 base pairs   out of   1,781,207,300  (100.0%)

         10,652 average read length
          3,797 standard deviation

  Base composition: 0.240(A) 0.260(C) 0.260(G) 0.240(T)

This shows a much lower number of base pairs than in the raw reads, but this is fine.

-----

From pre_assembly_stats.json

"genome_length": 100000000,
"length_cutoff": 10262,
"preassembled_bases": 1781207300,
"preassembled_coverage": 17.812,
"preassembled_mean": 10652.708,
"preassembled_n50": 11749,
"preassembled_p95": 16895,
"preassembled_reads": 167207,
"preassembled_seed_fragmentation": 1.128,
"preassembled_seed_truncation": 1758.356,
"preassembled_yield": 0.594,
"raw_bases": 5877358088,
"raw_coverage": 58.774,
"raw_mean": 7575.955,
"raw_n50": 10395,
"raw_p95": 16514,
"raw_reads": 775791,
"seed_bases": 3000126538,
"seed_coverage": 30.001,
"seed_mean": 14047.772,
"seed_n50": 13735,
"seed_p95": 21140,
"seed_reads": 213566

The preassembled coverage here is very low, at only 17x, but a drop between raw and preassembled is normal, yield is okay as > 50. Seed truncation is nice and low.
```

An assembly graph will also be created, asked Maria to run the following commands as I cannot due to permissions:

```bash
cd 2-asm-falcon
fc_ovlp_stats.py --fofn ../1-preads_ovl/merge-gather/las.fofn > ovlp.stats
```

This is plotted using the R script Plot_ovlp_stats.R

This has a cluster at the far left of the graph, this will inform coverage cut off values


#Run commands from Maria

```bash
screen -a

/bin/bash

source /home/sobczm/bin/FALCON-integrate/env.sh
/home/sobczm/bin/FALCON-integrate/fc_env/bin/fc_run.py fc_run.cfg
```

After running

```
cd 2-asm-falcon
perl /data/projects/sobczm/pfrag/2-asm-falcon/countFasta.pl p_ctg.fa
```

#Second attempt run with the following parameters changed:

```
max_cov = 100
min_cov = 2
```

#Third attempt increased max_cov as decreasing made it worse

```
max_cov = 150
```

This seems to be balancing act of contiguity vs assembly size - increasing it increases size but decreases contiguity

#Fourth trial, see what changing max_diff does - this looks like less of the repetitive regions have assembled, so the genome size is smaller, but the contiguity is worse

```
max_diff = 35
```

#Trial 5, increase length_cutoff, it made it horrible, 20Mb smaller, 4 times as many contigs!

```
length_cutoff=15000
```

#Trial 6, lower it, which was my initial intention. Still smaller with more contigs, make small increases up to default value to see if any are better. 9000 seems somewhat sensible, but again it looks like a trade-off between assembly size and assembly contiguity, need to see if Rob can enlighten me any further.

```
length_cutoff=5000 - then try 7500, then 9000, try 11,000 too
```

Now run through a set of parameters to optimise, start with the ones acting earliest then move through the pipeline, testing BUSCO every time. Parameters are: length_cutoff, length_cutoff_pr, falcon_sense_option min_cov, max_n_read, overlap_filtering_setting min_cov, max_cov, max_diff

Final parameters used:
length_cutoff = -1, genome_size = 100000000, seed_coverage = 30
length_cutoff_pr = 3500
falcon_sene_option min_cov = 4
max_n_read = 150
overlap_filtering_setting min_cov = 1
max_cov = 120
max_diff = 120

```
BUSCO statistics:
Complete and single copy genes: 266
Complete and duplicated genes: 6
Fragmented genes: 8
Missing genes: 23

Assembly statistics:
Genome size: 94,234,702 bp
Number of contigs: 288
N50: 916,748
GC content: 53.32%
```

#Polishing the assembly

FALCON produces two fasta files: primary contigs and associate contigs. Use FALCON_Unzip. This requires bam files to be created using pitchfork

##Copy bax.h5 files to triticum

```bash
for raw_data in $(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/raw_dna/pacbio/P.fragariae/Bc16/*/Analysis_Results/*.bax.h5)
do
    sshpass -f ./super_secret_file scp $raw_data vicker@10.1.10.170:/data/projects/adamst/P.fragariae/raw_pacbio_data/
done
rm ./super_secret_file
```

##Run pitchfork on bax.h5 files

```bash
bb=/home/sobczm/bin/pitchfork/workspace/bax2bam/bin
#Convert Bax to BAM for CCS
#S1
LD_LIBRARY_PATH=/home/sobczm/bin/pitchfork/deployment/lib $bb/bax2bam -o S1.bam m160505_144130_42165_c101002402550000001823228709161643_s1_p0.1.bax.h5 m160505_144130_42165_c101002402550000001823228709161643_s1_p0.2.bax.h5 m160505_144130_42165_c101002402550000001823228709161643_s1_p0.3.bax.h5
#S2
LD_LIBRARY_PATH=/home/sobczm/bin/pitchfork/deployment/lib $bb/bax2bam -o S2.bam m160505_190031_42165_c101002402550000001823228709161644_s1_p0.1.bax.h5 m160505_190031_42165_c101002402550000001823228709161644_s1_p0.2.bax.h5 m160505_190031_42165_c101002402550000001823228709161644_s1_p0.3.bax.h5
#S3
LD_LIBRARY_PATH=/home/sobczm/bin/pitchfork/deployment/lib $bb/bax2bam -o S3.bam m160505_231957_42165_c101002402550000001823228709161645_s1_p0.1.bax.h5 m160505_231957_42165_c101002402550000001823228709161645_s1_p0.2.bax.h5 m160505_231957_42165_c101002402550000001823228709161645_s1_p0.3.bax.h5
#S4
LD_LIBRARY_PATH=/home/sobczm/bin/pitchfork/deployment/lib $bb/bax2bam -o S4.bam m160506_033900_42165_c101002402550000001823228709161646_s1_p0.1.bax.h5 m160506_033900_42165_c101002402550000001823228709161646_s1_p0.2.bax.h5 m160506_033900_42165_c101002402550000001823228709161646_s1_p0.3.bax.h5
#S5
LD_LIBRARY_PATH=/home/sobczm/bin/pitchfork/deployment/lib $bb/bax2bam -o S5.bam m170121_175443_42165_c101117442550000001823252505221772_s1_p0.1.bax.h5 m170121_175443_42165_c101117442550000001823252505221772_s1_p0.2.bax.h5 m170121_175443_42165_c101117442550000001823252505221772_s1_p0.3.bax.h5
#S6
LD_LIBRARY_PATH=/home/sobczm/bin/pitchfork/deployment/lib $bb/bax2bam -o S6.bam m170121_221844_42165_c101117442550000001823252505221773_s1_p0.1.bax.h5 m170121_221844_42165_c101117442550000001823252505221773_s1_p0.2.bax.h5 m170121_221844_42165_c101117442550000001823252505221773_s1_p0.3.bax.h5
#S7
LD_LIBRARY_PATH=/home/sobczm/bin/pitchfork/deployment/lib $bb/bax2bam -o S7.bam m170122_044633_42165_c101117442550000001823252505221774_s1_p0.1.bax.h5 m170122_044633_42165_c101117442550000001823252505221774_s1_p0.2.bax.h5 m170122_044633_42165_c101117442550000001823252505221774_s1_p0.3.bax.h5
```

#After copying input_bam.fofn and fc_unzip.cfg, run unzip, as Rob's triticum login has no bash profile, manually export Maria's profile to my path too

This MUST be run from the directory where the inital FALCON run was performed

##Run FALCON_Unzip

```bash
screen -a

/bin/bash

cd /data/projects/adamst/P.fragariae
source /home/sobczm/bin/FALCON-integrate/env.sh

/home/sobczm/bin/FALCON-integrate/fc_env/bin/fc_unzip.py fc_unzip.cfg
```

To run quiver, the following two lines MUST be commented out of your profile.

```
# export PYTHONPATH="$PYTHONPATH:/data/software/smrtanalysis/install/smrtanalysis_2.3.0.140936/common/lib"
# export PYTHONPATH="$PYTHONPATH:/data/software/smrtanalysis/install/smrtanalysis_2.3.0.140936/analysis/lib/python2.7"
```

Check that this has been successful by checking your version of numpy in a python interface, if it is 1.7.1 then quiver will fail.

```python
python
import numpy
numpy.version.version
```

##Run Quiver

```bash
screen -a

/bin/bash

cd /data/projects/adamst/P.fragariae
source /home/sobczm/bin/FALCON-integrate/env.sh
/home/sobczm/bin/FALCON-integrate/fc_env/bin/fc_quiver.py fc_unzip.cfg
```

Check BUSCOs at every step, data listed below

```
After FALCON_Unzip:
BUSCO statistics: 264
Complete and single copy genes: 257
Complete and duplicated genes: 7
Fragmented genes: 10
Missing genes: 29

Assembly statistics:
Genome size: 91,008,576 bp
Number of contigs: 185
N50: 922,664
GC content: 53.36%

After Quiver:
BUSCO statistics: 273
Complete and single copy genes: 264
Complete and duplicated genes: 9
Fragmented genes: 5
Missing genes: 25

Assembly statistics:
Genome size: 91,011,663 bp
Number of contigs: 180
N50: 923,397
GC content: 53.39%
```

##Compare the two assemblies to see if any contigs have been removed due to lack of variation

```bash
/home/adamst/git_repos/scripts/phytophthora_fragariae/Robs_scripts/plot_compare_kmers.py 31 assembly/FALCON_Trial/quiver_results/cns_p_ctg.fasta assembly/FALCON_Trial/dec_min_cov_1/p_ctg.fa Quiver_assessement.png
```

##Polish genome using ten iterations of pilon

```bash
Assembly=assembly/FALCON_Trial/quiver_results/cns_p_ctg.fasta
Organism=P.fragariae
Strain=Bc16
IlluminaDir=$(ls -d qc_dna/paired/$Organism/$Strain)
echo $Strain
echo $Organism
TrimF1_Read=$(ls $IlluminaDir/F/*_trim.fq.gz | head -n1 | tail -n1);
TrimR1_Read=$(ls $IlluminaDir/R/*_trim.fq.gz | head -n1 | tail -n1);
TrimF2_Read=$(ls $IlluminaDir/F/*_trim.fq.gz | head -n2 | tail -n1);
TrimR2_Read=$(ls $IlluminaDir/R/*_trim.fq.gz | head -n2 | tail -n1);
echo $TrimF1_Read
echo $TrimR1_Read
echo $TrimF2_Read
echo $TrimR2_Read
OutDir=assembly/FALCON_Trial/quiver_results/polished
Iterations=10
ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/pilon
qsub $ProgDir/sub_pilon_2_libs.sh $Assembly $TrimF1_Read $TrimR1_Read $TrimF2_Read $TrimR2_Read $OutDir $Iterations diploid
```

Pilon froze on its final iteration, re-run, output will now be pilon_1.fasta

##Run BUSCO analysis after pilon

```bash
Assembly=assembly/FALCON_Trial/quiver_results/polished/pilon_1.fasta
Name=$(echo $Assembly | rev |cut -d '/' -f2 | rev)
echo "$Name"
ProgDir=/home/adamst/git_repos/tools/gene_prediction/busco
BuscoDB=Eukaryotic
OutDir=assembly/FALCON_Trial/quiver_results/$Name
qsub $ProgDir/sub_busco3.sh $Assembly $BuscoDB $OutDir
```

```
Before Pilon:
BUSCO statistics: 273
Complete and single copy genes: 264
Complete and duplicated genes: 9
Fragmented genes: 5
Missing genes: 25

Assembly statistics:
Genome size: 91,011,663 bp
Number of contigs: 180
N50: 923,397
GC content: 53.39%

After Pilon:
BUSCO statistics: 275
Complete and single copy genes: 266
Complete and duplicated genes: 9
Fragmented genes: 5
Missing genes: 23

Assembly statistics:
Genome size: 90,967,989 bp
Number of contigs: 180
N50: 923,458
GC content: 53.39%
```

#Illumina only SPAdes assembly has improved BUSCO statistics compared to the FALCON assembly. Run Quickmerge to see if it helps

```bash
PacBioAssembly=assembly/FALCON_Trial/quiver_results/polished/filtered_contigs/Bc16_contigs_renamed.fasta
Organism=P.fragariae
Strain=Bc16
IlluminaAssembly=assembly/spades/P.fragariae/Bc16/filtered_contigs/contigs_min_500bp.fasta
OutDir=assembly/merged_FALCON_spades/$Organism/$Strain
ProgDir=/home/adamst/git_repos/tools/seq_tools/assemblers/quickmerge
echo $IlluminaAssembly
qsub $ProgDir/sub_quickmerge.sh $PacBioAssembly $IlluminaAssembly $OutDir 923458
```

Regardless of whether the N50 of SPAdes or FALCON assembly it ends up with > 1000 contigs!
