# Load WGCNA package

library("WGCNA")
library("optparse")

options(stringsAsFactors = FALSE)

opt_list <- list(
  make_option("--gene_table", type = "character",
  help = "Input file of RNA-Seq data")
  )

opt <- parse_args(OptionParser(option_list = opt_list))
inp <- opt$gene_table

Exp_Data <- read.table(inp, header = FALSE, sep = "\t", stringsAsFactors = TRUE)
