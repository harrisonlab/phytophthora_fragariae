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
for FilePath in $(ls -d raw_rna/novogene/P.fragariae/Bc16/* | grep -v '0hr' | grep -v 'MD5.txt')
do
    echo $FilePath
    FileNum=$(ls $FilePath/F/*.gz | wc -l)
    for num in $(seq 1 $FileNum)
    do
        FileF=$(ls $FilePath/F/*.gz | head -n $num | tail -n1)
        FileR=$(ls $FilePath/R/*.gz | head -n $num | tail -n1)
        echo $FileF
        echo $FileR
        Jobs=$(qstat -u "*" | grep 'rna_qc' | grep 'qw' | wc -l)
        while [ $Jobs -gt 16 ]
        do
            sleep 5m
            printf "."
            Jobs=$(qstat | grep 'rna_qc' | grep 'qw' | wc -l)
        done		
        printf "\n"
        IlluminaAdapters=/home/adamst/git_repos/tools/seq_tools/ncbi_adapters.fa
        ProgDir=/home/adamst/git_repos/tools/seq_tools/rna_qc
        qsub -h $ProgDir/rna_qc_fastq-mcf.sh $FileF $FileR $IlluminaAdapters RNA
        JobID=$(qstat | grep 'rna' | tail -n 1 | cut -d ' ' -f1)
        Queue_Status=$(qstat | grep 'rna' | grep 'hqw' | wc -l)
        while (($Queue_Status > 0))
        do
            Queue_Status=$(qstat | grep 'rna' | grep 'hqw' | wc -l)
            load02=$(qstat -u "*" | grep 'blacklace02'| grep 'rna' | wc -l)
            load05=$(qstat -u "*" | grep 'blacklace05'| grep 'rna' | wc -l)
            load06=$(qstat -u "*" | grep 'blacklace06'| grep 'rna' | wc -l)
            load10=$(qstat -u "*" | grep 'blacklace10'| grep 'rna' | wc -l)
            if (($load02 < 3))
            then
                qalter $JobID -l h=blacklace02.blacklace
                sleep 5s
                qalter $JobID -h U
                sleep 5s
                echo "Submitted to node 2"
            elif (($load05 < 3))
            then
                qalter $JobID -l h=blacklace05.blacklace
                sleep 5s
                qalter $JobID -h U
                sleep 5s
                echo "Submitted to node 5"
            elif (($load06 < 3))
            then
                qalter $JobID -l h=blacklace06.blacklace
                sleep 5s
                qalter $JobID -h U
                sleep 5s
                echo "Submitted to node 6"
            elif (($load10 < 3))
            then
                qalter $JobID -l h=blacklace10.blacklace
                sleep 5s
                qalter $JobID -h U
                sleep 5s
                echo "Submitted to node 10"
            else
                echo "all nodes full, waiting ten minutes"
                sleep 10m
            fi
        done    
    done
done

mkdir -p qc_rna/novogene
mv qc_rna/P.fragariae qc_rna/novogene/.
```

###Visualise data quality using fastqc

Only submit three jobs at a time, copying 30 files is too much!

```bash
for RawData in $(ls qc_rna/novogene/P.fragariae/Bc16/*/*/*)
do
    echo $RawData
    ProgDir=/home/adamst/git_repos/tools/seq_tools/dna_qc
    qsub $ProgDir/run_fastqc.sh $RawData
done
```

```
Looks okay, AT rich at early timepoints as expected from a plant genome, rising to higher GC contents at later timepoints
```

#Align mycelium reads to FALCON assembly with STAR

```bash
for Assembly in $(ls repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa)
do
    Strain=Bc16
    Organism=P.fragariae
    echo "$Organism - $Strain"
    for FileF in $(ls qc_rna/novogene/P.fragariae/Bc16/mycelium/F/*_trim.fq.gz)
    do
        Jobs=$(qstat | grep 'sub_sta' | grep 'qw'| wc -l)
        while [ $Jobs -gt 1 ]
        do
            sleep 1m
            printf "."
            Jobs=$(qstat | grep 'sub_sta' | grep 'qw'| wc -l)
        done
        printf "\n"
        FileR=$(echo $FileF | sed 's&/F/&/R/&g'| sed 's/_1/_2/g')
        echo $FileF
        echo $FileR
        Timepoint=$(echo $FileF | rev | cut -d '/' -f3 | rev)
        echo "$Timepoint"
        Sample_Name=$(echo $FileF | rev | cut -d '/' -f1 | rev | sed 's/_1_trim.fq.gz//g')
        OutDir=alignment/star/$Organism/$Strain/$Timepoint/$Sample_Name
        ProgDir=/home/adamst/git_repos/tools/seq_tools/RNAseq
        qsub $ProgDir/sub_star.sh $Assembly $FileF $FileR $OutDir
    done
done
```

##Align all timepoints to *Fragaria vesca* genome v1.1

```bash
for FileF in $(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/qc_rna/novogene/P.fragariae/Bc16/*/F/*_trim.fq.gz | grep -v 'TA-3')
do
    Jobs=$(qstat | grep 'sub_sta' | grep 'qw'| wc -l)
    while [ $Jobs -gt 1 ]
    do
        sleep 1m
        printf "."
        Jobs=$(qstat | grep 'sub_sta' | grep 'qw'| wc -l)
    done
    printf "\n"
    FileR=$(echo $FileF | sed 's&/F/&/R/&g'| sed 's/_1/_2/g')
    echo $FileF
    echo $FileR
    Timepoint=$(echo $FileF | rev | cut -d '/' -f3 | rev)
    echo "$Timepoint"
    Sample_Name=$(echo $FileF | rev | cut -d '/' -f1 | rev | sed 's/_1_trim.fq.gz//g')
    OutDir=alignment/star/vesca_alignment/$Timepoint/$Sample_Name
    ProgDir=/home/adamst/git_repos/scripts/popgen/rnaseq
    Assembly=/home/sobczm/popgen/rnaseq/fvesca_v1.1_all.fa
    GFF=/home/sobczm/popgen/rnaseq/Fragaria_vesca_v1.1.a2.gff3
    qsub $ProgDir/sub_star_sensitive.sh $Assembly $FileF $FileR $OutDir $GFF
done
```

##Align unmapped reads to *P. fragariae* genomes

###FALCON assembly

```bash
for AlignDir in $(ls -d /home/groups/harrisonlab/project_files/phytophthora_fragariae/alignment/star/vesca_alignment/*/*)
do
    printf "\n"
    cat $AlignDir/star_aligmentUnmapped.out.mate1 | gzip -cf >$AlignDir/star_aligmentUnmapped.out.mate1.fq.gz
    cat $AlignDir/star_aligmentUnmapped.out.mate2 | gzip -cf >$AlignDir/star_aligmentUnmapped.out.mate2.fq.gz
    File1=$AlignDir/star_aligmentUnmapped.out.mate1.fq.gz
    File2=$AlignDir/star_aligmentUnmapped.out.mate2.fq.gz
    echo $File1
    echo $File2
    Timepoint=$(echo $AlignDir | rev | cut -d '/' -f2 | rev)
    echo "$Timepoint"
    Sample_Name=$(echo $AlignDir | rev | cut -d '/' -f1 | rev)
    OutDir=alignment/star/P.fragariae/Bc16/$Timepoint/$Sample_Name
    ProgDir=/home/adamst/git_repos/scripts/popgen/rnaseq
    Assembly=/home/groups/harrisonlab/project_files/phytophthora_fragariae/assembly/FALCON_Trial/quiver_results/polished/filtered_contigs/Bc16_contigs_renamed.fasta
    qsub $ProgDir/sub_star_sensitive.sh $Assembly $File1 $File2 $OutDir
done
```

###Illumina genomes

```bash
for Assembly in $(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/P.fragariae/*/filtered_contigs_repmask/*_contigs_unmasked.fa)
do
    for AlignDir in $(ls -d /home/groups/harrisonlab/project_files/phytophthora_fragariae/alignment/star/vesca_alignment/*/*)
    do
        Jobs=$(qstat | grep 'sub_sta' | grep 'qw'| wc -l)
        while [ $Jobs -gt 1 ]
        do
            sleep 1m
            printf "."
            Jobs=$(qstat | grep 'sub_sta' | grep 'qw'| wc -l)
        done
        printf "\n"
        File1=$AlignDir/star_aligmentUnmapped.out.mate1.fq.gz
        File2=$AlignDir/star_aligmentUnmapped.out.mate2.fq.gz
        echo $File1
        echo $File2
        Timepoint=$(echo $AlignDir | rev | cut -d '/' -f2 | rev)
        echo "$Timepoint"
        Sample_Name=$(echo $AlignDir | rev | cut -d '/' -f1 | rev)
        Strain=$(echo $Assembly | rev | cut -d '/' -f3 | rev)
        OutDir=alignment/star/P.fragariae/$Strain/$Timepoint/$Sample_Name
        ProgDir=/home/adamst/git_repos/scripts/popgen/rnaseq
        qsub $ProgDir/sub_star_sensitive.sh $Assembly $File1 $File2 $OutDir
    done
done
```

#Making a combined file of Braker and CodingQuary genes with additional ORF effector candidates

```bash
GeneGff=$(ls gene_pred/codingquarry/P.fragariae/Bc16/final/final_genes_appended.gff3)
GffOrfRxLR=$(ls analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_ORFsUniq_RxLR_EER_motif_hmm.gff)
GffOrfCRN=$(ls analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc16/Bc16_ORFsUniq_CRN_hmmer.bed)
Assembly=$(ls repeat_masked/quiver_results/Bc16/filtered_contigs_repmask/polished_contigs_softmasked.fa)
OutDir=gene_pred/annotation/P.fragariae/Bc16
mkdir -p $OutDir
ProgDir=/home/adamst/git_repos/tools/gene_prediction/augustus
$ProgDir/aug_gff_add_exon.py --inp_gff $GeneGff  \
	| sed 's/\(\tCDS\t.*\)transcript_id "\(.*\)"; gene_id.*/\1ID=\2.CDS; Parent=\2/g' \
	| sed 's/\(\exon\t.*\)transcript_id "\(.*\)"; gene_id.*/\1ID=\2.exon; Parent=\2/g' \
	| sed 's/transcript_id "/ID=/g' | sed 's/";/;/g' | sed 's/ gene_id "/Parent=/g' \
	| sed -r "s/\tg/\tID=g/g" | sed 's/ID=gene/gene/g' | sed -r "s/;$//g" \
	| sed "s/\ttranscript\t.*ID=\(.*\).t.*$/\0;Parent=\1/" \
	> $OutDir/Bc16_genes_incl_ORFeffectors.gff3
# cat $GeneGff > $OutDir/10300_genes_incl_ORFeffectors.gff3
ProgDir=/home/adamst/git_repos/scripts/phytophthora/10300_analysis
$ProgDir/gff_name2id.py --gff $GffOrfRxLR > $OutDir/ORF_RxLR_parsed.gff3
$ProgDir/gff_name2id.py --gff $GffOrfCRN > $OutDir/ORF_CRN_parsed.gff3

ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
$ProgDir/add_ORF_features.pl $OutDir/ORF_RxLR_parsed.gff3 $Assembly >> $OutDir/Bc16_genes_incl_ORFeffectors.gff3
$ProgDir/add_ORF_features.pl $OutDir/ORF_CRN_parsed.gff3 $Assembly >> $OutDir/Bc16_genes_incl_ORFeffectors.gff3
# Make gene models from gff files.
ProgDir=/home/adamst/git_repos/tools/gene_prediction/codingquary
Assembly=$(ls repeat_masked/quiver_results/Bc16/filtered_contigs_repmask/polished_contigs_softmasked.fa)
$ProgDir/gff2fasta.pl $Assembly $OutDir/Bc16_genes_incl_ORFeffectors.gff3 $OutDir/Bc16_genes_incl_ORFeffectors
# Note - these fasta files have not been validated - do not use
```
