#!/home/adamst/prog/R/R-3.2.5/Rscript

# Load packages

library("WGCNA")
library("optparse")

# Important option recommended in WGCNA documentation

options(stringsAsFactors = FALSE)

# Allow multi-threading

enableWGCNAThreads()
