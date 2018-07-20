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
    lines = f.readlines()
    for line in lines:
        if line.startswith('Gene_ID'):
            Header = line.strip('\n')
        else:
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
with open(conf.CNV_Sec) as f:
    lines = f.readlines()
    for line in lines:
        Secs.append(line)

TFs = []
with open(conf.CNV_TFs) as f:
    lines = f.readlines()
    for line in lines:
        TFs.append(line)

OutDir = conf.OutDir
cwd = os.getcwd()

# -----------------------------------------------------
# Step 2
# Identify genes with particular features and which organism they have a change
# in CNV in
# -----------------------------------------------------

# Assign gene features

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

# Identify isolate with CNV for each gene

Inc_Dec_dict = defaultdict(list)

for gene in Gene_set:
    CNVs = CNV_in_dict[gene]
    CNV_A = CNVs[0]
    CNV_B = CNVs[1]
    CNV_C = CNVs[2]
    # Check for single increase
    if CNV_A >= 1 and CNV_B >= 1:
        Increase = 'BC-16'
    elif CNV_A <= -1 and CNV_C >= 1:
        Increase = 'BC-1'
    elif CNV_B <= -1 and CNV_C <= -1:
        Increase = 'NOV-9'
    else:
        Increase = ''
    # Check for single decrease
    if CNV_A <= -1 and CNV_B <= -1:
        Decrease = 'BC-16'
    elif CNV_A >= 1 and CNV_C <= -1:
        Decrease = 'BC-1'
    elif CNV_B >= 1 and CNV_C >= 1:
        Decrease = 'NOV-9'
    else:
        Decrease = ''
    Inc_Dec_dict[gene] = [Increase, Decrease]

# -----------------------------------------------------
# Step 3
# Writes results to file
# -----------------------------------------------------

OutName = "CNV_details.tsv"
Output = "/".join([cwd, OutDir, OutName])

with open(Output, "w") as o:
    Header = "\t".join([Header, "Increased_CN", "Decreased_CN", "RxLR", "CRN",
                        "ApoP", "Secreted", "TF/TR"])
    o.write(Header)
    o.write("\n")
    for gene in Gene_set:
        CNV_1 = CNV_in_dict[gene][0]
        CNV_2 = CNV_in_dict[gene][1]
        CNV_3 = CNV_in_dict[gene][2]
        RxLR = features_dict[gene][0]
        CRN = features_dict[gene][1]
        ApoP = features_dict[gene][2]
        Sec = features_dict[gene][3]
        TF = features_dict[gene][4]
        Inc = Inc_Dec_dict[gene][0]
        Dec = Inc_Dec_dict[gene][1]
        Outline = "\t".join([gene, CNV_1, CNV_2, CNV_3, Inc, Dec, RxLR, CRN,
                            ApoP, Sec, TF])
        o.write(Outline)
        o.write("\n")
