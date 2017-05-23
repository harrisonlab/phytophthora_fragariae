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
mkdir -p mycelium/F
mkdir -p mycelium/R
mkdir -p 0hr/F
mkdir -p 0hr/R
mkdir -p 24hr/F
mkdir -p 24hr/R
mkdir -p 48hr/F
mkdir -p 48hr/R
mkdir -p 96hr/F
mkdir -p 96hr/R
mv TA-32_1* mycelium/F/.
mv TA-34_1* mycelium/F/.
mv TA-35_1* mycelium/F/.
mv TA-01_1* 0hr/F/.
mv TA-02_1* 0hr/F/.
mv TA-03_1* 0hr/F/.
mv TA-07_1* 24hr/F/.
mv TA-08_1* 24hr/F/.
mv TA-09_1* 24hr/F/.
mv TA-12_1* 48hr/F/.
mv TA-13_1* 48hr/F/.
mv TA-14_1* 48hr/F/.
mv TA-18_1* 96hr/F/.
mv TA-19_1* 96hr/F/.
mv TA-20_1* 96hr/F/.
mv TA-32_2* mycelium/R/.
mv TA-34_2* mycelium/R/.
mv TA-35_2* mycelium/R/.
mv TA-01_2* 0hr/R/.
mv TA-02_2* 0hr/R/.
mv TA-03_2* 0hr/R/.
mv TA-07_2* 24hr/R/.
mv TA-08_2* 24hr/R/.
mv TA-09_2* 24hr/R/.
mv TA-12_2* 48hr/R/.
mv TA-13_2* 48hr/R/.
mv TA-14_2* 48hr/R/.
mv TA-18_2* 96hr/R/.
mv TA-19_2* 96hr/R/.
mv TA-20_2* 96hr/R/.
```
