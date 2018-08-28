# Analysis of RNA-Seq data

## RNA-Seq data was downloaded from novogenes servers with the following commands

```bash
wget https://s3-eu-west-1.amazonaws.com/novogene-europe/HW/project/C101HW17030405_2.tar
mdkir -p /home/groups/harrisonlab/project_files/phytophthora_fragariae/raw_rna/novogene/
tar -C /home/groups/harrisonlab/project_files/phytophthora_fragariae/raw_rna/novogene/. -xvf /home/groups/harrisonlab/raw_data/raw_seq/P.frag/C101HW17030405_2.tar
```

## Reorganise data into timepoints: mycelium, 0hr, 24hr, 48hr and 96hr

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

## Perform qc on RNA-Seq timecourse and mycelium data

```bash
for FilePath in $(ls -d raw_rna/novogene/P.fragariae/Bc16/* | grep -v '0hr' \
| grep -v 'MD5.txt')
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

### Visualise data quality using fastqc

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
Looks okay, AT rich at early timepoints as expected from a plant genome,
rising to higher GC contents at later timepoints
```

## Align mycelium reads to FALCON assembly with STAR

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

## Align all timepoints to *Fragaria vesca* genome v1.1

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

## Gzip output files to save space on the disk. ONLY RUN THIS ONCE

```bash
for AlignDir in $(ls -d /home/groups/harrisonlab/project_files/phytophthora_fragariae/alignment/star/vesca_alignment/*/*)
do
    cat $AlignDir/star_aligmentUnmapped.out.mate1 | gzip -cf >$AlignDir/star_aligmentUnmapped.out.mate1.fq.gz
    cat $AlignDir/star_aligmentUnmapped.out.mate2 | gzip -cf >$AlignDir/star_aligmentUnmapped.out.mate2.fq.gz
done
```

## Align compressed files of unmapped reads from aligning to vesca

This star script had the following options added to the sub_star.sh script
in the ProgDir specified in the below commands:
--winAnchorMultimapNmax 200
--seedSearchStartLmax 30

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for AlignDir in $(ls -d /home/groups/harrisonlab/project_files/phytophthora_fragariae/alignment/star/vesca_alignment/*/*)
    do
        Organism=P.fragariae
        echo "$Organism - $Strain"
        printf "\n"
        File1=$AlignDir/star_aligmentUnmapped.out.mate1.fq.gz
        File2=$AlignDir/star_aligmentUnmapped.out.mate2.fq.gz
        echo $File1
        echo $File2
        Timepoint=$(echo $AlignDir | rev | cut -d '/' -f2 | rev)
        echo "$Timepoint"
        Sample_Name=$(echo $AlignDir | rev | cut -d '/' -f1 | rev)
        Jobs=$(qstat | grep 'sub_sta' | grep 'qw'| wc -l)
        while [ $Jobs -gt 1 ]
        do
            sleep 1m
            printf "."
            Jobs=$(qstat | grep 'sub_sta' | grep 'qw'| wc -l)
        done
        if [ -f /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/manual_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
        then
            Assembly=$(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/manual_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
            echo $Assembly
        elif [ -f /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
        then
            Assembly=$(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
            echo $Assembly
        elif [ -f /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
        then
            Assembly=$(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
            echo $Assembly
        else
            Assembly=$(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
            echo $Assembly
        fi
        OutDir=alignment/star/P.fragariae/$Strain/$Timepoint/$Sample_Name
        ProgDir=/home/adamst/git_repos/scripts/popgen/rnaseq
        qsub $ProgDir/sub_star_TA.sh $Assembly $File1 $File2 $OutDir
    done
done
```

##Align mycelial reads

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    Organism=P.fragariae
    echo "$Organism - $Strain"
    for FileF in $(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/qc_rna/novogene/P.fragariae/Bc16/mycelium/F/*_trim.fq.gz)
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
        if [ -f /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
        then
            Assembly=$(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
            echo $Assembly
        elif [ -f /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
        then
            Assembly=$(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
            echo $Assembly
        else
            Assembly=$(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
            echo $Assembly
        fi
        Timepoint=$(echo $FileF | rev | cut -d '/' -f3 | rev)
        echo "$Timepoint"
        Sample_Name=$(echo $FileF | rev | cut -d '/' -f1 | rev | sed 's/_1_trim.fq.gz//g')
        OutDir=alignment/star/$Organism/$Strain/$Timepoint/$Sample_Name
        mkdir -p $OutDir
        ProgDir=/home/adamst/git_repos/scripts/popgen/rnaseq
        qsub $ProgDir/sub_star_TA.sh $Assembly $FileF $FileR $OutDir
    done
done
```

## Quantification of gene models

```bash
Gff=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors_renamed.gff3
for BamFile in $(ls alignment/star/P.fragariae/Bc16/*/*/star_aligmentAligned.sortedByCoord.out.bam)
do
    OutDir=$(dirname $BamFile)
    Prefix=$(echo $BamFile | rev | cut -f2 -d '/' | rev)
    Jobs=$(qstat | grep 'sub_fea' | wc -l)
    while [ $Jobs -gt 5 ]
    do
        sleep 1m
        printf "."
        Jobs=$(qstat | grep 'sub_fea' | wc -l)
    done
    printf "\n"
    echo $Prefix
    ProgDir=/home/adamst/git_repos/tools/seq_tools/RNAseq
    qsub $ProgDir/sub_featureCounts.sh $BamFile $Gff $OutDir $Prefix
done
```

## A file was created with columns referring to experimental treatments

```bash
OutDir=alignment/star/P.fragariae/Bc16/DeSeq
mkdir -p $OutDir
printf "Sample.name\tTimepoint\tIsolate\n" > $OutDir/P.frag_Bc16_RNAseq_design.txt
# for File in $(ls alignment/star/P.cactorum/10300/Sample_*/Sample_*_featurecounts.txt); do
# Sample=$(echo $File | rev | cut -f2 -d '/' | rev)
# i=$(echo $Sample | sed 's/Sample_//g')
for i in $(seq 1 15)
do
    if [ $i == '1' ] || [ $i == '2' ] || [ $i == '3' ]
    then
        Timepoint='0hr'
    elif [ $i == '4' ] || [ $i == '5' ] || [ $i == '6' ]
    then
        Timepoint='24hr'
    elif [ $i == '7' ] || [ $i == '8' ] || [ $i == '9' ]
    then
        Timepoint='48hr'
    elif [ $i == '10' ] || [ $i == '11' ] || [ $i == '12' ]
    then
        Timepoint='96hr'
    elif [ $i == '13' ] || [ $i == '14' ] || [ $i == '15' ]
    then
        Timepoint='mycelium'
    fi
    if [ $i == '1' ] || [ $i == '2' ] || [ $i == '3' ]
    then
        Infection='mock'
    else
        Infection='Bc16'
    fi
    if [ $i == '1' ]
    then
        printf "TA.01\t$Timepoint\t$Infection\n"
    elif [ $i == '2' ]
    then
        printf "TA.02\t$Timepoint\t$Infection\n"
    elif [ $i == '3' ]
    then
        printf "TA.03\t$Timepoint\t$Infection\n"
    elif [ $i == '4' ]
    then
        printf "TA.07\t$Timepoint\t$Infection\n"
    elif [ $i == '5' ]
    then
        printf "TA.08\t$Timepoint\t$Infection\n"
    elif [ $i == '6' ]
    then
        printf "TA.09\t$Timepoint\t$Infection\n"
    elif [ $i == '7' ]
    then
        printf "TA.12\t$Timepoint\t$Infection\n"
    elif [ $i == '8' ]
    then
        printf "TA.13\t$Timepoint\t$Infection\n"
    elif [ $i == '9' ]
    then
        printf "TA.14\t$Timepoint\t$Infection\n"
    elif [ $i == '10' ]
    then
        printf "TA.18\t$Timepoint\t$Infection\n"
    elif [ $i == '11' ]
    then
        printf "TA.19\t$Timepoint\t$Infection\n"
    elif [ $i == '12' ]
    then
        printf "TA.20\t$Timepoint\t$Infection\n"
    elif [ $i == '13' ]
    then
        printf "TA.32\t$Timepoint\t$Infection\n"
    elif [ $i == '14' ]
    then
        printf "TA.34\t$Timepoint\t$Infection\n"
    elif [ $i == '15' ]
    then
        printf "TA.35\t$Timepoint\t$Infection\n"
    fi
done >> $OutDir/P.frag_Bc16_RNAseq_design.txt

# Edit header lines of feature counts files to ensure they have the treatment
# name rather than file name
OutDir=alignment/star/P.fragariae/Bc16/DeSeq
mkdir -p $OutDir
for File in $(ls alignment/star/P.fragariae/Bc16/*/*/*_featurecounts.txt)
do
    echo $File
    cp $File $OutDir/.
done
for File in $(ls $OutDir/*_featurecounts.txt)
do
    Prefix=$(echo $File | rev | cut -f1 -d '/' | rev | sed 's/_featurecounts.txt//g')
    sed -ie "s/star_aligmentAligned.sortedByCoord.out.bam/$Prefix/g" $File
done
```

## DeSeq commands

```R
#install.packages("pheatmap", Sys.getenv("R_LIBS_USER"), repos = "http://cran.case.edu" )

#install and load libraries
require("pheatmap")
require("data.table")

#load tables into a "list of lists"
qq <- lapply(list.files("alignment/star/P.fragariae/Bc16/DeSeq","*featurecounts.txt$",full.names=T,recursive=T),function(x) fread(x))

# ensure the samples column is the same name as the treament you want to use:
qq[7]

#mm <- qq%>%Reduce(function(dtf1,dtf2) inner_join(dtf1,dtf2,by=c("Geneid","Chr","Start","End","Strand","Length")), .)

#merge the "list of lists" into a single table
m <- Reduce(function(...) merge(..., all = T,by=c("Geneid","Chr","Start","End","Strand","Length")), qq)

#convert data.table to data.frame for use with DESeq2
countData <- data.frame(m[,c(1,7:(ncol(m))),with=F])
rownames(countData) <- countData[,1]
countData <- countData[,-1]

#indexes <- unique(gsub("(.*)_L00.*", "\\1", colnames(countData)))
indexes <- c("TA.07", "TA.08", "TA.09", "TA.12", "TA.13", "TA.14", "TA.18", "TA.19", "TA.20", "TA.32", "TA.34", "TA.35")

countData <- round(countData,0)
countDataSubset <- subset(countData, select = -c(1:3) )

#output countData
write.table(countDataSubset,"alignment/star/P.fragariae/Bc16/DeSeq/No_Mock_countData.txt",sep="\t",na="",quote=F)

#output gene details
write.table(m[,1:6,with=F],"alignment/star/P.fragariae/Bc16/DeSeq/No_Mock_genes.txt",sep="\t",quote=F,row.names=F)
# colnames(countData) <- sub("X","",colnames(countData)) countData <- countData[,colData$Sample]

#Running DeSeq2

#source("http://bioconductor.org/biocLite.R")
#biocLite("DESeq2")
require("DESeq2")

unorderedColData <- read.table("alignment/star/P.fragariae/Bc16/DeSeq/P.frag_Bc16_RNAseq_design.txt",header=T,sep="\t")
rownames(unorderedColData) <- unorderedColData$Sample.name
unorderedColDataSubset <- unorderedColData[indexes,]

colData <- data.frame(unorderedColDataSubset[ order(unorderedColDataSubset$Sample.name),])
unorderedData <- read.table("alignment/star/P.fragariae/Bc16/DeSeq/No_Mock_countData.txt",header=T,sep="\t")
countData <- data.frame(unorderedData[ , order(colnames(unorderedData))])
colData$Group <- paste0(colData$Isolate,'_', colData$Timepoint)
countData <- round(countData,0)

design <- ~Group
#design <- colData$Group

dds <-     DESeqDataSetFromMatrix(countData,colData,design)
#sizeFactors(dds) <- sizeFactors(estimateSizeFactors(dds, type = c("iterate")))
sizeFactors(dds) <- sizeFactors(estimateSizeFactors(dds, type = c("ratio")))
dds <- DESeq(dds, fitType="local")


#  #Run DESeq2 removing an outlier
#
#  library(DESeq2)
#  colData <- read.table("colData",header=T,sep="\t")
#  countData <- read.table("countData2",header=T,sep="\t")
#
#  colData$Group <- paste0(colData$Strain,colData$Light,colData$Time)
#  #Eliminate Frq08_DD24_rep3 sample from colData and countData
#  colData <- colData[!(colData$Sample=="Frq08_DD24_rep3"),]      
#  countData <- subset(countData, select=-Frq08_DD24_rep3)
#
#  design <- ~Group
#  dds <-  DESeqDataSetFromMatrix(countData,colData,design)
#  sizeFactors(dds) <- sizeFactors(estimateSizeFactors(dds))
#  dds <- DESeq(dds, fitType="local")
#
#Sample Distances

library("RColorBrewer")
install.packages("gplots")
library("gplots", Sys.getenv("R_LIBS_USER"))
library("ggplot2")
install.packages("ggrepel", Sys.getenv("R_LIBS_USER"), repos = "http://cran.case.edu")
library("ggrepel")

vst<-varianceStabilizingTransformation(dds)

pdf("alignment/star/P.fragariae/Bc16/DeSeq/heatmap_vst.pdf", width=12,height=12)
sampleDists<-dist(t(assay(vst)))

sampleDistMatrix <- as.matrix(sampleDists)
rownames(sampleDistMatrix) <- paste(vst$Group)
colnames(sampleDistMatrix) <- paste(vst$Group)
colours <- colorRampPalette( rev(brewer.pal(9, "Blues")) )(255)
heatmap( sampleDistMatrix,
  trace="none",  # turns off trace lines inside the heat map
  col=colours, # use on color palette defined earlier
  margins=c(12,12), # widens margins around plot
  srtCol=45,
  srtCol=45)
dev.off()

# Sample distances measured with rlog transformation:

rld <- rlog( dds )

pdf("alignment/star/P.fragariae/Bc16/DeSeq/heatmap_rld.pdf")
sampleDists <- dist( t( assay(rld) ) )
library("RColorBrewer")
sampleDistMatrix <- as.matrix( sampleDists )
rownames(sampleDistMatrix) <- paste(rld$Group)
colnames(sampleDistMatrix) <- paste(rld$Group)
colours = colorRampPalette( rev(brewer.pal(9, "Blues")) )(255)
heatmap( sampleDistMatrix, trace="none", col=colours, margins=c(12,12),srtCol=45)

#PCA plots

#vst<-varianceStabilizingTransformation(dds)
pdf("alignment/star/P.fragariae/Bc16/DeSeq/PCA_vst.pdf")
plotPCA(vst,intgroup=c("Isolate", "Timepoint"))
dev.off()

#Plot using rlog transformation:
pdf("alignment/star/P.fragariae/Bc16/DeSeq/PCA_rld.pdf")
plotPCA(rld,intgroup=c("Isolate", "Timepoint"))
dev.off()

pdf("alignment/star/P.fragariae/Bc16/DeSeq/PCA_additional.pdf")

dev.off()

#Plot using rlog transformation, showing sample names:

data <- plotPCA(rld, intgroup="Group", returnData=TRUE)
percentVar <- round(100 * attr(data, "percentVar"))

pca_plot<- ggplot(data, aes(PC1, PC2, color=Group)) +
 geom_point(size=3) +
 xlab(paste0("PC1: ",percentVar[1],"% variance")) +
 ylab(paste0("PC2: ",percentVar[2],"% variance")) + geom_text_repel(aes(label=colnames(rld)))
 coord_fixed()

ggsave("alignment/star/P.fragariae/Bc16/DeSeq/PCA_sample_names.pdf", pca_plot, dpi=300, height=10, width=12)

#Analysis of gene expression

#24hr vs mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_24hr","Bc16_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
#Settings used: upregulated: min. 2x fold change, ie. log2foldchange min 1.
#               downregulated: min. 0.5x fold change, ie. log2foldchange max -1.
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
# No threshold
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"alignment/star/P.fragariae/Bc16/DeSeq/Bc16_24hr_vs_Bc16_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"alignment/star/P.fragariae/Bc16/DeSeq/Bc16_24hr_vs_Bc16_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"alignment/star/P.fragariae/Bc16/DeSeq/Bc16_24hr_vs_Bc16_mycelium_down.txt",sep="\t",na="",quote=F)

#48hr vs mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_48hr","Bc16_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
#Settings used: upregulated: min. 2x fold change, ie. log2foldchange min 1.
#               downregulated: min. 0.5x fold change, ie. log2foldchange max -1.
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
# No threshold
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"alignment/star/P.fragariae/Bc16/DeSeq/Bc16_48hr_vs_Bc16_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"alignment/star/P.fragariae/Bc16/DeSeq/Bc16_48hr_vs_Bc16_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"alignment/star/P.fragariae/Bc16/DeSeq/Bc16_48hr_vs_Bc16_mycelium_down.txt",sep="\t",na="",quote=F)

#96hr vs mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_96hr","Bc16_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
#Settings used: upregulated: min. 2x fold change, ie. log2foldchange min 1.
#               downregulated: min. 0.5x fold change, ie. log2foldchange max -1.
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
# No threshold
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"alignment/star/P.fragariae/Bc16/DeSeq/Bc16_96hr_vs_Bc16_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"alignment/star/P.fragariae/Bc16/DeSeq/Bc16_96hr_vs_Bc16_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"alignment/star/P.fragariae/Bc16/DeSeq/Bc16_96hr_vs_Bc16_mycelium_down.txt",sep="\t",na="",quote=F)

#Make a table of raw counts, normalised counts and fpkm values:

raw_counts <- data.frame(counts(dds, normalized=FALSE))
colnames(raw_counts) <- paste(colData$Group)
write.table(raw_counts,"alignment/star/P.fragariae/Bc16/DeSeq/raw_counts.txt",sep="\t",na="",quote=F)
norm_counts <- data.frame(counts(dds, normalized=TRUE))
colnames(norm_counts) <- paste(colData$Group)
write.table(norm_counts,"alignment/star/P.fragariae/Bc16/DeSeq/normalised_counts.txt",sep="\t",na="",quote=F)

library(Biostrings)
library(naturalsort)
mygenes <- readDNAStringSet("gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors_renamed.cdna.fasta")
t1 <- counts(dds)
t1 <- mygenes[rownames(t1)]
rowRanges(dds) <- GRanges(t1@ranges@NAMES,t1@ranges)


# robust may be better set at fasle to normalise based on total counts rather than 'library normalisation factors'
fpkm_counts <- data.frame(fpkm(dds, robust = TRUE))
colnames(fpkm_counts) <- paste(colData$Group)
write.table(fpkm_counts,"alignment/star/P.fragariae/Bc16/DeSeq/fpkm_norm_counts.txt",sep="\t",na="",quote=F)
fpkm_counts <- data.frame(fpkm(dds, robust = FALSE))
colnames(fpkm_counts) <- paste(colData$Group)
write.table(fpkm_counts,"alignment/star/P.fragariae/Bc16/DeSeq/fpkm_counts.txt",sep="\t",na="",quote=F)
```

## Inital analysis of tables of DEGs

```bash
RxLR_Names_Bc16=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_Total_RxLR_motif_hmm_renamed.txt
CRN_Names_Bc16=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc16/Bc16_final_CRN_renamed.txt
ApoP_Names_Bc16=analysis/ApoplastP/P.fragariae/Bc16/Bc16_Total_ApoplastP_renamed.txt
for File in $(ls alignment/star/P.fragariae/Bc16/DeSeq/Bc16*.txt)
do
    Assessment=$(basename $File | sed "s/.txt//g")
    echo $Assessment
    echo "Total number of genes in dataset:"
    cat $File | grep -v 'baseMean' | wc -l
    echo "Total number of RxLRs in dataset:"
    RxLR_File=$(echo $File | sed "s/.txt/_RxLRs.txt/g")
    cat $File | head -n 1 > $RxLR_File
    cat $File | grep -w -f $RxLR_Names_Bc16 >> $RxLR_File
    cat $RxLR_File | tail -n +2 | wc -l
    echo "Total number of CRNs in dataset:"
    CRN_File=$(echo $File | sed "s/.txt/_CRNs.txt/g")
    cat $File | head -n 1 > $CRN_File
    cat $File | grep -w -f $CRN_Names_Bc16 >> $CRN_File
    cat $CRN_File | tail -n +2 | wc -l
    echo "Total number of Apoplastic effectors in dataset:"
    ApoP_File=$(echo $File | sed "s/.txt/_ApoP.txt/g")
    cat $File | head -n 1 > $ApoP_File
    cat $File | grep -w -f $ApoP_Names_Bc16 >> $ApoP_File
    cat $ApoP_File | tail -n +2 | wc -l
done
```

```
Bc16_24hr_vs_Bc16_mycelium_down
Total number of genes in dataset:
3,422
Total number of RxLRs in dataset:
109
Total number of CRNs in dataset:
9
Total number of Apoplastic effectors in dataset:
348
Bc16_24hr_vs_Bc16_mycelium
Total number of genes in dataset:
7,809
Total number of RxLRs in dataset:
247
Total number of CRNs in dataset:
20
Total number of Apoplastic effectors in dataset:
714
Bc16_24hr_vs_Bc16_mycelium_up
Total number of genes in dataset:
2,124
Total number of RxLRs in dataset:
107
Total number of CRNs in dataset:
3
Total number of Apoplastic effectors in dataset:
309
Bc16_48hr_vs_Bc16_mycelium_down
Total number of genes in dataset:
3,471
Total number of RxLRs in dataset:
126
Total number of CRNs in dataset:
17
Total number of Apoplastic effectors in dataset:
415
Bc16_48hr_vs_Bc16_mycelium
Total number of genes in dataset:
9,849
Total number of RxLRs in dataset:
316
Total number of CRNs in dataset:
36
Total number of Apoplastic effectors in dataset:
976
Bc16_48hr_vs_Bc16_mycelium_up
Total number of genes in dataset:
2,618
Total number of RxLRs in dataset:
128
Total number of CRNs in dataset:
2
Total number of Apoplastic effectors in dataset:
445
Bc16_96hr_vs_Bc16_mycelium_down
Total number of genes in dataset:
2,531
Total number of RxLRs in dataset:
106
Total number of CRNs in dataset:
8
Total number of Apoplastic effectors in dataset:
364
Bc16_96hr_vs_Bc16_mycelium
Total number of genes in dataset:
10,217
Total number of RxLRs in dataset:
337
Total number of CRNs in dataset:
26
Total number of Apoplastic effectors in dataset:
1,080
Bc16_96hr_vs_Bc16_mycelium_up
Total number of genes in dataset:
3,301
Total number of RxLRs in dataset:
141
Total number of CRNs in dataset:
5
Total number of Apoplastic effectors in dataset:
553
```

## Draw venn diagrams of differentially expressed genes

## All genes

### All DEGs

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
inp1=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_24hr_vs_Bc16_mycelium.txt
inp2=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_48hr_vs_Bc16_mycelium.txt
inp3=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_96hr_vs_Bc16_mycelium.txt
OutDir=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_all_DEGs.tsv
$ProgDir/parse_RNA-Seq.py --input_1 $inp1 --input_2 $inp2 --input_3 $inp3 --out_dir $OutDir
```

### Upregulated DEGs

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
inp1=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_24hr_vs_Bc16_mycelium_up.txt
inp2=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_48hr_vs_Bc16_mycelium_up.txt
inp3=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_96hr_vs_Bc16_mycelium_up.txt
OutDir=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_up_DEGs.tsv
$ProgDir/parse_RNA-Seq.py --input_1 $inp1 --input_2 $inp2 --input_3 $inp3 --out_dir $OutDir
```

### Downregulated DEGs

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
inp1=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_24hr_vs_Bc16_mycelium_down.txt
inp2=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_48hr_vs_Bc16_mycelium_down.txt
inp3=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_96hr_vs_Bc16_mycelium_down.txt
OutDir=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_down_DEGs.tsv
$ProgDir/parse_RNA-Seq.py --input_1 $inp1 --input_2 $inp2 --input_3 $inp3 --out_dir $OutDir
```

### Venn diagrams

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
WorkDir=alignment/star/P.fragariae/Bc16/DeSeq
$ProgDir/BC-16_All_DEGs_venn_diag.r --inp $WorkDir/Bc16_all_DEGs.tsv --out $WorkDir/Bc16_all_DEGs.pdf
$ProgDir/BC-16_All_DEGs_venn_diag.r --inp $WorkDir/Bc16_up_DEGs.tsv --out $WorkDir/Bc16_up_DEGs.pdf
$ProgDir/BC-16_All_DEGs_venn_diag.r --inp $WorkDir/Bc16_down_DEGs.tsv --out $WorkDir/Bc16_down_DEGs.pdf
```

## RxLRs

### All DEGs

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
inp1=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_24hr_vs_Bc16_mycelium_RxLRs.txt
inp2=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_48hr_vs_Bc16_mycelium_RxLRs.txt
inp3=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_96hr_vs_Bc16_mycelium_RxLRs.txt
OutDir=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_all_RxLRs_DEGs.tsv
$ProgDir/parse_RNA-Seq.py --input_1 $inp1 --input_2 $inp2 --input_3 $inp3 --out_dir $OutDir
```

### Upregulated DEGs

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
inp1=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_24hr_vs_Bc16_mycelium_up_RxLRs.txt
inp2=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_48hr_vs_Bc16_mycelium_up_RxLRs.txt
inp3=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_96hr_vs_Bc16_mycelium_up_RxLRs.txt
OutDir=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_up_RxLRs_DEGs.tsv
$ProgDir/parse_RNA-Seq.py --input_1 $inp1 --input_2 $inp2 --input_3 $inp3 --out_dir $OutDir
```

### Downregulated DEGs

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
inp1=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_24hr_vs_Bc16_mycelium_down_RxLRs.txt
inp2=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_48hr_vs_Bc16_mycelium_down_RxLRs.txt
inp3=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_96hr_vs_Bc16_mycelium_down_RxLRs.txt
OutDir=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_down_RxLRs_DEGs.tsv
$ProgDir/parse_RNA-Seq.py --input_1 $inp1 --input_2 $inp2 --input_3 $inp3 --out_dir $OutDir
```

### Venn diagrams

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
WorkDir=alignment/star/P.fragariae/Bc16/DeSeq
$ProgDir/BC-16_All_DEGs_venn_diag.r --inp $WorkDir/Bc16_all_RxLRs_DEGs.tsv --out $WorkDir/Bc16_all_RxLRs_DEGs.pdf
$ProgDir/BC-16_All_DEGs_venn_diag.r --inp $WorkDir/Bc16_up_RxLRs_DEGs.tsv --out $WorkDir/Bc16_up_RxLRs_DEGs.pdf
$ProgDir/BC-16_All_DEGs_venn_diag.r --inp $WorkDir/Bc16_down_RxLRs_DEGs.tsv --out $WorkDir/Bc16_down_RxLRs_DEGs.pdf
```

## CRNs

### All DEGs

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
inp1=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_24hr_vs_Bc16_mycelium_CRNs.txt
inp2=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_48hr_vs_Bc16_mycelium_CRNs.txt
inp3=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_96hr_vs_Bc16_mycelium_CRNs.txt
OutDir=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_all_CRNs_DEGs.tsv
$ProgDir/parse_RNA-Seq.py --input_1 $inp1 --input_2 $inp2 --input_3 $inp3 --out_dir $OutDir
```

### Upregulated DEGs

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
inp1=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_24hr_vs_Bc16_mycelium_up_CRNs.txt
inp2=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_48hr_vs_Bc16_mycelium_up_CRNs.txt
inp3=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_96hr_vs_Bc16_mycelium_up_CRNs.txt
OutDir=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_up_CRNs_DEGs.tsv
$ProgDir/parse_RNA-Seq.py --input_1 $inp1 --input_2 $inp2 --input_3 $inp3 --out_dir $OutDir
```

### Downregulated DEGs

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
inp1=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_24hr_vs_Bc16_mycelium_down_CRNs.txt
inp2=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_48hr_vs_Bc16_mycelium_down_CRNs.txt
inp3=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_96hr_vs_Bc16_mycelium_down_CRNs.txt
OutDir=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_down_CRNs_DEGs.tsv
$ProgDir/parse_RNA-Seq.py --input_1 $inp1 --input_2 $inp2 --input_3 $inp3 --out_dir $OutDir
```

### Venn diagrams

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
WorkDir=alignment/star/P.fragariae/Bc16/DeSeq
$ProgDir/BC-16_All_DEGs_venn_diag.r --inp $WorkDir/Bc16_all_CRNs_DEGs.tsv --out $WorkDir/Bc16_all_CRNs_DEGs.pdf
$ProgDir/BC-16_All_DEGs_venn_diag.r --inp $WorkDir/Bc16_up_CRNs_DEGs.tsv --out $WorkDir/Bc16_up_CRNs_DEGs.pdf
$ProgDir/BC-16_All_DEGs_venn_diag.r --inp $WorkDir/Bc16_down_CRNs_DEGs.tsv --out $WorkDir/Bc16_down_CRNs_DEGs.pdf
```

## Apoplastic effectors

### All DEGs

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
inp1=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_24hr_vs_Bc16_mycelium_ApoP.txt
inp2=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_48hr_vs_Bc16_mycelium_ApoP.txt
inp3=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_96hr_vs_Bc16_mycelium_ApoP.txt
OutDir=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_all_ApoP_DEGs.tsv
$ProgDir/parse_RNA-Seq.py --input_1 $inp1 --input_2 $inp2 --input_3 $inp3 --out_dir $OutDir
```

### Upregulated DEGs

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
inp1=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_24hr_vs_Bc16_mycelium_up_ApoP.txt
inp2=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_48hr_vs_Bc16_mycelium_up_ApoP.txt
inp3=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_96hr_vs_Bc16_mycelium_up_ApoP.txt
OutDir=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_up_ApoP_DEGs.tsv
$ProgDir/parse_RNA-Seq.py --input_1 $inp1 --input_2 $inp2 --input_3 $inp3 --out_dir $OutDir
```

### Downregulated DEGs

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
inp1=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_24hr_vs_Bc16_mycelium_down_ApoP.txt
inp2=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_48hr_vs_Bc16_mycelium_down_ApoP.txt
inp3=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_96hr_vs_Bc16_mycelium_down_ApoP.txt
OutDir=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_down_ApoP_DEGs.tsv
$ProgDir/parse_RNA-Seq.py --input_1 $inp1 --input_2 $inp2 --input_3 $inp3 --out_dir $OutDir
```

### Venn diagrams

```bash
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
WorkDir=alignment/star/P.fragariae/Bc16/DeSeq
$ProgDir/BC-16_All_DEGs_venn_diag.r --inp $WorkDir/Bc16_all_ApoP_DEGs.tsv --out $WorkDir/Bc16_all_ApoP_DEGs.pdf
$ProgDir/BC-16_All_DEGs_venn_diag.r --inp $WorkDir/Bc16_up_ApoP_DEGs.tsv --out $WorkDir/Bc16_up_ApoP_DEGs.pdf
$ProgDir/BC-16_All_DEGs_venn_diag.r --inp $WorkDir/Bc16_down_ApoP_DEGs.tsv --out $WorkDir/Bc16_down_ApoP_DEGs.pdf
```

## Extract fasta file of all DEGs for BLAST analysis

```bash
DEGFile=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_all_DEGs.tsv
DEGNames=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_all_DEGs_names.txt
Genes=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors_renamed.cds.fasta
DEGFasta=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_all_DEGs.fa
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
$ProgDir/extract_DEG_Names.py --input $DEGFile --output $DEGNames
ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
$ProgDir/extract_from_fasta.py --fasta $Genes --headers $DEGNames > $DEGFasta
```

New data arrived on BC-1 & NOV-9, three different methods will be used to
analyse expression differences by three different methods.

Method #1: Differential expression between isolates - Align all RNA-Seq to a
single genome, then use DeSeq2 to call DEGs and pull out gene IDs from the text
file. Do this on genomes of BC-16, BC-1 & NOV-9.

Method #2: For different differential expression by gene ID - Align RNA-Seq data
to the BC-16 reference genome, then call DEGs using mycelial reads from the same
isolate. Then compare between reference genomes by orthogroup ID.

Method #1 will give candidates for avirulence genes, whereas #2 will provide
differently differentially expressed genes.

## New RNA-Seq data was downloaded from novogenes servers with the following commands

```bash
mkdir -p /home/scratch/adamst/rna_seq/05012018
cd /home/scratch/adamst/rna_seq/05012018
wget https://s3-eu-west-1.amazonaws.com/novogene-europe/HW/project/C101HW17030405_20180102_5_Yvad6z.tar
tar -xf /home/scratch/adamst/rna_seq/05012018/C101HW17030405_20180102_5_Yvad6z.tar
```

## Reorganise raw data

```bash
mkdir -p P.fragariae/Bc1/48hr/F/
mkdir -p P.fragariae/Bc1/mycelium/F/
mkdir -p P.fragariae/Bc1/48hr/R/
mkdir -p P.fragariae/Bc1/mycelium/R/
mkdir -p P.fragariae/Nov9/72hr/F/
mkdir -p P.fragariae/Nov9/mycelium/F/
mkdir -p P.fragariae/Nov9/72hr/R/
mkdir -p P.fragariae/Nov9/mycelium/R/
mv C101HW17030405/raw_data/TA_B_P1_1.fq.gz P.fragariae/Bc1/48hr/F/.
mv C101HW17030405/raw_data/TA_B_P2_1.fq.gz P.fragariae/Bc1/48hr/F/.
mv C101HW17030405/raw_data/TA_B_P3_1.fq.gz P.fragariae/Bc1/48hr/F/.
mv C101HW17030405/raw_data/TA_B_M1_1.fq.gz P.fragariae/Bc1/mycelium/F/.
mv C101HW17030405/raw_data/TA_B_M2_1.fq.gz P.fragariae/Bc1/mycelium/F/.
mv C101HW17030405/raw_data/TA_B_M3_1.fq.gz P.fragariae/Bc1/mycelium/F/.
mv C101HW17030405/raw_data/TA_B_P1_2.fq.gz P.fragariae/Bc1/48hr/R/.
mv C101HW17030405/raw_data/TA_B_P2_2.fq.gz P.fragariae/Bc1/48hr/R/.
mv C101HW17030405/raw_data/TA_B_P3_2.fq.gz P.fragariae/Bc1/48hr/R/.
mv C101HW17030405/raw_data/TA_B_M1_2.fq.gz P.fragariae/Bc1/mycelium/R/.
mv C101HW17030405/raw_data/TA_B_M2_2.fq.gz P.fragariae/Bc1/mycelium/R/.
mv C101HW17030405/raw_data/TA_B_M3_2.fq.gz P.fragariae/Bc1/mycelium/R/.
mv C101HW17030405/raw_data/TA_NO_P1_1.fq.gz P.fragariae/Nov9/72hr/F/.
mv C101HW17030405/raw_data/TA_NO_P2_1.fq.gz P.fragariae/Nov9/72hr/F/.
mv C101HW17030405/raw_data/TA_NO_P3_1.fq.gz P.fragariae/Nov9/72hr/F/.
mv C101HW17030405/raw_data/TA_NO_M1_1.fq.gz P.fragariae/Nov9/mycelium/F/.
mv C101HW17030405/raw_data/TA_NO_M2_1.fq.gz P.fragariae/Nov9/mycelium/F/.
mv C101HW17030405/raw_data/TA_NO_M5_1.fq.gz P.fragariae/Nov9/mycelium/F/.
mv C101HW17030405/raw_data/TA_NO_P1_2.fq.gz P.fragariae/Nov9/72hr/R/.
mv C101HW17030405/raw_data/TA_NO_P2_2.fq.gz P.fragariae/Nov9/72hr/R/.
mv C101HW17030405/raw_data/TA_NO_P3_2.fq.gz P.fragariae/Nov9/72hr/R/.
mv C101HW17030405/raw_data/TA_NO_M1_2.fq.gz P.fragariae/Nov9/mycelium/R/.
mv C101HW17030405/raw_data/TA_NO_M2_2.fq.gz P.fragariae/Nov9/mycelium/R/.
mv C101HW17030405/raw_data/TA_NO_M5_2.fq.gz P.fragariae/Nov9/mycelium/R/.
mv C101HW17030405/raw_data/MD5.txt .
```

## Perform qc on RNA-Seq timecourse and mycelium data

```bash
for FilePath in $(ls -d /home/scratch/adamst/rna_seq/05012018/P.fragariae/*/*/)
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
        qsub $ProgDir/rna_qc_fastq-mcf_2.sh $FileF $FileR $IlluminaAdapters RNA
    done
done

mv qc_rna/Bc1/ qc_rna/novogene/P.fragariae/.
mv qc_rna/Nov9/ qc_rna/novogene/P.fragariae/.
```

### Visualise data quality using fastqc

Only submit three jobs at a time, copying 30 files is too much!

```bash
for RawData in $(ls qc_rna/novogene/P.fragariae/*/*/*/* | grep -v 'Bc16')
do
    echo $RawData
    Jobs=$(qstat -u "*" | grep 'run_fastqc' | wc -l)
    while [ $Jobs -gt 3 ]
    do
        sleep 1m
        printf "."
        Jobs=$(qstat -u "*" | grep 'run_fastqc' | wc -l)
    done
    ProgDir=/home/adamst/git_repos/tools/seq_tools/dna_qc
    qsub $ProgDir/run_fastqc.sh $RawData
done
```

```
All seem okay to me
```

## Align mycelial reads to assemblies

```bash
for Strain in Bc1 Nov9 Bc16
do
    if [ -f /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
    then
        Assembly=$(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    elif [ -f /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
    then
        Assembly=$(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    else
        Assembly=$(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    fi
    Organism=P.fragariae
    echo "$Organism - $Strain"
    for FileF in $(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/qc_rna/novogene/P.fragariae/*/mycelium/F/*_trim.fq.gz | grep -e 'Nov9' -e 'Bc1' | grep -v 'Bc16')
    do
        Jobs=$(qstat | grep 'sub_sta' | grep 'qw' | wc -l)
        while [ $Jobs -gt 1 ]
        do
            sleep 1m
            printf "."
            Jobs=$(qstat | grep 'sub_sta' | grep 'qw' | wc -l)
        done
        printf "\n"
        FileR=$(echo $FileF | sed 's&/F/&/R/&g' | sed 's/_1/_2/g')
        echo $FileF
        echo $FileR
        Timepoint=$(echo $FileF | rev | cut -d '/' -f3 | rev)
        echo "$Timepoint"
        Sample_Name=$(echo $FileF | rev | cut -d '/' -f1 | rev | sed 's/_1_trim.fq.gz//g')
        OutDir=alignment/star/$Organism/$Strain/$Timepoint/$Sample_Name
        ProgDir=/home/adamst/git_repos/scripts/popgen/rnaseq
        qsub $ProgDir/sub_star_TA.sh $Assembly $FileF $FileR $OutDir
    done
done
```

## Align all timepoints to *Fragaria vesca* genome v1.1

```bash
for FileF in $(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/qc_rna/novogene/P.fragariae/*/*/F/*_trim.fq.gz | grep -e "Bc1" -e "Nov9" | grep -v "Bc16" | grep -v "mycelium")
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
    OutDir=alignment/star/vesca_alignment/set2/$Timepoint/$Sample_Name
    ProgDir=/home/adamst/git_repos/scripts/popgen/rnaseq
    Assembly=/home/sobczm/popgen/rnaseq/fvesca_v1.1_all.fa
    GFF=/home/sobczm/popgen/rnaseq/Fragaria_vesca_v1.1.a2.gff3
    qsub $ProgDir/sub_star_sensitive.sh $Assembly $FileF $FileR $OutDir $GFF
done
```

## Gzip output files to save space on the disk and allow star to run correctly downstream. ONLY RUN THIS ONCE

```bash
for AlignDir in $(ls -d /home/groups/harrisonlab/project_files/phytophthora_fragariae/alignment/star/vesca_alignment/set2/*/*)
do
    cat $AlignDir/star_aligmentUnmapped.out.mate1 | gzip -cf > $AlignDir/star_aligmentUnmapped.out.mate1.fq.gz
    cat $AlignDir/star_aligmentUnmapped.out.mate2 | gzip -cf > $AlignDir/star_aligmentUnmapped.out.mate2.fq.gz
done
```

## Align compressed files of unmapped reads from aligning to vesca

This star script had the following options added to the sub_star.sh script in
the ProgDir specified in the below commands:
--winAnchorMultimapNmax 200
--seedSearchStartLmax 30

BC-16 RNA-Seq data

```bash
for Strain in Bc1 Nov9
do
    if [ -f /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
    then
        Assembly=$(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    elif [ -f /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
    then
        Assembly=$(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    else
        Assembly=$(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    fi
    Organism=P.fragariae
    echo "$Organism - $Strain"
    for AlignDir in $(ls -d /home/groups/harrisonlab/project_files/phytophthora_fragariae/alignment/star/vesca_alignment/*hr/*)
    do
        Organism=P.fragariae
        echo "$Organism - $Strain"
        printf "\n"
        File1=$AlignDir/star_aligmentUnmapped.out.mate1.fq.gz
        File2=$AlignDir/star_aligmentUnmapped.out.mate2.fq.gz
        echo $File1
        echo $File2
        Timepoint=$(echo $AlignDir | rev | cut -d '/' -f2 | rev)
        echo "$Timepoint"
        Sample_Name=$(echo $AlignDir | rev | cut -d '/' -f1 | rev)
        Jobs=$(qstat | grep 'sub_sta' | grep 'qw' | wc -l)
        while [ $Jobs -gt 1 ]
        do
            sleep 1m
            printf "."
            Jobs=$(qstat | grep 'sub_sta' | grep 'qw' | wc -l)
        done
        OutDir=alignment/star/P.fragariae/$Strain/$Timepoint/$Sample_Name
        ProgDir=/home/adamst/git_repos/scripts/popgen/rnaseq
        qsub $ProgDir/sub_star_TA.sh $Assembly $File1 $File2 $OutDir
    done
done
```

BC-1 and NOV-9 RNA-Seq data

```bash
for Strain in Bc1 Nov9 Bc16
do
    if [ -f /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
    then
        Assembly=$(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    elif [ -f /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
    then
        Assembly=$(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    else
        Assembly=$(ls /home/groups/harrisonlab/project_files/phytophthora_fragariae/repeat_masked/quiver_results/polished/filtered_contigs_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    fi
    Organism=P.fragariae
    echo "$Organism - $Strain"
    for AlignDir in $(ls -d /home/groups/harrisonlab/project_files/phytophthora_fragariae/alignment/star/vesca_alignment/set2/*/*)
    do
        Organism=P.fragariae
        echo "$Organism - $Strain"
        printf "\n"
        File1=$AlignDir/star_aligmentUnmapped.out.mate1.fq.gz
        File2=$AlignDir/star_aligmentUnmapped.out.mate2.fq.gz
        echo $File1
        echo $File2
        Timepoint=$(echo $AlignDir | rev | cut -d '/' -f2 | rev)
        echo "$Timepoint"
        Sample_Name=$(echo $AlignDir | rev | cut -d '/' -f1 | rev)
        Jobs=$(qstat | grep 'sub_sta' | grep 'qw' | wc -l)
        while [ $Jobs -gt 1 ]
        do
            sleep 1m
            printf "."
            Jobs=$(qstat | grep 'sub_sta' | grep 'qw' | wc -l)
        done
        OutDir=alignment/star/P.fragariae/$Strain/$Timepoint/$Sample_Name
        ProgDir=/home/adamst/git_repos/scripts/popgen/rnaseq
        qsub $ProgDir/sub_star_TA.sh $Assembly $File1 $File2 $OutDir
    done
done
```

## Quantification of gene models

```bash
for Strain in Bc16 Bc1 Nov9
do
    for BamFile in $(ls alignment/star/P.fragariae/$Strain/*/*/star_aligmentAligned.sortedByCoord.out.bam | grep -v "0hr")
    do
        Gff=gene_pred/annotation/P.fragariae/$Strain/*_genes_incl_ORFeffectors_renamed.gff3
        OutDir=analysis/DeSeq
        mkdir -p $OutDir
        Prefix="$Strain"_"$(echo $BamFile | rev | cut -f2 -d '/' | rev)"
        Jobs=$(qstat | grep 'sub_fea' | wc -l)
        while [ $Jobs -gt 5 ]
        do
            sleep 1m
            printf "."
            Jobs=$(qstat | grep 'sub_fea' | wc -l)
        done
        printf "\n"
        echo $Prefix
        ProgDir=/home/adamst/git_repos/tools/seq_tools/RNAseq
        qsub $ProgDir/sub_featureCounts.sh $BamFile $Gff $OutDir $Prefix
    done
done
```

## Create files with columns referring to experimental treatments

```bash
#Method 1
for OutDir in analysis/DeSeq/Method_1/Bc1 analysis/DeSeq/Method_1/Bc16 analysis/DeSeq/Method_1/Nov9
do
    mkdir -p $OutDir
    printf "Sample.name\tTimepoint\tIsolate\n" > $OutDir/P.frag_method1_RNAseq_design.txt
    for i in $(seq 1 15)
    do
        if [ $i == '1' ] || [ $i == '2' ] || [ $i == '3' ]
        then
            Timepoint='24hr'
            Infection='Bc16'
        elif [ $i == '4' ] || [ $i == '5' ] || [ $i == '6' ]
        then
            Timepoint='48hr'
            Infection='Bc16'
        elif [ $i == '7' ] || [ $i == '8' ] || [ $i == '9' ]
        then
            Timepoint='48hr'
            Infection='Bc1'
        elif [ $i == '10' ] || [ $i == '11' ] || [ $i == '12' ]
        then
            Timepoint='72hr'
            Infection='Nov9'
        elif [ $i == '13' ] || [ $i == '14' ] || [ $i == '15' ]
        then
            Timepoint='96hr'
            Infection='Bc16'
        fi
        if [ $i == '1' ]
        then
            printf "TA-07\t$Timepoint\t$Infection\n"
        elif [ $i == '2' ]
        then
            printf "TA-08\t$Timepoint\t$Infection\n"
        elif [ $i == '3' ]
        then
            printf "TA-09\t$Timepoint\t$Infection\n"
        elif [ $i == '4' ]
        then
            printf "TA-12\t$Timepoint\t$Infection\n"
        elif [ $i == '5' ]
        then
            printf "TA-13\t$Timepoint\t$Infection\n"
        elif [ $i == '6' ]
        then
            printf "TA-14\t$Timepoint\t$Infection\n"
        elif [ $i == '7' ]
        then
            printf "TA_B_P1\t$Timepoint\t$Infection\n"
        elif [ $i == '8' ]
        then
            printf "TA_B_P2\t$Timepoint\t$Infection\n"
        elif [ $i == '9' ]
        then
            printf "TA_B_P3\t$Timepoint\t$Infection\n"
        elif [ $i == '10' ]
        then
            printf "TA_NO_P1\t$Timepoint\t$Infection\n"
        elif [ $i == '11' ]
        then
            printf "TA_NO_P2\t$Timepoint\t$Infection\n"
        elif [ $i == '12' ]
        then
            printf "TA_NO_P3\t$Timepoint\t$Infection\n"
        elif [ $i == '13' ]
        then
            printf "TA-18\t$Timepoint\t$Infection\n"
        elif [ $i == '14' ]
        then
            printf "TA-19\t$Timepoint\t$Infection\n"
        elif [ $i == '15' ]
        then
            printf "TA-20\t$Timepoint\t$Infection\n"
        fi
    done >> $OutDir/P.frag_method1_RNAseq_design.txt
done

# Edit headers lines of featurecounts files to ensure they have the treatment
# name rather than the file name
OutDir=analysis/DeSeq/Method_1
for Strain in Bc1 Bc16 Nov9
do
    for File in $(ls analysis/DeSeq/"$Strain"_*_featurecounts.txt | grep -v "_M" | grep -v "TA-3")
    do
        echo $File
        cp $File $OutDir/$Strain/.
    done
    for File in $(ls $OutDir/$Strain/*_featurecounts.txt)
    do
        Prefix=$(echo $File | rev | cut -f1 -d '/' | rev | sed 's/_featurecounts.txt//g')
        sed -ie "s/star_aligmentAligned.sortedByCoord.out.bam/$Prefix/g" $File
    done
done

#Method 2

for OutDir in analysis/DeSeq/Method_2/Bc16 analysis/DeSeq/Method_2/Bc1 analysis/DeSeq/Method_2/Nov9
do
    mkdir -p $OutDir
    printf "Sample.name\tTimepoint\tIsolate\n" > $OutDir/P.frag_method2_RNAseq_design.txt
    for i in $(seq 1 24)
    do
        if [ $i == '1' ] || [ $i == '2' ] || [ $i == '3' ]
        then
            Timepoint='24hr'
            Infection='Bc16'
        elif [ $i == '4' ] || [ $i == '5' ] || [ $i == '6' ]
        then
            Timepoint='48hr'
            Infection='Bc16'
        elif [ $i == '7' ] || [ $i == '8' ] || [ $i == '9' ]
        then
            Timepoint='48hr'
            Infection='Bc1'
        elif [ $i == '10' ] || [ $i == '11' ] || [ $i == '12' ]
        then
            Timepoint='72hr'
            Infection='Nov9'
        elif [ $i == '13' ] || [ $i == '14' ] || [ $i == '15' ]
        then
            Timepoint='96hr'
            Infection='Bc16'
        elif [ $i == '16' ] || [ $i == '17' ] || [ $i == '18' ]
        then
            Timepoint='mycelium'
            Infection='Bc16'
        elif [ $i == '19' ] || [ $i == '20' ] || [ $i == '21' ]
        then
            Timepoint='mycelium'
            Infection='Bc1'
        elif [ $i == '22' ] || [ $i == '23' ] || [ $i == '24' ]
        then
            Timepoint='mycelium'
            Infection='Nov9'
        fi
        if [ $i == '1' ]
        then
            printf "TA-07\t$Timepoint\t$Infection\n"
        elif [ $i == '2' ]
        then
            printf "TA-08\t$Timepoint\t$Infection\n"
        elif [ $i == '3' ]
        then
            printf "TA-09\t$Timepoint\t$Infection\n"
        elif [ $i == '4' ]
        then
            printf "TA-12\t$Timepoint\t$Infection\n"
        elif [ $i == '5' ]
        then
            printf "TA-13\t$Timepoint\t$Infection\n"
        elif [ $i == '6' ]
        then
            printf "TA-14\t$Timepoint\t$Infection\n"
        elif [ $i == '7' ]
        then
            printf "TA_B_P1\t$Timepoint\t$Infection\n"
        elif [ $i == '8' ]
        then
            printf "TA_B_P2\t$Timepoint\t$Infection\n"
        elif [ $i == '9' ]
        then
            printf "TA_B_P3\t$Timepoint\t$Infection\n"
        elif [ $i == '10' ]
        then
            printf "TA_NO_P1\t$Timepoint\t$Infection\n"
        elif [ $i == '11' ]
        then
            printf "TA_NO_P2\t$Timepoint\t$Infection\n"
        elif [ $i == '12' ]
        then
            printf "TA_NO_P3\t$Timepoint\t$Infection\n"
        elif [ $i == '13' ]
        then
            printf "TA-18\t$Timepoint\t$Infection\n"
        elif [ $i == '14' ]
        then
            printf "TA-19\t$Timepoint\t$Infection\n"
        elif [ $i == '15' ]
        then
            printf "TA-20\t$Timepoint\t$Infection\n"
        elif [ $i == '16' ]
        then
            printf "TA-32\t$Timepoint\t$Infection\n"
        elif [ $i == '17' ]
        then
            printf "TA-34\t$Timepoint\t$Infection\n"
        elif [ $i == '18' ]
        then
            printf "TA-35\t$Timepoint\t$Infection\n"
        elif [ $i == '19' ]
        then
            printf "TA_B_M1\t$Timepoint\t$Infection\n"
        elif [ $i == '20' ]
        then
            printf "TA_B_M2\t$Timepoint\t$Infection\n"
        elif [ $i == '21' ]
        then
            printf "TA_B_M3\t$Timepoint\t$Infection\n"
        elif [ $i == '22' ]
        then
            printf "TA_NO_M1\t$Timepoint\t$Infection\n"
        elif [ $i == '23' ]
        then
            printf "TA_NO_M2\t$Timepoint\t$Infection\n"
        elif [ $i == '24' ]
        then
            printf "TA_NO_M5\t$Timepoint\t$Infection\n"
        fi
    done >> $OutDir/P.frag_method2_RNAseq_design.txt
done

# Edit headers lines of featurecounts files to ensure they have the treatment
# name rather than the file name
for Strain in Bc1 Bc16 Nov9
do
    OutDir=analysis/DeSeq/Method_2/$Strain
    for File in $(ls analysis/DeSeq/"$Strain"_*_featurecounts.txt)
    do
        echo $File
        cp $File $OutDir/.
    done
    for File in $(ls $OutDir/*_featurecounts.txt)
    do
        Prefix=$(echo $File | rev | cut -f1 -d '/' | rev | sed 's/_featurecounts.txt//g')
        sed -ie "s/star_aligmentAligned.sortedByCoord.out.bam/$Prefix/g" $File
    done
done
```

## DeSeq commands

## Method 1

BC-16

```R
#install and load libraries
require("pheatmap")
require("data.table")

#load tables into a "list of lists"
qq <- lapply(list.files("analysis/DeSeq/Method_1/Bc16","*featurecounts.txt$",full.names=T,recursive=T),function(x) fread(x))

# ensure the samples column is the same name as the treatment you want to use:
qq[7]

#merge the "list of lists" into a single table
m <- Reduce(function(...) merge(..., all = T,by=c("Geneid","Chr","Start","End","Strand","Length")), qq)

#convert data.table to data.frame for use with DESeq2
countData <- data.frame(m[,c(1,7:(ncol(m))),with=F])
rownames(countData) <- countData[,1]
countData <- countData[,-1]

#indexes <- unique(gsub("(.*)_L00.*", "\\1", colnames(countData)))
indexes <- c("TA-07", "TA-08", "TA-09", "TA-12", "TA-13", "TA-14", "TA_B_P1", "TA_B_P2", "TA_B_P3", "TA_NO_P1", "TA_NO_P2", "TA_NO_P3", "TA-18", "TA-19", "TA-20")

countData <- round(countData,0)

#output countData
write.table(countData,"analysis/DeSeq/Method_1/Bc16/Bc16_countData.txt",sep="\t",na="",quote=F)

#output gene details
write.table(m[,1:6,with=F],"analysis/DeSeq/Method_1/Bc16/Bc16_genes.txt",sep="\t",quote=F,row.names=F)

#Running DeSeq2

require("DESeq2")

unorderedColData <- read.table("analysis/DeSeq/Method_1/Bc16/P.frag_method1_RNAseq_design.txt",header=T,sep="\t")
rownames(unorderedColData) <- unorderedColData$Sample.name
unorderedColDataSubset <- unorderedColData[indexes,]

colData <- data.frame(unorderedColDataSubset[ order(unorderedColDataSubset$Sample.name),])
unorderedData <- read.table("analysis/DeSeq/Method_1/Bc16/Bc16_countData.txt",header=T,sep="\t")
countData <- data.frame(unorderedData[ , order(colnames(unorderedData))])
colData$Group <- paste0(colData$Isolate,'_', colData$Timepoint)
countData <- round(countData,0)

design <- ~Group

dds <-     DESeqDataSetFromMatrix(countData,colData,design)
sizeFactors(dds) <- sizeFactors(estimateSizeFactors(dds, type = c("ratio")))
dds <- DESeq(dds, fitType="local")

library("RColorBrewer")
library("gplots", Sys.getenv("R_LIBS_USER"))
library("ggplot2")
library("ggrepel")

vst<-varianceStabilizingTransformation(dds)

pdf("analysis/DeSeq/Method_1/Bc16/heatmap_vst.pdf", width=12,height=12)
sampleDists<-dist(t(assay(vst)))

sampleDistMatrix <- as.matrix(sampleDists)
rownames(sampleDistMatrix) <- paste(vst$Group)
colnames(sampleDistMatrix) <- paste(vst$Group)
colours <- colorRampPalette( rev(brewer.pal(9, "Blues")) )(255)
heatmap( sampleDistMatrix,
  trace="none",  # turns off trace lines inside the heat map
  col=colours, # use on color palette defined earlier
  margins=c(12,12), # widens margins around plot
  srtCol=45,
  srtCol=45)
dev.off()

# Sample distances measured with rlog transformation:

rld <- rlog( dds )

pdf("analysis/DeSeq/Method_1/Bc16/heatmap_rld.pdf")
sampleDists <- dist( t( assay(rld) ) )
library("RColorBrewer")
sampleDistMatrix <- as.matrix( sampleDists )
rownames(sampleDistMatrix) <- paste(rld$Group)
colnames(sampleDistMatrix) <- paste(rld$Group)
colours = colorRampPalette( rev(brewer.pal(9, "Blues")) )(255)
heatmap( sampleDistMatrix,
  trace="none",  # turns off trace lines inside the heat map
  col=colours, # use on color palette defined earlier
  margins=c(12,12), # widens margins around plot
  srtCol=45,
  srtCol=45)
dev.off()

#PCA plots

pdf("analysis/DeSeq/Method_1/Bc16/PCA_vst.pdf")
plotPCA(vst,intgroup=c("Isolate", "Timepoint"))
dev.off()

#Plot using rlog transformation:
pdf("analysis/DeSeq/Method_1/Bc16/PCA_rld.pdf")
plotPCA(rld,intgroup=c("Isolate", "Timepoint"))
dev.off()

pdf("analysis/DeSeq/Method_1/Bc16/PCA_additional.pdf")

dev.off()

#Plot using rlog transformation, showing sample names:

data <- plotPCA(rld, intgroup="Group", returnData=TRUE)
percentVar <- round(100 * attr(data, "percentVar"))

pca_plot<- ggplot(data, aes(PC1, PC2, color=Group)) +
 geom_point(size=3) +
 xlab(paste0("PC1: ",percentVar[1],"% variance")) +
 ylab(paste0("PC2: ",percentVar[2],"% variance")) + geom_text_repel(aes(label=colnames(rld)))
 coord_fixed()

ggsave("analysis/DeSeq/Method_1/Bc16/PCA_sample_names.pdf", pca_plot, dpi=300, height=10, width=12)

#Analysis of gene expression

#BC-16_24hrs vs BC-1

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_24hr","Bc1_48hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Bc16/Bc16_24hr_vs_Bc1_48hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Bc16/Bc16_24hr_vs_Bc1_48hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Bc16/Bc16_24hr_vs_Bc1_48hr_down.txt",sep="\t",na="",quote=F)

#BC-16_48hrs vs BC-1

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_48hr","Bc1_48hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Bc16/Bc16_48hr_vs_Bc1_48hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Bc16/Bc16_48hr_vs_Bc1_48hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Bc16/Bc16_48hr_vs_Bc1_48hr_down.txt",sep="\t",na="",quote=F)

#BC-16_96hrs vs BC-1

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_96hr","Bc1_48hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Bc16/Bc16_96hr_vs_Bc1_48hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Bc16/Bc16_96hr_vs_Bc1_48hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Bc16/Bc16_96hr_vs_Bc1_48hr_down.txt",sep="\t",na="",quote=F)

#BC-16_24hrs vs NOV-9

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_24hr","Nov9_72hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Bc16/Bc16_24hr_vs_Nov9_72hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Bc16/Bc16_24hr_vs_Nov9_72hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Bc16/Bc16_24hr_vs_Nov9_72hr_down.txt",sep="\t",na="",quote=F)

#BC-16_48hrs vs NOV-9

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_48hr","Nov9_72hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Bc16/Bc16_48hr_vs_Nov9_72hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Bc16/Bc16_48hr_vs_Nov9_72hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Bc16/Bc16_48hr_vs_Nov9_72hr_down.txt",sep="\t",na="",quote=F)

#BC-16_96hrs vs NOV-9

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_96hr","Nov9_72hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Bc16/Bc16_96hr_vs_Nov9_72hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Bc16/Bc16_96hr_vs_Nov9_72hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Bc16/Bc16_96hr_vs_Nov9_72hr_down.txt",sep="\t",na="",quote=F)

#BC-1 vs NOV-9

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc1_48hr","Nov9_72hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Bc16/Bc1_48hr_vs_Nov9_72hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Bc16/Bc1_48hr_vs_Nov9_72hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Bc16/Bc1_48hr_vs_Nov9_72hr_down.txt",sep="\t",na="",quote=F)

#Make a table of raw counts, normalised counts and fpkm values:

raw_counts <- data.frame(counts(dds, normalized=FALSE))
colnames(raw_counts) <- paste(colData$Group)
write.table(raw_counts,"analysis/DeSeq/Method_1/Bc16/raw_counts.txt",sep="\t",na="",quote=F)
norm_counts <- data.frame(counts(dds, normalized=TRUE))
colnames(norm_counts) <- paste(colData$Group)
write.table(norm_counts,"analysis/DeSeq/Method_1/Bc16/normalised_counts.txt",sep="\t",na="",quote=F)

library(Biostrings)
library(naturalsort)
mygenes <- readDNAStringSet("gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors_renamed.cdna.fasta")
t1 <- counts(dds)
t1 <- mygenes[rownames(t1)]
rowRanges(dds) <- GRanges(t1@ranges@NAMES,t1@ranges)

# robust may be better set at fasle to normalise based on total counts rather than 'library normalisation factors'
fpkm_counts <- data.frame(fpkm(dds, robust = TRUE))
colnames(fpkm_counts) <- paste(colData$Group)
write.table(fpkm_counts,"analysis/DeSeq/Method_1/Bc16/fpkm_norm_counts.txt",sep="\t",na="",quote=F)
fpkm_counts <- data.frame(fpkm(dds, robust = FALSE))
colnames(fpkm_counts) <- paste(colData$Group)
write.table(fpkm_counts,"analysis/DeSeq/Method_1/Bc16/fpkm_counts.txt",sep="\t",na="",quote=F)
```

BC-1

```R
#install and load libraries
require("pheatmap")
require("data.table")

#load tables into a "list of lists"
qq <- lapply(list.files("analysis/DeSeq/Method_1/Bc1","*featurecounts.txt$",full.names=T,recursive=T),function(x) fread(x))

# ensure the samples column is the same name as the treatment you want to use:
qq[7]

#merge the "list of lists" into a single table
m <- Reduce(function(...) merge(..., all = T,by=c("Geneid","Chr","Start","End","Strand","Length")), qq)

#convert data.table to data.frame for use with DESeq2
countData <- data.frame(m[,c(1,7:(ncol(m))),with=F])
rownames(countData) <- countData[,1]
countData <- countData[,-1]

#indexes <- unique(gsub("(.*)_L00.*", "\\1", colnames(countData)))
indexes <- c("TA-07", "TA-08", "TA-09", "TA-12", "TA-13", "TA-14", "TA_B_P1", "TA_B_P2", "TA_B_P3", "TA_NO_P1", "TA_NO_P2", "TA_NO_P3", "TA-18", "TA-19", "TA-20")

countData <- round(countData,0)

#output countData
write.table(countData,"analysis/DeSeq/Method_1/Bc1/Bc1_countData.txt",sep="\t",na="",quote=F)

#output gene details
write.table(m[,1:6,with=F],"analysis/DeSeq/Method_1/Bc1/Bc1_genes.txt",sep="\t",quote=F,row.names=F)

#Running DeSeq2

require("DESeq2")

unorderedColData <- read.table("analysis/DeSeq/Method_1/Bc1/P.frag_method1_RNAseq_design.txt",header=T,sep="\t")
rownames(unorderedColData) <- unorderedColData$Sample.name
unorderedColDataSubset <- unorderedColData[indexes,]

colData <- data.frame(unorderedColDataSubset[ order(unorderedColDataSubset$Sample.name),])
unorderedData <- read.table("analysis/DeSeq/Method_1/Bc1/Bc1_countData.txt",header=T,sep="\t")
countData <- data.frame(unorderedData[ , order(colnames(unorderedData))])
colData$Group <- paste0(colData$Isolate,'_', colData$Timepoint)
countData <- round(countData,0)

design <- ~Group

dds <-     DESeqDataSetFromMatrix(countData,colData,design)
sizeFactors(dds) <- sizeFactors(estimateSizeFactors(dds, type = c("ratio")))
dds <- DESeq(dds, fitType="local")

library("RColorBrewer")
library("gplots", Sys.getenv("R_LIBS_USER"))
library("ggplot2")
library("ggrepel")

vst<-varianceStabilizingTransformation(dds)

pdf("analysis/DeSeq/Method_1/Bc1/heatmap_vst.pdf", width=12,height=12)
sampleDists<-dist(t(assay(vst)))

sampleDistMatrix <- as.matrix(sampleDists)
rownames(sampleDistMatrix) <- paste(vst$Group)
colnames(sampleDistMatrix) <- paste(vst$Group)
colours <- colorRampPalette( rev(brewer.pal(9, "Blues")) )(255)
heatmap( sampleDistMatrix,
  trace="none",  # turns off trace lines inside the heat map
  col=colours, # use on color palette defined earlier
  margins=c(12,12), # widens margins around plot
  srtCol=45,
  srtCol=45)
dev.off()

# Sample distances measured with rlog transformation:

rld <- rlog( dds )

pdf("analysis/DeSeq/Method_1/Bc1/heatmap_rld.pdf")
sampleDists <- dist( t( assay(rld) ) )

sampleDistMatrix <- as.matrix(sampleDists)
rownames(sampleDistMatrix) <- paste(vst$Group)
colnames(sampleDistMatrix) <- paste(vst$Group)
colours <- colorRampPalette( rev(brewer.pal(9, "Blues")) )(255)
heatmap( sampleDistMatrix,
  trace="none",  # turns off trace lines inside the heat map
  col=colours, # use on color palette defined earlier
  margins=c(12,12), # widens margins around plot
  srtCol=45,
  srtCol=45)
dev.off()

#PCA plots

pdf("analysis/DeSeq/Method_1/Bc1/PCA_vst.pdf")
plotPCA(vst,intgroup=c("Isolate", "Timepoint"))
dev.off()

#Plot using rlog transformation:
pdf("analysis/DeSeq/Method_1/Bc1/PCA_rld.pdf")
plotPCA(rld,intgroup=c("Isolate", "Timepoint"))
dev.off()

pdf("analysis/DeSeq/Method_1/Bc1/PCA_additional.pdf")

dev.off()

#Plot using rlog transformation, showing sample names:

data <- plotPCA(rld, intgroup="Group", returnData=TRUE)
percentVar <- round(100 * attr(data, "percentVar"))

pca_plot<- ggplot(data, aes(PC1, PC2, color=Group)) +
 geom_point(size=3) +
 xlab(paste0("PC1: ",percentVar[1],"% variance")) +
 ylab(paste0("PC2: ",percentVar[2],"% variance")) + geom_text_repel(aes(label=colnames(rld)))
 coord_fixed()

ggsave("analysis/DeSeq/Method_1/Bc1/PCA_sample_names.pdf", pca_plot, dpi=300, height=10, width=12)

#Analysis of gene expression

#BC-16_24hrs vs BC-1

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_24hr","Bc1_48hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Bc1/Bc16_24hr_vs_Bc1_48hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Bc1/Bc16_24hr_vs_Bc1_48hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Bc1/Bc16_24hr_vs_Bc1_48hr_down.txt",sep="\t",na="",quote=F)

#BC-16_48hrs vs BC-1

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_48hr","Bc1_48hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Bc1/Bc16_48hr_vs_Bc1_48hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Bc1/Bc16_48hr_vs_Bc1_48hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Bc1/Bc16_48hr_vs_Bc1_48hr_down.txt",sep="\t",na="",quote=F)

#BC-16_96hrs vs BC-1

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_96hr","Bc1_48hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Bc1/Bc16_96hr_vs_Bc1_48hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Bc1/Bc16_96hr_vs_Bc1_48hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Bc1/Bc16_96hr_vs_Bc1_48hr_down.txt",sep="\t",na="",quote=F)

#BC-16_24hrs vs NOV-9

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_24hr","Nov9_72hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Bc1/Bc16_24hr_vs_Nov9_72hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Bc1/Bc16_24hr_vs_Nov9_72hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Bc1/Bc16_24hr_vs_Nov9_72hr_down.txt",sep="\t",na="",quote=F)

#BC-16_48hrs vs NOV-9

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_48hr","Nov9_72hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Bc1/Bc16_48hr_vs_Nov9_72hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Bc1/Bc16_48hr_vs_Nov9_72hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Bc1/Bc16_48hr_vs_Nov9_72hr_down.txt",sep="\t",na="",quote=F)

#BC-16_96hrs vs NOV-9

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_96hr","Nov9_72hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Bc1/Bc16_96hr_vs_Nov9_72hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Bc1/Bc16_96hr_vs_Nov9_72hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Bc1/Bc16_96hr_vs_Nov9_72hr_down.txt",sep="\t",na="",quote=F)

#BC-1 vs NOV-9

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc1_48hr","Nov9_72hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Bc1/Bc1_48hr_vs_Nov9_72hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Bc1/Bc1_48hr_vs_Nov9_72hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Bc1/Bc1_48hr_vs_Nov9_72hr_down.txt",sep="\t",na="",quote=F)

#Make a table of raw counts, normalised counts and fpkm values:

raw_counts <- data.frame(counts(dds, normalized=FALSE))
colnames(raw_counts) <- paste(colData$Group)
write.table(raw_counts,"analysis/DeSeq/Method_1/Bc1/raw_counts.txt",sep="\t",na="",quote=F)
norm_counts <- data.frame(counts(dds, normalized=TRUE))
colnames(norm_counts) <- paste(colData$Group)
write.table(norm_counts,"analysis/DeSeq/Method_1/Bc1/normalised_counts.txt",sep="\t",na="",quote=F)

library(Biostrings)
library(naturalsort)
mygenes <- readDNAStringSet("gene_pred/annotation/P.fragariae/Bc1/Bc1_genes_incl_ORFeffectors_renamed.cdna.fasta")
t1 <- counts(dds)
t1 <- mygenes[rownames(t1)]
rowRanges(dds) <- GRanges(t1@ranges@NAMES,t1@ranges)

# robust may be better set at fasle to normalise based on total counts rather than 'library normalisation factors'
fpkm_counts <- data.frame(fpkm(dds, robust = TRUE))
colnames(fpkm_counts) <- paste(colData$Group)
write.table(fpkm_counts,"analysis/DeSeq/Method_1/Bc1/fpkm_norm_counts.txt",sep="\t",na="",quote=F)
fpkm_counts <- data.frame(fpkm(dds, robust = FALSE))
colnames(fpkm_counts) <- paste(colData$Group)
write.table(fpkm_counts,"analysis/DeSeq/Method_1/Bc1/fpkm_counts.txt",sep="\t",na="",quote=F)
```

NOV-9

```R
#install and load libraries
require("pheatmap")
require("data.table")

#load tables into a "list of lists"
qq <- lapply(list.files("analysis/DeSeq/Method_1/Nov9","*featurecounts.txt$",full.names=T,recursive=T),function(x) fread(x))

# ensure the samples column is the same name as the treatment you want to use:
qq[7]

#merge the "list of lists" into a single table
m <- Reduce(function(...) merge(..., all = T,by=c("Geneid","Chr","Start","End","Strand","Length")), qq)

#convert data.table to data.frame for use with DESeq2
countData <- data.frame(m[,c(1,7:(ncol(m))),with=F])
rownames(countData) <- countData[,1]
countData <- countData[,-1]

#indexes <- unique(gsub("(.*)_L00.*", "\\1", colnames(countData)))
indexes <- c("TA-07", "TA-08", "TA-09", "TA-12", "TA-13", "TA-14", "TA_B_P1", "TA_B_P2", "TA_B_P3", "TA_NO_P1", "TA_NO_P2", "TA_NO_P3", "TA-18", "TA-19", "TA-20")

countData <- round(countData,0)

#output countData
write.table(countData,"analysis/DeSeq/Method_1/Nov9/Nov9_countData.txt",sep="\t",na="",quote=F)

#output gene details
write.table(m[,1:6,with=F],"analysis/DeSeq/Method_1/Nov9/Nov9_genes.txt",sep="\t",quote=F,row.names=F)

#Running DeSeq2

require("DESeq2")

unorderedColData <- read.table("analysis/DeSeq/Method_1/Nov9/P.frag_method1_RNAseq_design.txt",header=T,sep="\t")
rownames(unorderedColData) <- unorderedColData$Sample.name
unorderedColDataSubset <- unorderedColData[indexes,]

colData <- data.frame(unorderedColDataSubset[ order(unorderedColDataSubset$Sample.name),])
unorderedData <- read.table("analysis/DeSeq/Method_1/Nov9/Nov9_countData.txt",header=T,sep="\t")
countData <- data.frame(unorderedData[ , order(colnames(unorderedData))])
colData$Group <- paste0(colData$Isolate,'_', colData$Timepoint)
countData <- round(countData,0)

design <- ~Group

dds <-     DESeqDataSetFromMatrix(countData,colData,design)
sizeFactors(dds) <- sizeFactors(estimateSizeFactors(dds, type = c("ratio")))
dds <- DESeq(dds, fitType="local")

library("RColorBrewer")
library("gplots", Sys.getenv("R_LIBS_USER"))
library("ggplot2")
library("ggrepel")

vst<-varianceStabilizingTransformation(dds)

pdf("analysis/DeSeq/Method_1/Nov9/heatmap_vst.pdf", width=12,height=12)
sampleDists<-dist(t(assay(vst)))

sampleDistMatrix <- as.matrix(sampleDists)
rownames(sampleDistMatrix) <- paste(vst$Group)
colnames(sampleDistMatrix) <- paste(vst$Group)
colours <- colorRampPalette( rev(brewer.pal(9, "Blues")) )(255)
heatmap( sampleDistMatrix,
  trace="none",  # turns off trace lines inside the heat map
  col=colours, # use on color palette defined earlier
  margins=c(12,12), # widens margins around plot
  srtCol=45,
  srtCol=45)
dev.off()

# Sample distances measured with rlog transformation:

rld <- rlog( dds )

pdf("analysis/DeSeq/Method_1/Nov9/heatmap_rld.pdf")
sampleDists <- dist( t( assay(rld) ) )
library("RColorBrewer")
sampleDistMatrix <- as.matrix( sampleDists )
rownames(sampleDistMatrix) <- paste(rld$Group)
colnames(sampleDistMatrix) <- paste(rld$Group)
colours = colorRampPalette( rev(brewer.pal(9, "Blues")) )(255)
heatmap( sampleDistMatrix,
  trace="none",  # turns off trace lines inside the heat map
  col=colours, # use on color palette defined earlier
  margins=c(12,12), # widens margins around plot
  srtCol=45,
  srtCol=45)
dev.off()

#PCA plots

pdf("analysis/DeSeq/Method_1/Nov9/PCA_vst.pdf")
plotPCA(vst,intgroup=c("Isolate", "Timepoint"))
dev.off()

#Plot using rlog transformation:
pdf("analysis/DeSeq/Method_1/Nov9/PCA_rld.pdf")
plotPCA(rld,intgroup=c("Isolate", "Timepoint"))
dev.off()

pdf("analysis/DeSeq/Method_1/Nov9/PCA_additional.pdf")

dev.off()

#Plot using rlog transformation, showing sample names:

data <- plotPCA(rld, intgroup="Group", returnData=TRUE)
percentVar <- round(100 * attr(data, "percentVar"))

pca_plot<- ggplot(data, aes(PC1, PC2, color=Group)) +
 geom_point(size=3) +
 xlab(paste0("PC1: ",percentVar[1],"% variance")) +
 ylab(paste0("PC2: ",percentVar[2],"% variance")) + geom_text_repel(aes(label=colnames(rld)))
 coord_fixed()

ggsave("analysis/DeSeq/Method_1/Nov9/PCA_sample_names.pdf", pca_plot, dpi=300, height=10, width=12)

#Analysis of gene expression

#BC-16_24hrs vs BC-1

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_24hr","Bc1_48hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Nov9/Bc16_24hr_vs_Bc1_48hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Nov9/Bc16_24hr_vs_Bc1_48hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Nov9/Bc16_24hr_vs_Bc1_48hr_down.txt",sep="\t",na="",quote=F)

#BC-16_48hrs vs BC-1

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_48hr","Bc1_48hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Nov9/Bc16_48hr_vs_Bc1_48hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Nov9/Bc16_48hr_vs_Bc1_48hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Nov9/Bc16_48hr_vs_Bc1_48hr_down.txt",sep="\t",na="",quote=F)

#BC-16_96hrs vs BC-1

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_96hr","Bc1_48hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Nov9/Bc16_96hr_vs_Bc1_48hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Nov9/Bc16_96hr_vs_Bc1_48hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Nov9/Bc16_96hr_vs_Bc1_48hr_down.txt",sep="\t",na="",quote=F)

#BC-16_24hrs vs NOV-9

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_24hr","Nov9_72hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Nov9/Bc16_24hr_vs_Nov9_72hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Nov9/Bc16_24hr_vs_Nov9_72hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Nov9/Bc16_24hr_vs_Nov9_72hr_down.txt",sep="\t",na="",quote=F)

#BC-16_48hrs vs NOV-9

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_48hr","Nov9_72hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Nov9/Bc16_48hr_vs_Nov9_72hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Nov9/Bc16_48hr_vs_Nov9_72hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Nov9/Bc16_48hr_vs_Nov9_72hr_down.txt",sep="\t",na="",quote=F)

#BC-16_96hrs vs NOV-9

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_96hr","Nov9_72hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Nov9/Bc16_96hr_vs_Nov9_72hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Nov9/Bc16_96hr_vs_Nov9_72hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Nov9/Bc16_96hr_vs_Nov9_72hr_down.txt",sep="\t",na="",quote=F)

#BC-1 vs NOV-9

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc1_48hr","Nov9_72hr"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_1/Nov9/Bc1_48hr_vs_Nov9_72hr.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_1/Nov9/Bc1_48hr_vs_Nov9_72hr_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_1/Nov9/Bc1_48hr_vs_Nov9_72hr_down.txt",sep="\t",na="",quote=F)

#Make a table of raw counts, normalised counts and fpkm values:

raw_counts <- data.frame(counts(dds, normalized=FALSE))
colnames(raw_counts) <- paste(colData$Group)
write.table(raw_counts,"analysis/DeSeq/Method_1/Nov9/raw_counts.txt",sep="\t",na="",quote=F)
norm_counts <- data.frame(counts(dds, normalized=TRUE))
colnames(norm_counts) <- paste(colData$Group)
write.table(norm_counts,"analysis/DeSeq/Method_1/Nov9/normalised_counts.txt",sep="\t",na="",quote=F)

library(Biostrings)
library(naturalsort)
mygenes <- readDNAStringSet("gene_pred/annotation/P.fragariae/Nov9/Nov9_genes_incl_ORFeffectors_renamed.cdna.fasta")
t1 <- counts(dds)
t1 <- mygenes[rownames(t1)]
rowRanges(dds) <- GRanges(t1@ranges@NAMES,t1@ranges)

# robust may be better set at fasle to normalise based on total counts rather than 'library normalisation factors'
fpkm_counts <- data.frame(fpkm(dds, robust = TRUE))
colnames(fpkm_counts) <- paste(colData$Group)
write.table(fpkm_counts,"analysis/DeSeq/Method_1/Nov9/fpkm_norm_counts.txt",sep="\t",na="",quote=F)
fpkm_counts <- data.frame(fpkm(dds, robust = FALSE))
colnames(fpkm_counts) <- paste(colData$Group)
write.table(fpkm_counts,"analysis/DeSeq/Method_1/Nov9/fpkm_counts.txt",sep="\t",na="",quote=F)
```

## Method 2

BC-16

```R
#install and load libraries
require("pheatmap")
require("data.table")

#load tables into a "list of lists"
qq <- lapply(list.files("analysis/DeSeq/Method_2/Bc16","*featurecounts.txt$",full.names=T,recursive=T),function(x) fread(x))

# ensure the samples column is the same name as the treatment you want to use:
qq[7]

#merge the "list of lists" into a single table
m <- Reduce(function(...) merge(..., all = T,by=c("Geneid","Chr","Start","End","Strand","Length")), qq)

#convert data.table to data.frame for use with DESeq2
countData <- data.frame(m[,c(1,7:(ncol(m))),with=F])
rownames(countData) <- countData[,1]
countData <- countData[,-1]

#indexes <- unique(gsub("(.*)_L00.*", "\\1", colnames(countData)))
indexes <- c("TA-07", "TA-08", "TA-09", "TA-12", "TA-13", "TA-14", "TA_B_P1", "TA_B_P2", "TA_B_P3", "TA_NO_P1", "TA_NO_P2", "TA_NO_P3", "TA-18", "TA-19", "TA-20", "TA-32", "TA-34", "TA-35", "TA_B_M1", "TA_B_M2", "TA_B_M3", "TA_NO_M1", "TA_NO_M2", "TA_NO_M5")

countData <- round(countData,0)

#output countData
write.table(countData,"analysis/DeSeq/Method_2/Bc16/Method_2_Bc16_countData.txt",sep="\t",na="",quote=F)

#output gene details
write.table(m[,1:6,with=F],"analysis/DeSeq/Method_2/Bc16/Method_2_Bc16_genes.txt",sep="\t",quote=F,row.names=F)

#Running DeSeq2

require("DESeq2")

unorderedColData <- read.table("analysis/DeSeq/Method_2/Bc16/P.frag_method2_RNAseq_design.txt",header=T,sep="\t")
rownames(unorderedColData) <- unorderedColData$Sample.name
unorderedColDataSubset <- unorderedColData[indexes,]

colData <- data.frame(unorderedColDataSubset[ order(unorderedColDataSubset$Sample.name),])
unorderedData <- read.table("analysis/DeSeq/Method_2/Bc16/Method_2_Bc16_countData.txt",header=T,sep="\t")
countData <- data.frame(unorderedData[ , order(colnames(unorderedData))])
colData$Group <- paste0(colData$Isolate,'_', colData$Timepoint)
countData <- round(countData,0)

design <- ~Group

dds <-     DESeqDataSetFromMatrix(countData,colData,design)
sizeFactors(dds) <- sizeFactors(estimateSizeFactors(dds, type = c("ratio")))
dds <- DESeq(dds, fitType="local")

library("RColorBrewer")
library("gplots", Sys.getenv("R_LIBS_USER"))
library("ggplot2")
library("ggrepel")

vst<-varianceStabilizingTransformation(dds)

pdf("analysis/DeSeq/Method_2/Bc16/heatmap_vst.pdf", width=12,height=12)
sampleDists<-dist(t(assay(vst)))

sampleDistMatrix <- as.matrix(sampleDists)
rownames(sampleDistMatrix) <- paste(vst$Group)
colnames(sampleDistMatrix) <- paste(vst$Group)
colours <- colorRampPalette( rev(brewer.pal(9, "Blues")) )(255)
heatmap( sampleDistMatrix,
  trace="none",  # turns off trace lines inside the heat map
  col=colours, # use on color palette defined earlier
  margins=c(12,12), # widens margins around plot
  srtCol=45,
  srtCol=45)
dev.off()

# Sample distances measured with rlog transformation:

rld <- rlog( dds )

pdf("analysis/DeSeq/Method_2/Bc16/heatmap_rld.pdf")
sampleDists <- dist( t( assay(rld) ) )
library("RColorBrewer")
sampleDistMatrix <- as.matrix( sampleDists )
rownames(sampleDistMatrix) <- paste(rld$Group)
colnames(sampleDistMatrix) <- paste(rld$Group)
colours = colorRampPalette( rev(brewer.pal(9, "Blues")) )(255)
heatmap( sampleDistMatrix,
  trace="none",  # turns off trace lines inside the heat map
  col=colours, # use on color palette defined earlier
  margins=c(12,12), # widens margins around plot
  srtCol=45,
  srtCol=45)
dev.off()

#PCA plots

pdf("analysis/DeSeq/Method_2/Bc16/PCA_vst.pdf")
plotPCA(vst,intgroup=c("Isolate", "Timepoint"))
dev.off()

#Plot using rlog transformation:
pdf("analysis/DeSeq/Method_2/Bc16/PCA_rld.pdf")
plotPCA(rld,intgroup=c("Isolate", "Timepoint"))
dev.off()

pdf("analysis/DeSeq/Method_2/Bc16/PCA_additional.pdf")

dev.off()

#Plot using rlog transformation, showing sample names:

data <- plotPCA(rld, intgroup="Group", returnData=TRUE)
percentVar <- round(100 * attr(data, "percentVar"))

pca_plot<- ggplot(data, aes(PC1, PC2, color=Group)) +
 geom_point(size=3) +
 xlab(paste0("PC1: ",percentVar[1],"% variance")) +
 ylab(paste0("PC2: ",percentVar[2],"% variance")) + geom_text_repel(aes(label=colnames(rld)))
 coord_fixed()

ggsave("analysis/DeSeq/Method_2/Bc16/PCA_sample_names.pdf", pca_plot, dpi=300, height=10, width=12)

#Analysis of gene expression

#BC-16_24hrs vs BC-16_mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_24hr","Bc16_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_2/Bc16/Bc16_24hr_vs_Bc16_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_2/Bc16/Bc16_24hr_vs_Bc16_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_2/Bc16/Bc16_24hr_vs_Bc16_mycelium_down.txt",sep="\t",na="",quote=F)

#BC-16_48hrs vs BC-16_mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_48hr","Bc16_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_2/Bc16/Bc16_48hr_vs_Bc16_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_2/Bc16/Bc16_48hr_vs_Bc16_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_2/Bc16/Bc16_48hr_vs_Bc16_mycelium_down.txt",sep="\t",na="",quote=F)

#BC-16_96hrs vs BC-16_mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_96hr","Bc16_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_2/Bc16/Bc16_96hr_vs_Bc16_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_2/Bc16/Bc16_96hr_vs_Bc16_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_2/Bc16/Bc16_96hr_vs_Bc16_mycelium_down.txt",sep="\t",na="",quote=F)

#BC-1_48hrs vs BC-1_mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc1_48hr","Bc1_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_2/Bc16/Bc1_48hr_vs_Bc1_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_2/Bc16/Bc1_48hr_vs_Bc1_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_2/Bc16/Bc1_48hr_vs_Bc1_mycelium_down.txt",sep="\t",na="",quote=F)

#NOV-9_72hr vs NOV-9_mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Nov9_72hr","Nov9_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_2/Bc16/Nov9_72hr_vs_Nov9_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_2/Bc16/Nov9_72hr_vs_Nov9_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_2/Bc16/Nov9_72hr_vs_Nov9_mycelium_down.txt",sep="\t",na="",quote=F)

#Make a table of raw counts, normalised counts and fpkm values:

raw_counts <- data.frame(counts(dds, normalized=FALSE))
colnames(raw_counts) <- paste(colData$Group)
write.table(raw_counts,"analysis/DeSeq/Method_2/Bc16/raw_counts.txt",sep="\t",na="",quote=F)
norm_counts <- data.frame(counts(dds, normalized=TRUE))
colnames(norm_counts) <- paste(colData$Group)
write.table(norm_counts,"analysis/DeSeq/Method_2/Bc16/normalised_counts.txt",sep="\t",na="",quote=F)

library(Biostrings)
library(naturalsort)
mygenes <- readDNAStringSet("gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors_renamed.cdna.fasta")
t1 <- counts(dds)
t1 <- mygenes[rownames(t1)]
rowRanges(dds) <- GRanges(t1@ranges@NAMES,t1@ranges)

# robust may be better set at fasle to normalise based on total counts rather than 'library normalisation factors'
fpkm_counts <- data.frame(fpkm(dds, robust = TRUE))
colnames(fpkm_counts) <- paste(colData$Group)
write.table(fpkm_counts,"analysis/DeSeq/Method_2/Bc16/fpkm_norm_counts.txt",sep="\t",na="",quote=F)
fpkm_counts <- data.frame(fpkm(dds, robust = FALSE))
colnames(fpkm_counts) <- paste(colData$Group)
write.table(fpkm_counts,"analysis/DeSeq/Method_2/Bc16/fpkm_counts.txt",sep="\t",na="",quote=F)
```

BC-1

```R
#install and load libraries
require("pheatmap")
require("data.table")

#load tables into a "list of lists"
qq <- lapply(list.files("analysis/DeSeq/Method_2/Bc1","*featurecounts.txt$",full.names=T,recursive=T),function(x) fread(x))

# ensure the samples column is the same name as the treatment you want to use:
qq[7]

#merge the "list of lists" into a single table
m <- Reduce(function(...) merge(..., all = T,by=c("Geneid","Chr","Start","End","Strand","Length")), qq)

#convert data.table to data.frame for use with DESeq2
countData <- data.frame(m[,c(1,7:(ncol(m))),with=F])
rownames(countData) <- countData[,1]
countData <- countData[,-1]

#indexes <- unique(gsub("(.*)_L00.*", "\\1", colnames(countData)))
indexes <- c("TA-07", "TA-08", "TA-09", "TA-12", "TA-13", "TA-14", "TA_B_P1", "TA_B_P2", "TA_B_P3", "TA_NO_P1", "TA_NO_P2", "TA_NO_P3", "TA-18", "TA-19", "TA-20", "TA-32", "TA-34", "TA-35", "TA_B_M1", "TA_B_M2", "TA_B_M3", "TA_NO_M1", "TA_NO_M2", "TA_NO_M5")

countData <- round(countData,0)

#output countData
write.table(countData,"analysis/DeSeq/Method_2/Bc1/Method_2_Bc1_countData.txt",sep="\t",na="",quote=F)

#output gene details
write.table(m[,1:6,with=F],"analysis/DeSeq/Method_2/Bc1/Method_2_Bc1_genes.txt",sep="\t",quote=F,row.names=F)

#Running DeSeq2

require("DESeq2")

unorderedColData <- read.table("analysis/DeSeq/Method_2/Bc1/P.frag_method2_RNAseq_design.txt",header=T,sep="\t")
rownames(unorderedColData) <- unorderedColData$Sample.name
unorderedColDataSubset <- unorderedColData[indexes,]

colData <- data.frame(unorderedColDataSubset[ order(unorderedColDataSubset$Sample.name),])
unorderedData <- read.table("analysis/DeSeq/Method_2/Bc1/Method_2_Bc1_countData.txt",header=T,sep="\t")
countData <- data.frame(unorderedData[ , order(colnames(unorderedData))])
colData$Group <- paste0(colData$Isolate,'_', colData$Timepoint)
countData <- round(countData,0)

design <- ~Group

dds <-     DESeqDataSetFromMatrix(countData,colData,design)
sizeFactors(dds) <- sizeFactors(estimateSizeFactors(dds, type = c("ratio")))
dds <- DESeq(dds, fitType="local")

library("RColorBrewer")
library("gplots", Sys.getenv("R_LIBS_USER"))
library("ggplot2")
library("ggrepel")

vst<-varianceStabilizingTransformation(dds)

pdf("analysis/DeSeq/Method_2/Bc1/heatmap_vst.pdf", width=12,height=12)
sampleDists<-dist(t(assay(vst)))

sampleDistMatrix <- as.matrix(sampleDists)
rownames(sampleDistMatrix) <- paste(vst$Group)
colnames(sampleDistMatrix) <- paste(vst$Group)
colours <- colorRampPalette( rev(brewer.pal(9, "Blues")) )(255)
heatmap( sampleDistMatrix,
  trace="none",  # turns off trace lines inside the heat map
  col=colours, # use on color palette defined earlier
  margins=c(12,12), # widens margins around plot
  srtCol=45,
  srtCol=45)
dev.off()

# Sample distances measured with rlog transformation:

rld <- rlog( dds )

pdf("analysis/DeSeq/Method_2/Bc1/heatmap_rld.pdf")
sampleDists <- dist( t( assay(rld) ) )
library("RColorBrewer")
sampleDistMatrix <- as.matrix( sampleDists )
rownames(sampleDistMatrix) <- paste(rld$Group)
colnames(sampleDistMatrix) <- paste(rld$Group)
colours = colorRampPalette( rev(brewer.pal(9, "Blues")) )(255)
heatmap( sampleDistMatrix,
  trace="none",  # turns off trace lines inside the heat map
  col=colours, # use on color palette defined earlier
  margins=c(12,12), # widens margins around plot
  srtCol=45,
  srtCol=45)
dev.off()

#PCA plots

pdf("analysis/DeSeq/Method_2/Bc1/PCA_vst.pdf")
plotPCA(vst,intgroup=c("Isolate", "Timepoint"))
dev.off()

#Plot using rlog transformation:
pdf("analysis/DeSeq/Method_2/Bc1/PCA_rld.pdf")
plotPCA(rld,intgroup=c("Isolate", "Timepoint"))
dev.off()

pdf("analysis/DeSeq/Method_2/Bc1/PCA_additional.pdf")

dev.off()

#Plot using rlog transformation, showing sample names:

data <- plotPCA(rld, intgroup="Group", returnData=TRUE)
percentVar <- round(100 * attr(data, "percentVar"))

pca_plot<- ggplot(data, aes(PC1, PC2, color=Group)) +
 geom_point(size=3) +
 xlab(paste0("PC1: ",percentVar[1],"% variance")) +
 ylab(paste0("PC2: ",percentVar[2],"% variance")) + geom_text_repel(aes(label=colnames(rld)))
 coord_fixed()

ggsave("analysis/DeSeq/Method_2/Bc1/PCA_sample_names.pdf", pca_plot, dpi=300, height=10, width=12)

#Analysis of gene expression

#BC-16_24hrs vs BC-16_mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_24hr","Bc16_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_2/Bc1/Bc16_24hr_vs_Bc16_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_2/Bc1/Bc16_24hr_vs_Bc16_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_2/Bc1/Bc16_24hr_vs_Bc16_mycelium_down.txt",sep="\t",na="",quote=F)

#BC-16_48hrs vs BC-16_mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_48hr","Bc16_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_2/Bc1/Bc16_48hr_vs_Bc16_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_2/Bc1/Bc16_48hr_vs_Bc16_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_2/Bc1/Bc16_48hr_vs_Bc16_mycelium_down.txt",sep="\t",na="",quote=F)

#BC-16_96hrs vs BC-16_mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_96hr","Bc16_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_2/Bc1/Bc16_96hr_vs_Bc16_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_2/Bc1/Bc16_96hr_vs_Bc16_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_2/Bc1/Bc16_96hr_vs_Bc16_mycelium_down.txt",sep="\t",na="",quote=F)

#BC-1_48hrs vs BC-1_mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc1_48hr","Bc1_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_2/Bc1/Bc1_48hr_vs_Bc1_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_2/Bc1/Bc1_48hr_vs_Bc1_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_2/Bc1/Bc1_48hr_vs_Bc1_mycelium_down.txt",sep="\t",na="",quote=F)

#NOV-9_72hr vs NOV-9_mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Nov9_72hr","Nov9_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_2/Bc1/Nov9_72hr_vs_Nov9_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_2/Bc1/Nov9_72hr_vs_Nov9_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_2/Bc1/Nov9_72hr_vs_Nov9_mycelium_down.txt",sep="\t",na="",quote=F)

#Make a table of raw counts, normalised counts and fpkm values:

raw_counts <- data.frame(counts(dds, normalized=FALSE))
colnames(raw_counts) <- paste(colData$Group)
write.table(raw_counts,"analysis/DeSeq/Method_2/Bc1/raw_counts.txt",sep="\t",na="",quote=F)
norm_counts <- data.frame(counts(dds, normalized=TRUE))
colnames(norm_counts) <- paste(colData$Group)
write.table(norm_counts,"analysis/DeSeq/Method_2/Bc1/normalised_counts.txt",sep="\t",na="",quote=F)

library(Biostrings)
library(naturalsort)
mygenes <- readDNAStringSet("gene_pred/annotation/P.fragariae/Bc1/Bc1_genes_incl_ORFeffectors_renamed.cdna.fasta")
t1 <- counts(dds)
t1 <- mygenes[rownames(t1)]
rowRanges(dds) <- GRanges(t1@ranges@NAMES,t1@ranges)

# robust may be better set at fasle to normalise based on total counts rather than 'library normalisation factors'
fpkm_counts <- data.frame(fpkm(dds, robust = TRUE))
colnames(fpkm_counts) <- paste(colData$Group)
write.table(fpkm_counts,"analysis/DeSeq/Method_2/Bc1/fpkm_norm_counts.txt",sep="\t",na="",quote=F)
fpkm_counts <- data.frame(fpkm(dds, robust = FALSE))
colnames(fpkm_counts) <- paste(colData$Group)
write.table(fpkm_counts,"analysis/DeSeq/Method_2/Bc1/fpkm_counts.txt",sep="\t",na="",quote=F)
```

NOV-9

```R
#install and load libraries
require("pheatmap")
require("data.table")

#load tables into a "list of lists"
qq <- lapply(list.files("analysis/DeSeq/Method_2/Nov9","*featurecounts.txt$",full.names=T,recursive=T),function(x) fread(x))

# ensure the samples column is the same name as the treatment you want to use:
qq[7]

#merge the "list of lists" into a single table
m <- Reduce(function(...) merge(..., all = T,by=c("Geneid","Chr","Start","End","Strand","Length")), qq)

#convert data.table to data.frame for use with DESeq2
countData <- data.frame(m[,c(1,7:(ncol(m))),with=F])
rownames(countData) <- countData[,1]
countData <- countData[,-1]

#indexes <- unique(gsub("(.*)_L00.*", "\\1", colnames(countData)))
indexes <- c("TA-07", "TA-08", "TA-09", "TA-12", "TA-13", "TA-14", "TA_B_P1", "TA_B_P2", "TA_B_P3", "TA_NO_P1", "TA_NO_P2", "TA_NO_P3", "TA-18", "TA-19", "TA-20", "TA-32", "TA-34", "TA-35", "TA_B_M1", "TA_B_M2", "TA_B_M3", "TA_NO_M1", "TA_NO_M2", "TA_NO_M5")

countData <- round(countData,0)

#output countData
write.table(countData,"analysis/DeSeq/Method_2/Nov9/Method_2_Nov9_countData.txt",sep="\t",na="",quote=F)

#output gene details
write.table(m[,1:6,with=F],"analysis/DeSeq/Method_2/Nov9/Method_2_Nov9_genes.txt",sep="\t",quote=F,row.names=F)

#Running DeSeq2

require("DESeq2")

unorderedColData <- read.table("analysis/DeSeq/Method_2/Nov9/P.frag_method2_RNAseq_design.txt",header=T,sep="\t")
rownames(unorderedColData) <- unorderedColData$Sample.name
unorderedColDataSubset <- unorderedColData[indexes,]

colData <- data.frame(unorderedColDataSubset[ order(unorderedColDataSubset$Sample.name),])
unorderedData <- read.table("analysis/DeSeq/Method_2/Nov9/Method_2_Nov9_countData.txt",header=T,sep="\t")
countData <- data.frame(unorderedData[ , order(colnames(unorderedData))])
colData$Group <- paste0(colData$Isolate,'_', colData$Timepoint)
countData <- round(countData,0)

design <- ~Group

dds <-     DESeqDataSetFromMatrix(countData,colData,design)
sizeFactors(dds) <- sizeFactors(estimateSizeFactors(dds, type = c("ratio")))
dds <- DESeq(dds, fitType="local")

library("RColorBrewer")
library("gplots", Sys.getenv("R_LIBS_USER"))
library("ggplot2")
library("ggrepel")

vst<-varianceStabilizingTransformation(dds)

pdf("analysis/DeSeq/Method_2/Nov9/heatmap_vst.pdf", width=12,height=12)
sampleDists<-dist(t(assay(vst)))

sampleDistMatrix <- as.matrix(sampleDists)
rownames(sampleDistMatrix) <- paste(vst$Group)
colnames(sampleDistMatrix) <- paste(vst$Group)
colours <- colorRampPalette( rev(brewer.pal(9, "Blues")) )(255)
heatmap( sampleDistMatrix,
  trace="none",  # turns off trace lines inside the heat map
  col=colours, # use on color palette defined earlier
  margins=c(12,12), # widens margins around plot
  srtCol=45,
  srtCol=45)
dev.off()

# Sample distances measured with rlog transformation:

rld <- rlog( dds )

pdf("analysis/DeSeq/Method_2/Nov9/heatmap_rld.pdf")
sampleDists <- dist( t( assay(rld) ) )
library("RColorBrewer")
sampleDistMatrix <- as.matrix( sampleDists )
rownames(sampleDistMatrix) <- paste(rld$Group)
colnames(sampleDistMatrix) <- paste(rld$Group)
colours = colorRampPalette( rev(brewer.pal(9, "Blues")) )(255)
heatmap( sampleDistMatrix,
  trace="none",  # turns off trace lines inside the heat map
  col=colours, # use on color palette defined earlier
  margins=c(12,12), # widens margins around plot
  srtCol=45,
  srtCol=45)
dev.off()

#PCA plots

pdf("analysis/DeSeq/Method_2/Nov9/PCA_vst.pdf")
plotPCA(vst,intgroup=c("Isolate", "Timepoint"))
dev.off()

#Plot using rlog transformation:
pdf("analysis/DeSeq/Method_2/Nov9/PCA_rld.pdf")
plotPCA(rld,intgroup=c("Isolate", "Timepoint"))
dev.off()

pdf("analysis/DeSeq/Method_2/Nov9/PCA_additional.pdf")

dev.off()

#Plot using rlog transformation, showing sample names:

data <- plotPCA(rld, intgroup="Group", returnData=TRUE)
percentVar <- round(100 * attr(data, "percentVar"))

pca_plot<- ggplot(data, aes(PC1, PC2, color=Group)) +
 geom_point(size=3) +
 xlab(paste0("PC1: ",percentVar[1],"% variance")) +
 ylab(paste0("PC2: ",percentVar[2],"% variance")) + geom_text_repel(aes(label=colnames(rld)))
 coord_fixed()

ggsave("analysis/DeSeq/Method_2/Nov9/PCA_sample_names.pdf", pca_plot, dpi=300, height=10, width=12)

#Analysis of gene expression

#BC-16_24hrs vs BC-16_mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_24hr","Bc16_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_2/Nov9/Bc16_24hr_vs_Bc16_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_2/Nov9/Bc16_24hr_vs_Bc16_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_2/Nov9/Bc16_24hr_vs_Bc16_mycelium_down.txt",sep="\t",na="",quote=F)

#BC-16_48hrs vs BC-16_mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_48hr","Bc16_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_2/Nov9/Bc16_48hr_vs_Bc16_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_2/Nov9/Bc16_48hr_vs_Bc16_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_2/Nov9/Bc16_48hr_vs_Bc16_mycelium_down.txt",sep="\t",na="",quote=F)

#BC-16_96hrs vs BC-16_mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc16_96hr","Bc16_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_2/Nov9/Bc16_96hr_vs_Bc16_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_2/Nov9/Bc16_96hr_vs_Bc16_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_2/Nov9/Bc16_96hr_vs_Bc16_mycelium_down.txt",sep="\t",na="",quote=F)

#BC-1_48hrs vs BC-1_mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Bc1_48hr","Bc1_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_2/Nov9/Bc1_48hr_vs_Bc1_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_2/Nov9/Bc1_48hr_vs_Bc1_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_2/Nov9/Bc1_48hr_vs_Bc1_mycelium_down.txt",sep="\t",na="",quote=F)

#NOV-9_72hr vs NOV-9_mycelium

alpha <- 0.05
res= results(dds, alpha=alpha,contrast=c("Group","Nov9_72hr","Nov9_mycelium"))
sig.res <- subset(res,padj<=alpha)
sig.res <- sig.res[order(sig.res$padj),]
sig.res.upregulated <- sig.res[sig.res$log2FoldChange >=1, ]
sig.res.downregulated <- sig.res[sig.res$log2FoldChange <=-1, ]
sig.res.upregulated2 <- sig.res[sig.res$log2FoldChange >0, ]
sig.res.downregulated2 <- sig.res[sig.res$log2FoldChange <0, ]

write.table(sig.res,"analysis/DeSeq/Method_2/Nov9/Nov9_72hr_vs_Nov9_mycelium.txt",sep="\t",na="",quote=F)
write.table(sig.res.upregulated,"analysis/DeSeq/Method_2/Nov9/Nov9_72hr_vs_Nov9_mycelium_up.txt",sep="\t",na="",quote=F)
write.table(sig.res.downregulated,"analysis/DeSeq/Method_2/Nov9/Nov9_72hr_vs_Nov9_mycelium_down.txt",sep="\t",na="",quote=F)

#Make a table of raw counts, normalised counts and fpkm values:

raw_counts <- data.frame(counts(dds, normalized=FALSE))
colnames(raw_counts) <- paste(colData$Group)
write.table(raw_counts,"analysis/DeSeq/Method_2/Nov9/raw_counts.txt",sep="\t",na="",quote=F)
norm_counts <- data.frame(counts(dds, normalized=TRUE))
colnames(norm_counts) <- paste(colData$Group)
write.table(norm_counts,"analysis/DeSeq/Method_2/Nov9/normalised_counts.txt",sep="\t",na="",quote=F)

library(Biostrings)
library(naturalsort)
mygenes <- readDNAStringSet("gene_pred/annotation/P.fragariae/Nov9/Nov9_genes_incl_ORFeffectors_renamed.cdna.fasta")
t1 <- counts(dds)
t1 <- mygenes[rownames(t1)]
rowRanges(dds) <- GRanges(t1@ranges@NAMES,t1@ranges)

# robust may be better set at false to normalise based on total counts rather than 'library normalisation factors'
fpkm_counts <- data.frame(fpkm(dds, robust = TRUE))
colnames(fpkm_counts) <- paste(colData$Group)
write.table(fpkm_counts,"analysis/DeSeq/Method_2/Nov9/fpkm_norm_counts.txt",sep="\t",na="",quote=F)
fpkm_counts <- data.frame(fpkm(dds, robust = FALSE))
colnames(fpkm_counts) <- paste(colData$Group)
write.table(fpkm_counts,"analysis/DeSeq/Method_2/Nov9/fpkm_counts.txt",sep="\t",na="",quote=F)
```

## Use custom python scripts to create lists of genes in orthogroups

### Method 1, extracting names of only genes that are uniquely expressed

Create directories for results

```bash
mkdir -p analysis/DeSeq/Method_1/expression_results/all_genes
mkdir -p analysis/DeSeq/Method_1/expression_results/RxLRs
mkdir -p analysis/DeSeq/Method_1/expression_results/CRNs
mkdir -p analysis/DeSeq/Method_1/expression_results/ApoP
mkdir -p analysis/DeSeq/Method_1/expression_results/Secreted
mkdir -p analysis/DeSeq/Method_1/expression_results/TFs
```

Now generate results

```bash
screen -

qlogin

cd /home/groups/harrisonlab/project_files/phytophthora_fragariae

for Strain in Bc1 Bc16 Nov9
do
    FPKM=analysis/DeSeq/Method_1/$Strain/fpkm_counts.txt
    Orthogroups=analysis/orthology/OrthoFinder/formatted/Results_Aug18/Orthogroups.txt
    Org1=Bc16
    Org2=Bc1
    Org3=Nov9
    FPKM_min=5
    RxLRs=analysis/RxLR_effectors/combined_evidence/P.fragariae/$Strain/"$Strain"_Total_RxLR_motif_hmm_renamed.txt
    CRNs=analysis/CRN_effectors/hmmer_CRN/P.fragariae/$Strain/"$Strain"_final_CRN_renamed.txt
    ApoP=analysis/ApoplastP/P.fragariae/$Strain/"$Strain"_Total_ApoplastP_renamed.txt
    Secreted_CQ=gene_pred/combined_sigP_CQ/P.fragariae/$Strain/"$Strain"_secreted_renamed.txt
    Secreted_ORF=gene_pred/combined_sigP_ORF/P.fragariae/$Strain/"$Strain"_all_secreted_merged_renamed.txt
    TFs=analysis/transcription_factors/P.fragariae/$Strain/greedy/"$Strain"_TF_TR_Headers.txt
    OutDir=analysis/DeSeq/Method_1/expression_results
    Scripts=/home/adamst/git_repos/scripts/phytophthora_fragariae/RNA_Seq_scripts
    python $Scripts/Identify_unique_Expressed_Genes.py --FPKM_in $FPKM --Orthogroup_in $Orthogroups --Reference_name $Strain --Organism_1 $Org1 --Organism_2 $Org2 --Organism_3 $Org3 --FPKM_min $FPKM_min --RxLRs $RxLRs --CRNs $CRNs --ApoP $ApoP --Secreted_CQ $Secreted_CQ --Secreted_ORF $Secreted_ORF --TFs $TFs --OutDir $OutDir
    echo "$Strain done"
done
```

Now enumerate numbers of genes that are uniquely expressed

```bash
for Strain in Bc16 Bc1 Nov9
do
    OutDir=analysis/DeSeq/Method_1/expression_results
    echo "Analysis using $Strain as the reference genome:"
    printf "\n"
    Uniq_Bc16=$OutDir/all_genes/"$Strain"_Bc16_expressed_unique.txt
    Uniq_Bc1=$OutDir/all_genes/"$Strain"_Bc1_expressed_unique.txt
    Uniq_Nov9=$OutDir/all_genes/"$Strain"_Nov9_expressed_unique.txt
    echo "The number of BC-16 uniquely expressed genes is:"
    cat $Uniq_Bc16 | tail -n +2 | wc -l
    echo "The number of BC-1 uniquely expressed genes is:"
    cat $Uniq_Bc1 | tail -n +2 | wc -l
    echo "The number of NOV-9 uniquely expressed genes is:"
    cat $Uniq_Nov9 | tail -n +2 | wc -l
    Uniq_RxLRs_Bc16=$OutDir/RxLRs/"$Strain"_Bc16_expressed_unique_RxLRs.txt
    Uniq_RxLRs_Bc1=$OutDir/RxLRs/"$Strain"_Bc1_expressed_unique_RxLRs.txt
    Uniq_RxLRs_Nov9=$OutDir/RxLRs/"$Strain"_Nov9_expressed_unique_RxLRs.txt
    echo "The number of BC-16 uniquely expressed RxLRs is:"
    cat $Uniq_RxLRs_Bc16 | tail -n +2 | wc -l
    echo "The number of BC-1 uniquely expressed RxLRs is:"
    cat $Uniq_RxLRs_Bc1 | tail -n +2 | wc -l
    echo "The number of NOV-9 uniquely expressed RxLRs is:"
    cat $Uniq_RxLRs_Nov9 | tail -n +2 | wc -l
    Uniq_CRNs_Bc16=$OutDir/CRNs/"$Strain"_Bc16_expressed_unique_CRNs.txt
    Uniq_CRNs_Bc1=$OutDir/CRNs/"$Strain"_Bc1_expressed_unique_CRNs.txt
    Uniq_CRNs_Nov9=$OutDir/CRNs/"$Strain"_Nov9_expressed_unique_CRNs.txt
    echo "The number of BC-16 uniquely expressed CRNs is:"
    cat $Uniq_CRNs_Bc16 | tail -n +2 | wc -l
    echo "The number of BC-1 uniquely expressed CRNs is:"
    cat $Uniq_CRNs_Bc1 | tail -n +2 | wc -l
    echo "The number of NOV-9 uniquely expressed CRNs is:"
    cat $Uniq_CRNs_Nov9 | tail -n +2 | wc -l
    Uniq_ApoP_Bc16=$OutDir/ApoP/"$Strain"_Bc16_expressed_unique_ApoP.txt
    Uniq_ApoP_Bc1=$OutDir/ApoP/"$Strain"_Bc1_expressed_unique_ApoP.txt
    Uniq_ApoP_Nov9=$OutDir/ApoP/"$Strain"_Nov9_expressed_unique_ApoP.txt
    echo "The number of BC-16 uniquely expressed apoplastic effectors is:"
    cat $Uniq_ApoP_Bc16 | tail -n +2 | wc -l
    echo "The number of BC-1 uniquely expressed apoplastic effectors is:"
    cat $Uniq_ApoP_Bc1 | tail -n +2 | wc -l
    echo "The number of NOV-9 uniquely expressed apoplastic effectors is:"
    cat $Uniq_ApoP_Nov9 | tail -n +2 | wc -l
    Uniq_Sec_Bc16=$OutDir/Secreted/"$Strain"_Bc16_expressed_unique_secreted.txt
    Uniq_Sec_Bc1=$OutDir/Secreted/"$Strain"_Bc1_expressed_unique_secreted.txt
    Uniq_Sec_Nov9=$OutDir/Secreted/"$Strain"_Nov9_expressed_unique_secreted.txt
    echo "The number of BC-16 uniquely expressed secreted proteins is:"
    cat $Uniq_Sec_Bc16 | tail -n +2 | wc -l
    echo "The number of BC-1 uniquely expressed secreted proteins is:"
    cat $Uniq_Sec_Bc1 | tail -n +2 | wc -l
    echo "The number of NOV-9 uniquely expressed secreted proteins is:"
    cat $Uniq_Sec_Nov9 | tail -n +2 | wc -l
    Uniq_TFs_Bc16=$OutDir/TFs/"$Strain"_Bc16_expressed_unique_TFs.txt
    Uniq_TFs_Bc1=$OutDir/TFs/"$Strain"_Bc1_expressed_unique_TFs.txt
    Uniq_TFs_Nov9=$OutDir/TFs/"$Strain"_Nov9_expressed_unique_TFs.txt
    echo "The number of BC-16 uniquely expressed TFs is:"
    cat $Uniq_TFs_Bc16 | tail -n +2 | wc -l
    echo "The number of BC-1 uniquely expressed TFs is:"
    cat $Uniq_TFs_Bc1 | tail -n +2 | wc -l
    echo "The number of NOV-9 uniquely expressed TFs is:"
    cat $Uniq_TFs_Nov9 | tail -n +2 | wc -l
    printf "\n"
done
```

```
Analysis using Bc16 as the reference genome:

The number of BC-16 uniquely expressed genes is:
1,630
The number of BC-1 uniquely expressed genes is:
90
The number of NOV-9 uniquely expressed genes is:
482
The number of BC-16 uniquely expressed RxLRs is:
49
The number of BC-1 uniquely expressed RxLRs is:
3
The number of NOV-9 uniquely expressed RxLRs is:
10
The number of BC-16 uniquely expressed CRNs is:
3
The number of BC-1 uniquely expressed CRNs is:
0
The number of NOV-9 uniquely expressed CRNs is:
5
The number of BC-16 uniquely expressed apoplastic effectors is:
207
The number of BC-1 uniquely expressed apoplastic effectors is:
13
The number of NOV-9 uniquely expressed apoplastic effectors is:
59
The number of BC-16 uniquely expressed secreted proteins is:
380
The number of BC-1 uniquely expressed secreted proteins is:
21
The number of NOV-9 uniquely expressed secreted proteins is:
96
The number of BC-16 uniquely expressed TFs is:
24
The number of BC-1 uniquely expressed TFs is:
2
The number of NOV-9 uniquely expressed TFs is:
0

Analysis using Bc1 as the reference genome:

The number of BC-16 uniquely expressed genes is:
2,125
The number of BC-1 uniquely expressed genes is:
175
The number of NOV-9 uniquely expressed genes is:
869
The number of BC-16 uniquely expressed RxLRs is:
70
The number of BC-1 uniquely expressed RxLRs is:
6
The number of NOV-9 uniquely expressed RxLRs is:
37
The number of BC-16 uniquely expressed CRNs is:
2
The number of BC-1 uniquely expressed CRNs is:
0
The number of NOV-9 uniquely expressed CRNs is:
8
The number of BC-16 uniquely expressed apoplastic effectors is:
245
The number of BC-1 uniquely expressed apoplastic effectors is:
21
The number of NOV-9 uniquely expressed apoplastic effectors is:
171
The number of BC-16 uniquely expressed secreted proteins is:
477
The number of BC-1 uniquely expressed secreted proteins is:
38
The number of NOV-9 uniquely expressed secreted proteins is:
231
The number of BC-16 uniquely expressed TFs is:
22
The number of BC-1 uniquely expressed TFs is:
1
The number of NOV-9 uniquely expressed TFs is:
3

Analysis using Nov9 as the reference genome:

The number of BC-16 uniquely expressed genes is:
2,117
The number of BC-1 uniquely expressed genes is:
883
The number of NOV-9 uniquely expressed genes is:
502
The number of BC-16 uniquely expressed RxLRs is:
68
The number of BC-1 uniquely expressed RxLRs is:
48
The number of NOV-9 uniquely expressed RxLRs is:
16
The number of BC-16 uniquely expressed CRNs is:
0
The number of BC-1 uniquely expressed CRNs is:
5
The number of NOV-9 uniquely expressed CRNs is:
3
The number of BC-16 uniquely expressed apoplastic effectors is:
280
The number of BC-1 uniquely expressed apoplastic effectors is:
169
The number of NOV-9 uniquely expressed apoplastic effectors is:
79
The number of BC-16 uniquely expressed secreted proteins is:
512
The number of BC-1 uniquely expressed secreted proteins is:
233
The number of NOV-9 uniquely expressed secreted proteins is:
112
The number of BC-16 uniquely expressed TFs is:
23
The number of BC-1 uniquely expressed TFs is:
1
The number of NOV-9 uniquely expressed TFs is:
1
```

### Method 1, extracting names of only genes that are uniquely differentially expressed

Create directories for results

```bash
mkdir -p analysis/DeSeq/Method_1/DEG_results/all_genes
mkdir -p analysis/DeSeq/Method_1/DEG_results/RxLRs
mkdir -p analysis/DeSeq/Method_1/DEG_results/CRNs
mkdir -p analysis/DeSeq/Method_1/DEG_results/ApoP
mkdir -p analysis/DeSeq/Method_1/DEG_results/Secreted
mkdir -p analysis/DeSeq/Method_1/DEG_results/TFs
```

Now generate results

```bash
for Strain in Bc1 Bc16 Nov9
do
    DEG_files=$(ls analysis/DeSeq/Method_1/$Strain/*.txt | grep -e "up" -e "down")
    Orthogroups=analysis/orthology/OrthoFinder/formatted/Results_Aug18/Orthogroups.txt
    Min_LFC=3
    Min_Pval=0.05
    Org1=Bc16
    Org2=Bc1
    Org3=Nov9
    OutDir=analysis/DeSeq/Method_1/DEG_results
    RxLRs=analysis/RxLR_effectors/combined_evidence/P.fragariae/$Strain/"$Strain"_Total_RxLR_motif_hmm_renamed.txt
    CRNs=analysis/CRN_effectors/hmmer_CRN/P.fragariae/$Strain/"$Strain"_final_CRN_renamed.txt
    ApoP=analysis/ApoplastP/P.fragariae/$Strain/"$Strain"_Total_ApoplastP_renamed.txt
    Sec_CQ=gene_pred/combined_sigP_CQ/P.fragariae/$Strain/"$Strain"_secreted_renamed.txt
    Sec_ORF=gene_pred/combined_sigP_ORF/P.fragariae/$Strain/"$Strain"_all_secreted_merged_renamed.txt
    TFs=analysis/transcription_factors/P.fragariae/$Strain/greedy/"$Strain"_TF_TR_Headers.txt
    ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae/RNA_Seq_scripts
    python $ProgDir/Extract_pairwise_DEG_names.py --DEG_files $DEG_files --Orthogroup_in $Orthogroups --Reference_name $Strain --Min_LFC $Min_LFC --Sig_Level $Min_Pval --Organism_1 $Org1 --Organism_2 $Org2 --Organism_3 $Org3 --OutDir $OutDir --RxLRs $RxLRs --CRNs $CRNs --ApoP $ApoP --Secreted_CQ $Sec_CQ --Secreted_ORF $Sec_ORF --TFs $TFs
    echo "$Strain done"
done
```

Now enumerate numbers of genes that are differently differentially expressed

```bash
for Strain in Bc16 Bc1 Nov9
do
    OutDir=analysis/DeSeq/Method_1/DEG_results
    echo "Analysis using $Strain as the reference genome:"
    printf "\n"
    Uniq_Bc16=$OutDir/all_genes/"$Strain"_Bc16_unique_DEGs.txt
    Uniq_Bc1=$OutDir/all_genes/"$Strain"_Bc1_unique_DEGs.txt
    Uniq_Nov9=$OutDir/all_genes/"$Strain"_Nov9_unique_DEGs.txt
    echo "The number of BC-16 differently differentially expressed genes is:"
    cat $Uniq_Bc16 | tail -n +2 | wc -l
    echo "The number of BC-1 differently differentially expressed genes is:"
    cat $Uniq_Bc1 | tail -n +2 | wc -l
    echo "The number of NOV-9 differently differentially expressed genes is:"
    cat $Uniq_Nov9 | tail -n +2 | wc -l
    Uniq_RxLRs_Bc16=$OutDir/RxLRs/"$Strain"_Bc16_unique_DEGs_RxLRs.txt
    Uniq_RxLRs_Bc1=$OutDir/RxLRs/"$Strain"_Bc1_unique_DEGs_RxLRs.txt
    Uniq_RxLRs_Nov9=$OutDir/RxLRs/"$Strain"_Nov9_unique_DEGs_RxLRs.txt
    echo "The number of BC-16 differently differentially expressed RxLRs is:"
    cat $Uniq_RxLRs_Bc16 | tail -n +2 | wc -l
    echo "The number of BC-1 differently differentially expressed RxLRs is:"
    cat $Uniq_RxLRs_Bc1 | tail -n +2 | wc -l
    echo "The number of NOV-9 differently differentially expressed RxLRs is:"
    cat $Uniq_RxLRs_Nov9 | tail -n +2 | wc -l
    Uniq_CRNs_Bc16=$OutDir/CRNs/"$Strain"_Bc16_unique_DEGs_CRNs.txt
    Uniq_CRNs_Bc1=$OutDir/CRNs/"$Strain"_Bc1_unique_DEGs_CRNs.txt
    Uniq_CRNs_Nov9=$OutDir/CRNs/"$Strain"_Nov9_unique_DEGs_CRNs.txt
    echo "The number of BC-16 differently differentially expressed CRNs is:"
    cat $Uniq_CRNs_Bc16 | tail -n +2 | wc -l
    echo "The number of BC-1 differently differentially expressed CRNs is:"
    cat $Uniq_CRNs_Bc1 | tail -n +2 | wc -l
    echo "The number of NOV-9 differently differentially expressed CRNs is:"
    cat $Uniq_CRNs_Nov9 | tail -n +2 | wc -l
    Uniq_ApoP_Bc16=$OutDir/ApoP/"$Strain"_Bc16_unique_DEGs_ApoP.txt
    Uniq_ApoP_Bc1=$OutDir/ApoP/"$Strain"_Bc1_unique_DEGs_ApoP.txt
    Uniq_ApoP_Nov9=$OutDir/ApoP/"$Strain"_Nov9_unique_DEGs_ApoP.txt
    echo "The number of BC-16 differently differentially expressed apoplastic effectors is:"
    cat $Uniq_ApoP_Bc16 | tail -n +2 | wc -l
    echo "The number of BC-1 differently differentially expressed apoplastic effectors is:"
    cat $Uniq_ApoP_Bc1 | tail -n +2 | wc -l
    echo "The number of NOV-9 differently differentially expressed apoplastic effectors is:"
    cat $Uniq_ApoP_Nov9 | tail -n +2 | wc -l
    Uniq_Sec_Bc16=$OutDir/Secreted/"$Strain"_Bc16_unique_DEGs_Secreted.txt
    Uniq_Sec_Bc1=$OutDir/Secreted/"$Strain"_Bc1_unique_DEGs_Secreted.txt
    Uniq_Sec_Nov9=$OutDir/Secreted/"$Strain"_Nov9_unique_DEGs_Secreted.txt
    echo "The number of BC-16 differently differentially expressed secreted proteins is:"
    cat $Uniq_Sec_Bc16 | tail -n +2 | wc -l
    echo "The number of BC-1 differently differentially expressed secreted proteins is:"
    cat $Uniq_Sec_Bc1 | tail -n +2 | wc -l
    echo "The number of NOV-9 differently differentially expressed secreted proteins is:"
    cat $Uniq_Sec_Nov9 | tail -n +2 | wc -l
    Uniq_TFs_Bc16=$OutDir/TFs/"$Strain"_Bc16_unique_DEGs_TFs.txt
    Uniq_TFs_Bc1=$OutDir/TFs/"$Strain"_Bc1_unique_DEGs_TFs.txt
    Uniq_TFs_Nov9=$OutDir/TFs/"$Strain"_Nov9_unique_DEGs_TFs.txt
    echo "The number of BC-16 differently differentially expressed TFs/TRs is:"
    cat $Uniq_TFs_Bc16 | tail -n +2 | wc -l
    echo "The number of BC-1 differently differentially expressed TFs/TRs is:"
    cat $Uniq_TFs_Bc1 | tail -n +2 | wc -l
    echo "The number of NOV-9 differently differentially expressed TFs/TRs is:"
    cat $Uniq_TFs_Nov9 | tail -n +2 | wc -l
    printf "\n"
done
```

```
Analysis using Bc16 as the reference genome:

The number of BC-16 differently differentially expressed genes is:
142
The number of BC-1 differently differentially expressed genes is:
45
The number of NOV-9 differently differentially expressed genes is:
397
The number of BC-16 differently differentially expressed RxLRs is:
10
The number of BC-1 differently differentially expressed RxLRs is:
1
The number of NOV-9 differently differentially expressed RxLRs is:
11
The number of BC-16 differently differentially expressed CRNs is:
0
The number of BC-1 differently differentially expressed CRNs is:
0
The number of NOV-9 differently differentially expressed CRNs is:
2
The number of BC-16 differently differentially expressed apoplastic effectors is:
13
The number of BC-1 differently differentially expressed apoplastic effectors is:
1
The number of NOV-9 differently differentially expressed apoplastic effectors is:
9
The number of BC-16 differently differentially expressed secreted proteins is:
33
The number of BC-1 differently differentially expressed secreted proteins is:
5
The number of NOV-9 differently differentially expressed secreted proteins is:
67
The number of BC-16 differently differentially expressed TFs/TRs is:
0
The number of BC-1 differently differentially expressed TFs/TRs is:
2
The number of NOV-9 differently differentially expressed TFs/TRs is:
2

Analysis using Bc1 as the reference genome:

The number of BC-16 differently differentially expressed genes is:
375
The number of BC-1 differently differentially expressed genes is:
410
The number of NOV-9 differently differentially expressed genes is:
849
The number of BC-16 differently differentially expressed RxLRs is:
17
The number of BC-1 differently differentially expressed RxLRs is:
10
The number of NOV-9 differently differentially expressed RxLRs is:
31
The number of BC-16 differently differentially expressed CRNs is:
0
The number of BC-1 differently differentially expressed CRNs is:
0
The number of NOV-9 differently differentially expressed CRNs is:
6
The number of BC-16 differently differentially expressed apoplastic effectors is:
24
The number of BC-1 differently differentially expressed apoplastic effectors is:
47
The number of NOV-9 differently differentially expressed apoplastic effectors is:
16
The number of BC-16 differently differentially expressed secreted proteins is:
92
The number of BC-1 differently differentially expressed secreted proteins is:
110
The number of NOV-9 differently differentially expressed secreted proteins is:
213
The number of BC-16 differently differentially expressed TFs/TRs is:
3
The number of BC-1 differently differentially expressed TFs/TRs is:
7
The number of NOV-9 differently differentially expressed TFs/TRs is:
6

Analysis using Nov9 as the reference genome:

The number of BC-16 differently differentially expressed genes is:
411
The number of BC-1 differently differentially expressed genes is:
759
The number of NOV-9 differently differentially expressed genes is:
1,149
The number of BC-16 differently differentially expressed RxLRs is:
23
The number of BC-1 differently differentially expressed RxLRs is:
41
The number of NOV-9 differently differentially expressed RxLRs is:
33
The number of BC-16 differently differentially expressed CRNs is:
1
The number of BC-1 differently differentially expressed CRNs is:
3
The number of NOV-9 differently differentially expressed CRNs is:
3
The number of BC-16 differently differentially expressed apoplastic effectors is:
60
The number of BC-1 differently differentially expressed apoplastic effectors is:
8
The number of NOV-9 differently differentially expressed apoplastic effectors is:
47
The number of BC-16 differently differentially expressed secreted proteins is:
145
The number of BC-1 differently differentially expressed secreted proteins is:
171
The number of NOV-9 differently differentially expressed secreted proteins is:
218
The number of BC-16 differently differentially expressed TFs/TRs is:
0
The number of BC-1 differently differentially expressed TFs/TRs is:
2
The number of NOV-9 differently differentially expressed TFs/TRs is:
13
```

Now call candidate confidence for each isolate

BC-16, UK2

```bash
for num in 1
do
    Strain=Bc16
    Uniq_Exp_files=$(ls analysis/DeSeq/Method_1/expression_results/all_genes/*_"$Strain"_*expressed_unique.txt)
    Uniq_DEG_files=$(ls analysis/DeSeq/Method_1/DEG_results/all_genes/*_"$Strain"_*unique_DEGs.txt)
    Orthogroups=analysis/orthology/OrthoFinder/formatted/Results_Aug18/Orthogroups.txt
    Org2=Bc1
    Org3=Nov9
    Race_isolates="Bc16 A4"
    RxLRs=analysis/RxLR_effectors/combined_evidence/P.fragariae/$Strain/"$Strain"_Total_RxLR_motif_hmm_renamed.txt
    CRNs=analysis/CRN_effectors/hmmer_CRN/P.fragariae/$Strain/"$Strain"_final_CRN_renamed.txt
    ApoP=analysis/ApoplastP/P.fragariae/$Strain/"$Strain"_Total_ApoplastP_renamed.txt
    Sec_CQ=gene_pred/combined_sigP_CQ/P.fragariae/$Strain/"$Strain"_secreted_renamed.txt
    Sec_ORF=gene_pred/combined_sigP_ORF/P.fragariae/$Strain/"$Strain"_all_secreted_merged_renamed.txt
    TFs=analysis/transcription_factors/P.fragariae/$Strain/greedy/"$Strain"_TF_TR_Headers.txt
    OutDir=analysis/DeSeq/Method_1/candidates
    mkdir -p $OutDir
    ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae/RNA_Seq_scripts
    python $ProgDir/Call_Candidate_Confidence.py --Unique_Expression_Files $Uniq_Exp_files --Differently_DEG_File $Uniq_DEG_files --Orthogroup_in $Orthogroups --Organism_1 $Strain --Organism_2 $Org2 --Organism_3 $Org3 --Race_isolates $Race_isolates --Reference_name $Strain --RxLRs $RxLRs --CRNs $CRNs --ApoP $ApoP --Secreted_CQ $Sec_CQ --Secreted_ORF $Sec_ORF --TFs $TFs --OutDir $OutDir
done
```

BC-1, UK1

```bash
for num in 1
do
    Strain=Bc1
    Uniq_Exp_files=$(ls analysis/DeSeq/Method_1/expression_results/all_genes/*_"$Strain"_*expressed_unique.txt)
    Uniq_DEG_files=$(ls analysis/DeSeq/Method_1/DEG_results/all_genes/*_"$Strain"_*unique_DEGs.txt)
    Orthogroups=analysis/orthology/OrthoFinder/formatted/Results_Aug18/Orthogroups.txt
    Org2=Bc16
    Org3=Nov9
    Race_isolates="Bc1 Nov5"
    RxLRs=analysis/RxLR_effectors/combined_evidence/P.fragariae/$Strain/"$Strain"_Total_RxLR_motif_hmm_renamed.txt
    CRNs=analysis/CRN_effectors/hmmer_CRN/P.fragariae/$Strain/"$Strain"_final_CRN_renamed.txt
    ApoP=analysis/ApoplastP/P.fragariae/$Strain/"$Strain"_Total_ApoplastP_renamed.txt
    Sec_CQ=gene_pred/combined_sigP_CQ/P.fragariae/$Strain/"$Strain"_secreted_renamed.txt
    Sec_ORF=gene_pred/combined_sigP_ORF/P.fragariae/$Strain/"$Strain"_all_secreted_merged_renamed.txt
    TFs=analysis/transcription_factors/P.fragariae/$Strain/greedy/"$Strain"_TF_TR_Headers.txt
    OutDir=analysis/DeSeq/Method_1/candidates
    mkdir -p $OutDir
    ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae/RNA_Seq_scripts
    python $ProgDir/Call_Candidate_Confidence.py --Unique_Expression_Files $Uniq_Exp_files --Differently_DEG_File $Uniq_DEG_files --Orthogroup_in $Orthogroups --Organism_1 $Strain --Organism_2 $Org2 --Organism_3 $Org3 --Race_isolates $Race_isolates --Reference_name $Strain --RxLRs $RxLRs --CRNs $CRNs --ApoP $ApoP --Secreted_CQ $Sec_CQ --Secreted_ORF $Sec_ORF --TFs $TFs --OutDir $OutDir
done
```

NOV-9, UK3

```bash
for num in 1
do
    Strain=Nov9
    Uniq_Exp_files=$(ls analysis/DeSeq/Method_1/expression_results/all_genes/*_"$Strain"_*expressed_unique.txt)
    Uniq_DEG_files=$(ls analysis/DeSeq/Method_1/DEG_results/all_genes/*_"$Strain"_*unique_DEGs.txt)
    Orthogroups=analysis/orthology/OrthoFinder/formatted/Results_Aug18/Orthogroups.txt
    Org2=Bc16
    Org3=Bc1
    Race_isolates="Nov9 Nov27 Nov71"
    RxLRs=analysis/RxLR_effectors/combined_evidence/P.fragariae/$Strain/"$Strain"_Total_RxLR_motif_hmm._renamedtxt
    CRNs=analysis/CRN_effectors/hmmer_CRN/P.fragariae/$Strain/"$Strain"_final_CRN_renamed.txt
    ApoP=analysis/ApoplastP/P.fragariae/$Strain/"$Strain"_Total_ApoplastP_renamed.txt
    Sec_CQ=gene_pred/combined_sigP_CQ/P.fragariae/$Strain/"$Strain"_secreted_renamed.txt
    Sec_ORF=gene_pred/combined_sigP_ORF/P.fragariae/$Strain/"$Strain"_all_secreted_merged_renamed.txt
    TFs=analysis/transcription_factors/P.fragariae/$Strain/greedy/"$Strain"_TF_TR_Headers.txt
    OutDir=analysis/DeSeq/Method_1/candidates
    mkdir -p $OutDir
    ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae/RNA_Seq_scripts
    python $ProgDir/Call_Candidate_Confidence.py --Unique_Expression_Files $Uniq_Exp_files --Differently_DEG_File $Uniq_DEG_files --Orthogroup_in $Orthogroups --Organism_1 $Strain --Organism_2 $Org2 --Organism_3 $Org3 --Race_isolates $Race_isolates --Reference_name $Strain --RxLRs $RxLRs --CRNs $CRNs --ApoP $ApoP --Secreted_CQ $Sec_CQ --Secreted_ORF $Sec_ORF --TFs $TFs --OutDir $OutDir
done
```

Then enumerate the numbers of each gene and each type of effector

```bash
for Strain in Bc16 Bc1 Nov9
do
    echo "Analysis of $Strain"
    printf "\n"
    echo "The number of candidate genes regardless of confidence is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | wc -l
    echo "The number of candidate RxLRs regardless of confidence is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | cut -f11 | grep 'Yes' | wc -l
    echo "The number of candidate CRNs regardless of confidence is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | cut -f12 | grep 'Yes' | wc -l
    echo "The number of candidate apoplastic effectors regardless of confidence is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | cut -f13 | grep 'Yes' | wc -l
    echo "The number of candidate secreted proteins regardless of confidence level is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | cut -f14 | grep 'Yes' | wc -l
    echo "The number of candidate TFs/TRs regardless of confidence level is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | cut -f15 | grep 'Yes' | wc -l
    echo "The number of genes of confidence level 6 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "6" | wc -l
    echo "The number of RxLRs of confidence level 6 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "6" | cut -f11 | grep 'Yes' | wc -l
    echo "The number of CRNs of confidence level 6 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "6" | cut -f12 | grep 'Yes' | wc -l
    echo "The number of apoplastic effectors of confidence level 6 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "6" | cut -f13 | grep 'Yes' | wc -l
    echo "The number of secreted proteins of confidence level 6 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "6" | cut -f14 | grep 'Yes' | wc -l
    echo "The number of TFs/TRs of confidence level 6 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "6" | cut -f15 | grep 'Yes' | wc -l
    echo "The number of genes of confidence level 5 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "5" | wc -l
    echo "The number of RxLRs of confidence level 5 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "5" | cut -f11 | grep 'Yes' | wc -l
    echo "The number of CRNs of confidence level 5 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "5" | cut -f12 | grep 'Yes' | wc -l
    echo "The number of apoplastic effectors of confidence level 5 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "5" | cut -f13 | grep 'Yes' | wc -l
    echo "The number of secreted proteins of confidence level 5 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "5" | cut -f14 | grep 'Yes' | wc -l
    echo "The number of TFs/TRs of confidence level 5 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "5" | cut -f15 | grep 'Yes' | wc -l
    echo "The number of genes of confidence level 4 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "4" | wc -l
    echo "The number of RxLRs of confidence level 4 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "4" | cut -f11 | grep 'Yes' | wc -l
    echo "The number of CRNs of confidence level 4 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "4" | cut -f12 | grep 'Yes' | wc -l
    echo "The number of apoplastic effectors of confidence level 4 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "4" | cut -f13 | grep 'Yes' | wc -l
    echo "The number of secreted proteins of confidence level 4 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "4" | cut -f14 | grep 'Yes' | wc -l
    echo "The number of TFs/TRs of confidence level 4 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "4" | cut -f15 | grep 'Yes' | wc -l
    echo "The number of genes of confidence level 3 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "3" | wc -l
    echo "The number of RxLRs of confidence level 3 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "3" | cut -f11 | grep 'Yes' | wc -l
    echo "The number of CRNs of confidence level 3 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "3" | cut -f12 | grep 'Yes' | wc -l
    echo "The number of apoplastic effectors of confidence level 3 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "3" | cut -f13 | grep 'Yes' | wc -l
    echo "The number of secreted proteins of confidence level 3 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "3" | cut -f14 | grep 'Yes' | wc -l
    echo "The number of TFs/TRs of confidence level 3 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "3" | cut -f15 | grep 'Yes' | wc -l
    echo "The number of genes of confidence level 2 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "2" | wc -l
    echo "The number of RxLRs of confidence level 2 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "2" | cut -f11 | grep 'Yes' | wc -l
    echo "The number of CRNs of confidence level 2 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "2" | cut -f12 | grep 'Yes' | wc -l
    echo "The number of apoplastic effectors of confidence level 2 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "2" | cut -f13 | grep 'Yes' | wc -l
    echo "The number of secreted proteins of confidence level 2 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "2" | cut -f14 | grep 'Yes' | wc -l
    echo "The number of TFs/TRs of confidence level 2 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "2" | cut -f15 | grep 'Yes' | wc -l
    echo "The number of genes of confidence level 1 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "1" | wc -l
    echo "The number of RxLRs of confidence level 1 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "1" | cut -f11 | grep 'Yes' | wc -l
    echo "The number of CRNs of confidence level 1 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "1" | cut -f12 | grep 'Yes' | wc -l
    echo "The number of apoplastic effectors of confidence level 1 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "1" | cut -f13 | grep 'Yes' | wc -l
    echo "The number of secreted proteins of confidence level 1 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "1" | cut -f14 | grep 'Yes' | wc -l
    echo "The number of TFs/TRs of confidence level 1 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "1" | cut -f15 | grep 'Yes' | wc -l
    echo "The number of genes of confidence level 0 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "0" | wc -l
    echo "The number of RxLRs of confidence level 0 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "0" | cut -f11 | grep 'Yes' | wc -l
    echo "The number of CRNs of confidence level 0 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "0" | cut -f12 | grep 'Yes' | wc -l
    echo "The number of apoplastic effectors of confidence level 0 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "0" | cut -f13 | grep 'Yes' | wc -l
    echo "The number of secreted proteins of confidence level 0 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "0" | cut -f14 | grep 'Yes' | wc -l
    echo "The number of TFs/TRs of confidence level 0 is:"
    cat analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv | tail -n +2 | grep -w "0" | cut -f15 | grep 'Yes' | wc -l
    printf "\n"
done
```

```
Analysis of Bc16

The number of candidate genes regardless of confidence is:
302
The number of candidate RxLRs regardless of confidence is:
51
The number of candidate CRNs regardless of confidence is:
2
The number of candidate apoplastic effectors regardless of confidence is:
91
The number of candidate secreted proteins regardless of confidence level is:
272
The number of candidate TFs/TRs regardless of confidence level is:
23
The number of genes of confidence level 6 is:
14
The number of RxLRs of confidence level 6 is:
5
The number of CRNs of confidence level 6 is:
0
The number of apoplastic effectors of confidence level 6 is:
4
The number of secreted proteins of confidence level 6 is:
13
The number of TFs/TRs of confidence level 6 is:
0
The number of genes of confidence level 5 is:
4
The number of RxLRs of confidence level 5 is:
0
The number of CRNs of confidence level 5 is:
0
The number of apoplastic effectors of confidence level 5 is:
3
The number of secreted proteins of confidence level 5 is:
4
The number of TFs/TRs of confidence level 5 is:
0
The number of genes of confidence level 4 is:
24
The number of RxLRs of confidence level 4 is:
8
The number of CRNs of confidence level 4 is:
0
The number of apoplastic effectors of confidence level 4 is:
11
The number of secreted proteins of confidence level 4 is:
24
The number of TFs/TRs of confidence level 4 is:
0
The number of genes of confidence level 3 is:
172
The number of RxLRs of confidence level 3 is:
24
The number of CRNs of confidence level 3 is:
0
The number of apoplastic effectors of confidence level 3 is:
49
The number of secreted proteins of confidence level 3 is:
156
The number of TFs/TRs of confidence level 3 is:
15
The number of genes of confidence level 2 is:
46
The number of RxLRs of confidence level 2 is:
6
The number of CRNs of confidence level 2 is:
2
The number of apoplastic effectors of confidence level 2 is:
14
The number of secreted proteins of confidence level 2 is:
37
The number of TFs/TRs of confidence level 2 is:
5
The number of genes of confidence level 1 is:
42
The number of RxLRs of confidence level 1 is:
8
The number of CRNs of confidence level 1 is:
0
The number of apoplastic effectors of confidence level 1 is:
10
The number of secreted proteins of confidence level 1 is:
38
The number of TFs/TRs of confidence level 1 is:
3
The number of genes of confidence level 0 is:
0
The number of RxLRs of confidence level 0 is:
0
The number of CRNs of confidence level 0 is:
0
The number of apoplastic effectors of confidence level 0 is:
0
The number of secreted proteins of confidence level 0 is:
0
The number of TFs/TRs of confidence level 0 is:
0

Analysis of Bc1

The number of candidate genes regardless of confidence is:
114
The number of candidate RxLRs regardless of confidence is:
16
The number of candidate CRNs regardless of confidence is:
0
The number of candidate apoplastic effectors regardless of confidence is:
51
The number of candidate secreted proteins regardless of confidence level is:
107
The number of candidate TFs/TRs regardless of confidence level is:
7
The number of genes of confidence level 6 is:
0
The number of RxLRs of confidence level 6 is:
0
The number of CRNs of confidence level 6 is:
0
The number of apoplastic effectors of confidence level 6 is:
0
The number of secreted proteins of confidence level 6 is:
0
The number of TFs/TRs of confidence level 6 is:
0
The number of genes of confidence level 5 is:
0
The number of RxLRs of confidence level 5 is:
0
The number of CRNs of confidence level 5 is:
0
The number of apoplastic effectors of confidence level 5 is:
0
The number of secreted proteins of confidence level 5 is:
0
The number of TFs/TRs of confidence level 5 is:
0
The number of genes of confidence level 4 is:
2
The number of RxLRs of confidence level 4 is:
0
The number of CRNs of confidence level 4 is:
0
The number of apoplastic effectors of confidence level 4 is:
0
The number of secreted proteins of confidence level 4 is:
1
The number of TFs/TRs of confidence level 4 is:
1
The number of genes of confidence level 3 is:
1
The number of RxLRs of confidence level 3 is:
0
The number of CRNs of confidence level 3 is:
0
The number of apoplastic effectors of confidence level 3 is:
0
The number of secreted proteins of confidence level 3 is:
1
The number of TFs/TRs of confidence level 3 is:
0
The number of genes of confidence level 2 is:
11
The number of RxLRs of confidence level 2 is:
3
The number of CRNs of confidence level 2 is:
0
The number of apoplastic effectors of confidence level 2 is:
2
The number of secreted proteins of confidence level 2 is:
10
The number of TFs/TRs of confidence level 2 is:
1
The number of genes of confidence level 1 is:
100
The number of RxLRs of confidence level 1 is:
13
The number of CRNs of confidence level 1 is:
0
The number of apoplastic effectors of confidence level 1 is:
49
The number of secreted proteins of confidence level 1 is:
95
The number of TFs/TRs of confidence level 1 is:
5
The number of genes of confidence level 0 is:
0
The number of RxLRs of confidence level 0 is:
0
The number of CRNs of confidence level 0 is:
0
The number of apoplastic effectors of confidence level 0 is:
0
The number of secreted proteins of confidence level 0 is:
0
The number of TFs/TRs of confidence level 0 is:
0

Analysis of Nov9

The number of candidate genes regardless of confidence is:
186
The number of candidate RxLRs regardless of confidence is:
35
The number of candidate CRNs regardless of confidence is:
3
The number of candidate apoplastic effectors regardless of confidence is:
53
The number of candidate secreted proteins regardless of confidence level is:
168
The number of candidate TFs/TRs regardless of confidence level is:
12
The number of genes of confidence level 6 is:
0
The number of RxLRs of confidence level 6 is:
0
The number of CRNs of confidence level 6 is:
0
The number of apoplastic effectors of confidence level 6 is:
0
The number of secreted proteins of confidence level 6 is:
0
The number of TFs/TRs of confidence level 6 is:
0
The number of genes of confidence level 5 is:
0
The number of RxLRs of confidence level 5 is:
0
The number of CRNs of confidence level 5 is:
0
The number of apoplastic effectors of confidence level 5 is:
0
The number of secreted proteins of confidence level 5 is:
0
The number of TFs/TRs of confidence level 5 is:
0
The number of genes of confidence level 4 is:
15
The number of RxLRs of confidence level 4 is:
2
The number of CRNs of confidence level 4 is:
1
The number of apoplastic effectors of confidence level 4 is:
6
The number of secreted proteins of confidence level 4 is:
14
The number of TFs/TRs of confidence level 4 is:
0
The number of genes of confidence level 3 is:
21
The number of RxLRs of confidence level 3 is:
3
The number of CRNs of confidence level 3 is:
2
The number of apoplastic effectors of confidence level 3 is:
3
The number of secreted proteins of confidence level 3 is:
17
The number of TFs/TRs of confidence level 3 is:
2
The number of genes of confidence level 2 is:
28
The number of RxLRs of confidence level 2 is:
6
The number of CRNs of confidence level 2 is:
0
The number of apoplastic effectors of confidence level 2 is:
7
The number of secreted proteins of confidence level 2 is:
26
The number of TFs/TRs of confidence level 2 is:
1
The number of genes of confidence level 1 is:
122
The number of RxLRs of confidence level 1 is:
24
The number of CRNs of confidence level 1 is:
0
The number of apoplastic effectors of confidence level 1 is:
37
The number of secreted proteins of confidence level 1 is:
111
The number of TFs/TRs of confidence level 1 is:
9
The number of genes of confidence level 0 is:
0
The number of RxLRs of confidence level 0 is:
0
The number of CRNs of confidence level 0 is:
0
The number of apoplastic effectors of confidence level 0 is:
0
The number of secreted proteins of confidence level 0 is:
0
The number of TFs/TRs of confidence level 0 is:
0
```

## Produce a more detailed table of analyses

Includes coexpression modules, creation detailed in RNA_Seq_scripts/Co-Expression_Analysis.md
This is only for BC-16, BC-1 and NOV-9 need to be done separate

```bash
Strain=Bc16
for GeneGff in $(ls gene_pred/annotation/P.fragariae/$Strain/"$Strain"_genes_incl_ORFeffectors_renamed.gff3)
do
    Organism=$(echo $GeneGff | rev | cut -f3 -d '/' | rev)
    if [ -f repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    elif [ -f repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    else
        Assembly=$(ls repeat_masked/quiver_results/polished/filtered_contigs_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
        echo $Assembly
    fi
    InterPro=$(ls gene_pred/interproscan/$Organism/$Strain/*_interproscan.tsv)
    SwissProt=$(ls gene_pred/swissprot/$Organism/$Strain/greedy/swissprot_vMar2018_tophit_parsed.tbl)
    OutDir=gene_pred/annotation/$Organism/$Strain
    mkdir -p $OutDir
    # GeneFasta=$(ls gene_pred/annotation/P.cactorum/414_v2/414_v2_genes_incl_ORFeffectors.pep.fasta)
    GeneFasta=$(ls gene_pred/annotation/P.fragariae/$Strain/"$Strain"_genes_incl_ORFeffectors_renamed.cds.fasta)
    SigP2=$(ls gene_pred/final_sigP/$Organism/$Strain/*_aug_sp_renamed.aa)
    SigP2_ORF=$(ls gene_pred/ORF_sigP/$Organism/$Strain/*_aug_sp_renamed.aa)
    SigP3=$(ls gene_pred/final_signalp-3.0/$Organism/$Strain/*_aug_sp_renamed.aa)
    SigP3_ORF=$(ls gene_pred/ORF_signalp-3.0/$Organism/$Strain/*_aug_sp_renamed.aa)
    SigP4=$(ls gene_pred/final_signalp-4.1/$Organism/$Strain/*_aug_sp_renamed.aa)
    SigP4_ORF=$(ls gene_pred/ORF_signalp-4.1/$Organism/$Strain/*_aug_sp_renamed.aa)
    TMHMM_headers=$(ls gene_pred/trans_mem/$Organism/$Strain/greedy/*_TM_genes_pos_headers.txt)
    GPI_headers=$(ls gene_pred/GPIsom/$Organism/$Strain/greedy/GPI_pos.txt)
    PhobiusFa=$(ls analysis/phobius_CQ/$Organism/$Strain/*_phobius_renamed.fa)
    PhobiusFa_ORF=$(ls analysis/phobius_ORF/$Organism/$Strain/*_phobius_renamed.fa)
    #RxLR_Motif=$(ls analysis/RxLR_effectors/RxLR_EER_regex_finder/$Organism/$Strain/*_RxLR_EER_regex.fa | grep -v 'ORF')
    #RxLR_Hmm=$(ls analysis/RxLR_effectors/hmmer_RxLR/$Organism/$Strain/*_RxLR_hmmer.fa | grep -v 'ORF')
    #RxLR_WY=$(ls analysis/RxLR_effectors/hmmer_WY/$Organism/$Strain/*_WY_hmmer_headers.txt | grep -v 'ORF')
    RxLR_total=$(ls analysis/RxLR_effectors/combined_evidence/$Organism/$Strain/*_Total_RxLR_motif_hmm_renamed.txt)
    RxLR_ORF_total=$(ls analysis/RxLR_effectors/combined_evidence/$Organism/$Strain/*_total_ORF_RxLR_headers_renamed.txt)
    RxLR_EER_total=$(ls analysis/RxLR_effectors/combined_evidence/$Organism/$Strain/*_Total_RxLR_EER_motif_hmm_renamed.txt)
    RxLR_EER_ORF_total=$(ls analysis/RxLR_effectors/combined_evidence/$Organism/$Strain/*_total_ORF_RxLR_EER_headers_renamed.txt)
    #CRN_LFLAK=$(ls analysis/CRN_effectors/hmmer_CRN/$Organism/$Strain/*_pub_CRN_LFLAK_hmm.fa | grep -v 'ORF')
    #CRN_DWL=$(ls analysis/CRN_effectors/hmmer_CRN/$Organism/$Strain/*_pub_CRN_DWL_hmm.fa | grep -v 'ORF')
    CRN_total=$(ls analysis/CRN_effectors/hmmer_CRN/$Organism/$Strain/*_final_CRN_renamed.txt)
    ApoP_total=$(ls analysis/ApoplastP/$Organism/$Strain/*_Total_ApoplastP_renamed.txt)
    #	OrthoName=Pcac
    #	OrthoFile=$(ls analysis/orthology/orthomcl/Pcac_Pinf_Ppar_Pcap_Psoj/Pcac_Pinf_Ppar_Pcap_Psoj_orthogroups.txt)
    ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
    DEG_Files=$(ls analysis/DeSeq/Method_*/$Strain/*_vs_*.txt  | grep -v 'Method_3' | grep -v -e 'up' -e 'down' -e "CRN" -e "RxLR" -e "ApoP" | sed -e "s/$/ /g" | tr -d "\n")
    # $ProgDir/pacbio_anntoation_tables.py --gff_format gff3 --gene_gff $GeneGff --gene_fasta $GeneFasta --SigP2 $SigP2 --SigP4 $SigP4 --phobius $PhobiusTxt --RxLR_motif $RxLR_Motif --RxLR_Hmm $RxLR_Hmm --RxLR_WY $RxLR_WY --RxLR_total $RxLR_total --CRN_LFLAK $CRN_LFLAK --CRN_DWL $CRN_DWL --CRN_total $CRN_total --DEG_files $DEG_Files  > $OutDir/414_v2_gene_table_incl_exp.tsv
    # NormCount=$(ls alignment/star/P.cactorum/414_v2/DeSeq/normalised_counts.txt)
    RawCount=$(ls analysis/DeSeq/Method_2/$Strain/raw_counts.txt)
    FPKM=$(ls analysis/DeSeq/Method_2/$Strain/fpkm_counts.txt)
    OrthoName=$Strain
    OrthoFile=analysis/orthology/OrthoFinder/formatted/Results_Aug18/Orthogroups.txt
    Modules=analysis/coexpression/merged_modules/Genes_in_*.txt
    Transcription_factors=analysis/transcription_factors/$Organism/$Strain/greedy/*TF_TR_Headers.txt
    $ProgDir/pacbio_anntoation_tables_modified.py --gff_format gff3 --gene_gff $GeneGff --gene_fasta $GeneFasta --SigP2 $SigP2 --SigP2_ORF $SigP2_ORF --SigP3 $SigP3 --SigP3_ORF $SigP3_ORF --SigP4 $SigP4 --SigP4_ORF $SigP4_ORF --phobius $PhobiusFa --phobius_ORF $PhobiusFa_ORF --trans_mem $TMHMM_headers --GPI_anchor $GPI_headers --RxLR_total $RxLR_total --RxLR_total_ORF $RxLR_ORF_total --RxLR_EER_total $RxLR_EER_total --RxLR_EER_total_ORF $RxLR_EER_ORF_total --CRN_total $CRN_total --ApoP_total $ApoP_total --ortho_name $OrthoName --ortho_file $OrthoFile --DEG_files $DEG_Files --raw_counts $RawCount --fpkm $FPKM --Swissprot $SwissProt --InterPro $InterPro --modules $Modules --Transcription_factors $Transcription_factors > $OutDir/"$Strain"_gene_table_incl_exp.tsv
done

for Strain in Bc1 Nov9
do
    for GeneGff in $(ls gene_pred/annotation/P.fragariae/$Strain/"$Strain"_genes_incl_ORFeffectors_renamed.gff3)
    do
        Organism=$(echo $GeneGff | rev | cut -f3 -d '/' | rev)
        if [ -f repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
        then
            Assembly=$(ls repeat_masked/$Organism/$Strain/ncbi_edits_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
            echo $Assembly
        elif [ -f repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa ]
        then
            Assembly=$(ls repeat_masked/$Organism/$Strain/deconseq_Paen_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
            echo $Assembly
        else
            Assembly=$(ls repeat_masked/quiver_results/polished/filtered_contigs_repmask/*_softmasked_repeatmasker_TPSI_appended.fa)
            echo $Assembly
        fi
        InterPro=$(ls gene_pred/interproscan/$Organism/$Strain/*_interproscan.tsv)
        SwissProt=$(ls gene_pred/swissprot/$Organism/$Strain/greedy/swissprot_vJul2016_tophit_parsed.tbl)
        OutDir=gene_pred/annotation/$Organism/$Strain
        mkdir -p $OutDir
        # GeneFasta=$(ls gene_pred/annotation/P.cactorum/414_v2/414_v2_genes_incl_ORFeffectors.pep.fasta)
        GeneFasta=$(ls gene_pred/annotation/P.fragariae/$Strain/"$Strain"_genes_incl_ORFeffectors_renamed.cds.fasta)
        SigP2=$(ls gene_pred/final_sigP/$Organism/$Strain/*_aug_sp_renamed.aa)
        SigP2_ORF=$(ls gene_pred/ORF_sigP/$Organism/$Strain/*_aug_sp_renamed.aa)
        SigP3=$(ls gene_pred/final_signalp-3.0/$Organism/$Strain/*_aug_sp_renamed.aa)
        SigP3_ORF=$(ls gene_pred/ORF_signalp-3.0/$Organism/$Strain/*_aug_sp_renamed.aa)
        SigP4=$(ls gene_pred/final_signalp-4.1/$Organism/$Strain/*_aug_sp_renamed.aa)
        SigP4_ORF=$(ls gene_pred/ORF_signalp-4.1/$Organism/$Strain/*_aug_sp_renamed.aa)
        TMHMM_headers=$(ls gene_pred/trans_mem/$Organism/$Strain/greedy/*_TM_genes_pos_headers.txt)
        GPI_headers=$(ls gene_pred/GPIsom/$Organism/$Strain/greedy/GPI_pos.txt)
        PhobiusFa=$(ls analysis/phobius_CQ/$Organism/$Strain/*_phobius_renamed.fa)
        PhobiusFa_ORF=$(ls analysis/phobius_ORF/$Organism/$Strain/*_phobius_renamed.fa)
        #RxLR_Motif=$(ls analysis/RxLR_effectors/RxLR_EER_regex_finder/$Organism/$Strain/*_RxLR_EER_regex.fa | grep -v 'ORF')
        #RxLR_Hmm=$(ls analysis/RxLR_effectors/hmmer_RxLR/$Organism/$Strain/*_RxLR_hmmer.fa | grep -v 'ORF')
        #RxLR_WY=$(ls analysis/RxLR_effectors/hmmer_WY/$Organism/$Strain/*_WY_hmmer_headers.txt | grep -v 'ORF')
        RxLR_total=$(ls analysis/RxLR_effectors/combined_evidence/$Organism/$Strain/*_Total_RxLR_motif_hmm_renamed.txt)
        RxLR_ORF_total=$(ls analysis/RxLR_effectors/combined_evidence/$Organism/$Strain/*_total_ORF_RxLR_headers_renamed.txt)
        RxLR_EER_total=$(ls analysis/RxLR_effectors/combined_evidence/$Organism/$Strain/*_Total_RxLR_EER_motif_hmm_renamed.txt)
        RxLR_EER_ORF_total=$(ls analysis/RxLR_effectors/combined_evidence/$Organism/$Strain/*_total_ORF_RxLR_EER_headers_renamed.txt)
        #CRN_LFLAK=$(ls analysis/CRN_effectors/hmmer_CRN/$Organism/$Strain/*_pub_CRN_LFLAK_hmm.fa | grep -v 'ORF')
        #CRN_DWL=$(ls analysis/CRN_effectors/hmmer_CRN/$Organism/$Strain/*_pub_CRN_DWL_hmm.fa | grep -v 'ORF')
        CRN_total=$(ls analysis/CRN_effectors/hmmer_CRN/$Organism/$Strain/*_final_CRN_renamed.txt)
        ApoP_total=$(ls analysis/ApoplastP/$Organism/$Strain/*_Total_ApoplastP_renamed.txt)
        #	OrthoName=Pcac
        #	OrthoFile=$(ls analysis/orthology/orthomcl/Pcac_Pinf_Ppar_Pcap_Psoj/Pcac_Pinf_Ppar_Pcap_Psoj_orthogroups.txt)
        ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
        DEG_Files=$(ls analysis/DeSeq/Method_*/$Strain/*_vs_*.txt  | grep -v 'Method_3' | grep -v -e 'up' -e 'down' -e "CRN" -e "RxLR" -e "ApoP" | sed -e "s/$/ /g" | tr -d "\n")
        # $ProgDir/pacbio_anntoation_tables.py --gff_format gff3 --gene_gff $GeneGff --gene_fasta $GeneFasta --SigP2 $SigP2 --SigP4 $SigP4 --phobius $PhobiusTxt --RxLR_motif $RxLR_Motif --RxLR_Hmm $RxLR_Hmm --RxLR_WY $RxLR_WY --RxLR_total $RxLR_total --CRN_LFLAK $CRN_LFLAK --CRN_DWL $CRN_DWL --CRN_total $CRN_total --DEG_files $DEG_Files  > $OutDir/414_v2_gene_table_incl_exp.tsv
        # NormCount=$(ls alignment/star/P.cactorum/414_v2/DeSeq/normalised_counts.txt)
        RawCount=$(ls analysis/DeSeq/Method_2/$Strain/raw_counts.txt)
        FPKM=$(ls analysis/DeSeq/Method_2/$Strain/fpkm_counts.txt)
        OrthoName=$Strain
        OrthoFile=analysis/orthology/OrthoFinder/formatted/Results_Jan16/Orthogroups.txt
        Transcription_factors=analysis/transcription_factors/$Organism/$Strain/greedy/*TF_TR_Headers.txt
        $ProgDir/pacbio_anntoation_tables_modified_no_coexp.py --gff_format gff3 --gene_gff $GeneGff --gene_fasta $GeneFasta --SigP2 $SigP2 --SigP2_ORF $SigP2_ORF --SigP3 $SigP3 --SigP3_ORF $SigP3_ORF --SigP4 $SigP4 --SigP4_ORF $SigP4_ORF --phobius $PhobiusFa --phobius_ORF $PhobiusFa_ORF --trans_mem $TMHMM_headers --GPI_anchor $GPI_headers --RxLR_total $RxLR_total --RxLR_total_ORF $RxLR_ORF_total --RxLR_EER_total $RxLR_EER_total --RxLR_EER_total_ORF $RxLR_EER_ORF_total --CRN_total $CRN_total --ApoP_total $ApoP_total --ortho_name $OrthoName --ortho_file $OrthoFile --DEG_files $DEG_Files --raw_counts $RawCount --fpkm $FPKM --Swissprot $SwissProt --InterPro $InterPro --Transcription_factors $Transcription_factors > $OutDir/"$Strain"_gene_table_incl_exp.tsv
        (head -n 1 $OutDir/"$Strain"_gene_table_incl_exp.tsv && tail -n +2 $OutDir/"$Strain"_gene_table_incl_exp.tsv | sort | uniq) > $OutDir/"$Strain"_gene_table_incl_exp_nodup.tsv
    done
done
```

Extract details of the candidate genes from annotation tables for visual grepping

```bash
for Strain in Bc16 Bc1 Nov9
do
    candidates=analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs.tsv
    annotation_table=gene_pred/annotation/P.fragariae/$Strain/"$Strain"_gene_table_incl_exp.tsv
    OutFile=analysis/DeSeq/Method_1/candidates/"$Strain"_candidate_avrs_details.tsv
    ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae/RNA_Seq_scripts
    python $ProgDir/Extract_Candidate_Details.py --candidates $candidates --annotation_table $annotation_table --out_file $OutFile
    echo $Strain
done
```

## Investigate enriched functional annotations in DEGs vs all genes for BC-16

### Analysis of DEGs vs all genes

```bash
OutDir=analysis/enrichment/P.fragariae/Bc16/Whole_Genome
mkdir -p $OutDir
InterProTSV=gene_pred/interproscan/P.fragariae/Bc16/Bc16_interproscan.tsv
ProgDir=/home/adamst/git_repos/scripts/fusarium/analysis/gene_enrichment
$ProgDir/GO_prep_table.py --interpro $InterProTSV > $OutDir/Bc16_gene_GO_annots.tsv

ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
AnnotTable=gene_pred/annotation/P.fragariae/Bc16/Bc16_gene_table_incl_exp.tsv
DEGs=alignment/star/P.fragariae/Bc16/DeSeq/Bc16_all_DEGs_names.txt
AllGenes=$OutDir/Bc16_all_genes.txt
cat $AnnotTable | tail -n+2  | cut -f1 > $AllGenes
Set1Genes=$OutDir/Bc16_DEGs.txt
Set2Genes=$OutDir/Bc16_all_genes2.txt
AllGenes=$OutDir/Bc16_all_genes.txt
cat $DEGs | sed -e 's/$/\t0.001/g' > $Set1Genes
cat $AnnotTable | tail -n+2 | cut -f1 | grep -v $Set1Genes | sed -e 's/$/\t1.00/g' > $Set2Genes
cat $Set1Genes $Set2Genes > $AllGenes

$ProgDir/GO_enrichment.r --all_genes $AllGenes --GO_annotations $OutDir/Bc16_gene_GO_annots.tsv --out_dir $OutDir > $OutDir/output.txt
```

## Investigation of candidate gene

A very strong candidate for *Avr2* has been identified from previous analyses
Investigate whether this gene appears to be part of a family or not

### Extract FASTA file of the candidate gene and target genes

Header file created using nano for target - gene ID is g24882.t1

```bash
# Candidate gene
WorkDir=analysis/DeSeq/Method_1/candidates/BLAST_of_candidate
mkdir -p $WorkDir
Headers=$WorkDir/candidate_avr.txt
Fasta=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors_renamed.gene.fasta
ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
$ProgDir/extract_from_fasta.py --fasta $Fasta --headers $Headers > $WorkDir/target.fa

# All RxLRs
Headers=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_Total_RxLR_motif_hmm_renamed.txt
Fasta=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors_renamed.gene.fasta
cp $Headers Bc16_RxLRs.txt
cat Bc16_RxLRs.txt | sed 's/[.]t.//g' > $WorkDir/all_Bc16_RxLRs.txt
$ProgDir/extract_from_fasta.py --fasta $Fasta --headers $WorkDir/all_Bc16_RxLRs.txt > $WorkDir/all_Bc16_RxLRs.fa
input=$WorkDir/all_Bc16_RxLRs.fa
input_modified=$WorkDir/all_Bc16_RxLRs_corrected.fa
# Convert all bases to upper case
cat $input | awk 'BEGIN{FS=" "}{if(!/>/){print toupper($0)}else{print $1}}' \
> $input_modified
rm $input
mv $input_modified $input
# Remove duplicate genes
awk 'BEGIN{RS=">"}NR>1{sub("\n","\t"); gsub("\n",""); print RS$0}' $input | awk '!seen[$1]++' | awk -v OFS="\n" '{print $1,$2}' > $input_modified
rm $input
mv $input_modified $input
```

### Then BLAST against all RxLRs effectors

Run in screen session

```bash
qlogin

cd /home/groups/harrisonlab/project_files/phytophthora_fragariae/analysis/DeSeq/Method_1/candidates/BLAST_of_candidate
Genes=all_Bc16_RxLRs.fa
makeblastdb -in $Genes -input_type fasta -dbtype nucl -out BC-16_RxLRs.db

blastn -db BC-16_RxLRs.db -query target.fa -out candidate_BLAST.tbl -evalue 0.0000000001 -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qlen slen sstrand"
```
