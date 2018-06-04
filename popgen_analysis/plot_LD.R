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
