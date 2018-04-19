#!/home/adamst/prog/R/R-3.2.5/bin/Rscript

# Load libraries

library(optparse)
opt_list <- list(
    make_option("--Input_Table", type = "character", help = "Fisher contigency
    table to analyse"),
    make_option("--Output_File", type = "character", help = "Output tab
    separated file")
)

opt <- parse_args(OptionParser(option_list = opt_list))
Input_Table <- opt$Input_Table
Output_File <- opt$Output_File
