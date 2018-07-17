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
# Load input files
# -----------------------------------------------------

# -----------------------------------------------------
# Step 2
# Calculate average read depths per gene
# -----------------------------------------------------

# -----------------------------------------------------
# Step 3
# Calculate copy numbers for each gene
# -----------------------------------------------------

# -----------------------------------------------------
# Step 4
# Identify genes with copy number variation
# -----------------------------------------------------

# -----------------------------------------------------
# Step 5
# Write out results to tsv files
# -----------------------------------------------------
