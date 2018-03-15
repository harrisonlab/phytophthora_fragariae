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

lfile <- paste(outdir, "Cleaned_data.RData", sep = "/")
lnames <- load(file = lfile)
lfile2 <- paste(outdir, "modules.RData", sep = "/")
lnames2 <- load(file = lfile2)

# Load list of transcript IDs

transcripts <- names(datexpr)
