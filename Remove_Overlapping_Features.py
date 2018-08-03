#!/usr/bin/python

'''
This script is used to remove features identified as being duplicated by
bedtools from the gff
'''

import argparse

ap = argparse.ArgumentParser()
ap.add_argument('--inp_gff', required=True, type=str, help='Gff file for \
genes to be removed from')
ap.add_argument('--exclude_list', required=True, type=str, help='Text file \
of genes to be removed from the gff')
ap.add_argument('--output_gff', required=True, type=str, help='Gff file with \
genes in exclude list removed')
ap.add_argument('--removed_genes', required=True, type=str, help='File \
containing ID of all removed genes')
conf = ap.parse_args()

Gff_in = conf.inp_gff
Exclude = conf.exclude_list
Gff_out = conf.output_gff
Removed = conf.removed_genes

# -----------------------------------------------------
# Step 1
# Identify lines to be removed and create data structures for writing out
# -----------------------------------------------------

Genes_to_remove = []

with open(Exclude) as f:
    lines = f.readlines()
    for line in lines:
        gene = line.rstrip()
        Genes_to_remove.append(gene)

Removal_Set = set(Genes_to_remove)
