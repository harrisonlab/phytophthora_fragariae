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

Fst_in = conf.Fst_File
Fst_threshold = conf.Fst_Threshold
Kst_in = conf.Kst_File
Kst_threshold = conf.Kst_Threshold
Dxy_in = conf.Dxy_File
Dxy_threshold = conf.Dxy_Threshold
OutDir = conf.Out_Dir
OutPre = conf.Out_Prefix
cwd = os.getcwd()

print("Arguments parsed")

# Create data structures

Fst_dict = defaultdict(float)
Kst_dict = defaultdict(float)
Dxy_dict = defaultdict(float)
Gene_List = []

with open(Fst_in) as f:
    lines = f.readlines()
    for line in lines:
        split_line = line.split()
        ID_field = split_line[0]
        ID_split = ID_field.split('=')
        Gene_ID = ID_split[1]
        Fst_Value = split_line[1]
        Fst_dict[Gene_ID] = Fst_Value
        Gene_List.append(Gene_ID)

with open(Kst_in) as f:
    lines = f.readlines()
    for line in lines:
        split_line = line.split()
        ID_field = split_line[0]
        ID_split = ID_field.split('=')
        Gene_ID = ID_split[1]
        Kst_Value = split_line[1]
        Kst_dict[Gene_ID] = Kst_Value

with open(Dxy_in) as f:
    lines = f.readlines()
    for line in lines:
        split_line = line.split()
        ID_field = split_line[3]
        ID_split = ID_field.split('=')
        Gene_ID = ID_split[1]
        Dxy_Value = split_line[4]
        Dxy_dict[Gene_ID] = Dxy_Value

Gene_Set = set(Gene_List)

print("Data structures produced")

# -----------------------------------------------------
# Step 2
# Creates lists of genes exceeding threshold values
# -----------------------------------------------------

Low_Confidence = []
High_Confidence = []

for Gene in Gene_Set:
    Fst_Value = Fst_dict[Gene]
    Kst_Value = Kst_dict[Gene]
    Dxy_Value = Dxy_dict[Gene]
    if float(Fst_Value) >= float(Fst_threshold) and float(Kst_Value) >= \
       float(Kst_threshold) and float(Dxy_Value) >= float(Dxy_threshold):
        High_Confidence.append(Gene)
    if float(Fst_Value) >= float(Fst_threshold) or float(Fst_Value) >= \
       float(Fst_threshold) or float(Dxy_Value) >= float(Dxy_threshold):
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
