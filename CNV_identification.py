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

Location_dict = defaultdict(list)
Depths_dict = defaultdict(list)
Average_Depth_dict = defaultdict(list)

with open(gene_bed) as f:
    lines = f.readlines()
    for line in lines:
        split_line = line.split()
        gene_ID = split_line[3]
        contig_ID = split_line[0]
        start = split_line[1]
        end = split_line[2]
        Location_dict[gene_ID] = [contig_ID, start, end]

# -----------------------------------------------------
# Step 2
# Calculate averages necessary for adjusting read depth
# -----------------------------------------------------

# -----------------------------------------------------
# Step 3
# Adjust copy numbers for each gene and calculate copy number variation
# -----------------------------------------------------

# -----------------------------------------------------
# Step 4
# Write out results to tsv files
# -----------------------------------------------------
