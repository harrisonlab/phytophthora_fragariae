#!/usr/bin/python

'''
This script takes the results of CNV_identification.py and uses lists of genes
showing CNV of particular types, identifies which genome has a change in copy
number and assigns gene classes
'''

import argparse
from collections import defaultdict
import os

ap = argparse.ArgumentParser()
ap.add_argument('--Org1_ID', required=True, type=str, help='Name of organism \
                1')
ap.add_argument('--Org2_ID', required=True, type=str, help='Name of organism \
                2')
ap.add_argument('--Org3_ID', required=True, type=str, help='Name of organism \
                3')
ap.add_argument('--CNV_table', required=True, type=str, help='Table produced \
                by CNV_identification.py')
ap.add_argument('--CNV_RxLRs', required=True, type=str, help='File containing \
                names of RxLRs showing CNV')
ap.add_argument('--CNV_CRNs', required=True, type=str, help='File containing \
                names of CRNs showing CNV')
ap.add_argument('--CNV_ApoP', required=True, type=str, help='File containing \
                names of ApoP predictions showing CNV')
ap.add_argument('--CNV_Sec', required=True, type=str, help='File containing \
                names of secreted proteins showing CNV')
ap.add_argument('--CNV_TFs', required=True, type=str, help='File containing \
                names of transcription factors and transcriptional regulators \
                showing CNV')
ap.add_argument('--OutDir', required=True, type=str, help='Directory to write \
                results to')
conf = ap.parse_args()

# -----------------------------------------------------
# Step 1
# Load input files and create necessary data structures
# -----------------------------------------------------
