#Counting number of nucleotides
#Currently coverage estimate does not output a value.

```bash
F_IN=qc_dna/paired/P.fragariae/Bc16/F/Bc16_S2_L001_R1_001_160129_trim.fq.gz
R_IN=qc_dna/paired/P.fragariae/Bc16/R/Bc16_S2_L001_R2_001_160129_trim.fq.gz
F_FILE=qc_dna/paired/P.fragariae/Bc16/F/Bc16_S2_L001_R1_001_160129_trim.fq
R_FILE=qc_dna/paired/P.fragariae/Bc16/R/Bc16_S2_L001_R2_001_160129_trim.fq
GENOME_SZ=93000000
ProgDir=/home/master_files/prog_master/bin/count_nucl.pl
cat $F_IN | gunzip -c -f > $F_FILE
cat $R_IN | gunzip -c -f > $R_FILE
count_nucl.pl -i $F_FILE -i $R_FILE -g $GENOME_SZ
rm $F_FILE
rm $R_FILE
```
