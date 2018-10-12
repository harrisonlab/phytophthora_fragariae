#!/home/adamst/prog/R/R-3.2.5/bin/Rscript

library("PopGenome")
library("ggplot2")

######################## BEFORE RUNNING ################################
#Assign individuals to appropriate populations (or just 1!)
#This script calculates: Fay Wu's H and requires an outgroup species (coded as 'ancestral' population below)
#Output files either per contig or the entire genome (prefix genome_)
##!!!!!!!  DIPLOID organisms
##When using diploid organisms and input FASTA files generated using vcf_to_fasta.py, each sample will be artificially
#split into two sequences, 'sample_name' & prefix '_1' or '_2', for example FOC5_1, FOC5_2, each representing
#one haplotype. Both need to be input below.
Pfrag <- c("Bc1_1", "Bc1_2", "Nov5_1", "Nov5_2", "Bc16_1", "Bc16_2", "A4_1",
"A4_2", "Nov27_1", "Nov27_2", "Nov9_1", "Nov9_2", "Nov71_1", "Nov71_2")
#Assign outgroup samples to the "ancestral" population. The population name "ancestral" should
#not be changed as it evoked below on line 35.
ancestral <- c("SCRP249_1", "SCRP249_2", "SCRP324_1", "SCRP324_2", "SCRP333_1",
"SCRP333_2")
populations <- list(Pfrag)
#Number of populations assigned above.
population_no <- length(populations)
population_names <- c("Pfrag")
#########################################################################

#Folder containing FASTA alignments in the current dir
gff <- "gff"
all_folders <- list.dirs("contigs", full.names = FALSE)
#Remove the gff folder from PopGenome contig analysis
contig_folders <- all_folders[all_folders != "gff"]

#Loop through each contig-containing folder to calculate stats on each contig separately.
for (dir in contig_folders[contig_folders != ""]){
  contig_folder <- paste("contigs/", dir, sep = "")
  GENOME_class <- readData(contig_folder, gffpath = gff, include.unknown = TRUE)
  GENOME_class <- set.populations(GENOME_class, populations)
  GENOME_class <- set.outgroup(GENOME_class, new.outgroup = ancestral)

  #Calculate neutrality stats over genes
  GENOME_class_split <- splitting.data(GENOME_class, subsites = "gene")
  GENOME_class_split <- neutrality.stats(GENOME_class_split)
  fay_wu_h <- GENOME_class_split@Fay.Wu.H
  fay_wu_h_d <- as.data.frame(fay_wu_h)
  for (i in seq_along(population_names)){
    file_hist <- paste(dir, "_", population_names[i], "_FayWuH_per_gene.pdf",
    sep = "")
    fay_wu_h_len <- length(fay_wu_h_d[, i])
    fay_wu_h_na <- sum(sapply(fay_wu_h[, i], is.na))
    if (fay_wu_h_len > fay_wu_h_na){
      fay_wu_h_plot <- ggplot(fay_wu_h_d, aes(x = fay_wu_h_d[, i])) +
      geom_histogram(colour = "black", fill = "thistle4") + ggtitle(dir) +
      xlab("Fay & Wu's H") + ylab("Number of genes") +
      scale_x_continuous(breaks = pretty(fay_wu_h_d[, i], n = 10)) +
      theme(panel.grid.major = element_blank(),
      panel.grid.minor = element_blank(), panel.background = element_blank(),
      panel.border = element_rect(colour = "black", fill = NA, size = 1),
      axis.text = element_text(size = 14), axis.title = element_text(size = 18))
      ggsave(file_hist, fay_wu_h_plot)
  }
    file_table <- paste(dir, "_", population_names[i], "_FayWuH_per_gene.txt",
    sep = "")
    file_table2 <- paste("genome_", population_names[i],
    "_FayWuH_per_gene_all.txt", sep = "")
    current_gff <- paste(gff, "/", dir, ".gff", sep = "")
    gene_ids <- get_gff_info(GENOME_class_split, current_gff, chr = dir,
        feature = FALSE, extract.gene.names = TRUE)
    fay_wu_h_table <- cbind(gene_ids, fay_wu_h[, i])
    write.table(fay_wu_h_table, file = file_table, sep = "\t", quote = FALSE,
    col.names = FALSE)
    write.table(fay_wu_h_table, file = file_table2, sep = "\t", quote = FALSE,
    col.names = FALSE, append = TRUE)
  }

}

#Plot genome-wide histograms
for (i in seq_along(population_names)){
  #Tajima's D table
  file_table2 <- paste("genome_", population_names[i],
  "_FayWuH_per_gene_all.txt", sep = "")
  x <- as.data.frame(read.delim(file_table2))
  file_hist <- paste("genome_", population_names[i],
  "_FayWuH_per_gene_all.pdf", sep = "")
  fay_wu_h_plot <- ggplot(x, aes(x = x[, 3])) +
  geom_histogram(colour = "black", fill = "thistle1") + xlab("Fay & Wu's H") +
  ylab("Number of genes") +
  scale_x_continuous(breaks = pretty(x[, 3], n = 10)) +
  theme(panel.grid.major = element_blank(),
  panel.grid.minor = element_blank(), panel.background = element_blank(),
  panel.border = element_rect(colour = "black", fill = NA, size = 1),
  axis.text = element_text(size = 14), axis.title = element_text(size = 18))
  ggsave(file_hist, fay_wu_h_plot)
}
