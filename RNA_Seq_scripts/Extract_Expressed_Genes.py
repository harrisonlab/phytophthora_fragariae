#!/usr/bin/python

'''
This script uses the output of DeSeq2 to produce a list of genes that are expressed only in a single isolate and add orthogroup ID for each gene
'''

import sys,argparse
from collections import defaultdict
import numpy as np
import json

ap = argparse.ArgumentParser()
ap.add_argument('--FPKM_in',required=True,type=str,help='text output file from DeSeq2 commands of non-normalised FPKM values')
ap.add_argument('--Orthogroup_in',required=True,type=str,help='text output file of Orthogroups from OrthoFinder')
ap.add_argument('--Organism_name',required=True,type=str,help='Name of organism gene IDs are from in FPKM input file')
ap.add_argument('--Output_1',required=True,type=str,help='Output text file for isolate 1, three timepoints')
ap.add_argument('--Output_2',required=True,type=str,help='Output text file for isolate 2, one timepoint')
ap.add_argument('--Output_3',required=True,type=str,help='Output text file for isolate 3, one timepoint')
conf = ap.parse_args()

#-----------------------------------------------------
# Step 1
# Load input files
#-----------------------------------------------------

with open(conf.FPKM_in) as f:
    fpkm_lines = f.readlines()[1:]

with open(conf.Orthogroup_in) as f:
    Ortho_lines = f.readlines()

#-----------------------------------------------------
# Step 2
# Build dictonaries of count data and of orthogroups
#-----------------------------------------------------

Isolate1_dict = defaultdict(list)
Isolate2_dict = defaultdict(list)
Isolate3_dict = defaultdict(list)
transcript_list = []

for line in fpkm_lines:
    split_lines = line.split()
    transcript_id = split_lines[0]
    transcript_list.append(transcript_id)
    time_a_list = []
    time_a_list.append(float(split_lines[1]))
    time_a_list.append(float(split_lines[2]))
    time_a_list.append(float(split_lines[3]))
    time_a = np.mean(time_a_list)
    time_b_list = []
    time_b_list.append(float(split_lines[4]))
    time_b_list.append(float(split_lines[5]))
    time_b_list.append(float(split_lines[6]))
    time_b = np.mean(time_b_list)
    time_c_list = []
    time_c_list.append(float(split_lines[7]))
    time_c_list.append(float(split_lines[8]))
    time_c_list.append(float(split_lines[9]))
    time_c = np.mean(time_c_list)
    Isolate1_dict[transcript_id].extend([float(time_a), float(time_b), float(time_c)])
    time_d_list = []
    time_d_list.append(float(split_lines[10]))
    time_d_list.append(float(split_lines[11]))
    time_d_list.append(float(split_lines[12]))
    time_d = np.mean(time_d_list)
    Isolate2_dict[transcript_id].extend([float(time_d)])
    time_e_list = []
    time_e_list.append(float(split_lines[13]))
    time_e_list.append(float(split_lines[14]))
    time_e_list.append(float(split_lines[15]))
    time_e = np.mean(time_e_list)
    Isolate3_dict[transcript_id].extend([float(time_e)])

organism_name = conf.Organism_name
ortho_dict = defaultdict(list)
for line in Ortho_lines:
    line = line.rstrip()
    split_line = line.split()
    orthogroup = split_line[0]
    orthogroup = orthogroup.replace(":", "")
    genes_in_group = [ x for x in split_line if organism_name in x ]
    for gene in genes_in_group:
        gene = gene.replace(organism_name, '').replace('|', '')
        ortho_dict[gene].extend(orthogroup)

#-----------------------------------------------------
# Step 3
# Iterate over dictionaries to keep only those with FPKM > 5
#-----------------------------------------------------

Isolate1_candidates = defaultdict(list)
Isolate2_candidates = defaultdict(list)
Isolate3_candidates = defaultdict(list)

for transcript, fpkm in Isolate1_dict.items():
    if any(value >= 5 for value in fpkm):
        orthogroup = ortho_dict[transcript]
        Isolate1_candidates[transcript] = orthogroup

for transcript, fpkm in Isolate2_dict.items():
    if fpkm >= 5:
        orthogroup = ortho_dict[transcript]
        Isolate2_candidates[transcript] = orthogroup

for transcript, fpkm in Isolate3_dict.items():
    if fpkm >= 5:
        orthogroup = ortho_dict[transcript]
        Isolate3_candidates[transcript] = orthogroup

#-----------------------------------------------------
# Step 4
# Print text files of expressed genes using dictionaries
#-----------------------------------------------------

with open(conf.Output_1, 'w') as o:
    keys = Isolate1_candidates.keys()
    for item in keys:
        orthogroup = Isolate1_candidates[item]
        o.write(item"\t"orthogroup"\n")

with open(conf.Output_2, 'w') as o:
    keys = Isolate2_candidates.keys()
    for item in keys:
        orthogroup = Isolate2_candidates[item]
        o.write(item"\t"orthogroup"\n")

with open(conf.Output_3, 'w') as o:
    keys = Isolate3_candidates.keys()
    for item in keys:
        orthogroup = Isolate3_candidates[item]
        o.write(item"\t"orthogroup"\n")
