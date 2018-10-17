#!/usr/bin/python

'''
This script takes table output from Pf_popgenome_analysis.md for calculating
Fst, Kst and Dxy to determine population separation. Pull out high confidence
and low confidence genes for further analysis.
'''

import argparse
from collections import defaultdict
import os

ap = argparse.ArgumentParser()
ap.add_argument('--Fst_File', required=True, type=str, help='Tab separated text \
file of Fst values per gene')
ap.add_argument('--Fst_Threshold', required=True, type=float, help='Threshold \
value of Fst for carrying a gene forward')
ap.add_argument('--Kst_File', required=True, type=str, help='Tab separated text \
file of Kst values per gene')
ap.add_argument('--Kst_Threshold', required=True, type=float, help='Threshold \
value of Kst for carrying a gene forward')
ap.add_argument('--Dxy_File', required=True, type=str, help='Tab separated text \
file of Dxy values per gene')
ap.add_argument('--Dxy_Threshold', required=True, type=float, help='Threshold \
value of Dxy for carrying a gene forward')
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

Gene_set = set(Gene_List)

# -----------------------------------------------------
# Step 2
# Creates lists of genes exceeding threshold values
# -----------------------------------------------------
