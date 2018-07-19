# Genes with copy number variation between BC-16, BC-1 and NOV-9 were identified

Following publication of the following paper on *P. infestans*, a similar
approach to investigating CNV between three isolates representing each of the
races in the UK123 population.
Paper: https://doi.org/10.1186/s12862-018-1201-6

Illumina reads already aligned to BC-16 assembly in:
popgen_analysis/pre_SNP_calling_cleanup.md

## Calculate average read depth

### Convert gene gff to bed, required for samtools

```bash
gene_gff=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors.gff3
OutDir=CNV_analysis
mkdir -p $OutDir
ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
python $ProgDir/gff2bed.py --gff_in $gene_gff --out_dir $OutDir
```

### Sort output bed file

```bash
gene_bed=CNV_analysis/Bc16_genes_incl_ORFeffectors.bed
sorted_bed=CNV_analysis/Bc16_genes_incl_ORFeffectors_sorted.bed
sort -k1,1V -k2,2n -k3,3n $gene_bed > $sorted_bed
```

#### Some bam files were not sorted before, do this now

```bash
aligned_reads=analysis/genome_alignment/bowtie/P.fragariae/Bc1/vs_Bc16_FALCON/Bc1_polished_contigs_unmasked.fa_aligned.sam
sorted_bam=analysis/genome_alignment/bowtie/P.fragariae/Bc1/vs_Bc16_FALCON/Bc1_polished_contigs_unmasked.fa_aligned_sorted.bam
samtools sort -o $sorted_bam $aligned_reads
```

#### Create index files for those that are missing them

```bash
cd analysis/genome_alignment/bowtie/P.fragariae/Bc1/vs_Bc16_FALCON
bam_file=Bc1_polished_contigs_unmasked.fa_aligned_sorted.bam
samtools index $bam_file
cd ../../../../../../
```

### Use samtools to calculate read depth for each gene

```bash
for Isolate in Bc16 Bc1 Nov9
do
    aligned_bam=analysis/genome_alignment/bowtie/P.fragariae/$Isolate/vs_Bc16_FALCON/"$Isolate"_polished_contigs_unmasked.fa_aligned_sorted.bam
    sorted_bed=CNV_analysis/Bc16_genes_incl_ORFeffectors_sorted.bed
    output_table=CNV_analysis/"$Isolate"_read_depth.txt
    samtools bedcov $sorted_bed $aligned_bam > $output_table
done
```

## Identify genes displaying copy number variation

Uses a large amount of memory, so run via qlogin

```bash
Isolate_1=BC-16
Isolate_2=BC-1
Isolate_3=NOV-9
Isolate_1_depth=CNV_analysis/Bc16_read_depth.txt
Isolate_2_depth=CNV_analysis/Bc1_read_depth.txt
Isolate_3_depth=CNV_analysis/Nov9_read_depth.txt
bed_in=CNV_analysis/Bc16_genes_incl_ORFeffectors_sorted.bed
fasta_in=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors.gene.fasta
OutDir=CNV_analysis
ProgDir=/home/adamst/git_repos/scripts/phytophthora_fragariae
python $ProgDir/CNV_identification.py --Org1_ID $Isolate_1 --Org2_ID $Isolate_2 --Org3_ID $Isolate_3 --Org1_depth $Isolate_1_depth --Org2_depth $Isolate_2_depth --Org3_depth $Isolate_3_depth --gene_bed $bed_in --gene_fasta $fasta_in --OutDir $OutDir
```

### Summarise the results of CNV analysis

```bash
CNV_IDs=CNV_analysis/BC-16_BC-1_NOV-9_CNV_calls.tsv
CNV_Headers=CNV_analysis/Bc16_Bc1_Nov9_CNV_headers.txt
RxLRs=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_Total_RxLR_motif_hmm.txt
RxLR_CNVs=CNV_analysis/CNV_RxLRs.txt
CRNs=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc16/Bc16_final_CRN.txt
CRN_CNVs=CNV_analysis/CNV_CRNs.txt
ApoP=analysis/ApoplastP/P.fragariae/Bc16/Bc16_Total_ApoplastP.txt
ApoP_CNVs=CNV_analysis/CNV_ApoP.txt
Secreted=gene_pred/combined_sigP_CQ/P.fragariae/Bc16/Bc16_secreted.txt
Secreted_CNVs=CNV_analysis/CNV_Secreted.txt
TFs=analysis/transcription_factors/P.fragariae/Bc16/greedy/Bc16_TF_TR_Headers.txt
TF_CNVs=CNV_analysis/CNV_TF_TR.txt

for num in 1
do
    echo "The total number of genes identified as showing CNV is:"
    cat $CNV_IDs | tail -n+2 | cut -f1 > $CNV_Headers
    cat $CNV_Headers | wc -l
    echo "The number of RxLRs showing CNV is:"
    cat $CNV_Headers | grep -o -w -f $RxLRs > $RxLR_CNVs
    cat $RxLR_CNVs | wc -l
    echo "The number of CRNs showing CNV is:"
    cat $CNV_Headers | grep -o -w -f $CRNs > $CRN_CNVs
    cat $CRN_CNVs | wc -l
    echo "The number of apoplastic effectors showing CNV is:"
    cat $CNV_Headers | grep -o -w -f $ApoP > $ApoP_CNVs
    cat $ApoP_CNVs | wc -l
    echo "The number of secreted proteins showing CNV is:"
    cat $CNV_Headers | grep -o -w -f $Secreted > $Secreted_CNVs
    cat $Secreted_CNVs | wc -l
    echo "The number of transcript factors and transcriptional regulators showing CNV is:"
    cat $CNV_Headers | grep -o -w -f $TFs > $TF_CNVs
    cat $TF_CNVs | wc -l
done
```

```
The total number of genes identified as showing CNV is:
123
The number of RxLRs showing CNV is:
6
The number of CRNs showing CNV is:
0
The number of apoplastic effectors showing CNV is:
43
The number of secreted proteins showing CNV is:
0
The number of transcript factors and transcriptional regulators showing CNV is:
0
```
