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
softpower <- opt$sft

lfile <- paste(outdir, "Cleaned_data.RData", sep = "/")
lnames <- load(file = lfile)

# Calculate adjacency

adjacency <- adjacency(datexpr, power = softpower)

# Topological Overlap Matrix (TOM)

tom <- TOMsimilarity(adjacency)
disstom <- 1 - tom

# Clustering using TOM

genetree <- hclust(as.dist(disstom), method = "average")

file <- paste(outdir, "clustering_tree.pdf", sep = "/")
pdf(file, height = 9, width = 12)
sizeGrWindow(12, 9)
plot(genetree, xlab = "", sub = "", main = "Gene clustering on TOM-based
dissimilarity", labels = FALSE, hang = 0.04)
dev.off()
