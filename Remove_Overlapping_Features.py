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

lines_to_write = []
removed_genes = []

with open(Gff_in) as f:
    lines = f.readlines()
    for line in lines:
        split_line = line.split()
        col9 = split_line[8]
        if split_line[2] == 'gene':
            gene_ID = col9.split('=')[1]
            if gene_ID in Removal_Set:
                removed_genes.append(gene_ID)
            else:
                lines_to_write.append(line)
        elif split_line[2] == 'mRNA':
            gene_ID = col9.split('=')[2]
            if gene_ID in Removal_Set:
                removed_genes.append(gene_ID)
            else:
                lines_to_write.append(line)
        elif split_line[2] == 'start_codon':
            transcript_ID = col9.split('=')[1]
            gene_ID = transcript_ID.split('.')[0]
            if gene_ID in Removal_Set:
                removed_genes.append(gene_ID)
            else:
                lines_to_write.append(line)
        elif split_line[2] == 'CDS':
            transcript_ID = col9.split('=')[2]
            gene_ID = transcript_ID.split('.')[1]
            if gene_ID in Removal_Set:
                removed_genes.append(gene_ID)
            else:
                lines_to_write.append(line)
        elif split_line[2] == 'exon':
            transcript_ID = col9.split('=')[2]
            gene_ID = transcript_ID.split('.')[1]
            if gene_ID in Removal_Set:
                removed_genes.append(gene_ID)
            else:
                lines_to_write.append(line)
        elif split_line[2] == 'stop_codon':
            transcript_ID = col9.split('=')[1]
            gene_ID = transcript_ID.split('.')[0]
            if gene_ID in Removal_Set:
                removed_genes.append(gene_ID)
            else:
                lines_to_write.append(line)
        elif split_line[2] == 'intron':
            transcript_ID = col9.split('=')[1]
            gene_ID = transcript_ID.split('.')[0]
            if gene_ID in Removal_Set:
                removed_genes.append(gene_ID)
            else:
                lines_to_write.append(line)

Removed_Set = set(removed_genes)

# -----------------------------------------------------
# Step 2
# Write out files
# -----------------------------------------------------

with open(Gff_out) as o:
    for line in lines_to_write:
        o.write(line)

with open(Removed) as r:
    for gene in Removed_Set:
        r.write(gene)
        r.write("\n")
