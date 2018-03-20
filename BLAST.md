# BLAST for discovar reads of strawberry against the target Rpf2 region in vesca

```bash
qlogin -pe smp 8
mkdir /tmp/blast_fragaria
cd /tmp/blast_fragaria/
cp /home/adamst/redgauntlet_discovar/discovar_0.4375/a.final/a.lines.fasta discovar.fasta
cp /home/adamst/vesca_sequence_region/candidate_region.fa .
Region=candidate_region.fa
Genome=discovar.fasta
makeblastdb -in $Region -input_type fasta -dbtype nucl -out candidate_region.db
OutDir=genome_vs_region
mkdir -p $OutDir
blastn -db candidate_region.db -query $Genome -out \
$OutDir/genome_vs_region_hits.tbl -evalue 1e-10 -outfmt 6 -num_threads 8 \
-num_alignments 1
cp $OutDir/genome_vs_region_hits.tbl /home/adamst/blast_output/.
```

## BLAST done both ways around to make sure we get the correct hits out

```bash
qlogin -pe smp 8
mkdir /tmp/blast_fragaria
cd /tmp/blast_fragaria/
cp /home/adamst/redgauntlet_discovar/discovar_0.4375/a.final/a.lines.fasta discovar.fasta
cp /home/adamst/vesca_sequence_region/candidate_region.fa .
Region=candidate_region.fa
Genome=discovar.fasta
makeblastdb -in $Region -input_type fasta -dbtype nucl -out candidate_region.db
OutDir=genome_vs_region
mkdir -p $OutDir
blastn -db candidate_region.db -query $Genome \
-out $OutDir/genome_vs_region_hits.tbl -evalue 1e-10 \
-outfmt 6 -num_threads 8 -num_alignments 1
cp $OutDir/region_vs_genome_hits.tbl /home/adamst/blast_output/.
```

## Use Perl script to produce .csv file to parse to .gff

## On blacklace03

```bash
qlogin
mkdir -p /tmp/blast_fragaria
cd /tmp/blast_fragaria/
cp /home/adamst/redgauntlet_discovar/discovar_0.4375/a.final/a.lines.fasta discovar.fasta
cp /home/adamst/vesca_sequence_region/candidate_region.fa .
ProgDir=/home/adamst/git_repos/tools/pathogen/blast
Region=candidate_region.fa
Genome=discovar.fasta
OutDir=genome_vs_region
mkdir -p $OutDir
$ProgDir/blast2csv.pl discovar.fasta blastn candidate_region.fa 1 > $OutDir/genome_vs_region.csv
cp $OutDir/genome_vs_region.csv /home/adamst/blast_output/.
cd /tmp
rm -r blast_fragaria
```

## Use tab separated output (option 6) for BLAST with specifiers

```bash
qlogin -pe smp 8
mkdir /tmp/blast_fragaria
cd /tmp/blast_fragaria/
cp /home/adamst/redgauntlet_discovar/discovar_0.4375/a.final/a.lines.fasta discovar.fasta
cp /home/adamst/vesca_sequence_region/candidate_region.fa .
Region=candidate_region.fa
Genome=discovar.fasta
makeblastdb -in $Region -input_type fasta -dbtype nucl -out candidate_region.db
OutDir=genome_vs_region
mkdir -p $OutDir
blastn -db candidate_region.db -query $Genome \
-out $OutDir/genome_vs_region_hits.tbl -evalue 1e-10 \
-outfmt '6 qseqid qseq sseqid pident length mismatch gapopen qstart \
qend sstart send evalue bitscore gaps qlen' -num_threads 8 -num_alignments 1
cp $OutDir/genome_vs_region_hits.tbl /home/adamst/blast_output/.
cd /tmp/
rm -r blast_fragaria
```

## Filter BLAST using a python script

### Be sure to edit the python script as it is NOT written for general usage

```bash
python /home/adamst/git_repos/scripts/phytophthora_fragariae/filter_BLAST_hits.py
```

## Create annotation file

### Due to gaps in sequences Geneious rejects contigs, create annotation file

#### Check awk arguments, number is column number so may not be general

```bash
cat genome_vs_region_hits.tbl | awk '{ print $1,$8,$9 }' > genome_vs_region_hits.bed
```
