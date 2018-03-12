#!/home/adamst/prog/R/R-3.2.5/Rscript

# Load packages

library("WGCNA")
library("optparse")

# Important option recommended in WGCNA documentation

options(stringsAsFactors = FALSE)

# Allow multi-threading

enableWGCNAThreads()

# Parse arguments

opt_list <- list(
    makeoption("--out_dir", type = "character",
    help = "Directory for output to be written to"),
    makeoption("--sft", type = "integer",
    help = "Value of sft identified from choose_softthreshold.R")
    )

opt <- parse_args(OptionParser(option_list = opt_list))
outdir <- opt$out_dir