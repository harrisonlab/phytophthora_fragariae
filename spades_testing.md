
```bash
qlogin -pe smp 16 -l virtual_free=23G -l h=blacklace11.blacklace
```

# Screen opened and ssh into blacklace 11

```bash
<!-- Usage="submit_SPAdes.sh <F1_read.fa> <R1_read.fa> <F2_read.fa> <R2_read.fa> <F3_read.fa> <R3_read.fa> <output_directory> <correct/only-assembler> [<coverage_cutoff>]" -->
F1=$(ls qc_dna/paired/P.fragariae/Bc1/F/*.fq.gz | grep 'S1')
R1=$(ls qc_dna/paired/P.fragariae/Bc1/R/*.fq.gz | grep 'S1')
F2=$(ls qc_dna/paired/P.fragariae/Bc1/F/*.fq.gz | grep 'S3')
R2=$(ls qc_dna/paired/P.fragariae/Bc1/R/*.fq.gz | grep 'S3')
OutDir=assembly/spades/P.fragariae/Bc1
Correction=correct
Cutoff='10'

CurPath=$PWD
WorkDir=tmp/spades_test

F1_Read=$(basename $F1)
R1_Read=$(basename $R1)
F2_Read=$(basename $F2)
R2_Read=$(basename $R2)

cp $CurPath/$F1 $WorkDir
cp $CurPath/$R1 $WorkDir
cp $CurPath/$F2 $WorkDir
cp $CurPath/$R2 $WorkDir

echo  "Running SPADES with the following in='$F1 $R1 $F2 $R2' $OutDir" 2>&1 | tee -a output3.file
echo "You have set read correction to: $Correction" 2>&1 | tee -a output3.file
echo "Coverage cutoff set to $Cutoff" 2>&1 | tee -a output3.file
SpadesDir=/home/armita/prog/SPAdes-3.5.0-Linux/bin/

if [[ "$Correction" == 'correct' ]]; then
  $SpadesDir/spades.py \
      -k 21,33,55,77,99,127 \
      -m 368 \
      --phred-offset 33 \
      --careful \
      --pe1-1 $WorkDir/$F1_Read \
      --pe1-2 $WorkDir/$R1_Read \
      --pe2-1 $WorkDir/$F2_Read \
      --pe2-2 $WorkDir/$R2_Read \
      -t 16  \
      -o $WorkDir/. \
      --cov-cutoff "$Cutoff"
elif [[ "$Correction" == 'only-assembler' ]]; then
  $SpadesDir/spades.py \
      -k 21,33,55,77,99,127 \
      -m 180 \
      --phred-offset 33 \
      --careful \
      --only-assembler \
      --pe1-1 $WorkDir/$F1_Read \
      --pe1-2 $WorkDir/$R1_Read \
      --pe2-1 $WorkDir/$F2_Read \
      --pe2-2 $WorkDir/$R2_Read \
      -t 16  \
      -o $WorkDir/. \
      --cov-cutoff "$Cutoff"
else
  echo "Please set sixth option - whether you require read correction [correct / only-assembler]"
  exit
fi 2>&1 | tee -a output3.file
```
