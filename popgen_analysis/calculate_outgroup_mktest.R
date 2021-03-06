#!/home/adamst/prog/R/R-3.2.5/bin/Rscript

library("PopGenome")
library("ggplot2")

######################## BEFORE RUNNING ################################
#Assign individuals to 1 focal population and 1 outgroup population.
#!!!!!!
#If more than 1 focal populations present in the input, run the script multiple times,
#each time assigning the appropriate individuals into one select focal population.
#!!!!!!
#This script calculates: McDonald-Kreitman test
#Output files either per contig or the entire genome (prefix genome_)
##!!!!!!!  DIPLOID organisms
##When using diploid organisms and input FASTA files generated using vcf_to_fasta.py, each sample will be artificially
##one haplotype. Both need to be input below.
Pfrag <- c("Bc1_1", "Bc1_2", "Nov5_1", "Nov5_2", "Bc16_1", "Bc16_2", "A4_1",
"A4_2", "Nov27_1", "Nov27_2", "Nov9_1", "Nov9_2", "Nov71_1", "Nov71_2")
#Assign outgroup samples to the "ancestral" population. The population name "ancestral" should
#not be changed as it evoked below on line 33.
ancestral <- c("SCRP249_1", "SCRP249_2", "SCRP324_1", "SCRP324_2",
"SCRP333_1", "SCRP333_2")
populations <- list(Pfrag, ancestral)
population_names <- c("Pfrag")
#########################################################################
#Output column names explained: (More at: https://en.wikipedia.org/wiki/McDonald%E2%80%93Kreitman_test)
# P_nonsyn - nonsynonymous sites
# P_syn - synonymous sites
# D_nonsyn - fixed nonsynonymous sites
# D_syn - fixed synonymous sites
# neutrality.index (NI) - (P_nonsyn/P_syn)/(D_nonsyn/D_syn). The null hypothesis is that
# (P_nonsyn/P_syn) equals (D_nonsyn/D_syn). Ratios < 1 suggest the action of negative selection, > 1 positive selection
# alpha is - 1-neutrality.index
# Fisher.p-value - Is the neutrality index seen statistically significant
# In addition, output table with suffix "p_corrected" contains p-values corrected for
# multiple instances of p-value testing, using Benjamini-Hochberg correction.
#########################################################################

###Loop through each contig containing folder to calculate stats on each contig separately.
#Folder containing FASTA alignments in the current dir
gff <- "gff"
all_folders <- list.dirs("contigs", full.names = FALSE)
#Remove the gff folder from PopGenome contig analysis
contig_folders <- all_folders[all_folders != "gff"]

top_header <- c("gene_name", "P1_nonsyn",  "P2_nonsyn", "P1_syn", "P2_syn",
"D_nonsyn", "D_syn", "neutrality.index", "alpha", "Fisher.p-value")
file_table2 <- paste("genome_", population_names[1], "_MKT_per_gene_all.txt",
sep = "")
write.table(paste(top_header, collapse = "\t"), file = file_table2, sep = "\t",
quote = FALSE, row.names = FALSE, col.names = FALSE, append = TRUE)
for (dir in contig_folders[contig_folders != ""]){
  contig_folder <- paste("contigs/", dir, sep = "")
  GENOME_class <- readData(contig_folder, gffpath = gff, include.unknown = TRUE)
  GENOME_class <- set.populations(GENOME_class, populations)
  GENOME_class <- set.outgroup(GENOME_class, new.outgroup = ancestral)
  GENOME_class_split <- splitting.data(GENOME_class, subsites = "gene")

  #Carry out McDonald-Kreitman test and write the results to file
  GENOME_class_split <- MKT(GENOME_class_split, do.fisher.test = TRUE)
  MKT_d <- as.data.frame(GENOME_class_split@MKT)
  file_hist <- paste(dir, "_", population_names[1],
  "_MKT_neutrality_index_per_gene.pdf", sep = "")
  MKT_len <- length(MKT_d[, 7])
  MKT_na <- sum(sapply(MKT_d[, 7], is.na))
  if (MKT_len > MKT_na){
    mkt_plot <- ggplot(MKT_d, aes(x = MKT_d[, 7])) +
    geom_histogram(colour = "black", fill = "yellow") +
    xlab("MKT's neutrality index") + ylab("Number of genes") +
    scale_x_continuous(breaks = pretty(MKT_d[, 7], n = 10)) +
    theme(panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(), panel.background = element_blank(),
    panel.border = element_rect(colour = "black", fill = NA, size = 1),
    axis.text = element_text(size = 14), axis.title = element_text(size = 18))
    ggsave(file_hist, mkt_plot)
}
  current_gff <- paste(gff, "/", dir, ".gff", sep = "")
  gene_ids <- get_gff_info(GENOME_class_split, current_gff, chr = dir,
      feature = FALSE, extract.gene.names = TRUE)
  mkt_table <- cbind(gene_ids, GENOME_class_split@MKT)

  file_table <- paste(dir, "_", population_names[1], "_MKT_per_gene.txt",
  sep = "")
  total <- rbind(top_header, mkt_table)
  write.table(total, file = file_table, sep = "\t", quote = FALSE,
  col.names = FALSE, row.names = FALSE)
  write.table(mkt_table, file = file_table2, sep = "\t", quote = FALSE,
  col.names = FALSE, row.names = FALSE, append = TRUE)
}

###Plot genome wide histograms

  file_table2 <- paste("genome_", population_names[1], "_MKT_per_gene_all.txt",
  sep = "")
  x <- as.data.frame(read.delim(file_table2))
  file_hist <- paste("genome_", population_names[1],
  "_MKT_neutrality_index_per_gene_all.pdf", sep = "")
  mkt_plot <- ggplot(x, aes(x = x[, 8])) +
  geom_histogram(colour = "black", fill = "yellow4") +
  xlab("MKT's neutrality index") + ylab("Number of genes") +
  scale_x_continuous(breaks = pretty(x[, 8], n = 10)) +
  theme(panel.grid.major = element_blank(),
  panel.grid.minor = element_blank(), panel.background = element_blank(),
  panel.border = element_rect(colour = "black", fill = NA, size = 1),
  axis.text = element_text(size = 14), axis.title = element_text(size = 18))
  ggsave(file_hist, mkt_plot)

###Adjust the McDonald Kreitman Fisher's exact test results for multiple testing with Benjamini Hochberg correction
###Carried out genome wide
  y <- read.delim(file_table2, header = TRUE)
  #Remove gene entries with not enough polymorphism for MKT to be carried out.
  y <- na.omit(y)
  #Carry out BH adjustment for multiple testing
  adjusted_p_value <- p.adjust(y[, 10], method = "BH", n = length(y[, 8]))
  #Write the genome-wide MKT values table with adjusted p-values
  file_table3 <- paste("genome_", population_names[1],
  "_MKT_per_gene_all_p_corrected.txt", sep = "")
  adjust_column <- cbind(y, adjusted_p_value)
  write.table(adjust_column, file = file_table3, sep = "\t", quote = FALSE,
  col.names = TRUE, row.names = FALSE)
