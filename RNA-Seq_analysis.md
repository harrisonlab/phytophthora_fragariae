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
mv ../../C101HW17030405/raw_data/TA-32_1* mycelium/F/.
mv ../../C101HW17030405/raw_data/TA-34_1* mycelium/F/.
mv ../../C101HW17030405/raw_data/TA-35_1* mycelium/F/.
mv ../../C101HW17030405/raw_data/TA-01_1* 0hr/F/.
mv ../../C101HW17030405/raw_data/TA-02_1* 0hr/F/.
mv ../../C101HW17030405/raw_data/TA-03_1* 0hr/F/.
mv ../../C101HW17030405/raw_data/TA-07_1* 24hr/F/.
mv ../../C101HW17030405/raw_data/TA-08_1* 24hr/F/.
mv ../../C101HW17030405/raw_data/TA-09_1* 24hr/F/.
mv ../../C101HW17030405/raw_data/TA-12_1* 48hr/F/.
mv ../../C101HW17030405/raw_data/TA-13_1* 48hr/F/.
mv ../../C101HW17030405/raw_data/TA-14_1* 48hr/F/.
mv ../../C101HW17030405/raw_data/TA-18_1* 96hr/F/.
mv ../../C101HW17030405/raw_data/TA-19_1* 96hr/F/.
mv ../../C101HW17030405/raw_data/TA-20_1* 96hr/F/.
mv ../../C101HW17030405/raw_data/TA-32_2* mycelium/R/.
mv ../../C101HW17030405/raw_data/TA-34_2* mycelium/R/.
mv ../../C101HW17030405/raw_data/TA-35_2* mycelium/R/.
mv ../../C101HW17030405/raw_data/TA-01_2* 0hr/R/.
mv ../../C101HW17030405/raw_data/TA-02_2* 0hr/R/.
mv ../../C101HW17030405/raw_data/TA-03_2* 0hr/R/.
mv ../../C101HW17030405/raw_data/TA-07_2* 24hr/R/.
mv ../../C101HW17030405/raw_data/TA-08_2* 24hr/R/.
mv ../../C101HW17030405/raw_data/TA-09_2* 24hr/R/.
mv ../../C101HW17030405/raw_data/TA-12_2* 48hr/R/.
mv ../../C101HW17030405/raw_data/TA-13_2* 48hr/R/.
mv ../../C101HW17030405/raw_data/TA-14_2* 48hr/R/.
mv ../../C101HW17030405/raw_data/TA-18_2* 96hr/R/.
mv ../../C101HW17030405/raw_data/TA-19_2* 96hr/R/.
mv ../../C101HW17030405/raw_data/TA-20_2* 96hr/R/.
mv ../../C101HW17030405/raw_data/MD5.txt .
```

##Perform qc on RNA-Seq timecourse and mycelium data

```bash
for FilePath in $(ls -d raw_rna/novogene/P.fragariae/Bc16/*)
do
    echo $FilePath
    FileNum=$(ls $FilePath/F/*.gz | wc -l)
    for num in $(seq 1 $FileNum)
    do
        FileF=$(ls $FilePath/F/*.gz | head -n $num | tail -n1)
        FileR=$(ls $FilePath/R/*.gz | head -n $num | tail -n1)
        echo $FileF
        echo $FileR
        Jobs=$(qstat | grep 'rna_qc' | grep 'qw' | wc -l)
        while [ $Jobs -gt 16 ]
        do
            sleep 5m
            printf "."
            Jobs=$(qstat | grep 'rna_qc' | grep 'qw' | wc -l)
        done		
        printf "\n"
        IlluminaAdapters=/home/adamst/git_repos/tools/seq_tools/ncbi_adapters.fa
        ProgDir=/home/adamst/git_repos/tools/seq_tools/rna_qc
        qsub $ProgDir/rna_qc_fastq-mcf.sh $FileF $FileR $IlluminaAdapters RNA
    done
done
```

--progress here--
