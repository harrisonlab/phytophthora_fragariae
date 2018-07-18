#!/usr/bin/python

'''
This script uses a selection of tables created using samtools depth of average
read depth for each gene in a reference genome when reads from two other
isolates and itself are aligned. This script identifies genes showing high
levels of copy number variation and writes them to a tsv
'''

import argparse
from collections import defaultdict
import os
from Bio import SeqIO
from Bio.SeqUtils import GC
from scipy import stats

ap = argparse.ArgumentParser()
ap.add_argument('--Org1_ID', required=True, type=str, help='Name of organism 1 \
                ')
ap.add_argument('--Org1_depth', required=True, type=str, help='Text table \
                containing the average read depth of genes in organism 1 \
                sequencing reads')
ap.add_argument('--Org2_ID', required=True, type=str, help='Name of organism 2 \
                ')
ap.add_argument('--Org2_depth', required=True, type=str, help='Text table \
                containing the average read depth of genes in organism 2 \
                sequencing reads')
ap.add_argument('--Org3_ID', required=True, type=str, help='Name of organism 3 \
                ')
ap.add_argument('--Org3_depth', required=True, type=str, help='Text table \
                containing the average read depth of genes in organism 3 \
                sequencing reads')
ap.add_argument('--gene_bed', required=True, type=str, help='bed file \
                containing gene locations in the reference assembly')
ap.add_argument('--gene_fasta', required=True, type=str, help='Fasta file \
                containing the gene sequences of the referene assembly, \
                required for normalising by GC content')
ap.add_argument('--OutDir', required=True, type=str, help='Output directory for \
                results tsv to be written to')
conf = ap.parse_args()

# -----------------------------------------------------
# Step 1
# Load input files and calculate average read depths
# -----------------------------------------------------

Org1 = conf.Org1_ID
Org2 = conf.Org2_ID
Org3 = conf.Org3_ID

Org1_depth = conf.Org1_depth
Org2_depth = conf.Org2_depth
Org3_depth = conf.Org3_depth

gene_bed = conf.gene_bed
gene_fasta = conf.gene_fasta

OutDir = conf.OutDir
cwd = os.getcwd()

print("Arguments parsed")

# ID locations of genes

Location_dict = defaultdict(list)
Gene_IDs = []

with open(gene_bed) as f:
    lines = f.readlines()
    for line in lines:
        split_line = line.split()
        gene_ID = split_line[3]
        Gene_IDs.append(gene_ID)
        contig_ID = split_line[0]
        start = split_line[1]
        end = split_line[2]
        Location_dict[gene_ID] = [contig_ID, start, end]

Gene_set = set(Gene_IDs)

print("Gene locations identified")

# Get per base read depths

Org1_Depths_dict = defaultdict(list)

with open(Org1_depth) as f:
    depth_lines = f.readlines()
    for depth_line in depth_lines:
        depth_split_line = depth_line.split()
        depth_contig = depth_split_line[0]
        depth_pos = depth_split_line[1]
        depth = depth_split_line[2]
        for gene in Gene_set:
            gene_contig = Location_dict[gene][0]
            gene_start = Location_dict[gene][1]
            gene_end = Location_dict[gene][2]
            if depth_contig == gene_contig:
                if depth_pos >= gene_start and depth_pos <= gene_end:
                    Org1_Depths_dict[gene].append(depth)

Org2_Depths_dict = defaultdict(list)

with open(Org2_depth) as f:
    depth_lines = f.readlines()
    for depth_line in depth_lines:
        depth_split_line = depth_line.split()
        depth_contig = depth_split_line[0]
        depth_pos = depth_split_line[1]
        depth = depth_split_line[2]
        for gene in Gene_set:
            gene_contig = Location_dict[gene][0]
            gene_start = Location_dict[gene][1]
            gene_end = Location_dict[gene][2]
            if depth_contig == gene_contig:
                if depth_pos >= gene_start and depth_pos <= gene_end:
                    Org2_Depths_dict[gene].append(depth)

Org3_Depths_dict = defaultdict(list)

with open(Org3_depth) as f:
    depth_lines = f.readlines()
    for depth_line in depth_lines:
        depth_split_line = depth_line.split()
        depth_contig = depth_split_line[0]
        depth_pos = depth_split_line[1]
        depth = depth_split_line[2]
        for gene in Gene_set:
            gene_contig = Location_dict[gene][0]
            gene_start = Location_dict[gene][1]
            gene_end = Location_dict[gene][2]
            if depth_contig == gene_contig:
                if depth_pos >= gene_start and depth_pos <= gene_end:
                    Org3_Depths_dict[gene].append(depth)

print("Per base read depth identified")

# Calculate average read depth per gene

Org1_ARD_dict = defaultdict(float)
Org2_ARD_dict = defaultdict(float)
Org3_ARD_dict = defaultdict(float)
Org1_ARDs = []
Org2_ARDs = []
Org3_ARDs = []

for gene in Gene_set:
    Org1_depths = Org1_Depths_dict[gene]
    Org2_depths = Org2_Depths_dict[gene]
    Org3_depths = Org3_Depths_dict[gene]
    Org1_ARD = float(sum(Org1_depths)/len(Org1_depths))
    Org2_ARD = float(sum(Org2_depths)/len(Org2_depths))
    Org3_ARD = float(sum(Org3_depths)/len(Org3_depths))
    Org1_ARD_dict[gene] = Org1_ARD
    Org2_ARD_dict[gene] = Org2_ARD
    Org3_ARD_dict[gene] = Org3_ARD
    Org1_ARDs.append(Org1_ARD)
    Org2_ARDs.append(Org2_ARD)
    Org3_ARDs.append(Org3_ARD)

print("Average read depth per gene calculated")

# -----------------------------------------------------
# Step 2
# Calculate averages necessary for adjusting read depth
# -----------------------------------------------------

# Calculate overall mean average read depth for each isolate

Org1_Mean_ARD = float(sum(Org1_ARDs)/len(Org1_ARDs))
Org2_Mean_ARD = float(sum(Org2_ARDs)/len(Org2_ARDs))
Org3_Mean_ARD = float(sum(Org3_ARDs)/len(Org3_ARDs))

print("Overall mean average read depths calculated")

# Calculate GC% for each gene

GC_dict = defaultdict(float)
GC_values = []

for rec in SeqIO.parse(gene_fasta, "fasta"):
    gene_ID = rec.id
    GC = GC(rec.seq)
    GC_dict[gene_ID] = GC
    GC_values.append(GC)

print("GC content values identified per gene")

# Assign genes to a GC percentile

Org1_ARD_percentile_dict = defaultdict(list)
Org2_ARD_percentile_dict = defaultdict(list)
Org3_ARD_percentile_dict = defaultdict(list)
gene_percentile_dict = defaultdict(float)

for gene in Gene_set:
    GC = GC_dict[gene]
    Org1_ARD = Org1_ARD_dict[gene]
    Org2_ARD = Org2_ARD_dict[gene]
    Org3_ARD = Org3_ARD_dict[gene]
    percentile = int(stats.percentileofscore(GC_values, GC, kind='weak'))
    Org1_ARD_percentile_dict[percentile].append(Org1_ARD)
    Org2_ARD_percentile_dict[percentile].append(Org2_ARD)
    Org3_ARD_percentile_dict[percentile].append(Org3_ARD)
    gene_percentile_dict[gene] = percentile

print("GC content percentiles identified")

# Calculate mean ARD for each GC percentile for each organism

Org1_GC_Mean_ARDs_dict = defaultdict(float)
Org2_GC_Mean_ARDs_dict = defaultdict(float)
Org3_GC_Mean_ARDs_dict = defaultdict(float)

for percentile in range(0, 101, 1):
    Org1_ARDs = Org1_ARD_percentile_dict[percentile]
    Org2_ARDs = Org2_ARD_percentile_dict[percentile]
    Org3_ARDs = Org3_ARD_percentile_dict[percentile]
    Org1_GC_Mean_ARD = float(sum(Org1_ARDs)/len(Org1_ARDs))
    Org2_GC_Mean_ARD = float(sum(Org2_ARDs)/len(Org2_ARDs))
    Org3_GC_Mean_ARD = float(sum(Org3_ARDs)/len(Org3_ARDs))
    Org1_GC_Mean_ARDs_dict[percentile] = Org1_GC_Mean_ARD
    Org2_GC_Mean_ARDs_dict[percentile] = Org2_GC_Mean_ARD
    Org3_GC_Mean_ARDs_dict[percentile] = Org3_GC_Mean_ARD

print("Mean average read depth for each GC content percentile calculated")

# -----------------------------------------------------
# Step 3
# Adjust average read depth for each gene and calculate copy number variation
# -----------------------------------------------------

# Adjust ARD, using Kamoun lab method

Org1_aARD = defaultdict(float)
Org2_aARD = defaultdict(float)
Org3_aARD = defaultdict(float)

for gene in Gene_set:
    Org1_ARD = Org1_ARD_dict[gene]
    Org2_ARD = Org2_ARD_dict[gene]
    Org3_ARD = Org3_ARD_dict[gene]
    GC_percentile = gene_percentile_dict[gene]
    Org1_mean_ARD_GC = Org1_GC_Mean_ARDs_dict[GC_percentile]
    Org1_aARD = float(Org1_ARD * float(Org1_Mean_ARD / Org1_mean_ARD_GC))
    Org2_mean_ARD_GC = Org2_GC_Mean_ARDs_dict[GC_percentile]
    Org2_aARD = float(Org2_ARD * float(Org2_Mean_ARD / Org2_mean_ARD_GC))
    Org3_mean_ARD_GC = Org3_GC_Mean_ARDs_dict[GC_percentile]
    Org3_aARD = float(Org3_ARD * float(Org3_Mean_ARD / Org3_mean_ARD_GC))
    Org1_aARD[gene] = Org1_aARD
    Org2_aARD[gene] = Org2_aARD
    Org3_aARD[gene] = Org3_aARD

print("Average read depth values adjusted")

# Calculate copy numbers for each gene in each organism, Kamoun lab method

Org1_CN_dict = defaultdict(float)
Org2_CN_dict = defaultdict(float)
Org3_CN_dict = defaultdict(float)

for gene in Gene_set:
    Org1_aARD = Org1_aARD[gene]
    Org2_aARD = Org2_aARD[gene]
    Org3_aARD = Org3_aARD[gene]
    Org1_CN = float(Org1_aARD / Org1_Mean_ARD)
    Org2_CN = float(Org2_aARD / Org2_Mean_ARD)
    Org3_CN = float(Org3_aARD / Org3_Mean_ARD)
    Org1_CN_dict[gene] = Org1_CN
    Org2_CN_dict[gene] = Org2_CN
    Org3_CN_dict[gene] = Org3_CN

print("Copy numbers calculated for each gene")

# Calculate copy number variations between organisms

Org1_vs_Org2_CNV_dict = defaultdict(float)
Org1_vs_Org3_CNV_dict = defaultdict(float)
Org2_vs_Org3_CNV_dict = defaultdict(float)

for gene in Gene_set:
    Org1_CN = Org1_CN_dict[gene]
    Org2_CN = Org2_CN_dict[gene]
    Org3_CN = Org3_CN_dict[gene]
    Org1_vs_Org2_CNV = float(Org1_CN - Org2_CN)
    Org1_vs_Org3_CNV = float(Org1_CN - Org3_CN)
    Org2_vs_Org3_CNV = float(Org2_CN - Org3_CN)
    Org1_vs_Org2_CNV_dict[gene] = Org1_vs_Org2_CNV
    Org1_vs_Org3_CNV_dict[gene] = Org1_vs_Org3_CNV
    Org2_vs_Org3_CNV_dict[gene] = Org2_vs_Org3_CNV

print("Pairwise copy number variations calculated")

# -----------------------------------------------------
# Step 4
# Write out results to tsv files
# -----------------------------------------------------

# Identify genes showing CNV

Out_File = "_".join([Org1, Org2, Org3, "CNV", "calls.tsv"])
Output = "/".join([cwd, OutDir, Out_File])

Head_1 = "_".join([Org1, "vs", Org2, "CNV"])
Head_2 = "_".join([Org1, "vs", Org3, "CNV"])
Head_3 = "_".join([Org2, "vs", Org3, "CNV"])

Header = "\t".join(["Gene_ID", Head_1, Head_2, Head_3])

with open(Output, "w") as o:
    o.write(Header)
    o.write("\n")
    for gene in Gene_set:
        Org1_vs_Org2_CNV = Org1_vs_Org2_CNV_dict[gene]
        Org1_vs_Org3_CNV = Org1_vs_Org3_CNV_dict[gene]
        Org2_vs_Org3_CNV = Org2_vs_Org3_CNV_dict[gene]
        if Org1_vs_Org2_CNV >= 1 or Org1_vs_Org2_CNV <= -1 or \
           Org1_vs_Org3_CNV >= 1 or Org1_vs_Org3_CNV <= -1 or \
           Org1_vs_Org3_CNV >= 1 or Org1_vs_Org3_CNV <= -1:
            Outline = "\t".join([gene, Org1_vs_Org2_CNV, Org1_vs_Org3_CNV,
                                Org2_vs_Org3_CNV])
            o.write(Outline)
            o.write("\n")

print("Outfiles written and script complete")
