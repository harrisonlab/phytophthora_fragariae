Commands for generating a circos plot for P. cac isolate Bc16


```bash
  OutDir=analysis/circos/P.fragariae/Bc16
  mkdir -p $OutDir
  # Convert the Bc16 genome into circos format
  ProgDir=~/git_repos/emr_repos/scripts/fusarium/pathogen/identify_LS_chromosomes/circos
  Genome=assembly/merged_canu_spades/P.fragariae/Bc16/95m/filtered_contigs/Bc16_contigs_renamed.fasta
  $ProgDir/fasta2circos.py --genome $Genome --contig_prefix "" > $OutDir/Bc16_genome.txt

  # Make 100kb windows for plots
  $ProgDir/fasta2gff_windows.py --genome $Genome > $OutDir/Bc16_100kb_windows.gff
  # Identify GC content in 100kb windows
  $ProgDir/gc_content2circos.py --genome $Genome --gff $OutDir/Bc16_100kb_windows.gff > $OutDir/Bc16_GC_scatterplot.txt

  ## Identify gene density in 100Kb windows
  # GeneGff=gene_pred/codingquary/P.fragariae/Bc16/final/final_genes_appended.gff3
  # bedtools coverage -a $GeneGff -b $OutDir/Bc16_100kb_windows.gff > $OutDir/Bc16_gene_density.bed
  ## Convert coverage bed files into circos format
  # $ProgDir/coverage_bed2circos.py --bed $OutDir/Bc16_gene_density.bed > $OutDir/Bc16_gene_density_lineplot.txt

  # # Plot location of RxLR genes as a scatterplot
  # RxLR_gff=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_total_RxLR.gff
  # $ProgDir/gff2circos_scatterplot.py --gff $RxLR_gff --feature gene --value 0.66 > $OutDir/Bc16_RxLR_scatterplot.txt
  # # Plot location of CRN genes as a scatterplot
  # CRN_gff=analysis/CRN_effectors/hmmer_CRN/P.fragariae/Bc16/Bc16_pub_CRN_LFLAK_DWL.gff
  # $ProgDir/gff2circos_scatterplot.py --gff $CRN_gff --feature gene --value 0.33 > $OutDir/Bc16_CRN_scatterplot.txt

  # Convert FoC MiSeq reads aligning in 100kb windows into coverage stats
  for ReadsBam in $(ls analysis/genome_alignment/bowtie/P.*/*/vs_Bc16/95m_contigs_unmasked.fa_aligned_sorted.bam); do
    Strain=$(echo $ReadsBam | rev | cut -f3 -d '/' | rev)
    Organism=$(echo $ReadsBam | rev | cut -f4 -d '/' | rev)
    # AlignDir=$(dirname $ReadsBam)
    echo "$Organism - $Strain"
    bedtools coverage -abam $ReadsBam -b $OutDir/Bc16_100kb_windows.gff > $OutDir/"$Strain"_coverage_vs_Bc16.bed
    # Convert coverage bed files into circos format
    $ProgDir/coverage_bed2circos.py --bed $OutDir/"$Strain"_coverage_vs_Bc16.bed > $OutDir/"$Strain"_coverage_vs_Bc16_scatterplot.txt
  done


  # It was noted that only the first 200 contigs could be displayed. The genome file
  # was modified accordingly:
  cat $OutDir/Bc16_genome.txt | head -n200 > $OutDir/Bc16_genome_200_contigs.txt

  circos -conf /home/armita/git_repos/emr_repos/scripts/phytophthora_fragariae/genome_alignment/circos/Bc16_circos.conf -outputdir $OutDir



```


Note - Bedtools overestimates coverage from paired end data, treating an overlapping paired read as 2X coverage.
You should therefore be careful to use coverage plots as a representation of areas that show coverage rather
than a quantification of coverage in an area. Discussed at: https://www.biostars.org/p/172179/
