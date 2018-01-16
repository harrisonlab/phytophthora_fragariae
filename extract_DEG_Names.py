#!/usr/bin/python

'''
This script uses the tsv file produced by parsing RNA-Seq with a previous python script to extract only DEGs above a certain threshold
'''

import sys,argparse
from collections import defaultdict

ap = argparse.ArgumentParser()
ap.add_argument('--input',required=True,type=str,help='tsv file of binary presence table of DEGs')
ap.add_argument('--output',required=True,type=str,help='Output text file of gene names')

#-----------------------------------------------------
# Step 1
# Load .tsv file into a dictionary
#-----------------------------------------------------

DEG_dict = defaultdict(list)
with open(conf.input) as f:
    DEG_lines = f.readlines()
    for line in DEG_lines:
        if line.startswith('Gene_Name'):
            continue
        else:
            split_line = line.split()
            gene_name = split_line[0]
            time_a = split_line[1]
            time_b = split_line[2]
            time_c = split_line[3]
            DEG_dict[gene_name].extend([time_a, time_b, time_c])
