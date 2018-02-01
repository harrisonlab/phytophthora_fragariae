#!/usr/bin/python

'''
This script uses the output of DeSeq2 to produce a list of genes that are expressed only in a single isolate and add orthogroup ID for each gene, also identifies and classifies unique genes
'''

import sys,argparse
from collections import defaultdict
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('--FPKM_in',required=True,type=str,help='text output file from DeSeq2 commands of non-normalised FPKM values')
ap.add_argument('--Orthogroup_in',required=True,type=str,help='text output file of Orthogroups from OrthoFinder')
ap.add_argument('--Reference_name',required=True,type=str,help='Name of organism gene IDs are from in FPKM input file')
ap.add_argument('--Organism_1',required=True,type=str,help='Name of isolate 1, three timepoints')
ap.add_argument('--Organism_2',required=True,type=str,help='Name of isolate 2, one timepoint')
ap.add_argument('--Organism_3',required=True,type=str,help='Name of isolate 3, one timepoint')
ap.add_argument('--FPKM_min',required=True,type=float,help='Minimum FPKM value to accept as evidence of expression')
ap.add_argument('--RxLRs',required=True,type=str,help='File of all RxLR names for aligned genome')
ap.add_argument('--CRNs',required=True,type=str,help='File of all CRN names for aligned genome')
ap.add_argument('--ApoP',required=True,type=str,help='File of all hits from ApoplastP')
ap.add_argument('--Secreted_CQ',required=True,type=str,help='File of all secreted gene models')
ap.add_argument('--Secreted_ORF',required=True,type=str,help='File of all secreted ORF fragments')
conf = ap.parse_args()

#-----------------------------------------------------
# Step 1
# Load input files
#-----------------------------------------------------

with open(conf.FPKM_in) as f:
    fpkm_lines = f.readlines()[1:]

with open(conf.Orthogroup_in) as f:
    Ortho_lines = f.readlines()

Org1 = conf.Organism_1
Org2 = conf.Organism_2
Org3 = conf.Organism_3

print("Input files loaded")

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
    Isolate1_dict[transcript_id] = [float(time_a), float(time_b), float(time_c)]
    time_d_list = []
    time_d_list.append(float(split_lines[10]))
    time_d_list.append(float(split_lines[11]))
    time_d_list.append(float(split_lines[12]))
    time_d = np.mean(time_d_list)
    Isolate2_dict[transcript_id] = float(time_d)
    time_e_list = []
    time_e_list.append(float(split_lines[13]))
    time_e_list.append(float(split_lines[14]))
    time_e_list.append(float(split_lines[15]))
    time_e = np.mean(time_e_list)
    Isolate3_dict[transcript_id] = float(time_e)

Reference_name = conf.Reference_name
ortho_dict = defaultdict(list)
for line in Ortho_lines:
    line = line.rstrip()
    split_line = line.split()
    orthogroup = split_line[0]
    orthogroup = orthogroup.replace(":", "")
    genes_in_group = [ x for x in split_line if Reference_name in x ]
    for gene in genes_in_group:
        gene = gene.replace(Reference_name, '').replace('|', '')
        ortho_dict[gene] = orthogroup

print("FPKM & Orthogroup libraries built")

#-----------------------------------------------------
# Step 3
# Iterate over dictionaries to keep only those with FPKM > 5
#-----------------------------------------------------

Isolate1_candidates = defaultdict(list)
Isolate2_candidates = defaultdict(list)
Isolate3_candidates = defaultdict(list)
FPKM = conf.FPKM_min

for transcript, fpkm in Isolate1_dict.items():
    if any(value >= FPKM for value in fpkm):
        if transcript in ortho_dict.keys():
            orthogroup = ortho_dict[transcript]
            Isolate1_candidates[transcript] = orthogroup
        else:
            Isolate1_candidates[transcript] = "None"

for transcript, fpkm in Isolate2_dict.items():
    if fpkm >= FPKM:
        if transcript in ortho_dict.keys():
            orthogroup = ortho_dict[transcript]
            Isolate2_candidates[transcript] = orthogroup
        else:
            Isolate2_candidates[transcript] = "None"

for transcript, fpkm in Isolate3_dict.items():
    if fpkm >= FPKM:
        if transcript in ortho_dict.keys():
            orthogroup = ortho_dict[transcript]
            Isolate3_candidates[transcript] = orthogroup
        else:
            Isolate3_candidates[transcript] = "None"

print("Expressed genes identified")

#-----------------------------------------------------
# Step 4
# Print text files of expressed genes using dictionaries
#-----------------------------------------------------

with open(Reference_name"_"Org1"_expressed.txt", 'w') as o:
    keys = Isolate1_candidates.keys()
    for item in keys:
        orthogroup = Isolate1_candidates[item]
        output = "\t".join([item, orthogroup])
        o.write(output)
        o.write("\n")

with open(Reference_name"_"Org2"_expressed.txt", 'w') as o:
    keys = Isolate2_candidates.keys()
    for item in keys:
        orthogroup = Isolate2_candidates[item]
        output = "\t".join([item, orthogroup])
        o.write(output)
        o.write("\n")

with open(Reference_name"_"Org3"_expressed.txt", 'w') as o:
    keys = Isolate3_candidates.keys()
    for item in keys:
        orthogroup = Isolate3_candidates[item]
        output = "\t".join([item, orthogroup])
        o.write(output)
        o.write("\n")

print("Initial output files created for all genes")

#-----------------------------------------------------
# Step 5
# Identify genes that are uniquely expressed
#-----------------------------------------------------

Isolate1_set = set(Isolate1_candidates.keys())
Isolate1_uniq = []
Isolate2_set = set(Isolate2_candidates.keys())
Isolate2_uniq = []
Isolate3_set = set(Isolate3_candidates.keys())
Isolate3_uniq = []

for transcript in Isolate1_set:
    if transcript not in Isolate2_set:
        if transcript not in Isolate3_set:
            Isolate1_uniq.append(transcript)

for transcript in Isolate2_set:
    if transcript not in Isolate1_set:
        if transcript not in Isolate3_set:
            Isolate2_uniq.append(transcript)

for transcript in Isolate3_set:
    if transcript not in Isolate2_set:
        if transcript not in Isolate1_set:
            Isolate3_uniq.append(transcript)

#-----------------------------------------------------
# Step 6
# Print all uniquely expressed genes to text file
#-----------------------------------------------------
