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

Org1 = conf.Org1_ID
Org2 = conf.Org2_ID
Org3 = conf.Org3_ID

CNV_in_dict = defaultdict(list)
Genes = []

with open(conf.CNV_table) as f:
    lines = f.readlines()[1]
    for line in lines:
        split_line = line.split()
        Gene = split_line[0]
        CNV_1 = split_line[1]
        CNV_2 = split_line[2]
        CNV_3 = split_line[3]
        CNV_in_dict[Gene] = [CNV_1, CNV_2, CNV_3]
        Genes.append(Gene)

Gene_set = set(Genes)

RxLRs = []
with open(conf.CNV_RxLRs) as f:
    lines = f.readlines()
    for line in lines:
        RxLRs.append(line)

CRNs = []
with open(conf.CNV_CRNs) as f:
    lines = f.readlines()
    for line in lines:
        CRNs.append(line)

ApoPs = []
with open(conf.CNV_ApoP) as f:
    lines = f.readlines()
    for line in lines:
        ApoPs.append(line)

Secs = []
with opn(conf.CNV_Sec) as f:
    lines = f.readlines()
    for line in lines:
        Secs.append(line)

TFs = []
with open(conf.CNV_TFs) as f:
    lines = f.readlines()
    for line in lines:
        TFs.append(line)

OutDir = conf.OutDir

# -----------------------------------------------------
# Step 2
# Identify genes with particular features and which organism they have a change
# in CNV in
# -----------------------------------------------------

features_dict = defaultdict(list)

for gene in Gene_set:
    if gene in RxLRs:
        RxLR = 'Yes'
    else:
        RxLR = ''
    if gene in CRNs:
        CRN = 'Yes'
    else:
        CRN = ''
    if gene in ApoPs:
        ApoP = 'Yes'
    else:
        ApoP = ''
    if gene in Secs:
        Sec = 'Yes'
    else:
        Sec = ''
    if gene in TFs:
        TF = 'Yes'
    else:
        TF = ''
    features_dict[gene] = [RxLR, CRN, ApoP, Sec, TF]
