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
Hotspot_df <- read.table(Hotspot_file)
Recomb_df_corrected <- Recomb_df[-c(1), ]

# Plot graph

Rho_plot <- ggplot(data = Recomb_df_corrected,
    aes(x = Recomb_df_corrected$Loci, y = Recomb_df_corrected$Mean_rho,
    group = 1)) + geom_line(colour = "grey") +
    labs(x = "Contig position (kb)", y = "Mean recombination rate") +
    geom_rect(data = Hotspot_df, inherit.aes = FALSE, fill = "blue",
        aes(xmin = Hotspot_df$V1, xmax = Hotspot_df$V2,
            ymin = -5, ymax = -1)) +
    scale_x_continuous(breaks = round(seq(min(0),
    max(Recomb_df_corrected$Loci), by = 100), 1)) +
    scale_y_continuous(breaks = round(seq(min(0),
    max(Recomb_df_corrected$Mean_rho), by = 5), 1)) +
    theme(panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(), panel.background = element_blank(),
    panel.border = element_rect(colour = "black", fill = NA, size = 1),
    axis.text = element_text(size = 14), axis.title = element_text(size = 18))

# Save graph to file

ggsave(outfile, Rho_plot, width = 21, height = 7)
