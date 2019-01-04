#!/usr/bin/Rscript

# Plot a 3-way Venn diagram from a tab delimited file containing a matrix showing
 # presence /absence of orthogroups between 3 sets of genomes.

 # This is intended to be used on the output of the orthoMCL pipeline following
 # building of the matrix using:
 # ~/git_repos/emr_repos/tools/pathogen/orthology/orthoMCL/orthoMCLgroups2tab.py

 # The script also requires the colorspace package. This can be downloaded by
 # opening R and running the following command:

 #get config options
library("optparse")
library("VennDiagram")
opt_list <- list(
    make_option("--inp", type = "character",
    help = "tab seperated file containing matrix of presence of orthogroups"),
    make_option("--out", type = "character",
    help = "output venn diagram in pdf format")
)
opt <- parse_args(OptionParser(option_list = opt_list))
f <- opt$inp
o <- opt$out

orthotabs <- data.frame()
orthotabs <- read.table(f)
df1 <- t(orthotabs)
summary(df1)

A4 <- subset(df1, df1[, "A4"] == 1 & df1[, "Nov5"] == 0 & df1[, "Nov27"] == 0 &
df1[, "Nov71"] == 0 & df1[, "Bc16"] == 0 & df1[, "Nov9"] == 0 &
df1[, "Bc1"] == 0)
BC16 <- subset(df1, df1[, "A4"] == 0 & df1[, "Nov5"] == 0 &
df1[, "Nov27"] == 0 & df1[, "Nov71"] == 0 & df1[, "Bc16"] == 1 &
df1[, "Nov9"] == 0 & df1[, "Bc1"] == 0)
Others <- subset(df1, df1[, "A4"] == 0 & df1[, "Nov5"] != 0 &
df1[, "Nov27"] != 0 & df1[, "Nov71"] != 0 & df1[, "Bc16"] == 0 &
df1[, "Nov9"] != 0 & df1[, "Bc1"] != 0)

# Set up labels
label1 <- paste("A4", "(UK2)", sep = "\n" )
label2 <- paste("BC-16", "(UK2)", sep = "\n" )
label3 <-
paste("NOV-5 (UK1), NOV-27 (UK3), NOV-71 (UK3),", "NOV-9 (UK3) & BC-1 (UK1)",
sep = "\n" )

n123 <- nrow(subset(df1, df1[, "A4"] == 1 & df1[, "Nov5"] != 0 &
df1[, "Nov27"] != 0 & df1[, "Nov71"] != 0 & df1[, "Bc16"] == 1 &
df1[, "Nov9"] != 0 & df1[, "Bc1"] != 0))
n12 <- n123 + nrow(subset(df1, df1[, "A4"] == 1 & df1[, "Nov5"] == 0 &
df1[, "Nov27"] == 0 & df1[, "Nov71"] == 0 & df1[, "Bc16"] == 1 &
df1[, "Nov9"] == 0 & df1[, "Bc1"] == 0))
n13 <- n123 + nrow(subset(df1, df1[, "A4"] == 1 & df1[, "Nov5"] != 0 &
df1[, "Nov27"] != 0 & df1[, "Nov71"] != 0 & df1[, "Bc16"] == 0 &
df1[, "Nov9"] != 0 & df1[, "Bc1"] != 0))
n23 <- n123 + nrow(subset(df1, df1[, "A4"] == 0 & df1[, "Nov5"] != 0 &
df1[, "Nov27"] != 0 & df1[, "Nov71"] != 0 & df1[, "Bc16"] == 1 &
df1[, "Nov9"] != 0 & df1[, "Bc1"] != 0))
summary(n12)
summary(n13)
summary(n23)
summary(n123)

area1 <- (nrow(A4) + (n12 - n123) + (n13 - n123) + n123)
area2 <- (nrow(BC16) + (n12 - n123) + (n23 - n123) + n123)
area3 <- (nrow(Others) + (n13 - n123) + (n23 - n123) + n123)
nrow(A4)
nrow(BC16)
nrow(Others)
n12
n13
n23
n123
area1
area2
area3

pdf(o)
draw.triple.venn(area1, area2, area3,
    n12, n23, n13,
    n123,
    category = c(label1, label2, label3),
#    rep("", 4),
    rotation = 1,
    reverse = FALSE,
    lwd = rep(2, 3),
    lty = rep("solid", 3),
    col = rep("black", 3),
    fill = c("forestgreen", "royalblue2", "khaki1"),
    alpha = rep(0.5, 3),
    label.col = rep("black", 7),
    cex = rep(2, 7),
    fontface = rep("plain", 7),
    fontfamily = rep("sans", 7),
    cat.pos = c(-40, 40, 180),
    cat.dist = c(0.15, 0.15, 0.1),
    cat.col = rep("black", 3),
    cat.cex = rep(2, 3),
    cat.fontface = rep("plain", 3),
    cat.fontfamily = rep("sans", 3),
    cat.just = list(c(0.5, 1), c(0.5, 1), c(0.5, 0)),
    cat.default.pos = "outer",
    cat.prompts = FALSE,
    rotation.degree = 0,
    rotation.centre = c(0.5, 0.5),
    ind = TRUE, sep.dist = 0.05, offset = 0,
    )


dev.off()

singles <- df1[grepl("single*", rownames(df1)), ]
print("A4")
total_1 <- nrow(subset (df1, df1[, "A4"] == 1))
missing_1 <- (total_1 - area1)
uniq_1 <- sum(singles[, "A4"])
paste("The total number of orthogroups and singleton genes in this isolate: ",
total_1)
paste("The total number of orthogroups and singleton genes not in the
venn diagram: ", missing_1)
paste("The total number of singleton genes not in the venn diagram: ", uniq_1)
print("NOV-5")
total_2 <- nrow(subset (df1, df1[, "Nov5"] == 1))
missing_2 <- (total_2 - area3)
uniq_2 <- sum(singles[, "Nov5"])
paste("The total number of orthogroups and singleton genes in this isolate: ",
total_2)
paste("The total number of orthogroups and singleton genes not in the
venn diagram: ", missing_2)
paste("The total number of singleton genes not in the venn diagram: ", uniq_2)
print("NOV-27")
total_3 <- nrow(subset (df1, df1[, "Nov27"] == 1))
missing_3 <- (total_3 - area3)
uniq_3 <- sum(singles[, "Nov27"])
paste("The total number of orthogroups and singleton genes in this isolate: ",
total_3)
paste("The total number of orthogroups and singleton genes not in the
venn diagram: ", missing_3)
paste("The total number of singleton genes not in the venn diagram: ", uniq_3)
print("NOV-71")
total_4 <- nrow(subset (df1, df1[, "Nov71"] == 1))
missing_4 <- (total_4 - area3)
uniq_4 <- sum(singles[, "Nov71"])
paste("The total number of orthogroups and singleton genes in this isolate: ",
total_4)
paste("The total number of orthogroups and singleton genes not in the
venn diagram: ", missing_4)
paste("The total number of singleton genes not in the venn diagram: ", uniq_4)
print("BC-16")
total_5 <- nrow(subset (df1, df1[, "Bc16"] == 1))
missing_5 <- (total_5 - area2)
uniq_5 <- sum(singles[, "Bc16"])
paste("The total number of orthogroups and singleton genes in this isolate: ",
total_5)
paste("The total number of orthogroups and singleton genes not in the
venn diagram: ", missing_5)
paste("The total number of singleton genes not in the venn diagram: ", uniq_5)
print("NOV-9")
total_6 <- nrow(subset (df1, df1[, "Nov9"] == 1))
missing_6 <- (total_6 - area3)
uniq_6 <- sum(singles[, "Nov9"])
paste("The total number of orthogroups and singleton genes in this isolate: ",
total_6)
paste("The total number of orthogroups and singleton genes not in the
venn diagram: ", missing_6)
paste("The total number of singleton genes not in the venn diagram: ", uniq_6)
print("BC-1")
total_7 <- nrow(subset (df1, df1[, "Bc1"] == 1))
missing_7 <- (total_6 - area3)
uniq_7 <- sum(singles[, "Bc1"])
paste("The total number of orthogroups and singleton genes in this isolate: ",
total_7)
paste("The total number of orthogroups and singleton genes not in the
venn diagram: ", missing_7)
paste("The total number of singleton genes not in the venn diagram: ", uniq_7)

warnings()
q()
