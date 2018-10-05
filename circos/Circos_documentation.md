Sets up variables for Circos

```bash
ProgDir=/home/adamst/git_repos/scripts/fusarium/pathogen/identify_LS_chromosomes/circos/
Bc16_genome=repeat_masked/quiver_results/polished/filtered_contigs_repmask/polished_contigs_unmasked.fa
OutDir=analysis/circos/P.fragariae/Bc16/new
mkdir -p $OutDir
```

Convert the Bc16 genome into circos format

```bash
$ProgDir/fasta2circos.py --genome $Bc16_genome --contig_prefix "" > $OutDir/Bc16_genome.txt
```

Make 100kb windows for plots

```bash
$ProgDir/fasta2gff_windows.py --genome $Bc16_genome > $OutDir/Bc16_100kb_windows.gff
```

Convert P.frag MiSeq reads aligning in 100kb windows into coverage stats and convert bed files to circos format

```bash
for Strain in Bc1 Nov9
do
    for ReadsBam in $(analysis/genome_alignment/bowtie/P.fragariae/$Strain/vs_Bc16_FALCON/"$Strain"_polished_contigs_unmasked.fa_aligned_sorted.bam)
    do
        Organism=$(echo $ReadsBam | rev | cut -f4 -d '/' | rev)
        AlignDir=$(dirname $ReadsBam)
        echo "$Organism - $Strain"
        bedtools coverage -abam $ReadsBam -b $OutDir/Bc16_100kb_windows.gff > $AlignDir/"$Strain"_coverage_vs_Bc16.bed
        $ProgDir/coverage_bed2circos.py --bed $AlignDir/"$Strain"_coverage_vs_Bc16.bed > $OutDir/"$Strain"_coverage_vs_Bc16_scatterplot.txt
    done
done
```

Create Gff of renamed effectors

```bash
Gene_Gff=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors_renamed.gff3
RxLR_Gff=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_renamed_RxLRs.gff
CRN_Gff=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc16/Bc16_renamed_CRNs.gff
ApoP_Gff=analysis/ApoplastP/P.fragariae/Bc16/Bc16_renamed_ApoPs.gff
RxLR_Headers=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_Total_RxLR_motif_hmm_renamed.txt
CRN_Headers=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc16/Bc16_final_CRN_renamed.tx
ApoP_Headers=analysis/ApoplastP/P.fragariae/Bc16/Bc16_Total_ApoplastP_renamed.txt
cat $Gene_Gff | grep -w -f $RxLR_Headers > $RxLR_Gff
cat $Gene_Gff | grep -w -f $CRN_Headers > $CRN_Gff
cat $Gene_Gff | grep -w -f $ApoP_Headers > $ApoP_Gff
```

Plot location of BC-16 RxLRs and CRNs as a scatterplot

```bash
ProgDir=/home/adamst/git_repos/scripts/fusarium/pathogen/identify_LS_chromosomes/circos
$ProgDir/gff2circos_scatterplot.py --gff $RxLR_Gff --feature gene --value 1 > $OutDir/Bc16_RxLR_plot.txt
$ProgDir/gff2circos_scatterplot.py --gff $CRN_Gff --feature CDS --value 1 > $OutDir/Bc16_CRN_plot.txt
$ProgDir/gff2circos_scatterplot.py --gff $ApoP_Gff --feature CDS --value 1 > $OutDir/Bc16_ApoP_plot.txt
```

```bash
circos -conf /home/adamst/git_repos/scripts/phytophthora_fragariae/circos/Pf_reassembly_circos.conf -outputdir ./$OutDir
```
