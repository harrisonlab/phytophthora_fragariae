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
    make_option("--unmerge", type = "character",
    help = "Y or N, Y exports unmerged modules, N does not")
    )

opt <- parse_args(OptionParser(option_list = opt_list))
outdir <- opt$out_dir
unmerge <- opt$unmerge

lfile <- paste(outdir, "Cleaned_data.RData", sep = "/")
lnames <- load(file = lfile)
lfile2 <- paste(outdir, "modules.RData", sep = "/")
lnames2 <- load(file = lfile2)

# Load list of transcript IDs and write out merged modules

transcripts <- names(datexpr)
for (module in unique(modulecolours)){
    modgenes <- (modulecolours == module)
    modtranscripts <- transcripts[modgenes]
    filename <- paste("Genes_in_", module, ".txt", sep = "")
    file <- paste(outdir, "merged_modules", filename, sep = "/")
    write.table(as.data.frame(modtranscripts), file = file, row.names = FALSE,
    col.names = FALSE)
}

# Write out unmerged modules

for (module in unique(dynamiccolours)){
    modgenes <- (dynamiccolours == module)
    modtranscripts <- transcripts[modgenes]
    filename <- paste("Genes_in_", module, ".txt", sep = "")
    file <- paste(outdir, "unmerged_modules", filename, sep = "/")
    write.table(as.data.frame(modtranscripts), file = file, row.names = FALSE,
    col.names = FALSE)
}
