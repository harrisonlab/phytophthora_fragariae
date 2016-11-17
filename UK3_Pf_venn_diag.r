#!/usr/bin/Rscript

# Plot a 4-way Venn diagram from a tab delimited file containing a matrix showing
 # presence /absence of orthogroups within 4 isolates.

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

# print(area1, area2, area3, area4)

# colname1 <- paste(colnames(df1)[1])
# colname2 <- paste(colnames(df1)[2])
# colname3 <- paste(colnames(df1)[3])
# colname4 <- paste(colnames(df1)[4])

label1 <- paste("NOV-27", sep="" )
label2 <- paste("NOV-71", sep="" )
label3 <- paste("NOV-9", sep="" )
label4 <- paste("A4, NOV-5, BC-16 & BC-1", sep="" )

NOV27=subset(df1, df1[,"A4"] == 0 & df1[,"Nov5"] == 0 & df1[,"Nov27"] == 1 & df1[,"Nov71"] == 0 & df1[,"Bc16"] == 0 & df1[,"Nov9"] == 0 & df1[,"Bc1"] == 0)
NOV71=subset(df1, df1[,"A4"] == 0 & df1[,"Nov5"] == 0 & df1[,"Nov27"] == 0 & df1[,"Nov71"] == 1 & df1[,"Bc16"] == 0 & df1[,"Nov9"] == 0 & df1[,"Bc1"] == 0)
NOV9=subset(df1, df1[,"A4"] == 0 & df1[,"Nov5"] == 0 & df1[,"Nov27"] == 0 & df1[,"Nov71"] == 0 & df1[,"Bc16"] == 0 & df1[,"Nov9"] == 1 & df1[,"Bc1"] == 0)
Others=subset(df1, df1[,"A4"] != 0 & df1[,"Nov5"] != 0 & df1[,"Nov27"] == 0 & df1[,"Nov71"] == 0 & df1[,"Bc16"] != 0 & df1[,"Nov9"] == 0 & df1[,"Bc1"] != 0)

n1234=nrow(subset(df1, df1[,"A4"] != 0 & df1[,"Nov5"] != 0 & df1[,"Nov27"] == 1 & df1[,"Nov71"] == 1 & df1[,"Bc16"] != 0 & df1[,"Nov9"] == 1 & df1[,"Bc1"] != 0))
n123=n1234 + nrow(subset(df1, df1[,"A4"] == 0 & df1[,"Nov5"] == 0 & df1[,"Nov27"] == 1 & df1[,"Nov71"] == 1 & df1[,"Bc16"] == 0 & df1[,"Nov9"] == 1 & df1[,"Bc1"] == 0))
n124=n1234 + nrow(subset(df1, df1[,"A4"] != 0 & df1[,"Nov5"] != 0 & df1[,"Nov27"] == 1 & df1[,"Nov71"] == 1 & df1[,"Bc16"] != 0 & df1[,"Nov9"] == 0 & df1[,"Bc1"] != 0))
n134=n1234 + nrow(subset(df1, df1[,"A4"] != 0 & df1[,"Nov5"] != 0 & df1[,"Nov27"] == 1 & df1[,"Nov71"] == 0 & df1[,"Bc16"] != 0 & df1[,"Nov9"] == 1 & df1[,"Bc1"] != 0))
n234=n1234 + nrow(subset(df1, df1[,"A4"] != 0 & df1[,"Nov5"] != 0 & df1[,"Nov27"] == 0 & df1[,"Nov71"] == 1 & df1[,"Bc16"] != 0 & df1[,"Nov9"] == 1 & df1[,"Bc1"] != 0))
n12=n1234 + n123 + n124 + nrow(subset(df1, df1[,"A4"] == 0 & df1[,"Nov5"] == 0 & df1[,"Nov27"] == 1 & df1[,"Nov71"] == 1 & df1[,"Bc16"] == 0 & df1[,"Nov9"] == 0 & df1[,"Bc1"] == 0))
n13=n1234 + n123 + n134 + nrow(subset(df1, df1[,"A4"] == 0 & df1[,"Nov5"] == 0 & df1[,"Nov27"] == 1 & df1[,"Nov71"] == 0 & df1[,"Bc16"] == 0 & df1[,"Nov9"] == 1 & df1[,"Bc1"] == 0))
n14=n1234 + n124 + n134 + nrow(subset(df1, df1[,"A4"] != 0 & df1[,"Nov5"] != 0 & df1[,"Nov27"] == 1 & df1[,"Nov71"] == 0 & df1[,"Bc16"] != 0 & df1[,"Nov9"] == 0 & df1[,"Bc1"] != 0))
n23=n1234 + n123 + n234 + nrow(subset(df1, df1[,"A4"] == 0 & df1[,"Nov5"] == 0 & df1[,"Nov27"] == 0 & df1[,"Nov71"] == 1 & df1[,"Bc16"] == 0 & df1[,"Nov9"] == 1 & df1[,"Bc1"] == 0))
n24=n1234 + n124 + n234 + nrow(subset(df1, df1[,"A4"] != 0 & df1[,"Nov5"] != 0 & df1[,"Nov27"] == 0 & df1[,"Nov71"] == 1 & df1[,"Bc16"] != 0 & df1[,"Nov9"] == 0 & df1[,"Bc1"] != 0))
n34=n1234 + n134 + n234 + nrow(subset(df1, df1[,"A4"] != 0 & df1[,"Nov5"] != 0 & df1[,"Nov27"] == 0 & df1[,"Nov71"] == 0 & df1[,"Bc16"] != 0 & df1[,"Nov9"] == 1 & df1[,"Bc1"] != 0))
summary(n12)
summary(n123)
summary(n1234)

area1=(nrow(NOV27) + n1234 + (n123 - n1234) + (n124 - n1234) + (n134 - n1234) + (n12 - (n123 - n1234) - (n124 - n1234) - n1234) + (n13 - (n123 - n1234) - (n134 - n1234) - n1234) + (n14 - (n124 - n1234) - (n134 - n1234) - n1234))
area2=(nrow(NOV71) + n1234 + (n123 - n1234) + (n124 - n1234) + (n234 - n1234) + (n12 - (n123 - n1234) - (n124 - n1234) - n1234) + (n23 - (n123 - n1234) - (n234 - n1234) - n1234) + (n24 - (n124 - n1234) - (n234 - n1234) - n1234))
area3=(nrow(NOV9) + n1234 + (n123 - n1234) + (n134 - n1234) + (n234 - n1234) + (n13 - (n123 - n1234) - (n134 - n1234) - n1234) + (n23 - (n123 - n1234) - (n234 - n1234) - n1234) + (n34 - (n134 - n1234) - (n234 - n1234) - n1234))
area4=(nrow(Others) + n1234 + (n124 - n1234) + (n134 - n1234) + (n234 - n1234) + (n14 - (n124 - n1234) - (n134 - n1234) - n1234) + (n24 - (n124 - n1234) - (n234 - n1234) - n1234) + (n34 - (n134 - n1234) - (n234 - n1234) - n1234))

pdf(o)
draw.quad.venn(area1, area2, area3, area4,
    n12, n13, n14, n23, n24, n34,
    n123, n124, n134, n234,
    n1234,
    category = c(label1, label2, label3, label4),
#    rep("", 4),
    lwd = rep(2, 4), lty = rep("solid", 4),
    col = rep("black", 4), fill = NULL, alpha = rep(0.5, 4),
    label.col = rep("black", 15), cex = rep(1, 15), fontface = rep("plain", 15),
    fontfamily = rep("serif", 15), cat.pos = c(-15, 15, 0, 0),
    cat.dist = c(0.22, 0.22, 0.11, 0.11), cat.col = rep("black", 4),
    cat.cex = rep(1, 4), cat.fontface = rep("plain", 4),
    cat.fontfamily = rep("serif", 4), cat.just = rep(list(c(0.5, 0.5)), 4),
    rotation.degree = 0, rotation.centre = c(0.5, 0.5)
    )
dev.off()
# singles = df1[grepl("single*", rownames(df1)), ]
# uniq_1=sum(singles[, 1])
# uniq_2=sum(singles[, 2])
# uniq_3=sum(singles[, 3])
# uniq_4=sum(singles[, 4])
# orthogroups = df1[grepl("orthogroup*", rownames(df1)), ]
# inpara_1 = sum(orthogroups[,1] == 1 & orthogroups[,2] == 0 & orthogroups[,3] == 0 & orthogroups[,4] == 0)
# inpara_2 = sum(orthogroups[,1] == 0 & orthogroups[,2] == 1 & orthogroups[,3] == 0 & orthogroups[,4] == 0)
# inpara_3 = sum(orthogroups[,1] == 0 & orthogroups[,2] == 0 & orthogroups[,3] == 1 & orthogroups[,4] == 0)
# inpara_4 = sum(orthogroups[,1] == 0 & orthogroups[,2] == 0 & orthogroups[,3] == 0 & orthogroups[,4] == 1)
# label1
# uniq_1
# inpara_1
# label2
# uniq_2
# inpara_2
# label3
# uniq_3
# inpara_3
# label4
# uniq_4
# inpara_4

warnings()
q()
