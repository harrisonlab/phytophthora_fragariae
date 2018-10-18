#!/home/adamst/prog/R/R-3.2.5/bin/Rscript

# Load libraries

library("optparse")

# Load command line options

opt_list <- list(
    make_option("--Input_Table", type = "character", help = "Fisher contigency
    table to analyse"),
    make_option("--Output_Directory", type = "character", help = "Directory
    where ouput files are written to"),
    make_option("--Confidence_ID", type = "character", help = "Confidence level
    being analysed"),
    make_option("--Gene_Type", type = "character", help = "Type of gene being
    analysed")
)

opt <- parse_args(OptionParser(option_list = opt_list))
Input_Table <- opt$Input_Table
Output_Directory <- opt$Output_Directory
Confidence_ID <- opt$Confidence_ID
Gene_Type <- opt$Gene_Type

# Create data structures pre-analysis

Fisher_Table <- data.frame()
Fisher_Table <- read.table(Input_Table, header = FALSE, sep = "\t")

Fisher_Matrix <- matrix(c(Fisher_Table$V2[1], Fisher_Table$V2[2],
Fisher_Table$V3[1], Fisher_Table$V3[2]), nrow = 2, dimnames = list(
    Annotation = c(Gene_Type, "Other Genes"), Gene_Set = c(Confidence_ID,
        "Genome")))

Out_enriched_up <- paste(Output_Directory, "enriched_up.txt", sep = "/")
Out_enriched_down <- paste(Output_Directory, "enriched_down.txt", sep = "/")
Out_enriched_2_way <- paste(Output_Directory, "enriched_2_way.txt", sep = "/")

results_greater <- fisher.test(Fisher_Matrix, y = NULL, workspace = 200000,
hybrid = FALSE, control = list(), or = 1, alternative = "greater",
conf.int = TRUE, conf.level = 0.95, simulate.p.value = FALSE, B = 2000)
outline <- paste(Confidence_ID, Gene_Type, results_greater$p.value, sep = "\t")
write(outline, file = Out_enriched_up, append = T)

results_less <- fisher.test(Fisher_Matrix, y = NULL, workspace = 200000,
hybrid = FALSE, control = list(), or = 1, alternative = "less",
conf.int = TRUE, conf.level = 0.95, simulate.p.value = FALSE, B = 2000)
outline <- paste(Confidence_ID, Gene_Type, results_less$p.value, sep = "\t")
write(outline, file = Out_enriched_down, append = T)

results_2_way <- fisher.test(Fisher_Matrix, y = NULL, workspace = 200000,
hybrid = FALSE, control = list(), or = 1, alternative = "two.sided",
conf.int = TRUE, conf.level = 0.95, simulate.p.value = FALSE, B = 2000)
outline <- paste(Confidence_ID, Gene_Type, results_2_way$p.value, sep = "\t")
write(outline, file = Out_enriched_2_way, append = T)
