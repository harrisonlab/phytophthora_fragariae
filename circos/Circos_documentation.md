In order to examine the genomic structure of Phytophthora fragariae

Alignment of raw MiSeq reads vs the BC-16 genome

Sequence data for isolates with a data from only the MiSeq was aligned against the BC-16 PacBio sequenced genome

single MiSeq run

```bash
Reference=repeat_masked/P.fragariae/Bc16/filtered_contigs_repmask/95m_contigs_unmasked.fa
for StrainPath in $(ls -d qc_dna/paired/P.fragariae/* | grep -v '62471' | grep -v 'Bc16' | grep -v 'Nov71' | grep -v 'Bc1' | grep -v 'Nov9')
do
    Organism=$(echo $StrainPath | rev | cut -f2 -d '/' | rev)
    Strain=$(echo $StrainPath | rev | cut -f1 -d '/' | rev)
    echo "$Organism - $Strain"
    F_Read=$(ls $StrainPath/F/*.fq.gz)
    R_Read=$(ls $StrainPath/R/*.fq.gz)
    echo $F_Read
    echo $R_Read
    OutDir=analysis/genome_alignment/bowtie/$Organism/$Strain/vs_Bc16_unmasked_max1200
    ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/genome_alignment
    qsub $ProgDir/bowtie/sub_bowtie.sh $Reference $F_Read $R_Read $OutDir $Strain
done
```

two MiSeq runs

```bash
Reference=repeat_masked/P.fragariae/Bc16/filtered_contigs_repmask/95m_contigs_unmasked.fa
for StrainPath in $(ls -d qc_dna/paired/P.*/* | grep -v '62471' | grep -v 'Bc16' | grep -v 'SCRP245_v2' | grep -v 'ONT3' | grep -v 'A4' | grep -v 'Bc23' | grep -v 'Nov27' | grep -v 'Nov5' | grep -v 'Nov77' | grep -v 'Bc1' | grep -v 'Nov9')
do
    echo $StrainPath
    Strain=$(echo $StrainPath | rev | cut -f1 -d '/' | rev)
    Organism=$(echo $StrainPath | rev | cut -f2 -d '/' | rev)
    echo "$Organism - $Strain"
    F1_Read=$(ls $StrainPath/F/*_trim.fq.gz | head -n1 | tail -n1)
    R1_Read=$(ls $StrainPath/R/*_trim.fq.gz | head -n1 | tail -n1)
    F2_Read=$(ls $StrainPath/F/*_trim.fq.gz | head -n2 | tail -n1)
    R2_Read=$(ls $StrainPath/R/*_trim.fq.gz | head -n2 | tail -n1)
    echo $F1_Read
    echo $R1_Read
    echo $F2_Read
    echo $R2_Read
    OutDir=analysis/genome_alignment/bowtie/$Organism/$Strain/vs_Bc16_unmasked_max1200
    ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/genome_alignment
    qsub $ProgDir/bowtie/sub_bowtie_2lib.sh $Reference $F1_Read $R1_Read $F2_Read $R2_Read $OutDir $Strain
done
```

for three MiSeq reads

```bash
Reference=repeat_masked/P.fragariae/Bc16/filtered_contigs_repmask/95m_contigs_unmasked.fa
for StrainPath in $(ls -d qc_dna/paired/P.*/* | grep -v '62471' | grep -v 'Bc16' | grep -v 'SCRP245_v2' | grep -v 'ONT3' | grep -v 'A4' | grep -v 'Bc23' | grep -v 'Nov27' | grep -v 'Nov5' | grep -v 'Nov77' | grep -v 'Nov71')
do
    echo $StrainPath
    Strain=$(echo $StrainPath | rev | cut -f1 -d '/' | rev)
    Organism=$(echo $StrainPath | rev | cut -f2 -d '/' | rev)
    echo "$Organism - $Strain"
    F1_Read=$(ls $StrainPath/F/*_trim.fq.gz | head -n1 | tail -n1)
    R1_Read=$(ls $StrainPath/R/*_trim.fq.gz | head -n1 | tail -n1)
    F2_Read=$(ls $StrainPath/F/*_trim.fq.gz | head -n2 | tail -n1)
    R2_Read=$(ls $StrainPath/R/*_trim.fq.gz | head -n2 | tail -n1)
    F3_Read=$(ls $StrainPath/F/*_trim.fq.gz | head -n3 | tail -n1)
    R3_Read=$(ls $StrainPath/R/*_trim.fq.gz | head -n3 | tail -n1)
    echo $F1_Read
    echo $R1_Read
    echo $F2_Read
    echo $R2_Read
    echo $F3_Read
    echo $R3_Read
    OutDir=analysis/genome_alignment/bowtie/$Organism/$Strain/vs_Bc16_unmasked_max1200
    ProgDir=/home/adamst/git_repos/tools/seq_tools/genome_alignment
    qsub $ProgDir/bowtie/sub_bowtie_3lib.sh $Reference $F1_Read $R1_Read $F2_Read $R2_Read $F3_Read $R3_Read $OutDir $Strain
done
```

Sets up variables for Circos

```bash
ProgDir=/home/armita/git_repos/emr_repos/scripts/fusarium/pathogen/identify_LS_chromosomes/circos/
Bc16_genome=repeat_masked/P.fragariae/Bc16/filtered_contigs_repmask/95m_contigs_unmasked.fa
OutDir=analysis/circos/P.fragariae/Bc16
mkdir -p $OutDir
```

Convert the Fus2 genome into circos format

```bash
$ProgDir/fasta2circos.py --genome $Bc16_genome --contig_prefix "" > $OutDir/Bc16_genome.txt
```

# Make 100kb windows for plots
$ProgDir/fasta2gff_windows.py --genome $Fus2_genome > $OutDir/Fus2_100kb_windows.gff

# Convert FoC MiSeq reads aligning in 100kb windows into coverage stats
for ReadsBam in $(ls analysis/genome_alignment/bowtie/N.*/*/*/R0905_contigs_unmasked.fa_aligned_sorted.bam); do
Organism=$(echo $ReadsBam | rev | cut -f4 -d '/' | rev)
Strain=$(echo $ReadsBam | rev | cut -f3 -d '/' | rev)
AlignDir=$(dirname $ReadsBam)
echo "$Organism - $Strain"
#bedtools coverage -abam $ReadsBam -b $OutDir/R0905_pacbio_canu_100kb_windows.gff > $AlignDir/"$Strain"_coverage_vs_R0905.bed

# Convert coverage bed files into circos format
$ProgDir/coverage_bed2circos.py --bed $AlignDir/"$Strain"_coverage_vs_R0905.bed > $OutDir/"$Strain"_coverage_vs_R0905_scatterplot.txt
done

# Plot location of FoL gene Blast hits as a scatterplot
for GffFile in $(ls analysis/blast_homology/*/Fus2_pacbio_test_merged/*_chr_*_gene_single_copy.aa_hits.gff); do
echo $GffFile
Chr=$(echo $GffFile | rev |cut -f1 -d'/' | rev | cut -f6 -d '_')
$ProgDir/gff2circos_scatterplot.py --gff $GffFile --feature Chr"$Chr"_gene_homolog > $OutDir/FoL_chr"$Chr"_genes.txt
done

# Plot location of Fus2 genes in pathogen-shared orthogroups as scatterplot
GffFile=analysis/orthology/orthomcl/FoC_vs_Fo_vs_FoL/Fus2_genes/Fus2_path_shared_genes.gff
$ProgDir/gff2circos_scatterplot.py --gff $GffFile --feature gene --value '1' > $OutDir/Fus2_path_shared_genes_plot.txt

circos -conf /home/armita/git_repos/emr_repos/scripts/fusarium/pathogen/identify_LS_chromosomes/circos/Fus2/APS_plot/Fus2_APS_circos.conf -outputdir ./$OutDir
```
