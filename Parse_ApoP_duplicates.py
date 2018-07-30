#!/usr/bin/python

'''
Sometimes an ORF fragment is classified as an ApoplastP hit when the
overlapping Augustus gene is not. Prioritise the gene with an effector
prediction.
'''

import argparse
from collections import defaultdict
import os

ap = argparse.ArgumentParser()
ap.add_argument('--gff_in', required=True, type=str, help='input gff file')
ap.add_argument('--gff_out', required=True, type=str, help='output gff file')
ap.add_argument('--Aug_ApoP', required=True, type=str, help='File of Augustus \
ApoplastP predictions')
ap.add_argument('--ORF_ApoP', required=True, type=str, help='File of ORF \
ApoplastP predictions')
conf = ap.parse_args()

# -----------------------------------------------------
# Step 1
# Parse arguments
# -----------------------------------------------------

In_Gff = conf.gff_in
Out_Gff = conf.gff_out
ApoP_Aug = conf.Aug_ApoP
ApoP_ORF = conf.ORF_ApoP
cwd = os.getcwd()

# -----------------------------------------------------
# Step 2
# Create dictionary of gene locations and list of ApoPs
# -----------------------------------------------------

location_dict = defaultdict(list)
ApoPs = []

with open(In_Gff) as f:
    lines = f.readlines()
    for line in lines:
        split_line = line.split()
        if split_line[2] == 'mRNA':
            col9 = split_line[8]
            gene_ID = col9.split(';')[0].replace('ID=', '')
            contig = split_line[0]
            start = split_line[3]
            end = split_line[4]
            key = "_".join([contig, start, end])
            location_dict[key].append(gene_ID)

with open(ApoP_Aug) as f:
    lines = f.readlines()
    for line in lines:
        ApoPs.append(line)

with open(ApoP_ORF) as f:
    lines = f.readlines()
    for line in lines:
        ApoPs.append(line)

ApoP_set = set(ApoPs)

# -----------------------------------------------------
# Step 3
# Check where two genes are at the same location and preferentially keep ApoP
# -----------------------------------------------------
