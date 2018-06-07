#!/home/adamst/prog/R/R-3.2.5/bin/Rscript

# Load libraries

library("optparse")

opt_list <- list(
    make_option("--out_file", type = "character",
    help = "Output file for figure to be written to"),
    make_option("--Chromosome_number", type = "integer",
    help = "The number of individuals sampled *
    number of chromosomes sequenced * ploidy"),
    make_option("--LD_statistics", type = "character",
    help = "Output from vcftools LD statistics calling, contains r^2
    and positions of variants"),
    make_option("--units", type = "character",
    help = "Units the distance is measured in, eg. bp, kb, Mb etc."),
    make_option("--window_size", type = "integer",
    help = "Window size used for calculating LD statistics,
    used as largest bin maximum size"),
    make_option("--bin_size", type = "integer",
    help = "Size of bin for data to be put in"),
    make_option("--Cstart", type = "double",
    help = "Starting value for C, recommended 0.1")
)

opt <- parse_args(OptionParser(option_list = opt_list))
outfile <- opt$out_file
n <- opt$Chromosome_number
LD_file <- opt$LD_statistics
units <- opt$units
Cstart <- opt$Cstart

# Parse output file into necessary variables

input <- read.table(LD_file, header = TRUE)

input$Distance <- input$POS2 - input$POS1

# Bin data

data <- tapply(test$R.2, cut(test$Distance, seq(0, window_size,
    by = bin_size)), mean)

# Fit binned data to Hills and Weir decay function
