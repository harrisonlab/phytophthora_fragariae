#!/home/adamst/prog/R/R-3.2.5/bin/Rscript

# Load libraries

library("optparse")

opt_list <- list(
    make_option("--out_file", type = "character",
    help = "Output file for figure to be written to"),
    make_option("--Chromosome_number", type = "integer",
    help = "The number of chromosomes (or contigs) sampled"),
    make_option("--LD_statistics", type = "character",
    help = "Output from vcftools LD statistics calling, contains r^2
    and positions of variants")
)

opt <- parse_args(OptionParser(option_list = opt_list))
outfile <- opt$out_file
Chrom_Num <- opt$Chromosome_number
LD_file <- opt$LD_statistics

# Parse output file into necessary variables

input <- read.table(LD_file, header = TRUE)

input$Distance <- input$POS2 - input$POS1
distance <- c(input$Distance)

r_sqd <- c(input$R.2)
