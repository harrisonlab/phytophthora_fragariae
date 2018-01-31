#!/usr/bin/python

'''
This script uses the output of DeSeq2 to produce a list of genes that are differntially expressed only in a single isolate and add orthogroup ID for each gene. For aligning multiple isolates RNA to one reference.
'''

import sys,argparse
from collections import defaultdict
import json
from sets import Set

ap = argparse.ArgumentParser()
ap.add_argument('--DEG_files',required=True,nargs='+',type=str,help='space spererated list of files containing DEG information')
ap.add_argument('--Orthogroup_in',required=True,type=str,help='text output file of Orthogroups from OrthoFinder')
ap.add_argument('--Reference_name',required=True,type=str,help='Name of organism gene IDs are from in DEG input file')
ap.add_argument('--Min_LFC',required=True,type=float,help='Minimum log fold change for a gene to be called a DEG')
ap.add_argument('--Sig_Level',required=True,type=float,help='Minimum p-value for a DEG to be considered significant')
conf = ap.parse_args()

#-----------------------------------------------------
# Step 1
# Load input files
#-----------------------------------------------------

LFC = conf.Min_LFC
Sig_Level = conf.Sig_Level

DEG_files = conf.DEG_files
DEG_list = []
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
                log_change = split_line[2]
                P_val = split_line[6]
                if abs(log_change) >= LFC and P_val <= Sig_Level:
                    entryname = "_".join([filename, gene_name])
                    DEG_list.append(entryname)

reference_name = conf.Reference_name
ortho_dict = defaultdict(list)
for line in Ortho_lines:
    line = line.rstrip()
    split_line = line.split()
    orthogroup = split_line[0]
    orthogroup = orthogroup.replace(":", "")
    genes_in_group = [ x for x in split_line if reference_name in x ]
    for gene in genes_in_group:
        gene = gene.replace(reference_name, '').replace('|', '')
        ortho_dict[gene] = orthogroup

#-----------------------------------------------------
# Step 2
# Create organism variables
#-----------------------------------------------------

Organism = []
for DEG_file in DEG_files:
    Organism_ID = DEG_file.split('/')[-1].split('_')[0]
    Organisms.append(Organism_ID)


Organism = set(Organism)
Organism1 = list(Organism)[0]

#-----------------------------------------------------
# Step 3
# Create dictionaries for output
#-----------------------------------------------------

#Organism1
Org1 = []
for item in DEG_list:
    if item.split('/')[-1].split('_')[0] == Organism1:
        transcript_id = item.split('/').split('_')[6]
        Org1.append(transcript_id)

Org1_set = set(Org1)
Org1_dict = defaultdict(str)

for transcript in Org1_set:
    orthogroup = ortho_dict[transcript]
    Org1_dict[transcript].extend(orthogroup)

#-----------------------------------------------------
# Step 4
# Write output files
#-----------------------------------------------------

with open(Organism1".txt") as f:
    o.write(json.dumps(Org1_dict))
