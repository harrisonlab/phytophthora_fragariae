#!/usr/bin/python

'''
This script takes table output from Pf_popgenome_analysis.md for calculating
Fu and Li's F* and D* to determine population separation. Pull out high
confidence and low confidence genes for further analysis.
'''

import argparse
from collections import defaultdict
import os

ap = argparse.ArgumentParser()
ap.add_argument('--Fu_Li_D_File', required=True, type=str, help='Tab separated text \
file of Fu and Li D* values per gene')
ap.add_argument('--Fu_Li_F_File', required=True, type=str, help='Tab separated text \
file of Fu and Li F* values per gene')
ap.add_argument('--Out_Dir', required=True, type=str, help='Output directory')
ap.add_argument('--Out_Prefix', required=True, type=str, help='Prefix for output \
file')
conf = ap.parse_args()

# -----------------------------------------------------
# Step 1
# Load input files and build data structures
# -----------------------------------------------------

Fu_Li_F_in = conf.Fu_Li_F_File
Fu_Li_D_in = conf.Fu_Li_D_File
OutDir = conf.Out_Dir
OutPre = conf.Out_Prefix
cwd = os.getcwd()

print("Arguments parsed")

# Create data structures

F_dict = defaultdict(float)
D_dict = defaultdict(float)
Gene_List = []

with open(Fu_Li_F_in) as f:
    lines = f.readlines()
    for line in lines:
        split_line = line.split("\t")
        ID_field = split_line[1]
        ID_split = ID_field.split('=')
        Gene_ID = ID_split[1]
        F_Value = split_line[2]
        if F_Value != "NA" or F_Value != "NaN":
            F_dict[Gene_ID] = F_Value
        Gene_List.append(Gene_ID)

with open(Fu_Li_D_in) as f:
    lines = f.readlines()
    for line in lines:
        split_line = line.split("\t")
        ID_field = split_line[1]
        ID_split = ID_field.split('=')
        Gene_ID = ID_split[1]
        D_Value = split_line[2]
        if D_Value != "NA" or D_Value != "NaN":
            D_dict[Gene_ID] = D_Value
        Gene_List.append(Gene_ID)

Gene_Set = set(Gene_List)

print("Data structures produced")

# -----------------------------------------------------
# Step 2
# Creates lists of genes exceeding threshold values
# -----------------------------------------------------

Low_Confidence = []
High_Confidence = []

for Gene in Gene_Set:
    F_Value = F_dict[Gene]
    D_Value = D_dict[Gene]
    if float(F_Value) < 0 and float(D_Value) < 0:
        High_Confidence.append(Gene)
    if float(F_Value) < 0 or float(D_Value) < 0:
        Low_Confidence.append(Gene)

print("List of genes exceeding thresholds produced")

# -----------------------------------------------------
# Step 3
# Writes out files
# -----------------------------------------------------

Low_Out_name = "_".join([OutPre, "Low_Conf.txt"])
Low_Out = "/".join([cwd, OutDir, Low_Out_name])

High_Out_name = "_".join([OutPre, "High_Conf.txt"])
High_Out = "/".join([cwd, OutDir, High_Out_name])

with open(Low_Out, "w") as o:
    for item in Low_Confidence:
        o.write(item)
        o.write("\n")

with open(High_Out, "w") as o:
    for item in High_Confidence:
        o.write(item)
        o.write("\n")

print("Output files written")
