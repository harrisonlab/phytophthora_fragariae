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
n <- opt$Chromosome_number
LD_file <- opt$LD_statistics

# Parse output file into necessary variables

input <- read.table(LD_file, header = TRUE)

input$Distance <- input$POS2 - input$POS1
distance <- c(input$Distance)

LD_data <- c(input$R.2)

# Fit results to decomposition model
# Following code from:
# https://fabiomarroni.wordpress.com/2011/08/09/estimate-decay-of-linkage-disequilibrium-with-distance/

HW_st <- c(C = 0.1)
HW_nonlinear <- nls(LD_data~ ( (10 + C * distance) / ( (2 + C *
    distance) * (11 + C * distance))) * (1 + ( (3 + C * distance) * (12 +
        12 * C * distance + (C * distance) ^ 2)) / (n * (2 + C *
            distance) * (11 + C * distance))), start = HW_st,
            control = nls.control(maxiter = 100))
tt <- summary(HW_nonlinear)
new_rho <- tt$parameters[1]
fpoints <- ( (10 + new_rho * distance) / ( (2 + new_rho * distance) * (11 +
    new_rho * distance))) * (1 + ( (3 + new_rho * distance) * (12 + 12 *
        new_rho * distance + (new_rho * distance) ^ 2)) / (n * (2 + new_rho *
            distance) * (11 + new_rho * distance)))

# Calculate the half-decay distance

df <- data.frame(distance, fpoints)
maxld <- max(LD_data)
half_decay <- maxld / 2
half_decay_distance <- df$distance[which.min(abs(df$fpoints - half_decay))]
cat("Half decay distance of LD r^2: ", half_decay_distance)

# Plot LD points and a dotted line

pdf(outfile)
ld_df <- data.frame(distance, fpoints)
ld_df <- ld_df[order(ld_df$distance), ]
plot(distance, LD_data, pch = 19, cex = 0.9)
lines(ld_df$distance, ld_df$fpoints, lty = 3, lwd = 1.2)
dev.off()
