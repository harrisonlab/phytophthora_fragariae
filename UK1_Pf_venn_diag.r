#!/usr/bin/Rscript

# Plot a 3-way Venn diagram from a tab delimited file containing a matrix showing
 # presence /absence of orthogroups between 3 genomes.

 # This is intended to be used on the output of the orthoMCL pipeline following
 # building of the matrix using:
 # ~/git_repos/emr_repos/tools/pathogen/orthology/orthoMCL/orthoMCLgroups2tab.py

# This script requires the optparse R package. This can be downloaded by opening
# R and running the following command:
# install.packages("optparse",repos="http://cran.uk.r-project.org")
# When given the option, install this package to a local library.

#get config options
library(optparse)
library(VennDiagram, lib.loc="/home/armita/R-packages/")
opt_list = list(
    make_option("--inp", type="character", help="tab seperated file containing matrix of presence of orthogroups"),
    make_option("--out", type="character", help="output venn diagram in pdf format")
#    make_option("--maxrf", type="double", default=0.2, help="max rf to consider as linked"),
#    make_option("--minlod", type="double", default=20.0, help="min LOD to consider as linked")
)
opt = parse_args(OptionParser(option_list=opt_list))
f = opt$inp
o = opt$out

orthotabs <-data.frame()
orthotabs <- read.table(f)
df1 <- t(orthotabs)
summary(df1)


area1=sum(df1[, 1])
area2=sum(df1[, 2])
area3=sum(df1[, 3])

# print(area1, area2, area3, area4)

colname1 <- paste(colnames(df1)[1])
colname2 <- paste(colnames(df1)[2])
colname3 <- paste(colnames(df1)[3])

label1 <- paste(colname1, ' (', area1, ')', sep="" )
label2 <- paste(colname2, ' (', area2, ')', sep="" )
label3 <- paste(colname3, ' (', area3, ')', sep="" )

n12=nrow(subset(df1, df1[,1] == 1 & df1[,2] == 1))
n13=nrow(subset(df1, df1[,1] == 1 & df1[,3] == 1))
n23=nrow(subset(df1, df1[,2] == 1 & df1[,3] == 1))
n123=nrow(subset(df1, df1[,1] == 1 & df1[,2] == 1 & df1[,3] == 1))
label1
area1
label2
area2
label3
area3
n12
n13
n23
n123
summary(n12)
summary(n123)
pdf(o)
draw.triple.venn(area1, area2, area3,
    n12, n23, n13,
    n123,
    category = c(label1, label2, label3),
#    rep("", 4),
    rotation = 1,
    reverse = FALSE,
    #euler.d = TRUE,
    #scaled = TRUE,
    lwd = rep(2, 3),
    lty = rep("solid", 3),
    col = rep("black", 3),
    fill = NULL,
    alpha = rep(0.5, 3),
    label.col = rep("black", 7),
    cex = rep(1, 7),
    fontface = rep("plain", 7),
    fontfamily = rep("serif", 7),
    cat.pos = c(-40, 40, 180),
    cat.dist = c(0.05, 0.05, 0.025),
    cat.col = rep("black", 3),
    cat.cex = rep(1, 3),
    cat.fontface = rep("plain", 3),
    cat.fontfamily = rep("serif", 3),
    cat.just = list(c(0.5, 1), c(0.5, 1), c(0.5, 0)),
    cat.default.pos = "outer",
    cat.prompts = FALSE,
    rotation.degree = 0,
    rotation.centre = c(0.5, 0.5),
    ind = TRUE, sep.dist = 0.05, offset = 0,
    )

dev.off()
singles = df1[grepl("single*", rownames(df1)), ]
uniq_1=sum(singles[, 1])
uniq_2=sum(singles[, 2])
uniq_3=sum(singles[, 3])
orthogroups = df1[grepl("orthogroup*", rownames(df1)), ]
inpara_1 = sum(orthogroups[,1] == 1 & orthogroups[,2] == 0 & orthogroups[,3] == 0)
inpara_2 = sum(orthogroups[,1] == 0 & orthogroups[,2] == 1 & orthogroups[,3] == 0)
inpara_3 = sum(orthogroups[,1] == 0 & orthogroups[,2] == 0 & orthogroups[,3] == 1)
label1
uniq_1
inpara_1
label2
uniq_2
inpara_2
label3
uniq_3
inpara_3

warnings()
q()
