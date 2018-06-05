#!/home/adamst/prog/R/R-3.2.5/bin/Rscript

# Load libraries

library("ggplot2")
library("optparse")

# Parse arguments

opt_list <- list(
    make_option("--out_file", type = "character",
    help = "Output file for figure to be written to"),
    make_option("--res_in", type = "character",
    help = "File containing the mean recombination rates at different loci"),
    make_option("--hotspot_in", type = "character",
    help = "File containing the locations of recombination hotspots")
)

opt <- parse_args(OptionParser(option_list = opt_list))
outfile <- opt$out_file
Recomb_file <- opt$res_in
Hotspot_file <- opt$hotspot_in

# Load input files

Recomb_df <- read.table(Recomb_file, header = TRUE)
Hotspot_df <- read.table(Hotspot_file, header = TRUE)
Recomb_df_corrected <- Recomb_df[-c(1), ]

# Plot graph

Rho_plot <- ggplot(data = Recomb_df_corrected, aes(x = Loci, y = Mean_rho,
    group = 1)) + geom_line() + geom_point() +
    labs(x = "Contig position (bp)", y = "Mean recombination rate")

# Save graph to file

ggsave(outfile, Rho_plot, width = 21, height = 7)
