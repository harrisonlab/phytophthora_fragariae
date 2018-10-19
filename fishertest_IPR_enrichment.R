#!/home/adamst/prog/R/R-3.2.5/bin/Rscript

# Load libraries

library("optparse")

# Load command line options

opt_list <- list(
    make_option("--Input_Table", type = "character", help = "Fisher contigency
    table to analyse"),
    make_option("--Output_Directory", type = "character", help = "Directory
    where ouput files are written to"),
    make_option("--IPR_term", type = "character", help = "IPR term being
    examined for enrichment")
)

opt <- parse_args(OptionParser(option_list = opt_list))
Input_Table <- opt$Input_Table
Output_Directory <- opt$Output_Directory
IPR_term <- opt$IPR_term

# Create data structures pre-analysis

Fisher_Table <- data.frame()
Fisher_Table <- read.table(Input_Table, header = FALSE, sep = "\t")

Fisher_Matrix <- matrix(c(Fisher_Table$V2[1], Fisher_Table$V2[2],
Fisher_Table$V3[1], Fisher_Table$V3[2]), nrow = 2, dimnames = list(
    Annotation = c(IPR_term, "Other Genes"), Gene_Set = c("Separated_Genes",
    "Genome")))

# Run Fishers exact test: one way, which way depending on relative proportions

Spearated_IPRs <- Fisher_Table$V2[1]
Separated_Genes <- Fisher_Table$V2[2]
Genome_IPRs <- Fisher_Table$V3[1]
Genome_Genes <- Fisher_Table$V3[2]

Separated_Ratio <- Spearated_IPRs / (Separated_Genes + Spearated_IPRs)
Genome_Ratio <- Genome_IPRs / (Genome_Genes + Genome_IPRs)

Out_enriched_up <- paste(Output_Directory, "enriched_up.txt", sep = "/")
Out_enriched_down <- paste(Output_Directory, "enriched_down.txt", sep = "/")
Out_enriched_equal <- paste(Output_Directory, "enriched_equal.txt", sep = "/")

if (Separated_Ratio > Genome_Ratio){
    results <- fisher.test(Fisher_Matrix, y = NULL, workspace = 200000,
    hybrid = FALSE, control = list(), or = 1, alternative = "greater",
    conf.int = TRUE, conf.level = 0.95, simulate.p.value = FALSE, B = 2000)
    outline <- paste(IPR_term, results$p.value, sep = "\t")
    write(outline, file = Out_enriched_up, append = T)
}
