#!/home/adamst/prog/R/R-3.2.5/bin/Rscript

# This is based on commands listed in the folowing stack overflow answer
# https://stackoverflow.com/questions/15376075/cluster-analysis-in-r-determine-the-optimal-number-of-clusters/15376462#15376462

# Load packages

library("optparse")

# Parse arguments

opt_list <- list(
    make_option("--in_file", type = "character",
    help = "input file of FPKM values"),
    make_option("--out_file_SSE", type = "character",
    help = "output file of SSE scree plot")
)

opt <- parse_args(OptionParser(option_list = opt_list))
inp <- opt$in_file
out_SSE <- opt$out_file_SSE

# Load in file and draw SSE plot

exp_data <- read.csv(inp, header = TRUE, sep = "\t")
wss <- (nrow(exp_data) - 1) * sum(apply(exp_data, 2, var))
for (i in 2:15) wss [i] <- sum(kmeans(exp_data, centers = 1)$withinss)
pdf(out_SSE)
plot(1:15, wss, type = "b", xlab = "Number of Clusters",
ylab = "Within groups sum of squares")
dev.off()
