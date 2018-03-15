#!/home/adamst/prog/R/R-3.2.5/Rscript

# Load packages

library("WGCNA")
library("optparse")

# Import option recommended in WGCNA documentation

options(stringsAsFactors = FALSE)

# Parse arguments

opt_list <- list(
    make_option("--out_dir", type = "character",
    help = "Directory for output to be written to")
    )

opt <- parse_args(OptionParser(option_list = opt_list))
outdir <- opt$out_dir
