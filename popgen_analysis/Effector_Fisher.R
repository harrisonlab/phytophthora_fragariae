#!/home/adamst/prog/R/R-3.2.5/bin/Rscript

# Load libraries

library("optparse")

# Load command line options

opt_list <- list(
    make_option("--Input_Table", type = "character", help = "Fisher contigency
    table to analyse"),
    make_option("--Output_Directory", type = "character", help = "Directory
    where ouput files are written to"),
    make_option("--Effector_type", type = "character", help = "IPR term being
    examined for enrichment")
)

opt <- parse_args(OptionParser(option_list = opt_list))
Input_Table <- opt$Input_Table
Output_Directory <- opt$Output_Directory
Effector_type <- opt$Effector_type

# Create data structures pre-analysis

Fisher_Table <- data.frame()
Fisher_Table <- read.table(Input_Table, header = FALSE, sep = "\t")

Fisher_Matrix <- matrix(c(Fisher_Table$V2[1], Fisher_Table$V2[2],
Fisher_Table$V3[1], Fisher_Table$V3[2]), nrow = 2, dimnames = list(
    Annotation = c(Effector_type, "Other Genes"), Gene_Set = c(
        "Separated_Genes", "Genome")))

# Run Fishers exact test: one way, which way depending on relative proportions

Spearated_Effectors <- Fisher_Table$V2[1]
Separated_Genes <- Fisher_Table$V2[2]
Genome_Effectors <- Fisher_Table$V3[1]
Genome_Genes <- Fisher_Table$V3[2]

Separated_Ratio <- Spearated_Effectors / (Separated_Genes + Spearated_Effectors)
Genome_Ratio <- Genome_Effectors / (Genome_Genes + Genome_Effectors)

Out_enriched_up <- paste(Output_Directory, "enriched_up.txt", sep = "/")
Out_enriched_down <- paste(Output_Directory, "enriched_down.txt", sep = "/")
Out_enriched_equal <- paste(Output_Directory, "enriched_equal.txt", sep = "/")

if (Separated_Ratio > Genome_Ratio){
    results <- fisher.test(Fisher_Matrix, y = NULL, workspace = 200000,
    hybrid = FALSE, control = list(), or = 1, alternative = "greater",
    conf.int = TRUE, conf.level = 0.95, simulate.p.value = FALSE, B = 2000)
    outline <- paste(Effector_type, results$p.value, sep = "\t")
    write(outline, file = Out_enriched_up, append = T)
}

# if (Separated_Ratio < Genome_Ratio){
#     results <- fisher.test(Fisher_Matrix, y = NULL, workspace = 200000,
#     hybrid = FALSE, control = list(), or = 1, alternative = "less",
#     conf.int = TRUE, conf.level = 0.95, simulate.p.value = FALSE, B = 2000)
#     outline <- paste(IPR_term, results$p.value, sep = "\t")
#     write(outline, file = Out_enriched_down, append = T)
# }
#
# if (Separated_Ratio == Genome_Ratio){
#     results <- fisher.test(Fisher_Matrix, y = NULL, workspace = 200000,
#     hybrid = FALSE, control = list(), or = 1, alternative = "two.sided",
#     conf.int = TRUE, conf.level = 0.95, simulate.p.value = FALSE, B = 2000)
#     outline <- paste(IPR_term, results$p.value, sep = "\t")
#     write(outline, file = Out_enriched_equal, append = T)
# }
