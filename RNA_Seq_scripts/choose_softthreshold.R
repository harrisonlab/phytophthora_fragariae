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
make_option("--out_dir", type = "character",
  help = "Directory for plots to be written to")
  )

opt <- parse_args(OptionParser(option_list = opt_list))
outdir <- opt$out_dir

# Load previous scripts output

lfile <- paste(outdir, "Cleaned_data.RData", sep = "/")
lnames <- load(file = lfile)

# Step-by-step construction of the network & module ID

# Testing soft-thresholding power values

powers <- c(c(1:10), seq(from = 12, to = 20, by = 2))

sft <- pickSoftThreshold(datexpr, powerVector = powers, verbose = 5)

# Draw a plot to allow manual picking of sft value
