#!/usr/bin/Rscript

# Load packages

library("WGCNA")
library("optparse")

# Important option recommended in WGCNA documentation

options(stringsAsFactors = FALSE)

# Allow multi-threading

enableWGCNAThreads()

# Parse arguments

opt_list <- list(
make_option("--out_dir", type = "character",
  help = "Directory for plots to be written to")
  )

opt <- parse_args(OptionParser(option_list = opt_list))
outdir <- opt$out_dir
