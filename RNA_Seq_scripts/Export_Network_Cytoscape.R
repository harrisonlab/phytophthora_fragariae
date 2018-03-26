#!/home/adamst/prog/R/R-3.2.5/bin/Rscript

# Load packages

library("WGCNA")
library("optparse")

# Import option recommended in WGCNA documentation

options(stringsAsFactors = FALSE)

# Parse arguments

opt_list <- list(
    make_option("--out_dir", type = "character",
    help = "Directory for output to be written to"),
    make_option("--module", type = "character",
    help = "module to export for visualisation in Cytoscape")
    )

opt <- parse_args(OptionParser(option_list = opt_list))
outdir <- opt$out_dir

lfile <- paste(outdir, "Cleaned_data.RData", sep = "/")
lnames <- load(file = lfile)
lfile2 <- paste(outdir, "modules.RData", sep = "/")
lnames2 <- load(file = lfile2)

# Set variables for writing out files for Cytoscape

transcripts <- names(datexpr)
modules <- unique(modulecolours)
inmodule <- is.finite(match(modulecolours, modules))
modtranscripts <- transcripts[inmodule]
modtom <- tom[inmodule, inmodule]
dimnames(modtom) <- list(modtranscripts, modtranscripts)

# Write out files for Cytoscape

cyt <- exportNetworkToCytoscape(modtom,
edgeFile = paste(outdir, "cyt_inp_edges_all_modules.txt", sep = "/"),
nodeFile = paste(outdir, "cyt_inp_nodes_all_modules.txt", sep = "/"),
weighted = TRUE, threshold = 0.02, nodeNames = modtranscripts,
altNodeNames = modtranscripts, nodeAttr = modulecolours[inmodule])
