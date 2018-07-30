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
Apops = []
