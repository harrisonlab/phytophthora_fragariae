#!/usr/bin/python

'''
This script will analyse results from each repetition of DREME and extract
motifs present in 90% of runs
With significance thresholds of: 0.1, 0.05, 0.01 and 0.001
'''

import argparse
from collections import defaultdict

# -----------------------------------------------------
# Step 1
# Import variables
# -----------------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument('--inputs', required=True, type=str, help='Lists of files \
from repeated runs of DREME')
ap.add_argument(--'output', required=True, type=str, help='Location to output \
results to')
conf = ap.parse_args()

# -----------------------------------------------------
# Step 2
# Load motifs and p-values into a dictionary
# -----------------------------------------------------

motif_dict = defaultdict(list)

Files = conf.inputs
for File in Files:
    with open(File) as f:
        Lines = f.readlines()
        for line in Lines:
            if line.startswith('# BEST'):
                list = line.split()
                P_val = list[6]
                Motif = [2]
                defaultdict[Motif].append(P_val)
