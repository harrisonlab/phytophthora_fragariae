#!/usr/bin/python

'''
This script will analyse results from a Fishers Exact Test on enrichment
for RxLRs, CRNs, ApoplastP hits and combined Effectors vs the genome
With significance thresholds of: 0.1, 0.05, 0.01 and 0.001
'''

import argparse
from collections import defaultdict
import os

# -----------------------------------------------------
# Step 1
# Import variables
# -----------------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument('--inputs', required=True, type=str, nargs='+', help='List of \
files from all Fisher tests')
ap.add_argument('--outdir', required=True, type=str, help='Directory to output \
results to')
conf = ap.parse_args()

cwd = os.getcwd()

# -----------------------------------------------------
# Step 2
# Creates dictionary of each gene type in each option
# -----------------------------------------------------

enrichment_dict = defaultdict(float)

keys = []

Files = conf.inputs
for File in Files:
    with open(File) as f:
        Lines = f.readlines()
        for line in Lines:
            split_line = line.split()
            Module_ID = str(split_line[0])
            Gene_type = str(split_line[1])
            P_value = float(split_line[2])
            key = "_".join([Module_ID, Gene_type])
            keys.append(key)
            enrichment_dict[key] = P_value

# -----------------------------------------------------
# Step 3
# Make a list of tests which pass p-value thresholds for writing out
# -----------------------------------------------------

Significant_1e3 = []
Significant_1e2 = []
Significant_5e2 = []
Significant_1e1 = []
Non_Significant = []

for key in keys:
    P_value = enrichment_dict[key]
    if P_value <= 0.001:
        Significant_1e3.append(key)
    elif P_value <= 0.01:
        Significant_1e2.append(key)
    elif P_value <= 0.05:
        Significant_5e2.append(key)
    elif P_value <= 0.1:
        Significant_1e1.append(key)
    else:
        Non_Significant.append(key)

# -----------------------------------------------------
# Step 4
# Write out files
# -----------------------------------------------------

OutDir = conf.outdir

# Threshold of 0.001

Out_File = "Significant_enrichment_0.001.txt"
Output = "/".join([cwd, OutDir, Out_File])

with open(Output, 'w') as o:
    for item in Significant_1e3:
        P_value = enrichment_dict[item]
        to_write = "\t".join([item, P_value])
        o.write(to_write)
        o.write("\n")

# Threshold of 0.01

Out_File = "Significant_enrichment_0.01.txt"
Output = "/".join([cwd, OutDir, Out_File])

with open(Output, 'w') as o:
    for item in Significant_1e2:
        P_value = enrichment_dict[item]
        to_write = "\t".join([item, P_value])
        o.write(to_write)
        o.write("\n")

# Threshold of 0.05

Out_File = "Significant_enrichment_0.05.txt"
Output = "/".join([cwd, OutDir, Out_File])

with open(Output, 'w') as o:
    for item in Significant_5e2:
        P_value = enrichment_dict[item]
        to_write = "\t".join([item, P_value])
        o.write(to_write)
        o.write("\n")

# Threshold of 0.1

Out_File = "Significant_enrichment_0.1.txt"
Output = "/".join([cwd, OutDir, Out_File])

with open(Output, 'w') as o:
    for item in Significant_1e1:
        P_value = enrichment_dict[item]
        to_write = "\t".join([item, P_value])
        o.write(to_write)
        o.write("\n")
