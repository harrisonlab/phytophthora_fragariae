#!/home/adamst/prog/R/R-3.2.5/bin/Rscript

# Load libraries

library("optparse")

# Load command line options

opt_list <- list(
    make_option("--Input_Table", type = "character", help = "Fisher contigency
    table to analyse"),
    make_option("--Output_File", type = "character", help = "Output tab
    separated file"),
    make_option("--Module_ID", type = "character", help = "Name of module being
    analysed"),
    make_option("--Gene_Type", type = "character", help = "Type of gene being
    analysed")
)

opt <- parse_args(OptionParser(option_list = opt_list))
Input_Table <- opt$Input_Table
Output_File <- opt$Output_File
Module_ID <- opt$Module_ID
Gene_Type <- opt$Gene_Type

# Create data structures pre-analysis

Fisher_Table <- data.frame()
Fisher_Table <- read.table(Input_Table, header = FALSE, sep = "\t")

Fisher_Matrix <- matrix(c(Fisher_Table$V2[1], Fisher_Table$V2[2],
Fisher_Table$V3[1], Fisher_Table$V3[2]), nrow = 2, dimnames = list(
    Annotation = c(Gene_Type, "Other Genes"), Gene_Set = c(Module_ID, "Genome")
))

# Run Fishers exact test: two-way test

results <- fisher.test(Fisher_Matrix, y = NULL, workspace = 200000,
hybrid = FALSE, control = list(), or = 1, alternative = "two.sided",
conf.int = TRUE, conf.level = 0.95, simulate.p.value = FALSE, B = 2000)

# Write out results

outline <- paste(Module_ID, Gene_Type, results$p.value, sep = "\t")
write(outline, file = Output_File, append = T)
