#Analysis of RNA-Seq data

##RNA-Seq data was downloaded from novogenes servers with the following commands

```bash
wget https://s3-eu-west-1.amazonaws.com/novogene-europe/HW/project/C101HW17030405_2.tar
mdkir -p /home/groups/harrisonlab/project_files/phytophthora_fragariae/raw_rna/novogene/
tar -C /home/groups/harrisonlab/project_files/phytophthora_fragariae/raw_rna/novogene/. -xvf /home/groups/harrisonlab/raw_data/raw_seq/P.frag/C101HW17030405_2.tar
```

##Reorganise data into timepoints: mycelium, 0hr, 24hr, 48hr and 96hr

```bash
cd /home/groups/harrisonlab/project_files/phytophthora_fragariae/raw_rna/novogene/
mdkir -p P.fragariae/Bc16
cd P.fragariae/Bc16
mkdir mycelium
mkdir 0hr
mkdir 24hr
mkdir 48hr
mkdir 96hr
mv TA-32_* mycelium/.
mv TA-34_* mycelium/.
mv TA-35_* mycelium/.
mv TA-01_* 0hr/.
mv TA-02_* 0hr/.
mv TA-03_* 0hr/.
mv TA-07_* 24hr/.
mv TA-08_* 24hr/.
mv TA-09_* 24hr/.
mv TA-12_* 48hr/.
mv TA-13_* 48hr/.
mv TA-14_* 48hr/.
mv TA-18_* 96hr/.
mv TA-19_* 96hr/.
mv TA-20_* 96hr/.
```
