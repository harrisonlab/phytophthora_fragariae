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

exp_data <- read.tsv(inp, sep = "\t")

datexpr0 <- as.data.frame(t(exp_data[, c(26:33)]))
names(datexpr0) <- exp_data$transcript_id
rownames(datexpr0) <- names(exp_data)[c(26:33)]
