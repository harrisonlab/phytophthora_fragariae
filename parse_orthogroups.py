#!/usr/bin/python

'''
This script uses an orthology group txt file output from OrthoMCL to create a count table for the number of genes per strain in each orthogroup
'''

from sets import Set
import sys,argparse
from collections import defaultdict
import re
import numpy
import csv

#-----------------------------------------------------
# Step 1
# Import variables & load input files
# Copied from orthoMCLgroups2fasta.py
#-----------------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument('--orthogroups',required=True,type=str,help='text file output of OrthoMCL orthogroups')
ap.add_argument('--out_dir',required=True,type=str,help='the directory where the count tble is output to')
conf = ap.parse_args()

with open(conf.orthogroups) as f:
    ortho_lines = f.readlines()

#-----------------------------------------------------
# Step 2
# Build a dictionary of orthogroups
# Copied from orthoMCLgroups2fasta.py
#-----------------------------------------------------

ortho_dict = defaultdict(list)
for line in ortho_lines:
    line = line.rstrip()
    split_line = line.split()
    orthogroup = split_line[0].replace('orthogroup', '')
    orthogroup = orthogroup.replace(':', '')
    for gene in split_line[1:]:
        ortho_dict[orthogroup].append(gene)

#-----------------------------------------------------
# Step 3
# Create counts for each entry and write to a table
#-----------------------------------------------------
# For each strain in each orthogroup, add the constituent genes to a set. Count the number of genes in this set and print to a table.

keys = []
sorted_keys = []
keys = ortho_dict.keys()
a = np.array([Orthogroup, A4, Bc1, Bc16, Bc23, Nov27, Nov5, Nov71, Nov77, Nov9, ONT3, SCRP245_v2])

keys.sort(key=int)
ortho_list = []
for group_name in keys:
    print ("orthogroup" + str(group_name))
    print ("Counting genes in orthogroup: " + str(group_name))
    A4 = ortho_dict[group_name].count("A4|")
    Bc1 = ortho_dict[group_name].count("Bc1|")
    Bc16 = ortho_dict[group_name].count("Bc16|")
    Bc23 = ortho_dict[group_name].count("Bc23|")
    Nov5 = ortho_dict[group_name].count("Nov5|")
    Nov27 = ortho_dict[group_name].count("Nov27|")
    Nov9 = ortho_dict[group_name].count("Nov9|")
    Nov71 = ortho_dict[group_name].count("Nov71|")
    Nov77 = ortho_dict[group_name].count("Nov77|")
    ONT3 = ortho_dict[group_name].count("ONT3|")
    SCRP245 = ortho_dict[group_name].count("SCRP245_v2|")
    to_add = [group_name, A4, Bc1, Bc16, Bc23, Nov27, Nov5, Nov71, Nov77, Nov9, ONT3, SCRP245]
    a = numpy.append(a, to_add, axis=0)

outfile = str(conf.out_dir)
with open(outfile, "wb") as o:
    writer = csv.writer(o)
    writer.writerows(a)
