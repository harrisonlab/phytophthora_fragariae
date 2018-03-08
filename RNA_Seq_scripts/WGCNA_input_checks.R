# Load WGCNA package

library("WGCNA")
library("optparse")

# Important option recommended by WGCNA

options(stringsAsFactors = FALSE)

# Parse in arguments to script

opt_list <- list(
  make_option("--gene_table", type = "character",
  help = "Input file of RNA-Seq data")
  )

opt <- parse_args(OptionParser(option_list = opt_list))
inp <- opt$gene_table

# Load input file

exp_data <- read.tsv(inp, sep = "\t")

# Parse data as WGCNA tutorial recommends

datexpr0 <- as.data.frame(t(exp_data[, c(26:33)]))
names(datexpr0) <- exp_data$transcript_id
rownames(datexpr0) <- names(exp_data)[c(26:33)]
