#!/usr/bin/python

'''
This script uses an orthology group txt file output from OrthoMCL to create a
count table for the number of genes per strain in each orthogroup
'''

import argparse
from collections import defaultdict
import numpy
import csv

# -----------------------------------------------------
# Step 1
# Import variables & load input files
# Copied from orthoMCLgroups2fasta.py
# -----------------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument('--orthogroups', required=True, type=str, help='text file output \
of OrthoMCL orthogroups')
ap.add_argument('--out_dir', required=True, type=str, help='the tsv file where \
the count table is output to')
conf = ap.parse_args()

with open(conf.orthogroups) as f:
    ortho_lines = f.readlines()

# -----------------------------------------------------
# Step 2
# Build a dictionary of orthogroups
# Copied from orthoMCLgroups2fasta.py
# -----------------------------------------------------

ortho_dict = defaultdict(list)
for line in ortho_lines:
    line = line.rstrip()
    split_line = line.split()
    orthogroup = split_line[0]
    orthogroup = orthogroup.replace(':', '')
    for gene in split_line[1:]:
        ortho_dict[orthogroup].append(gene)

# -----------------------------------------------------
# Step 3
# Create counts for each entry and write to a table
# -----------------------------------------------------
# For each strain in each orthogroup, add the constituent genes to a set.
# Count the number of genes in this set and print to a table.
# Strain names and reshape commands need to be specified every time.

keys = []
sorted_keys = []
keys = ortho_dict.keys()
a = numpy.array(["Orthogroup", "A3_5", "FusGr1"], dtype='a10')

keys.sort()
ortho_list = []
for group_name in keys:
    print (str(group_name))
    print ("Counting genes in orthogroup: " + str(group_name))
    A3_5 = str(ortho_dict[group_name]).count("A3_5|")
    FusGr1 = str(ortho_dict[group_name]).count("FusGr1|")
    group_names = group_name
    to_add = [group_names, A3_5, FusGr1]
    a = numpy.append(a, to_add, axis=0)

z = len(keys) + 1
a = numpy.reshape(a, (z, 3))

outfile = str(conf.out_dir)
with open(outfile, "w") as o:
    writer = csv.writer(o, delimiter='\t')
    writer.writerows(a)
