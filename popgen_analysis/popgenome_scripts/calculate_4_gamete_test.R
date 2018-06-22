library("PopGenome")
library("ggplot2")

######################## BEFORE RUNNING ################################
#Assign individuals to appropriate populations (or just 1!)
#This script calculates: haplotype-based statistics
#More than one population needs to be defined, of course!
UK1 <- c("Bc1_1", "Bc1_2", "Nov5_1", "Nov5_2")
UK2 <- c("Bc16_1", "Bc16_2", "A4_1", "A4_2")
UK3 <- c("Nov27_1", "Nov27_2", "Nov9_1", "Nov9_2", "Nov71_1", "Nov71_2")
CA4 <- c("ONT3_1", "ONT3_2")
CA5 <- c("Bc23_1", "Bc23_2")
UN <- c("SCRP245_v2_1", "SCRP245_v2_2")
#Need to set argument diploid=TRUE if using diploid genomes in the below command:
populations <- list(UK1, UK2, UK3, CA4, CA4, UN)
#Number of populations assigned above.
population_no <- length(populations)
pairs <- choose(population_no, 2)
population_names <- c("UK1", "UK2", "UK3", "CA4", "CA5", "UN")
#Pop names given in the same order, as above.
#Interval and jump size used in the sliding window analysis
interval <-  1000
jump_size <-  interval / 10
#########################################################################

#Folder containing FASTA alignments in the current dir
gff <- "gff"
all_folders <- list.dirs("contigs", full.names = FALSE)
#Remove the gff folder from PopGenome contig analysis
contig_folders <- all_folders[all_folders != "gff"]

###Loop through each contig containing folder to calculate stats on each contig separately.
for (dir in contig_folders[contig_folders != ""]){
  contig_folder <- paste("contigs/", dir, sep = "")
  GENOME.class <- readData(contig_folder, gffpath = gff, include.unknown = TRUE)
  GENOME.class <- set.populations(GENOME.class, populations)

  GENOME.class.split <- splitting.data(GENOME.class, subsites = "gene")
  GENOME.class.split <- F_ST.stats(GENOME.class.split)
  get.F_ST(GENOME.class.split)

  GENOME.class.slide <- sliding.window.transform(GENOME.class,
      width = interval, jump = jump_size, type = 2, whole.data = TRUE)
  GENOME.class.slide <- F_ST.stats(GENOME.class.slide)
  get.F_ST(GENOME.class.slide)

#FOUR GAMETE test
#per gene
GENOME.class.split <- recomb.stats(GENOME.class.split)
fourgamete_split <- get.recomb(GENOME.class.split)
#per interval
GENOME.class.slide <- recomb.stats(GENOME.class.slide)
fourgamete_slide <- get.recomb(GENOME.class.slide)

#Loop over each population: print figure and table with raw data to file
for (i in seq_along(population_names)){
  fgt <- unlist(fourgamete_split[i])
  file_hist <- paste(dir, "_", population_names[i], "_4GT_per_gene.pdf",
  sep = "")
  fgt_plot <- ggplot(as.data.frame(fgt), aes(x = as.data.frame(fgt))) +
  geom_histogram(colour = "black", fill = "cornsilk") + ggtitle(dir) +
  xlab("Four gamete test") + ylab("Number of genes") +
  scale_x_continuous(breaks = pretty(fgt, n = 10))
  ggsave(file_hist, fgt_plot)
  file_table <- paste(dir, "_", population_names[i], "_4GT_per_gene.txt",
  sep = "")
  file_table2 <- paste("genome_", population_names[i],
  "_4GT_per_gene_all.txt", sep = "")
  current_gff <- paste(gff, "/", dir, ".gff", sep = "")
  gene_ids <- get_gff_info(GENOME.class.split, current_gff, chr = dir,
      feature = FALSE, extract.gene.names = TRUE)
  fgt_table <- cbind(gene_ids, as.data.frame(fourgamete_split[i]))
  write.table(fgt_table, file = file_table, sep = "\t", quote = FALSE,
  col.names = FALSE)
  write.table(fgt_table, file = file_table2, sep = "\t", quote = FALSE,
  col.names = FALSE, append = TRUE)
}

for (i in seq_along(population_names)){
  fgt <- unlist(fourgamete_slide[i])
  file_slide <- paste(dir, "_", population_names[i],
  "_4GT_per_sliding_window.pdf", sep = "")
  slide_plot <- ggplot(as.data.frame(fgt), aes(x = xaxis,
      y = as.data.frame(fgt))) +
      geom_smooth(colour = "black", fill = "greenyellow") + ggtitle(dir) +
      xlab("Contig coordinate (kbp)") + ylab("Four gamete test") +
      scale_x_continuous(breaks = pretty(xaxis, n = 10))
  ggsave(file_slide, slide_plot)
  #write table with raw data
  slide_table <- paste(dir, "_", population_names[i],
  "_4GT_per_sliding_window.txt", sep = "")
  write.table(as.data.frame(fourgamete_slide[i]), file = slide_table,
  sep = "\t", quote = FALSE, col.names = FALSE)
}

}

for (i in seq_along(population_names)){
  #Pi (hap)
  file_table2 <- paste("genome_", population_names[i],
  "_Pi_hap_per_gene_all.txt", sep = "")
  x <- as.data.frame(read.delim(file_table2))
  file_hist <- paste("genome_", population_names[i],
  "_Pi_hap_per_gene_all.pdf", sep = "")
  pi_plot <- ggplot(x, aes(x = x[, 3])) +
  geom_histogram(colour = "black", fill = "blue") +
  xlab(expression(paste(pi, " (hap) per gene"))) + ylab("Number of genes") +
  scale_x_continuous(breaks = pretty(x[, 3], n = 10))
  ggsave(file_hist, pi_plot)
  #Total FST (hap)
  file_table2 <- paste("genome_", population_names[i],
  "_total_FST_hap_per_gene_all.txt", sep = "")
  x <- as.data.frame(read.delim(file_table2))
  file_hist <- paste("genome_", population_names[i],
  "_total_FST_hap_per_gene_all.pdf", sep = "")
  fst_plot <- ggplot(x, aes(x = x[, 3])) +
  geom_histogram(colour = "black", fill = "darkseagreen") +
  xlab(expression(paste("Total FST (hap) per gene"))) +
  ylab("Number of genes") + scale_x_continuous(breaks = pretty(x[, 3], n = 10))
  ggsave(file_hist, fst_plot)
  #Four gamete test
  file_table2 <- paste("genome_", population_names[i], "_4GT_per_gene_all.txt",
  sep = "")
  x <- as.data.frame(read.delim(file_table2))
  file_hist <- paste("genome_", population_names[i], "_4GT_per_gene_all.pdf",
  sep = "")
  fgt_plot <- ggplot(x, aes(x = x[, 3])) +
  geom_histogram(colour = "black", fill = "cornsilk") +
  xlab("Four gamete test") + ylab("Number of genes") +
  scale_x_continuous(breaks = pretty(x[, 3], n = 10))
  ggsave(file_hist, fgt_plot)
}

for (i in seq(pairs)){
#Pairwise FST (hap)
file_table2 <- paste("genome_pairwise_FST_hap_per_gene_all", i, ".txt",
sep = "")
x <- as.data.frame(read.delim(file_table2))
file_hist <- paste("genome_pairwise_FST_hap_per_gene_all", i, ".pdf", sep = "")
fst_plot <- ggplot(x, aes(x = x[, 2])) +
geom_histogram(colour = "black", fill = "cadetblue") +
xlab(expression(paste("Pairwise FST (hap) per gene"))) +
ylab("Number of genes") + scale_x_continuous(breaks = pretty(x[, 2], n = 10))
ggsave(file_hist, fst_plot)
}

#Dxy (hap)
file_table2 <- "genome_dxy_hap_per_gene_all.txt"
x <- as.data.frame(read.delim(file_table2))
file_hist <- "genome_dxy_hap_per_gene_all.pdf"
dxy_plot <- ggplot(x, aes(x = x[, 3])) +
geom_histogram(colour = "black", fill = "green") + xlab("Dxy (hap) per gene") +
ylab("Number of genes") + scale_x_continuous(breaks = pretty(x[, 3], n = 10))
ggsave(file_hist, dxy_plot)
