#!/usr/bin/python

'''
This script will analyse results from a Fishers Exact Test on enrichment
for specified gene types, with a specified False Discovery Rate
and specified P-value threshold
'''

import argparse
from collections import defaultdict
import os
import statsmodels.sandbox.stats.multicomp as stats

# -----------------------------------------------------
# Step 1
# Import variables
# -----------------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument('--inputs', required=True, type=str, nargs='+', help='List of \
files from all Fisher tests')
ap.add_argument('--outdir', required=True, type=str, help='Directory to output \
results to')
ap.add_argument('--FDR', required=True, type=float, help='False Discovery rate \
for Benjamini-Hochberg multi-test correction')
ap.add_argument('--Types', required=True, type=str, nargs='+', help='List of \
genes types to parse the enrichment results of')
ap.add_argument('--Threshold', required=True, type=float, help='P-value at \
which the null hypothesis of no enrichment is accepted')
conf = ap.parse_args()

cwd = os.getcwd()

# -----------------------------------------------------
# Step 2
# Creates dictionary of each gene type in each option and corrects p-values
# -----------------------------------------------------

BH_dict = defaultdict(float)
BO_dict = defaultdict(float)
uncorrected_dict = defaultdict(float)

keys = []
P_vals = []

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
            P_vals.append(P_value)
            uncorrected_dict[key] = P_value

FDR = conf.FDR
Benjamini_Pval_array = stats.multipletests(P_vals, alpha=FDR, method='fdr_bh',
                                           is_sorted=False, returnsorted=False)

Bonferroni_Pval_array = stats.multipletests(P_vals, alpha=FDR,
                                            method='bonferroni',
                                            is_sorted=False,
                                            returnsorted=False)

i = 0
for key in keys:
    P_value_BH = Benjamini_Pval_array[1][i]
    BH_dict[key] = P_value_BH
    P_value_BO = Bonferroni_Pval_array[1][i]
    BO_dict[key] = P_value_BO
    i = i + 1

# -----------------------------------------------------
# Step 3
# Make a list of tests which pass p-value thresholds for writing out
# -----------------------------------------------------

Significant = []
Non_Significant = []

Threshold = conf.Threshold

for key in keys:
    P_value = uncorrected_dict[key]
    if P_value < Threshold:
        Significant.append(key)
    else:
        Non_Significant.append(key)

# -----------------------------------------------------
# Step 4
# Split dictionary into separate dictionaries by gene type & significance
# Also write out file
# -----------------------------------------------------

Types = conf.Types
OutDir = conf.outdir
Header = "\t".join(["Module_Gene_type", "P-value", "Benjamini P-value",
                    "Bonferroni P-value"])

for Type in Types:
    Type_Sig_uncorrected_dict = defaultdict(float)
    Type_Sig_BH_dict = defaultdict(float)
    Type_Sig_BO_dict = defaultdict(float)
    Type_NonSig_uncorrected_dict = defaultdict(float)
    Type_NonSig_BH_dict = defaultdict(float)
    Type_NonSig_BO_dict = defaultdict(float)
    Type_Sig = []
    Type_NonSig = []
    for key in keys:
        if Type in key and key in Significant:
            Type_Sig.append(key)
        elif Type in key and key in Non_Significant:
            Type_NonSig.append(key)
    Out_Sig_File = "_".join([Type, "Significant_enrichment.tsv"])
    Out_NonSig_File = "_".join([Type, "NonSignificant_enrichment.tsv"])
    Sig_Output = "/".join([cwd, OutDir, Out_Sig_File])
    NonSig_Ouput = "/".join([cwd, OutDir, Out_NonSig_File])
    with open(Sig_Output, 'w') as o:
        o.write(Header)
        o.write("\n")
        for item in Type_Sig:
            P_value = uncorrected_dict[item]
            P_value_BH = BH_dict[item]
            P_value_BO = BO_dict[item]
            to_write = "\t".join([item, str(P_value), str(P_value_BH),
                                  str(P_value_BO)])
            o.write(to_write)
            o.write("\n")
        o.close()
    with open(NonSig_Ouput, 'w') as o:
        o.write(Header)
        o.write("\n")
        for item in Type_NonSig:
            P_value = uncorrected_dict[item]
            P_value_BH = BH_dict[item]
            P_value_BO = BO_dict[item]
            to_write = "\t".join([item, str(P_value), str(P_value_BH),
                                  str(P_value_BO)])
            o.write(to_write)
            o.write("\n")
        o.close()
