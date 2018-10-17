#!/usr/bin/python

'''
This script extracts Interproscan annotations for genes and builds Fisher
contigency tables showing number of annotated genes in a specified set
in comparison to a second set of genes.
'''

import argparse
from collections import defaultdict
import re

ap = argparse.ArgumentParser()
ap.add_argument('--Interpro', required=True, type=str, help='Interproscan \
annotations in a parsed .tsv format')
ap.add_argument('--Set1_Genes', required=True, type=str, help='List of genes \
in set 1, one gene per line')
ap.add_argument('--Set2_Genes', required=True, type=str, help='List of genes \
in set 2, one gene per line')
ap.add_argument('--Out_Dir', required=True, type=str, help='Output directory \
to write files to')

conf = ap.parse_args()

# -----------------------------------------------------
# Step 1
# Create dictionaries of the number of genes for each IPR annotation
# -----------------------------------------------------

Genes_set1 = conf.Set1_Genes
Genes_set2 = conf.Set2_Genes
IPRs = conf.Interpro

Genes_1 = []
Genes_2 = []

with open(Genes_set1) as f:
    lines = f.readlines()
    for line in lines:
        Gene = line.rstrip()
        Genes_1.append(Gene)

with open(Genes_set2) as f:
    lines = f.readlines()
    for line in lines:
        Gene = line.rstrip()
        Genes_2.append(Gene)

Genes_1s = set(Genes_1)
Genes_2s = set(Genes_2)

set1_dict = defaultdict(int)
set2_dict = defaultdict(int)
set1_count = 0
set2_count = 0
seen_IPR_set = set()

with open(IPRs) as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        split_line = line.split("\t")
        Gene_ID = split_line[0]
        m = re.findall("IPR......", line)
        if m:
            IPR_set = set(m)
        else:
            IPR_set = set(["no_annotation"])
        if Gene_ID in Genes_1s:
            for IPR in IPR_set:
                set1_dict[IPR] += 1
            set1_count += 1
            [seen_IPR_set.add(x) for x in IPR_set]
        elif Gene_ID in Genes_2s:
            for IPR in IPR_set:
                set2_dict[IPR] += 1
            set2_count += 1
            [seen_IPR_set.add(x) for x in IPR_set]

print set1_count
print set2_count

# -----------------------------------------------------
# Step 2
# Write out files
# -----------------------------------------------------

for IPR in seen_IPR_set:
    set1_IPR = set1_dict[IPR]
    set2_IPR = set2_dict[IPR]
    set1_others = set1_count - set1_IPR
    set2_others = set2_count - set2_IPR
    outline1 = "\t".join([str(IPR), str(set1_IPR), str(set2_IPR)]) + "\n"
    outline2 = "\t".join(["Other genes", str(set1_others),
                         str(set2_others)]) + "\n"
    outfile = "".join([conf.Out_Dir, "/", IPR, "_fishertable.txt"])
    with open(outfile, 'w') as o:
        o.write("".join([outline1, outline2]))
        o.close()
