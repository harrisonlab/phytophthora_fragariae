#!/usr/bin/python

'''
This script uses the output of DeSeq2 to produce a list of genes that are differntially expressed only in a single isolate and add orthogroup ID for each gene
'''

import sys,argparse
from collections import defaultdict
import numpy as np
import json
from sets import Set

ap = argparse.ArgumentParser()
ap.add_argument('--DEG_files',required=True,nargs='+',type=str,help='space spererated list of files containing DEG information')
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

DEG_files = conf.DEG_files
DEG_dict = defaultdict(list)
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
                entryname = "_".join([filename, gene_name])
                DEG_dict[entryname].extend([log_change, P_val])

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
        ortho_dict[gene] = orthogroup
