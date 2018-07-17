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

### Use samtools to calculate read depth for each gene

```bash
for Isolate in Bc16 Bc1 Nov9
do
    aligned_bam=analysis/genome_alignment/bowtie/P.fragariae/$Isolate/vs_Bc16_FALCON/"$Isolate"_polished_contigs_unmasked.fa_aligned_sorted.bam
    sorted_bed=CNV_analysis/Bc16_genes_incl_ORFeffectors_sorted.bed
    output_table=CNV_analysis/"$Isolate"_read_depth.txt
    samtools depth -a -b $sorted_bed $aligned_bam > $output_table
done
```
