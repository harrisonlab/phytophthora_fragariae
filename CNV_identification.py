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

# Calculate average depth per gene

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

# -----------------------------------------------------
# Step 2
# Calculate averages necessary for adjusting read depth
# -----------------------------------------------------

# Calculate overall mean average read depth for each isolate

Org1_MeanARD = float(sum(Org1_ARDs)/len(Org1_ARDs))
Org2_MeanARD = float(sum(Org2_ARDs)/len(Org2_ARDs))
Org3_MeanARD = float(sum(Org3_ARDs)/len(Org3_ARDs))

# Calculate GC% for each gene

GC_dict = defaultdict(float)
GC_values = []

for rec in SeqIO.parse(gene_fasta, "fasta"):
    gene_ID = rec.id
    GC = GC(rec.seq)
    GC_dict[gene_ID] = GC
    GC_values.append(GC)

# Assign genes to a GC percentile

Org1_ARD_percentile_dict = defaultdict(list)
Org2_ARD_percentile_dict = defaultdict(list)
Org3_ARD_percentile_dict = defaultdict(list)
gene_percentile_dict = defaultdict(list)

for gene in Gene_set:
    GC = GC_dict[gene]
    Org1_ARD = Org1_ARD_dict[gene]
    Org2_ARD = Org2_ARD_dict[gene]
    Org3_ARD = Org3_ARD_dict[gene]
    percentile = int(stats.percentileofscore(GC_values, GC, kind='weak'))
    Org1_ARD_percentile_dict[percentile].append(Org1_ARD)
    Org2_ARD_percentile_dict[percentile].append(Org2_ARD)
    Org3_ARD_percentile_dict[percentile].append(Org3_ARD)
    gene_percentile_dict[percentile].append(gene)

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

# -----------------------------------------------------
# Step 3
# Adjust average read depth for each gene and calculate copy number variation
# -----------------------------------------------------



# -----------------------------------------------------
# Step 4
# Write out results to tsv files
# -----------------------------------------------------
