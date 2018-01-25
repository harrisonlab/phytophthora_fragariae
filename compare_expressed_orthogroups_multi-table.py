#!/usr/bin/python

'''
This script takes three gene tables produced by pacbio_anntoation_tables_modified.py as input and outputs text files with a list of uniquely differentially expressed genes, based on orthogroup.
'''

from sets import Set
import sys,argparse
from collections import defaultdict

#-----------------------------------------------------
# Step 1
# Import variables, load input files and create sets of orthogroup names
#-----------------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument('--input_1',required=True,type=str,help='gene table for isolate #1')
ap.add_argument('--input_2',required=True,type=str,help='gene table for isolate #2')
ap.add_argument('--input_3',required=True,type=str,help='gene table for isolate #3')
ap.add_argument('--output_1',required=True,type=str,help='text file for output of isolate #1 candidates')
ap.add_argument('--output_2',required=True,type=str,help='text file for output of isolate #2 candidates')
ap.add_argument('--output_3',required=True,type=str,help='text file for output of isolate #3 candidates')
conf = ap.parse_args()

inp1_dict = defaultdict(list)
with open(conf.input_1) as f1:
    inp1_lines = f1.readlines()[1:]
    inp1_orthogroups = []
    for x in inp1_lines:
        FPKM_24 = float(x.split('\t')[21])
        FPKM_48 = float(x.split('\t')[22])
        FPKM_96 = float(x.split('\t')[23])
        FPKM_Mycelium = float(x.split('\t')[24])
        LFC_24 = float(x.split('\t')[25])
        LFC_48 = float(x.split('\t')[27])
        LFC_96 = float(x.split('\t')[29])
        P_val_24 = float(x.split('\t')[26])
        P_val_48 = float(x.split('\t')[28])
        P_val_96 = float(x.split('\t')[30])
        if FPKM_24 >= 5 or FPKM_48 >= 5 or FPKM_96 >= 5 or FPKM_Mycelium >= 5:
            if (LFC_24 >= 1 and P_val_24 <= 0.05) or (LFC_48 >= 1 and P_val_48 <= 0.05) or (LFC_96 >= 1 and P_val_96 <=0.05):
                gene_ID = x.split('\t')[0]
                orthogroup_ID = x.split('\t')[16]
                inp1_orthogroups.append(orthogroup_ID)
                inp1_dict[orthogroup_ID].append(gene_ID)

inp2_dict = defaultdict(list)
with open(conf.input_1) as f2:
    inp2_lines = f2.readlines()[1:]
    inp2_orthogroups = []
    for x in inp2_lines:
        FPKM_Plant = float(x.split('\t')[19])
        FPKM_Mycelium = float(x.split('\t')[20])
        LFC = float(x.split('\t')[21])
        P_val = float(x.split('\t')[22])
        if FPKM_Plant >= 5 or FPKM_Mycelium >= 5:
            if LFC >= 1 and P_val <= 0.05:
                gene_ID = x.split('\t')[0]
                orthogroup_ID = x.split('\t')[16]
                inp2_orthogroups.append(orthogroup_ID)
                inp2_dict[orthogroup_ID].append(gene_ID)
