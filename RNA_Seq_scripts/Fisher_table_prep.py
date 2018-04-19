#!/usr/bin/python

'''
This script will count the number of RxLRs, CRNs, ApoplastP hits and combined
effector genes in a coexpressed module compared to and the rest of the genome
'''

import argparse
import numpy
from collections import defaultdict
import os

# -----------------------------------------------------
# Step 1
# Import command line arguments
# -----------------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument('--Module_RxLRs', required=True, type=str, help='List of RxLRs \
in a coexpression module')
ap.add_argument('--Module_CRNs', required=True, type=str, help='List of CRNs \
in a coexpression module')
ap.add_argument('--Module_ApoP', required=True, type=str, help='List of ApoP \
hits in a coexpression module')
ap.add_argument('--Module_Effectors', required=True, type=str, help='List of Effectors \
in a coexpression module')
ap.add_argument('--Module_Genes', required=True, type=str, help='Complete list \
of genes in a coexpression module')
ap.add_argument('--Module_Name', required=True, type=str, help='Name of the \
module being analysed')
ap.add_argument('--Genome_RxLRs', required=True, type=float, help='Number of \
total RxLRs in the genome')
ap.add_argument('--Genome_CRNs', required=True, type=float, help='Number of \
total CRNs in the genome')
ap.add_argument('--Genome_ApoP', required=True, type=float, help='Number of \
total ApoP hits in the genome')
ap.add_argument('--Genome_Effectors', required=True, type=float, help='Number of \
total Effectorss in the genome')
ap.add_argument('--Genome_Genes', required=True, type=float, help='Number of \
total genes in the genome')
ap.add_argument('--OutDir', required=True, type=str, help='Directory to write \
output files to')
conf = ap.parse_args()

# -----------------------------------------------------
# Step 2
# Load input files to variables
# -----------------------------------------------------

RxLRs = []
with open(conf.Module_RxLRs) as f:
    for line in f.readlines:
        RxLRs.append(line)

RxLR_Set = set(RxLRs)

CRNs = []
with open(conf.Module_CRNs) as f:
    for line in f.readlines:
        CRNs.append(line)

CRN_Set = set(CRNs)

ApoP = []
with open(conf.Module_ApoP) as f:
    for line in f.readlines:
        ApoP.append(line)

ApoP_Set = set(ApoP)

Effectors = []
with open(conf.Module_Effectors) as f:
    for line in f.readlines:
        Effectors.append(line)

Effector_Set = set(Effectors)
