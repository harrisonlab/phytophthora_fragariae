#!/home/adamst/prog/R/R-3.2.5/bin/Rscript

# Load packages

library("optparse")

# Parse arguments

opt_list <- list(
    make_option("--in_file", type = "character",
    help = "input file of FPKM values"),
    make_option("--out_file", type = "character",
    help = "output of SSE scree plot")
)

opt <- parse_args(OptionParser(option_list = opt_list))
inp <- opt$in_file
out <- opt$out_file
