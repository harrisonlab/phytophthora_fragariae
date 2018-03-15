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

# Select module transcripts

modules <- names(modulecolours)
transcripts <- names(datexpr)
inmodule <- is.finite(match(modulecolours, modules))
modtranscripts <- transcripts[inmodule]

# Select corresponding TOM value

modtom <- tom[inmodule, inmodule]
dimnames(modtom) <- list(modtranscripts, modtranscripts)

# Export the network into edge & node list files for Cytoscape

cyt <- exportNetworkToCytoscape(modtom,
    edgeFile = paste("Cytoscape_Input_Edges", paste(modules, collapse = "-"),
    ".txt", sep = ""), nodeFile = paste("Cytoscape_Input_Nodes",
    paste(modules, collapse = "-"), ".txt", sep = ""), weighted = TRUE,
    threshold = 0.02, nodeNames = modtranscripts,
    altNodeNames = modtranscripts, nodeAttr = modulecolours[inmodule])
