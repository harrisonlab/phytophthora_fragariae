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

# Check for excessive missing values and ID outliers

gsg <- goodSamplesGenes(datexpr0, verbose = 3)
gsg$allOK

# Remove any genes and samples that do not pass the cut

if (!gsg$allOK){
    # Print items removed
    if (sum(!gsg$goodGenes) > 0)
        printFlush(paste("Removing genes:", paste(names(datexpr0)[
        !gsg$goodGenes], collapse = ", ")))
    if (sum(!gsg$goodSamples) > 0)
        printFlush(paste("Removing samples:", paste(rownames(datexpr0)[
        !gsg$goodSamples], collapse = ", ")))
    # Remove items that fail QC
    datexpr0 <- datexpr0[gsg$goodSamples, gsg$goodGenes]
}

# Cluster samples to check for outliers

sampletree <- hclust(dist(datexpr0), method = "average")
pdf("analysis/coexpression/sample_clustering.pdf", width = 12, height = 9)
par(cex = 0.6)
par(mar = c(0, 4, 2, 0))
plot(sampletree, main = "Sample clustering to detect outliers", sub = "",
xlab = "", cex.lab = 1.5, cex.axis = 1.5, cex.main = 2)

# Remove outlier samples, the height may need changing so be sure to check

abline(h = 15, col = "red")
clust <- cuttreeStatic(sampletree, cutHeight = 15, minSize = 10)
table(clust)
keepsamples <- (clust == 1)
datexpr <- datexpr0[keepsamples, ]
ngenes <- ncol(datexpr)
nsamples <- nrow(datexpr)
