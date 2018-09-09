# Commands to prepare gene annotations and raw reads for submission to NCBI

This appears to be a complex procedure, following Andy's commands in
phytophthora repository. With a few additional scripts I developed.
Bioprojects & Biosamples have already been created.
This is for *P. fragariae* and *P. rubi*

## Raw read submission

Read data was copied for submission to NCBI

```bash
# P.frag Illumina
for Isolate in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    Organism=P.fragariae
    echo "$Organism - $Isolate - Illumina"
    OutDir=genome_submission/$Organism/$Isolate/Reads/SRA
    mkdir -p $OutDir
    for File in $(ls raw_dna/paired/$Organism/$Isolate/*/*.fastq.gz)
    do
        echo $File
        cp $File $OutDir/.
    done
    Read_dir=genome_submission/$Organism/$Isolate/Reads
    tar -czf $Read_dir/PF_"$Isolate"_Illumina_SRA.tar.gz $OutDir
    rm -r $OutDir
done

# P.frag PacBio
for num in 1
do
    Isolate=Bc16
    Organism=P.fragariae
    echo "$Organism - $Isolate - PacBio"
    OutDir=genome_submission/$Organism/$Isolate/Reads/SRA
    mkdir -p $OutDir
    for File in $(ls raw_dna/pacbio/$Organism/$Isolate/extracted/*fastq.gz)
    do
        echo $File
        cp $File $OutDir/.
    done
    Read_dir=genome_submission/$Organism/$Isolate/Reads
    tar -czf $Read_dir/PF_"$Isolate"_PacBio_SRA.tar.gz $OutDir
    rm -r $OutDir
done

# P.frag ONT
for num in 1
do
    Isolate=Nov9
    Isolate_in=NOV-9
    Organism=P.fragariae
    echo "$Organism - $Isolate - ONT"
    OutDir=genome_submission/$Organism/$Isolate/Reads/SRA
    mkdir -p $OutDir
    for File in $(ls raw_dna/minion/$Organism/$Isolate_in/*.fastq.gz)
    do
        echo $File
        cp $File $OutDir/.
    done
    Read_dir=genome_submission/$Organism/$Isolate/Reads
    tar -czf $Read_dir/PF_"$Isolate"_ONT_SRA.tar.gz $OutDir
    rm -r $OutDir
done

# P.rubi Illumina
for Isolate in SCRP249 SCRP324 SCRP333
do
    Organism=P.rubi
    echo "$Organism - $Isolate - Illumina"
    OutDir=genome_submission/$Organism/$Isolate/Reads/SRA
    mkdir -p $OutDir
    for File in $(ls ../phytophthora_rubi/raw_dna/paired/$Organism/$Isolate/*/*.fastq.gz)
    do
        echo $File
        cp $File $OutDir/.
    done
    Read_dir=genome_submission/$Organism/$Isolate/Reads
    tar -czf $Read_dir/PR_"$Isolate"_Illumina_SRA.tar.gz $OutDir
    rm -r $OutDir
done

# RNA-Seq of BC-16
for Isolate in Bc16
do
    Organism=P.fragariae
    echo "$Organism - $Isolate - RNA-Seq"
    OutDir=genome_submission/$Organism/$Isolate/Reads/SRA
    for Timepoint in mycelium 0hr 24hr 48hr 96hr
    do
        mkdir -p $OutDir
        Time=$(echo $Timepoint | sed 's/hr/hpi/g' | sed 's/mycelium/Mycelium/g')
        for File in $(ls raw_rna/novogene/$Organism/$Isolate/$Timepoint/*/*.fq.gz)
        do
            echo $File
            cp $File $OutDir/.
        done
        Read_dir=genome_submission/$Organism/$Isolate/Reads
        tar -czf $Read_dir/PF_BC-16_"$Time"_RNA_SRA.tar.gz $OutDir
        rm -r $OutDir
    done
done

# RNA-Seq of BC-1
for Isolate in Bc1
do
    Organism=P.fragariae
    echo "$Organism - $Isolate - RNA-Seq"
    OutDir=genome_submission/$Organism/$Isolate/Reads/SRA
    for Timepoint in mycelium 48hr
    do
        mkdir -p $OutDir
        Time=$(echo $Timepoint | sed 's/hr/hpi/g' | sed 's/mycelium/Mycelium/g')
        for File in $(ls /data/scratch/adamst/rna_seq/05012018/$Organism/$Isolate/$Timepoint/*/*.fq.gz)
        do
            echo $File
            cp $File $OutDir/.
        done
        Read_dir=genome_submission/$Organism/$Isolate/Reads
        tar -czf $Read_dir/PF_BC-1_"$Time"_RNA_SRA.tar.gz $OutDir
        rm -r $OutDir
    done
done

# RNA-Seq of NOV-9
for Isolate in Nov9
do
    Organism=P.fragariae
    echo "$Organism - $Isolate - RNA-Seq"
    OutDir=genome_submission/$Organism/$Isolate/Reads/SRA
    for Timepoint in mycelium 72hr
    do
        mkdir -p $OutDir
        Time=$(echo $Timepoint | sed 's/hr/hpi/g' | sed 's/mycelium/Mycelium/g')
        for File in $(ls /data/scratch/adamst/rna_seq/05012018/$Organism/$Isolate/$Timepoint/*/*.fq.gz)
        do
            echo $File
            cp $File $OutDir/.
        done
        Read_dir=genome_submission/$Organism/$Isolate/Reads
        tar -czf $Read_dir/PF_NOV-9_"$Time"_RNA_SRA.tar.gz $OutDir
        rm -r $OutDir
    done
done
```

### Submit reads to NCBI

```bash
# P.frag PacBio
Isolate=Bc16
Organism=P.fragariae
cd genome_submission/$Organism/$Isolate/Reads

ftp ftp-private.ncbi.nlm.nih.gov
cd uploads/thomas.adams@emr.ac.uk_tSvQhcry
mkdir SRA_submission
cd SRA_submission
tick
put PF_"$Isolate"_PacBio_SRA.tar.gz
exit

cd ../../../../

# P.frag ONT
Isolate=Nov9
Organism=P.fragariae
cd genome_submission/$Organism/$Isolate/Reads

ftp ftp-private.ncbi.nlm.nih.gov
cd uploads/thomas.adams@emr.ac.uk_tSvQhcry
cd SRA_submission
tick
put PF_"$Isolate"_ONT_SRA.tar.gz
exit

cd ../../../../

# P.frag Illumina
# for Isolate in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
Organism=P.fragariae
cd genome_submission/$Organism/$Isolate/Reads

ftp ftp-private.ncbi.nlm.nih.gov
cd uploads/thomas.adams@emr.ac.uk_tSvQhcry
cd SRA_submission
tick
put PF_"$Isolate"_Illumina_SRA.tar.gz
exit

cd ../../../../

# P.rubi Illumina
# for Isolate in SCRP249 SCRP324 SCRP333
Organism=P.rubi
cd genome_submission/$Organism/$Isolate/Reads
ftp ftp-private.ncbi.nlm.nih.gov
cd uploads/thomas.adams@emr.ac.uk_tSvQhcry
cd SRA_submission
tick
put PR_"$Isolate"_Illumina_SRA.tar.gz
exit

cd ../../../../
```

## Submission steps for annotations

Fasta files were uploaded initially to allow for contamination screen
(See Genbank_corrections.md), however as the MiSeq genomes were submitted as a
batch submission, I have been advised there is no way to update them and the
whole submission has to be repeated.

### Make a table for locus tags

```bash
printf "PF001 SAMN07449679 A4
PF002 SAMN07449680 Bc1
PF003 SAMN07449681 Bc16
PF004 SAMN07449682 Bc23
PF005 SAMN07449683 Nov27
PF006 SAMN07449684 Nov5
PF007 SAMN07449685 Nov71
PF008 SAMN07449686 Nov77
PF009 SAMN07449687 Nov9
PF010 SAMN07449688 ONT3
PF011 SAMN07449689 SCRP245_v2
PR001 SAMN07449690 SCRP249
PR002 SAMN07449691 SCRP324
PR003 SAMN07449692 SCRP333" > genome_submission/Pf_Pr_locus_tags.txt
```

## Prepare files for submission

### Directory structure created

```bash
# P.frag genomes

for Isolate in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    Organism=P.fragariae
    echo "$Organism - $Isolate"
    OutDir=genome_submission/$Organism/$Isolate
    mkdir -p $OutDir
done

# P.rubi Illumina genomes

for Isolate in SCRP249 SCRP324 SCRP333
do
    Organism=P.rubi
    echo "$Organism - $Isolate"
    OutDir=genome_submission/$Organism/$Isolate
    mkdir -p $OutDir
done
```

### Sbt file

A template was created from the genbank template tool for A4. The Biosample
was then modified for each isolate. File transferred by scp and modified with
nano. URL below:

```
http://www.ncbi.nlm.nih.gov/WebSub/template.cgi
```

#### Correct duplicate genes - preferentially keep effector calls

```bash
# P.frag
for Gff in $(ls gene_pred/annotation/*/*/*_genes_incl_ORFeffectors.gff3)
do
    Species=$(echo $Gff | rev | cut -f3 -d '/' | rev)
    Isolate=$(echo $Gff | rev | cut -f2 -d '/' | rev)
    echo "$Species - $Isolate"
    Gff_out=gene_pred/annotation/$Species/$Isolate/"$Isolate"_genes_incl_ORFeffectors_nodup.gff3
    Aug_ApoP=analysis/ApoplastP/$Species/$Isolate/*_ApoplastP_headers.txt
    ORF_ApoP=analysis/ApoplastP/$Species/$Isolate/*_ApoplastP_ORF_merged_headers.txt
    Unclear_Genes=gene_pred/annotation/$Species/$Isolate/Unclear_duplicates.txt
    ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
    python $ProgDir/Parse_ApoP_duplicates.py --gff_in $Gff --gff_out $Gff_out \
    --Aug_ApoP $Aug_ApoP --ORF_ApoP $ORF_ApoP --Unclear_Genes $Unclear_Genes
done

# P.rubi
for Gff in $(ls ../phytophthora_rubi/gene_pred/annotation/*/*/*_genes_incl_ORFeffectors.gff3)
do
    Species=$(echo $Gff | rev | cut -f3 -d '/' | rev)
    Isolate=$(echo $Gff | rev | cut -f2 -d '/' | rev)
    echo "$Species - $Isolate"
    Gff_out=../phytophthora_rubi/gene_pred/annotation/$Species/$Isolate/"$Isolate"_genes_incl_ORFeffectors_nodup.gff3
    Aug_ApoP=../phytophthora_rubi/analysis/ApoplastP/$Species/$Isolate/*_ApoplastP_headers.txt
    ORF_ApoP=../phytophthora_rubi/analysis/ApoplastP/$Species/$Isolate/*_ApoplastP_ORF_merged_headers.txt
    Unclear_Genes=../phytophthora_rubi/gene_pred/annotation/$Species/$Isolate/Unclear_duplicates.txt
    ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
    python $ProgDir/Parse_ApoP_duplicates.py --gff_in $Gff --gff_out $Gff_out \
    --Aug_ApoP $Aug_ApoP --ORF_ApoP $ORF_ApoP --Unclear_Genes $Unclear_Genes
done
```

#### Bedtools used to identify intersecting gene models and effector ORFs

```bash
# P.frag
for Gff in $(ls gene_pred/final/*/*/final/final_genes_appended.gff3)
do
    Species=$(echo $Gff | rev | cut -f4 -d '/' | rev)
    Isolate=$(echo $Gff | rev | cut -f3 -d '/' | rev)
    echo "$Species - $Isolate"
    OutDir=gene_pred/annotation/$Species/$Isolate
    RxLR_No_ApoP=$OutDir/ORF_RxLR_No_ApoP_parsed.gff3
    RxLR_Plus_ApoP=$OutDir/ORF_RxLR_Plus_ApoP_parsed.gff3
    CRN_No_ApoP=$OutDir/ORF_CRN_No_ApoP_parsed.gff3
    CRN_Plus_ApoP=$OutDir/ORF_CRN_Plus_ApoP_parsed.gff3
    ApoP_No_RxLR_CRN=$OutDir/ORF_ApoP_No_RxLR_CRN_parsed.gff3
    # RxLR_No_ApoP
    bedtools intersect -wo -a $Gff -b $RxLR_No_ApoP | grep -e "AUGUSTUS.gene" \
    -e "CodingQuarry_v2.0.gene" -e "PGNCodingQuarry_v2.0" | grep \
    "RxLR_ORF.gene" | cut -f1,9,18 | sed 's/ID=//g' | tr -d ';' > $OutDir/RxLR_No_ApoP_ORFs_intersecting_non-effector_genes.txt
    # RxLR_Plus_ApoP
    bedtools intersect -wo -a $Gff -b $RxLR_Plus_ApoP | grep -e "AUGUSTUS.gene" \
    -e "CodingQuarry_v2.0.gene" -e "PGNCodingQuarry_v2.0" | grep \
    "RxLR_ORF_+_ApoplastP_ORF.gene" | cut -f1,9,18 | sed 's/ID=//g' | tr \
    -d ';' > $OutDir/RxLR_Plus_ApoP_ORFs_intersecting_non-effector_genes.txt
    # CRN_No_ApoP
    bedtools intersect -wo -a $Gff -b $CRN_No_ApoP | grep -e "AUGUSTUS.gene" \
    -e "CodingQuarry_v2.0.gene" -e "PGNCodingQuarry_v2.0" | grep \
    "CRN_ORF.gene" | cut -f1,9,18 | sed 's/ID=//g' | tr -d ';' > $OutDir/CRN_No_ApoP_ORFs_intersecting_non-effector_genes.txt
    # CRN_Plus_ApoP
    bedtools intersect -wo -a $Gff -b $CRN_Plus_ApoP | grep -e "AUGUSTUS.gene" \
    -e "CodingQuarry_v2.0.gene" -e "PGNCodingQuarry_v2.0" | grep \
    "CRN_ORF_+_ApoplastP_ORF.gene" | cut -f1,9,18 | sed 's/ID=//g' | tr \
    -d ';' > $OutDir/CRN_Plus_ApoP_ORFs_intersecting_non-effector_genes.txt
    # ApoP_No_RxLR_CRN
    bedtools intersect -wo -a $Gff -b $ApoP_No_RxLR_CRN | grep \
    -e "AUGUSTUS.gene" -e "CodingQuarry_v2.0.gene" \
    -e "PGNCodingQuarry_v2.0" | grep "ApoplastP_ORF.gene" | cut \
    -f1,9,18 | sed 's/ID=//g' | tr -d ';' > $OutDir/ApoP_No_RxLR_CRN_ORFs_intersecting_non-effector_genes.txt
done

# P.rubi
for Gff in $(ls ../phytophthora_rubi/gene_pred/final/*/*/final/final_genes_appended.gff3)
do
    Species=$(echo $Gff | rev | cut -f4 -d '/' | rev)
    Isolate=$(echo $Gff | rev | cut -f3 -d '/' | rev)
    echo "$Species - $Isolate"
    OutDir=../phytophthora_rubi/gene_pred/annotation/$Species/$Isolate
    RxLR_No_ApoP=$OutDir/ORF_RxLR_No_ApoP_parsed.gff3
    RxLR_Plus_ApoP=$OutDir/ORF_RxLR_Plus_ApoP_parsed.gff3
    CRN_No_ApoP=$OutDir/ORF_CRN_No_ApoP_parsed.gff3
    CRN_Plus_ApoP=$OutDir/ORF_CRN_Plus_ApoP_parsed.gff3
    ApoP_No_RxLR_CRN=$OutDir/ORF_ApoP_No_RxLR_CRN_parsed.gff3
    # RxLR_No_ApoP
    bedtools intersect -wo -a $Gff -b $RxLR_No_ApoP | grep -e "AUGUSTUS.gene" \
    -e "CodingQuarry_v2.0.gene" -e "PGNCodingQuarry_v2.0" | grep \
    "RxLR_ORF.gene" | cut -f1,9,18 | sed 's/ID=//g' | tr -d ';' > $OutDir/RxLR_No_ApoP_ORFs_intersecting_non-effector_genes.txt
    # RxLR_Plus_ApoP
    bedtools intersect -wo -a $Gff -b $RxLR_Plus_ApoP | grep -e "AUGUSTUS.gene" \
    -e "CodingQuarry_v2.0.gene" -e "PGNCodingQuarry_v2.0" | grep \
    "RxLR_ORF_+_ApoplastP_ORF.gene" | cut -f1,9,18 | sed 's/ID=//g' | tr \
    -d ';' > $OutDir/RxLR_Plus_ApoP_ORFs_intersecting_non-effector_genes.txt
    # CRN_No_ApoP
    bedtools intersect -wo -a $Gff -b $CRN_No_ApoP | grep -e "AUGUSTUS.gene" \
    -e "CodingQuarry_v2.0.gene" -e "PGNCodingQuarry_v2.0" | grep \
    "CRN_ORF.gene" | cut -f1,9,18 | sed 's/ID=//g' | tr -d ';' > $OutDir/CRN_No_ApoP_ORFs_intersecting_non-effector_genes.txt
    # CRN_Plus_ApoP
    bedtools intersect -wo -a $Gff -b $CRN_Plus_ApoP | grep -e "AUGUSTUS.gene" \
    -e "CodingQuarry_v2.0.gene" -e "PGNCodingQuarry_v2.0" | grep \
    "CRN_ORF_+_ApoplastP_ORF.gene" | cut -f1,9,18 | sed 's/ID=//g' | tr \
    -d ';' > $OutDir/CRN_Plus_ApoP_ORFs_intersecting_non-effector_genes.txt
    # ApoP_No_RxLR_CRN
    bedtools intersect -wo -a $Gff -b $ApoP_No_RxLR_CRN | grep \
    -e "AUGUSTUS.gene" -e "CodingQuarry_v2.0.gene" \
    -e "PGNCodingQuarry_v2.0" | grep "ApoplastP_ORF.gene" | cut \
    -f1,9,18 | sed 's/ID=//g' | tr -d ';' > $OutDir/ApoP_No_RxLR_CRN_ORFs_intersecting_non-effector_genes.txt
done
```

#### Remove genes to ensure no overlapping predictions

```bash
# P.frag
for Gff in $(ls gene_pred/annotation/*/*/*_genes_incl_ORFeffectors_nodup.gff3)
do
    Isolate=$(echo $Gff | rev | cut -f2 -d '/' | rev)
    Species=$(echo $Gff | rev | cut -f3 -d '/' | rev)
    echo "$Species - $Isolate"
    OutDir=$(dirname $Gff)
    MergeDir=$(ls -d gene_pred/annotation/$Species/$Isolate)
    cat $MergeDir/RxLR_No_ApoP_ORFs_intersecting_non-effector_genes.txt \
    $MergeDir/RxLR_Plus_ApoP_ORFs_intersecting_non-effector_genes.txt \
    $MergeDir/CRN_No_ApoP_ORFs_intersecting_non-effector_genes.txt \
    $MergeDir/CRN_Plus_ApoP_ORFs_intersecting_non-effector_genes.txt \
    $MergeDir/ApoP_No_RxLR_CRN_ORFs_intersecting_non-effector_genes.txt | cut \
    -f3 > $MergeDir/exclude_list.txt
    PreFilter=$(cat $Gff | grep -w 'gene' | wc -l)
    FilterList=$(cat $OutDir/exclude_list.txt | wc -l)
    UniqueFilterList=$(cat $OutDir/exclude_list.txt | sort | uniq | wc -l)
    ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
    Exclude_List=$OutDir/exclude_list.txt
    Gff_out=$OutDir/"$Isolate"_genes_incl_ORFeffectors_filtered.gff3
    Removed_Genes=$OutDir/Removed_Genes.txt
    python $ProgDir/Remove_Overlapping_Features.py --inp_gff $Gff \
    --exclude_list $Exclude_List --output_gff $Gff_out --removed_genes $Removed_Genes
    GenesRemoved=$(cat $Removed_Genes | wc -l)
    FinalGenes=$(cat $OutDir/"$Isolate"_genes_incl_ORFeffectors_filtered.gff3 | \
    grep -w 'gene' | wc -l)
    printf "$Species\t$Isolate\t$PreFilter\t$FilterList\t$UniqueFilterList\t$GenesRemoved\t$FinalGenes\n"
done

# P.rubi
for Gff in $(ls ../phytophthora_rubi/gene_pred/annotation/*/*/*_genes_incl_ORFeffectors_nodup.gff3)
do
    Isolate=$(echo $Gff | rev | cut -f2 -d '/' | rev)
    Species=$(echo $Gff | rev | cut -f3 -d '/' | rev)
    echo "$Species - $Isolate"
    OutDir=$(dirname $Gff)
    MergeDir=$(ls -d ../phytophthora_rubi/gene_pred/annotation/$Species/$Isolate)
    cat $MergeDir/RxLR_No_ApoP_ORFs_intersecting_non-effector_genes.txt \
    $MergeDir/RxLR_Plus_ApoP_ORFs_intersecting_non-effector_genes.txt \
    $MergeDir/CRN_No_ApoP_ORFs_intersecting_non-effector_genes.txt \
    $MergeDir/CRN_Plus_ApoP_ORFs_intersecting_non-effector_genes.txt \
    $MergeDir/ApoP_No_RxLR_CRN_ORFs_intersecting_non-effector_genes.txt | cut \
    -f3 > $MergeDir/exclude_list.txt
    PreFilter=$(cat $Gff | grep -w 'gene' | wc -l)
    FilterList=$(cat $OutDir/exclude_list.txt | wc -l)
    UniqueFilterList=$(cat $OutDir/exclude_list.txt | sort | uniq | wc -l)
    ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
    Exclude_List=$OutDir/exclude_list.txt
    Gff_out=$OutDir/"$Isolate"_genes_incl_ORFeffectors_filtered.gff3
    Removed_Genes=$OutDir/Removed_Genes.txt
    python $ProgDir/Remove_Overlapping_Features.py --inp_gff $Gff \
    --exclude_list $Exclude_List --output_gff $Gff_out --removed_genes $Removed_Genes
    GenesRemoved=$(cat $Removed_Genes | wc -l)
    FinalGenes=$(cat $OutDir/"$Isolate"_genes_incl_ORFeffectors_filtered.gff3 | \
    grep -w 'gene' | wc -l)
    printf "$Species\t$Isolate\t$PreFilter\t$FilterList\t$UniqueFilterList\t$GenesRemoved\t$FinalGenes\n"
done
```

```
Species Isolate PreFilter   FilterList  UniqueFilterList    GenesRemoved    FinalGenes
P.fragariae     A4      40,970   7,658    7,347    7,347       33,623
P.fragariae     Bc16    49,772   9,026    8,669    8,669       41,103
P.fragariae     Bc1     41,242   7,807    7,551    7,551       33,691
P.fragariae     Bc23    40,603   7,715    7,458    7,457       33,146
P.fragariae     Nov27   41,364   7,812    7,567    7,567       33,797
P.fragariae     Nov5    41,030   7,587    7,332    7,331       33,699
P.fragariae     Nov71   40,470   7,574    7,328    7,327       33,143
P.fragariae     Nov77   40,915   7,578    7,334    7,334       33,581
P.fragariae     Nov9    40,960   7,677    7,434    7,433       33,527
P.fragariae     ONT3    40,231   7,048    6,814    6,814       33,417
P.fragariae     SCRP245_v2      40,148   7,170    6,927    6,925       33,223
P.rubi  SCRP249 42,134   8,220    7,995    7,994       34,140
P.rubi  SCRP324 41,381   7,847    7,637    7,634       33,747
P.rubi  SCRP333 43,245   8,284    8,024    8,022       35,223
```

#### Check for further duplication, rename the genes and extract fasta files

```bash
# P.frag
for Gff in $(ls gene_pred/annotation/*/*/*_genes_incl_ORFeffectors_filtered.gff3)
do
    Isolate=$(echo $Gff | rev | cut -f2 -d '/' | rev)
    Species=$(echo $Gff | rev | cut -f3 -d '/' | rev)
    echo "$Species - $Isolate"
    OutDir=$(dirname $Gff)
    Gff_Filtered=$OutDir/filtered_duplicates.gff
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/codingquary
    $ProgDir/remove_dup_features.py --inp_gff $Gff --out_gff $Gff_Filtered
    Gff_Renamed=$OutDir/"$Isolate"_genes_incl_ORFeffectors_renamed.gff3
    Log_File=$OutDir/Renaming_log.log
    $ProgDir/gff_rename_genes.py --inp_gff $Gff_Filtered \
    --conversion_log $Log_File > $Gff_Renamed
    rm $Gff_Filtered
    if [ -f \
    repeat_masked/$Species/$Isolate/manual_edits_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Species/$Isolate/manual_edits_repmask/*_softmasked.fa)
        echo $Assembly
    elif [ -f \
    repeat_masked/$Species/$Isolate/ncbi_edits_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Species/$Isolate/ncbi_edits_repmask/*_softmasked.fa)
        echo $Assembly
    elif [ -f \
    repeat_masked/$Species/$Isolate/deconseq_Paen_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Species/$Isolate/deconseq_Paen_repmask/*_softmasked.fa)
        echo $Assembly
    else
        Assembly=$(ls repeat_masked/quiver_results/polished/filtered_contigs_repmask/*_softmasked.fa)
        echo $Assembly
    fi
    $ProgDir/gff2fasta.pl $Assembly $Gff_Renamed $OutDir/"$Isolate"_genes_incl_ORFeffectors_renamed
    # Perl script uses * for stop codons, NCBI want X
    sed -i 's/\*/X/g' $OutDir/"$Isolate"_genes_incl_ORFeffectors_renamed.pep.fasta
done

# P.rubi
for Gff in $(ls ../phytophthora_rubi/gene_pred/annotation/*/*/*_genes_incl_ORFeffectors_filtered.gff3)
do
    Isolate=$(echo $Gff | rev | cut -f2 -d '/' | rev)
    Species=$(echo $Gff | rev | cut -f3 -d '/' | rev)
    echo "$Species - $Isolate"
    OutDir=$(dirname $Gff)
    Gff_Filtered=$OutDir/filtered_duplicates.gff
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/codingquary
    $ProgDir/remove_dup_features.py --inp_gff $Gff --out_gff $Gff_Filtered
    Gff_Renamed=$OutDir/"$Isolate"_genes_incl_ORFeffectors_renamed.gff3
    Log_File=$OutDir/Renaming_log.log
    $ProgDir/gff_rename_genes.py --inp_gff $Gff_Filtered --conversion_log $Log_File > $Gff_Renamed
    rm $Gff_Filtered
    if [ -f ../phytophthora_rubi/repeat_masked/$Species/$Isolate/manual_edits_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls ../phytophthora_rubi/repeat_masked/$Species/$Isolate/manual_edits_repmask/*_softmasked.fa)
        echo $Assembly
    elif [ -f ../phytophthora_rubi/repeat_masked/$Species/$Isolate/ncbi_edits_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls ../phytophthora_rubi/repeat_masked/$Species/$Isolate/ncbi_edits_repmask/*_softmasked.fa)
        echo $Assembly
    elif [ -f ../phytophthora_rubi/repeat_masked/$Species/$Isolate/deconseq_Paen_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls ../phytophthora_rubi/repeat_masked/$Species/$Isolate/deconseq_Paen_repmask/*_softmasked.fa)
        echo $Assembly
    fi
    $ProgDir/gff2fasta.pl $Assembly $Gff_Renamed $OutDir/"$Isolate"_genes_incl_ORFeffectors_renamed
    # Perl script uses * for stop codons, NCBI want X
    sed -i 's/\*/X/g' $OutDir/"$Isolate"_genes_incl_ORFeffectors_renamed.pep.fasta
done
```

Any duplicates identified by this script were manually investigated for how
they slipped through previous attempts to remove them

```
No duplicates identified
```

##### Collect statistics

```bash
# P.frag
for Transcriptome in $(ls gene_pred/annotation/*/*/*_genes_incl_ORFeffectors_renamed.pep.fasta)
do
    Isolate=$(echo $Transcriptome | rev | cut -f2 -d '/' | rev)
    Species=$(echo $Transcriptome | rev | cut -f3 -d '/' | rev)
    Gff=$(echo $Transcriptome | sed 's/.pep.fasta/.gff3/g')
    Genes=$(cat $Gff | grep -w 'gene' | wc -l)
    Proteins=$(cat $Transcriptome | grep '>' | wc -l)
    printf "$Species\t$Isolate\t$Genes\t$Proteins\n"
done

# P.rubi
for Transcriptome in $(ls ../phytophthora_rubi/gene_pred/annotation/*/*/*_genes_incl_ORFeffectors_renamed.pep.fasta)
do
    Isolate=$(echo $Transcriptome | rev | cut -f2 -d '/' | rev)
    Species=$(echo $Transcriptome | rev | cut -f3 -d '/' | rev)
    Gff=$(echo $Transcriptome | sed 's/.pep.fasta/.gff3/g')
    Genes=$(cat $Gff | grep -w 'gene' | wc -l)
    Proteins=$(cat $Transcriptome | grep '>' | wc -l)
    printf "$Species\t$Isolate\t$Genes\t$Proteins\n"
done
```

```
Species Isolate Genes   Proteins
P.fragariae	A4	33,623	34,434
P.fragariae	Bc16	41,168	41,465
P.fragariae	Bc1	33,691	34,500
P.fragariae	Bc23	33,146	33,971
P.fragariae	Nov27	33,797	34,624
P.fragariae	Nov5	33,699	34,515
P.fragariae	Nov71	33,143	33,967
P.fragariae	Nov77	33,581	34,409
P.fragariae	Nov9	33,527	34,361
P.fragariae	ONT3	33,417	34,216
P.fragariae	SCRP245_v2	33,223	34,010
P.rubi  SCRP249 34,140   34,485
P.rubi  SCRP324 33,747   34,232
P.rubi  SCRP333 35,223   35,539
```

Annotations (Interproscan & Swissprot) must be performed here - commands in README.md

#### Setting variables

Variables containing the locations of files and options for scripts were set

```bash
AnnieDir=/home/armita/prog/annie/genomeannotation-annie-c1e848b
ProgDir=/home/adamst/git_repos/tools/genbank_submission
LabID=AdamsNIABEMR
```

### Generating .tbl file using GAG

The Genome Annotation Generator (GAG.py) can convert gffs to .tbl files
It can also add interpro & swissprot annotations using Annie

#### Extracting annotations (Annie)

Interpro & Swissprot annotation were extracted using Annie. Output was filtered
to keep only annotations with references to NCBI approved databases
NOTE: transcripts must be re-labeled as mRNA

```bash
# P.frag isolates
for Isolate in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    Organism=P.fragariae
    echo "$Organism - $Isolate"
    OutDir=genome_submission/$Organism/$Isolate
    Gff=$(ls gene_pred/annotation/$Organism/$Isolate/"$Isolate"_genes_incl_ORFeffectors_renamed.gff3)
    InterProTab=$(ls gene_pred/interproscan/$Organism/$Isolate/"$Isolate"_interproscan.tsv)
    SwissProtBlast=$(ls gene_pred/swissprot/$Organism/$Isolate/greedy/swissprot_vMar2018_tophit_parsed.tbl)
    SwissProtFasta=/home/groups/harrisonlab/uniprot/swissprot/uniprot_sprot.fasta
    python $AnnieDir/annie.py -ipr $InterProTab -g $Gff -b $SwissProtBlast -db $SwissProtFasta -o $OutDir/annie_output.csv --fix_bad_products
    ProgDir=/home/adamst/git_repos/tools/genbank_submission
    $ProgDir/edit_tbl_file/annie_corrector.py --inp_csv $OutDir/annie_output.csv --out_csv $OutDir/annie_corrected_output.csv
done

# P.rubi isolates
for Isolate in SCRP249 SCRP324 SCRP333
do
    Organism=P.rubi
    echo "$Organism - $Isolate"
    OutDir=genome_submission/$Organism/$Isolate
    Gff=$(ls ../phytophthora_rubi/gene_pred/annotation/$Organism/$Isolate/"$Isolate"_genes_incl_ORFeffectors_renamed.gff3)
    InterProTab=$(ls ../phytophthora_rubi/gene_pred/interproscan/$Organism/$Isolate/"$Isolate"_interproscan.tsv)
    SwissProtBlast=$(ls ../phytophthora_rubi/gene_pred/swissprot/$Organism/$Isolate/greedy/swissprot_vMar2018_tophit_parsed.tbl)
    SwissProtFasta=/home/groups/harrisonlab/uniprot/swissprot/uniprot_sprot.fasta
    python $AnnieDir/annie.py -ipr $InterProTab -g $Gff -b $SwissProtBlast -db $SwissProtFasta -o $OutDir/annie_output.csv --fix_bad_products
    ProgDir=/home/adamst/git_repos/tools/genbank_submission
    $ProgDir/edit_tbl_file/annie_corrector.py --inp_csv $OutDir/annie_output.csv --out_csv $OutDir/annie_corrected_output.csv
done
```

#### Running GAG

GAG was run using the modified GFF as well as the output of annie.
Outputs database references incorrectly, so these are modified

```bash
# P.frag
for Isolate in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    Organism=P.fragariae
    echo "$Organism - $Isolate"
    if [ -f repeat_masked/$Organism/$Isolate/manual_edits_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Isolate/manual_edits_repmask/*_softmasked.fa)
        echo $Assembly
    elif [ -f repeat_masked/$Organism/$Isolate/ncbi_edits_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Isolate/ncbi_edits_repmask/*_softmasked.fa)
        echo $Assembly
    elif [ -f repeat_masked/$Organism/$Isolate/deconseq_Paen_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Isolate/deconseq_Paen_repmask/*_softmasked.fa)
        echo $Assembly
    else
        Assembly=$(ls repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_softmasked.fa)
        echo $Assembly
    fi
    OutDir=genome_submission/$Organism/$Isolate
    Gff=$(ls gene_pred/annotation/$Organism/$Isolate/"$Isolate"_genes_incl_ORFeffectors_renamed.gff3)
    mkdir -p $OutDir/gag/round_1
    gag.py -f $Assembly -g $Gff -a $OutDir/annie_corrected_output.csv --fix_start_stop -o $OutDir/gag/round_1 2>&1 | tee $OutDir/gag_log_1.txt
    sed -i 's/Dbxref/db_xref/g' $OutDir/gag/round_1/genome.tbl
done

# P.rubi
for Isolate in SCRP249 SCRP324 SCRP333
do
    Organism=P.rubi
    echo "$Organism - $Isolate"
    if [ -f ../phytophthora_rubi/repeat_masked/$Organism/$Isolate/manual_edits_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls ../phytophthora_rubi/repeat_masked/$Organism/$Isolate/manual_edits_repmask/*_softmasked.fa)
        echo $Assembly
    elif [ -f ../phytophthora_rubi/repeat_masked/$Organism/$Isolate/ncbi_edits_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls ../phytophthora_rubi/repeat_masked/$Organism/$Isolate/ncbi_edits_repmask/*_softmasked.fa)
        echo $Assembly
    elif [ -f ../phytophthora_rubi/repeat_masked/$Organism/$Isolate/deconseq_Paen_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls ../phytophthora_rubi/repeat_masked/$Organism/$Isolate/deconseq_Paen_repmask/*_softmasked.fa)
        echo $Assembly
    fi
    OutDir=genome_submission/$Organism/$Isolate
    Gff=$(ls ../phytophthora_rubi/gene_pred/annotation/$Organism/$Isolate/"$Isolate"_genes_incl_ORFeffectors_renamed.gff3)
    mkdir -p $OutDir/gag/round_1
    gag.py -f $Assembly -g $Gff -a $OutDir/annie_corrected_output.csv --fix_start_stop -o $OutDir/gag/round_1 2>&1 | tee $OutDir/gag_log_1.txt
    sed -i 's/Dbxref/db_xref/g' $OutDir/gag/round_1/genome.tbl
done
```

### tbl2asn round 1

tbl2asn was run to collect error reports on the current formatting.
All input files must be in same dir with same basename

```bash
# P.frag
for Isolate in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    Organism=P.fragariae
    echo "$Organism - $Isolate"
    OutDir=genome_submission/$Organism/$Isolate
    if [ -f repeat_masked/$Organism/$Isolate/manual_edits_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Isolate/manual_edits_repmask/*_softmasked.fa)
        echo $Assembly
    elif [ -f repeat_masked/$Organism/$Isolate/ncbi_edits_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Isolate/ncbi_edits_repmask/*_softmasked.fa)
        echo $Assembly
    elif [ -f repeat_masked/$Organism/$Isolate/deconseq_Paen_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Organism/$Isolate/deconseq_Paen_repmask/*_softmasked.fa)
        echo $Assembly
    else
        Assembly=$(ls repeat_masked/quiver_results/polished/filtered_contigs_repmask/*_softmasked.fa)
        echo $Assembly
    fi
    cp $Assembly $OutDir/gag/round_1/genome.fsa
    SbtFile=genome_submission/$Organism/$Isolate/template.sbt
    cp $SbtFile $OutDir/gag/round_1/template.sbt
    mkdir -p $OutDir/tbl2asn/round_1
    tbl2asn -p $OutDir/gag/round_1/. -t $OutDir/gag/round_1/template.sbt -r $OutDir/tbl2asn/round_1 -M n -X E -Z $OutDir/gag/round_1/discrep.txt -j "[organism=$Organism] [strain=$Isolate]"
done

# P.rubi
for Isolate in SCRP249 SCRP324 SCRP333
do
    Organism=P.rubi
    echo "$Organism - $Isolate"
    OutDir=genome_submission/$Organism/$Isolate
    if [ -f ../phytophthora_rubi/repeat_masked/$Organism/$Isolate/manual_edits_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls ../phytophthora_rubi/repeat_masked/$Organism/*/manual_edits_repmask/*_softmasked.fa)
        echo $Assembly
    elif [ -f ../phytophthora_rubi/repeat_masked/$Organism/$Isolate/ncbi_edits_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls ../phytophthora_rubi/repeat_masked/$Organism/*/ncbi_edits_repmask/*_softmasked.fa)
        echo $Assembly
    elif [ -f ../phytophthora_rubi/repeat_masked/$Organism/$Isolate/deconseq_Paen_repmask/*_softmasked.fa ]
    then
        Assembly=$(ls ../phytophthora_rubi/repeat_masked/$Organism/$Isolate/deconseq_Paen_repmask/*_softmasked.fa)
        echo $Assembly
    fi
    cp $Assembly $OutDir/gag/round_1/genome.fsa
    SbtFile=genome_submission/$Organism/$Isolate/template.sbt
    cp $SbtFile $OutDir/gag/round_1/template.sbt
    mkdir -p $OutDir/tbl2asn/round_1
    tbl2asn -p $OutDir/gag/round_1/. -t $OutDir/gag/round_1/template.sbt -r $OutDir/tbl2asn/round_1 -M n -X E -Z $OutDir/gag/round_1/discrep.txt -j "[organism=$Organism] [strain=$Isolate]"
done
```

### Edit produced tbl file

tbl2asn produces an error log, Andy has produced a python script to correct
some of these errors

```bash
# P.frag
for Isolate in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    Species=P.fragariae
    echo "$Species - $Isolate"
    OutDir=genome_submission/$Species/$Isolate
    Locus_tag=$(cat genome_submission/Pf_Pr_locus_tags.txt | grep -w "$Isolate" | cut -f1 -d ' ')
    echo $Locus_tag
    mkdir -p $OutDir/gag/edited
    Tbl_in=$OutDir/gag/round_1/genome.tbl
    Val_in=$OutDir/tbl2asn/round_1/genome.val
    Tbl_out=$OutDir/gag/edited/genome.tbl
    ProgDir=/home/adamst/git_repos/tools/genbank_submission/edit_tbl_file
    $ProgDir/ncbi_tbl_corrector.py --inp_tbl $Tbl_in --inp_val $Val_in --locus_tag $Locus_tag --lab_id $LabID --gene_id "remove" --edits stop pseudo unknown_UTR correct_partial --remove_product_locus_tags "True" --del_name_from_prod "True" --out_tbl $Tbl_out
done

# P.rubi
for Isolate in SCRP249 SCRP324 SCRP333
do
    Species=P.rubi
    echo "$Species - $Isolate"
    OutDir=genome_submission/$Species/$Isolate
    Locus_tag=$(cat genome_submission/Pf_Pr_locus_tags.txt | grep -w "$Isolate" | cut -f1 -d ' ')
    echo $Locus_tag
    mkdir -p $OutDir/gag/edited
    Tbl_in=$OutDir/gag/round_1/genome.tbl
    Val_in=$OutDir/tbl2asn/round_1/genome.val
    Tbl_out=$OutDir/gag/edited/genome.tbl
    ProgDir=/home/adamst/git_repos/tools/genbank_submission/edit_tbl_file
    $ProgDir/ncbi_tbl_corrector.py --inp_tbl $Tbl_in --inp_val $Val_in --locus_tag $Locus_tag --lab_id $LabID --gene_id "remove" --edits stop pseudo unknown_UTR correct_partial --remove_product_locus_tags "True" --del_name_from_prod "True" --out_tbl $Tbl_out
done
```

#### Generate a structured comment detailing annotation methods

```bash
# P.frag
for Isolate in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    Species=P.fragariae
    echo "$Species - $Isolate"
    OutDir=genome_submission/$Species/$Isolate
    printf "StructuredCommentPrefix\t##Genome-Annotation-Data-START##
    Annotation Provider\tHarrison Lab NIAB-EMR
    Annotation Date\tAUG-2018
    Annotation Version\tRelease 1.01
    Annotation Method\tAb initio gene prediction: Braker 1.9 and CodingQuarry 2.0; Functional annotation: Swissprot (March 2018 release) and Interproscan 5.18-57.0" \
    > $OutDir/gag/edited/annotation_methods.strcmt.txt
done

# P.frag
for Isolate in SCRP249 SCRP324 SCRP333
do
    Species=P.rubi
    echo "$Species - $Isolate"
    OutDir=genome_submission/$Species/$Isolate
    printf "StructuredCommentPrefix\t##Genome-Annotation-Data-START##
    Annotation Provider\tHarrison Lab NIAB-EMR
    Annotation Date\tAUG-2018
    Annotation Version\tRelease 1.01
    Annotation Method\tAb initio gene prediction: Braker 1.9 and CodingQuarry 2.0; Functional annotation: Swissprot (March 2018 release) and Interproscan 5.18-57.0" \
    > $OutDir/gag/edited/annotation_methods.strcmt.txt
done
```

### Final run of tbl2asn

Following correction of the .tbl file, tbl2asn was rerun to provide the submission
file.

The -l paired-ends -a r10k inform handling of runs of Ns, show that paired ends
used to estimate gaps & runs > 10 represent gaps.

```bash
# P.frag
for Isolate in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    Species=P.fragariae
    echo "$Species - $Isolate"
    OutDir=genome_submission/$Species/$Isolate
    Final_Name="$Species"_"$Isolate"_Adams_2018
    if [ -f repeat_masked/$Species/$Isolate/manual_edits_repmask/*_unmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Species/$Isolate/manual_edits_repmask/*_unmasked.fa)
        echo $Assembly
    elif [ -f repeat_masked/$Species/$Isolate/ncbi_edits_repmask/*_unmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Species/$Isolate/ncbi_edits_repmask/*_unmasked.fa)
        echo $Assembly
    elif [ -f repeat_masked/$Species/$Isolate/deconseq_Paen_repmask/*_unmasked.fa ]
    then
        Assembly=$(ls repeat_masked/$Species/$Isolate/deconseq_Paen_repmask/*_unmasked.fa)
        echo $Assembly
    else
        Assembly=$(ls repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa)
        echo $Assembly
    fi
    cp $Assembly $OutDir/gag/edited/genome.fsa
    SbtFile=genome_submission/$Species/$Isolate/template.sbt
    cp $SbtFile $OutDir/gag/edited/genome.sbt
    mkdir -p $OutDir/tbl2asn/final
    tbl2asn -p $OutDir/gag/edited/. -t $OutDir/gag/edited/genome.sbt -r $OutDir/tbl2asn/final -M n -X E -Z $OutDir/tbl2asn/final/discrep.txt -j "[organism=$Species] [strain=$Isolate]" -l paired-ends -a r10k -w $OutDir/gag/edited/annotation_methods.strcmt.txt
    cat $OutDir/tbl2asn/final/genome.sqn | sed 's/_pilon//g' | sed 's/title " \[NAH\S*\w/title "Saccharopine dehydrogenase/g' | sed 's/" \[NAH\S*\w"/"Saccharopine dehydrogenase"/g' | sed 's/Phospho-2-dehydro-3-deoxyheptonate aldolase_/Phospho-2-dehydro-3-deoxyheptonate aldolase/g' | sed 's/aldolase_/aldolase/g' | sed 's/\[isomerizing\]/isomerizing/g' | sed 's/\[glutamine-hydrolyzing\]/glutamine-hydrolyzing/g' | sed 's/\[acylating\]/acylating/g' | sed 's/\[ammonia\]/ammonia/g' | sed 's/\[carboxylating\]/carboxylating/g' | sed 's/\[(S)-acetoin forming\]/(S)-acetoin forming/g' | sed 's/\[Mn\]/Mn/g' | sed 's/\[asymmetrical\]/asymmetrical/g' > $OutDir/tbl2asn/final/"$Final_Name".sqn
done

# P.rubi
for Isolate in SCRP249 SCRP324 SCRP333
do
    Species=P.rubi
    echo "$Species - $Isolate"
    OutDir=genome_submission/$Species/$Isolate
    Final_Name="$Species"_"$Isolate"_Adams_2018
    if [ -f ../phytophthora_rubi/repeat_masked/$Species/$Isolate/manual_edits_repmask/*_unmasked.fa ]
    then
        Assembly=$(ls ../phytophthora_rubi/repeat_masked/$Species/$Isolate/manual_edits_repmask/*_unmasked.fa)
        echo $Assembly
    elif [ -f ../phytophthora_rubi/repeat_masked/$Species/$Isolate/ncbi_edits_repmask/*_unmasked.fa ]
    then
        Assembly=$(ls ../phytophthora_rubi/repeat_masked/$Species/$Isolate/ncbi_edits_repmask/*_unmasked.fa)
        echo $Assembly
    elif [ -f ../phytophthora_rubi/repeat_masked/$Species/$Isolate/deconseq_Paen_repmask/*_unmasked.fa ]
    then
        Assembly=$(ls ../phytophthora_rubi/repeat_masked/$Species/$Isolate/deconseq_Paen_repmask/*_unmasked.fa)
        echo $Assembly
    fi
    cp $Assembly $OutDir/gag/edited/genome.fsa
    SbtFile=genome_submission/$Species/$Isolate/template.sbt
    cp $SbtFile $OutDir/gag/edited/genome.sbt
    mkdir -p $OutDir/tbl2asn/final
    tbl2asn -p $OutDir/gag/edited/. -t $OutDir/gag/edited/genome.sbt -r $OutDir/tbl2asn/final -M n -X E -Z $OutDir/tbl2asn/final/discrep.txt -j "[organism=$Species] [strain=$Isolate]" -l paired-ends -a r10k -w $OutDir/gag/edited/annotation_methods.strcmt.txt
    cat $OutDir/tbl2asn/final/genome.sqn | sed 's/_pilon//g' | sed 's/title " \[NAH\S*\w/title "Saccharopine dehydrogenase/g' | sed 's/" \[NAH\S*\w"/"Saccharopine dehydrogenase"/g' | sed 's/Phospho-2-dehydro-3-deoxyheptonate aldolase_/Phospho-2-dehydro-3-deoxyheptonate aldolase/g' | sed 's/aldolase_/aldolase/g' | sed 's/\[isomerizing\]/isomerizing/g' | sed 's/\[glutamine-hydrolyzing\]/glutamine-hydrolyzing/g' | sed 's/\[acylating\]/acylating/g' | sed 's/\[ammonia\]/ammonia/g' | sed 's/\[carboxylating\]/carboxylating/g' | sed 's/\[(S)-acetoin forming\]/(S)-acetoin forming/g' | sed 's/\[Mn\]/Mn/g' | sed 's/\[asymmetrical\]/asymmetrical/g' > $OutDir/tbl2asn/final/"$Final_Name".sqn
done
```

Some genes are flagged with a range error and rejected by NCBI.
This is because for some reason CodingQuarry has some predictions that are
longer the contig, perhaps due to cufflinks transcript assembly.
These genes were corrected manually to end at the end of the contig in the gff
file and sqn generated again.

#### Generate discrepancy files for each genome

Add this line to profile to use asndisc

```
PATH=${PATH}:/home/adamst/prog/ncbi_asndisc
```

Generate NCBI style discrepancy files

```bash
for sqn_dir in $(ls -d genome_submission/P.*/*/tbl2asn/final)
do
    asndisc -p $sqn_dir -x Adams_2018.sqn -o $sqn_dir/discrep.val -X ALL -P t
done
```

Any error labelled as FATAL will cause issues when submitting to NCBI
correct these if you can before submitting

#### Upload commands

```bash
# Bc16 only

Organism=P.fragariae
Isolate=Bc16
cd genome_submission/$Organism/$Isolate/tbl2asn/final
ftp ftp-private.ncbi.nlm.nih.gov

cd uploads/thomas.adams@emr.ac.uk_tSvQhcry
mkdir Bc16_PacBio
cd Bc16_PacBio
tick
put P.fragariae_Bc16_Adams_2018.sqn
exit

cd ../../../../../

# P.frag
# for Isolate in A4 Bc1 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2

Organism=P.fragariae
cd genome_submission/$Organism/$Isolate/tbl2asn/final
ftp ftp-private.ncbi.nlm.nih.gov

cd uploads/thomas.adams@emr.ac.uk_tSvQhcry
mkdir Batch_sqn
cd Batch_sqn
tick
put "$Organism"_"$Isolate"_Adams_2018.sqn
exit

cd ../../../../../

# P.rubi
# for Isolate in SCRP249 SCRP324 SCRP333

Organism=P.rubi
cd genome_submission/$Organism/$Isolate/tbl2asn/final
ftp ftp-private.ncbi.nlm.nih.gov

cd uploads/thomas.adams@emr.ac.uk_tSvQhcry
mkdir Batch_sqn
cd Batch_sqn
tick
put "$Organism"_"$Isolate"_Adams_2018.sqn
exit

cd ../../../../../
```
