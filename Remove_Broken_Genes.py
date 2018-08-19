#!/usr/bin/python

'''
This script is used to remove features where the front is missing due to a
contig break and there is not an intron at the break
'''

import argparse
from collections import defaultdict

ap = argparse.ArgumentParser()
ap.add_argument('--inp_gff', required=True, type=str, help='Gff file for genes \
to be removed from')
ap.add_argument('--out_gff', required=True, type=str, help='Output Gff file')
ap.add_argument('--broken_genes', required=True, type=str, help='Text file of \
names of genes removed by this script')
conf = ap.parse_args()

Gff_in = conf.inp_gff
Gff_out = conf.out_gff
Broken_out = conf.broken_genes

# -----------------------------------------------------
# Step 1
# Create dictionaries of genes with various features
# -----------------------------------------------------

Start = []
CDS = []
Intron = []

with open(Gff_in) as f:
    lines = f.readlines()
    for line in lines:
        split_line = line.split()
        col9 = split_line[8]
        if split_line[2] == 'start_codon':
            transcript = col9.split('=')[1]
            gene = transcript.split('.')[0]
            Start.append(gene)
        elif split_line[2] == 'CDS':
            transcript = col9.split('=')[1]
            gene = transcript.split('.')[0]
            CDS.append(gene)
        elif split_line[2] == 'intron':
            transcript = col9.split('=')[1]
            gene = transcript.split('.')[0]
            Intron.append(gene)
