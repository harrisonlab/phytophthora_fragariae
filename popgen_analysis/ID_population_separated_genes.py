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
ap.add_argument('--Kst_File', required=True, type=str, help='Tab separated text \
file of Kst values per gene')
ap.add_argument('--Dxy_File', required=True, type=str, help='Tab separated text \
file of Dxy values per gene')
ap.add_argument('--Out_Dir', required=True, type=str, help='Output directory')
ap.add_argument('--Out_Prefix', required=True, type=str, help='Prefix for output \
file')
conf = ap.parse_args()

# -----------------------------------------------------
# Step 1
# Load input files and build data structures
# -----------------------------------------------------

Fst_in = conf.Fst_File
Kst_in = conf.Kst_File
Dxy_in = conf.Dxy_File
OutDir = conf.Out_Dir
OutPre = conf.Out_Prefix
cwd = os.getcwd()

print("Arguments parsed")
