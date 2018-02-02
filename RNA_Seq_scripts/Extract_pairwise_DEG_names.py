#!/usr/bin/python

'''
This script uses the output of DeSeq2 to produce a list of genes that are differntially expressed only in a single isolate and add orthogroup ID for each gene. Only works for three isolates.
'''

import sys,argparse
from collections import defaultdict
from sets import Set
import os

ap = argparse.ArgumentParser()
ap.add_argument('--DEG_files',required=True,nargs='+',type=str,help='space spererated list of files containing DEG information')
ap.add_argument('--Orthogroup_in',required=True,type=str,help='text output file of Orthogroups from OrthoFinder')
ap.add_argument('--Reference_name',required=True,type=str,help='Name of organism gene IDs are from in DEG input file')
ap.add_argument('--Min_LFC',required=True,type=float,help='Minimum log fold change for a gene to be called a DEG')
ap.add_argument('--Sig_Level',required=True,type=float,help='Minimum p-value for a DEG to be considered significant')
ap.add_argument('--Organism_1',required=True,type=str,help='Name of isolate 1, three timepoints')
ap.add_argument('--Organism_2',required=True,type=str,help='Name of isolate 2, one timepoint')
ap.add_argument('--Organism_3',required=True,type=str,help='Name of isolate 3, one timepoint')
ap.add_argument('--OutDir',required=True,type=str,help='Directory to write output files to')
conf = ap.parse_args()

#-----------------------------------------------------
# Step 1
# Load input files
#-----------------------------------------------------

LFC = conf.Min_LFC
Sig_Level = conf.Sig_Level

DEG_files = conf.DEG_files
DEG_list = []
LFC_values = defaultdict(float)
P_values = defaultdict(float)
for DEG_file in DEG_files:
    with open(DEG_file) as f:
        filename = DEG_file
        DEG_lines = f.readlines()
        for line in DEG_lines:
            if line.startswith('baseMean'):
                continue
            else:
                split_line = line.split()
                gene_name = split_line[0]
                log_change = float(split_line[2])
                P_val = float(split_line[6])
                if abs(log_change) >= LFC and P_val <= Sig_Level:
                    entryname = "_".join([filename, gene_name])
                    DEG_list.append(entryname)
                    LFC_values[entryname] = log_change
                    P_values[entryname] = P_val

reference_name = conf.Reference_name
ortho_dict = defaultdict(str)
for line in Ortho_lines:
    line = line.rstrip()
    split_line = line.split()
    orthogroup = split_line[0]
    orthogroup = orthogroup.replace(":", "")
    genes_in_group = [ x for x in split_line if reference_name in x ]
    for gene in genes_in_group:
        gene = gene.replace(reference_name, '').replace('|', '')
        ortho_dict[gene] = orthogroup

Org1 = conf.Organism_1
Org2 = conf.Organism_2
Org3 = conf.Organism_3

OutDir = conf.OutDir

cwd = os.getcwd()

print("Input files loaded")

#-----------------------------------------------------
# Step 3
# Create dictionaries for output
#-----------------------------------------------------

#Organism1 vs Organism2
Org1_vs_Org2 = []
Org1_vs_Org2_LFC = defaultdict(float)
Org1_vs_Org2_Pval = defaultdict(float)

for item in DEG_list:
    if item.split('/')[-1].split('_')[0] == Organism1 and item.split('/')[-1].split('_')[3] == Organism2 and item.split('/')[-1].split('_')[5] == "up":
        transcript_id = item.split('/').split('_')[6]
        Org1_vs_Org2.append(transcript_id)
        Org1_vs_Org2_LFC[transcript_id] = LFC_values[item]
        Org1_vs_Org2_Pval[transcript_id] = P_values[item]
    elif item.split('/')[-1].split('_')[0] == Organism2 and item.split('/')[-1].split('_')[3] == Organism1 and item.split('/')[-1].split('_')[5] == "down":
        transcript_id = item.split('/').split('_')[6]
        Org1_vs_Org2.append(transcript_id)
        Org1_vs_Org2_LFC[transcript_id] = LFC_values[item]
        Org1_vs_Org2_Pval[transcript_id] = P_values[item]

Org1_vs_Org2_set = set(Org1_vs_Org2)

#Organism1 vs Organism3
Org1_vs_Org3 = []
Org1_vs_Org3_LFC = defaultdict(float)
Org1_vs_Org3_Pval = defaultdict(float)

for item in DEG_list:
    if item.split('/')[-1].split('_')[0] == Organism1 and item.split('/')[-1].split('_')[3] == Organism3 and item.split('/')[-1].split('_')[5] == "up":
        transcript_id = item.split('/').split('_')[6]
        Org1_vs_Org3.append(transcript_id)
        Org1_vs_Org3_LFC[transcript_id] = LFC_values[item]
        Org1_vs_Org3_Pval[transcript_id] = P_values[item]
    elif item.split('/')[-1].split('_')[0] == Organism3 and item.split('/')[-1].split('_')[3] == Organism1 and item.split('/')[-1].split('_')[5] == "down":
        transcript_id = item.split('/').split('_')[6]
        Org1_vs_Org3.append(transcript_id)
        Org1_vs_Org3_LFC[transcript_id] = LFC_values[item]
        Org1_vs_Org3_Pval[transcript_id] = P_values[item]

Org1_vs_Org3_set = set(Org1_vs_Org3)

#Organism2 vs Organism1
Org2_vs_Org1 = []
Org2_vs_Org1_LFC = defaultdict(float)
Org2_vs_Org1_Pval = defaultdict(float)

for item in DEG_list:
    if item.split('/')[-1].split('_')[0] == Organism2 and item.split('/')[-1].split('_')[3] == Organism1 and item.split('/')[-1].split('_')[5] == "up":
        transcript_id = item.split('/').split('_')[6]
        Org2_vs_Org1.append(transcript_id)
        Org2_vs_Org1_LFC[transcript_id] = LFC_values[item]
        Org2_vs_Org1_Pval[transcript_id] = P_values[item]
    elif item.split('/')[-1].split('_')[0] == Organism1 and item.split('/')[-1].split('_')[3] == Organism2 and item.split('/')[-1].split('_')[5] == "down":
        transcript_id = item.split('/').split('_')[6]
        Org2_vs_Org1.append(transcript_id)
        Org2_vs_Org1_LFC[transcript_id] = LFC_values[item]
        Org2_vs_Org1_Pval[transcript_id] = P_values[item]

Org2_vs_Org1_set = set(Org2_vs_Org1)

#Organism2 vs Organism3
Org2_vs_Org3 = []
Org2_vs_Org3_LFC = defaultdict(float)
Org2_vs_Org3_Pval = defaultdict(float)

for item in DEG_list:
    if item.split('/')[-1].split('_')[0] == Organism2 and item.split('/')[-1].split('_')[3] == Organism3 and item.split('/')[-1].split('_')[5] == "up":
        transcript_id = item.split('/').split('_')[6]
        Org2_vs_Org3.append(transcript_id)
        Org2_vs_Org3_LFC[transcript_id] = LFC_values[item]
        Org2_vs_Org3_Pval[transcript_id] = P_values[item]
    elif item.split('/')[-1].split('_')[0] == Organism3 and item.split('/')[-1].split('_')[3] == Organism2 and item.split('/')[-1].split('_')[5] == "down":
        transcript_id = item.split('/').split('_')[6]
        Org2_vs_Org3.append(transcript_id)
        Org2_vs_Org3_LFC[transcript_id] = LFC_values[item]
        Org2_vs_Org3_Pval[transcript_id] = P_values[item]

Org2_vs_Org3_set = set(Org2_vs_Org3)

#Organism3 vs Organism1
Org3_vs_Org1 = []
Org3_vs_Org1_LFC = defaultdict(float)
Org3_vs_Org1_Pval = defaultdict(float)

for item in DEG_list:
    if item.split('/')[-1].split('_')[0] == Organism3 and item.split('/')[-1].split('_')[3] == Organism1 and item.split('/')[-1].split('_')[5] == "up":
        transcript_id = item.split('/').split('_')[6]
        Org3_vs_Org1.append(transcript_id)
        Org3_vs_Org1_LFC[transcript_id] = LFC_values[item]
        Org3_vs_Org1_Pval[transcript_id] = P_values[item]
    elif item.split('/')[-1].split('_')[0] == Organism1 and item.split('/')[-1].split('_')[3] == Organism3 and item.split('/')[-1].split('_')[5] == "down":
        transcript_id = item.split('/').split('_')[6]
        Org3_vs_Org1.append(transcript_id)
        Org3_vs_Org1_LFC[transcript_id] = LFC_values[item]
        Org3_vs_Org1_Pval[transcript_id] = P_values[item]

Org3_vs_Org1_set = set(Org3_vs_Org1)

#Organism3 vs Organism2
Org3_vs_Org2 = []
Org3_vs_Org2_LFC = defaultdict(float)
Org3_vs_Org2_Pval = defaultdict(float)

for item in DEG_list:
    if item.split('/')[-1].split('_')[0] == Organism3 and item.split('/')[-1].split('_')[3] == Organism2 and item.split('/')[-1].split('_')[5] == "up":
        transcript_id = item.split('/').split('_')[6]
        Org3_vs_Org2.append(transcript_id)
        Org3_vs_Org2_LFC[transcript_id] = LFC_values[item]
        Org3_vs_Org2_Pval[transcript_id] = P_values[item]
    elif item.split('/')[-1].split('_')[0] == Organism2 and item.split('/')[-1].split('_')[3] == Organism3 and item.split('/')[-1].split('_')[5] == "down":
        transcript_id = item.split('/').split('_')[6]
        Org3_vs_Org2.append(transcript_id)
        Org3_vs_Org2_LFC[transcript_id] = LFC_values[item]
        Org3_vs_Org2_Pval[transcript_id] = P_values[item]

Org3_vs_Org2_set = set(Org3_vs_Org2)

#-----------------------------------------------------
# Step 4
# Create unique sets for DEGs of each isolate
#-----------------------------------------------------

Org1_uniq = []
Org2_uniq = []
Org3_uniq = []

for transcript in Org1_vs_Org2_set:
    if transcript in Org1_vs_Org3_set:
        Org1_uniq.append(transcript)

for transcript in Org2_vs_Org1_set:
    if transcript in Org2_vs_Org3_set:
        Org2_uniq.append(transcript)

for transcript in Org3_vs_Org1_set:
    if transcript in Org3_vs_Org2_set:
        Org3_uniq.append(transcript)

Org1_uniq_set = set(Org1_uniq)
Org2_uniq_set = set(Org2_uniq)
Org3_uniq_set = set(Org3_uniq)

#-----------------------------------------------------
# Step 5
# Write out text files for all genes that are uniquely differentially expressed
#-----------------------------------------------------

Org1_file = "_".join([reference_name, Org1, "all_unique_DEGs.txt"])
Org2_file = "_".join([reference_name, Org2, "all_unique_DEGs.txt"])
Org3_file = "_".join([reference_name, Org3, "all_unique_DEGs.txt"])

Org1_out = "/".join([cwd, OutDir, Org1_file])
Org2_out = "/".join([cwd, OutDir, Org2_file])
Org3_out = "/".join([cwd, OutDir, Org3_file])

LFC1 = "_".join(["LFC", Org1])
LFC2 = "_".join(["LFC", Org2])
LFC3 = "_".join(["LFC", Org3])
PV1 = "_".join(["P-value", "adjusted", Org1])
PV2 = "_".join(["P-value", "adjusted", Org2])
PV3 = "_".join(["P-value", "adjusted", Org3])

Header = "\t".join(["Gene_ID", "Orthogroup", LFC2, PV2, LFC3, PV3])

with open(Org1_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for transcript in Org1_uniq_set:
        orthogroup = ortho_dict[transcript]
