#!/home/adamst/prog/R/R-3.2.5/Rscript

# Load packages

library("WGCNA")
library("optparse")

# Import option recommended in WGCNA documentation

options(stringsAsFactors = FALSE)

# Parse arguments

opt_list <- list(
    make_option("--out_dir", type = "character",
    help = "Directory for output to be written to"),
    make_option("--gene_table", type = "character",
    help = "Input file of RNA-Seq data")
    )

opt <- parse_args(OptionParser(option_list = opt_list))
outdir <- opt$out_dir
inp <- opt$gene_table

exp_data <- read.csv(inp, sep = "\t")

lfile <- paste(outdir, "Cleaned_data.RData", sep = "/")
lnames <- load(file = lfile)
lfile2 <- paste(outdir, "modules.RData", sep = "/")
lnames2 <- load(file = lfile2)

# Match gene names to IDs in the annotation file
