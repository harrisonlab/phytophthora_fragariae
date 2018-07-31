#!/usr/bin/python

'''
Sometimes an ORF fragment is classified as an ApoplastP hit when the
overlapping Augustus gene is not. Prioritise the gene with an effector
prediction.
'''

import argparse
from collections import defaultdict

ap = argparse.ArgumentParser()
ap.add_argument('--gff_in', required=True, type=str, help='input gff file')
ap.add_argument('--gff_out', required=True, type=str, help='output gff file')
ap.add_argument('--Aug_ApoP', required=True, type=str, help='File of Augustus \
ApoplastP predictions')
ap.add_argument('--ORF_ApoP', required=True, type=str, help='File of ORF \
ApoplastP predictions')
ap.add_argument('--Unclear_Genes', required=True, type=str, help='File of \
genes where it is unclear which model to accept')
conf = ap.parse_args()

# -----------------------------------------------------
# Step 1
# Parse arguments
# -----------------------------------------------------

In_Gff = conf.gff_in
Out_Gff = conf.gff_out
ApoP_Aug = conf.Aug_ApoP
ApoP_ORF = conf.ORF_ApoP

print("Command line arguments parsed")

# -----------------------------------------------------
# Step 2
# Create dictionary of gene locations and list of ApoPs
# -----------------------------------------------------

location_dict = defaultdict(list)
ApoPs = []

with open(In_Gff) as f:
    input_lines = f.readlines()
    for line in input_lines:
        split_line = line.split()
        if split_line[2] == 'mRNA':
            col9 = split_line[8]
            gene_ID = col9.split(';')[0].replace('ID=', '')
            contig = split_line[0]
            start = split_line[3]
            end = split_line[4]
            key = "_".join([contig, start, end])
            location_dict[key].append(gene_ID)

with open(ApoP_Aug) as f:
    lines = f.readlines()
    for line in lines:
        line_to_add = line.rstrip()
        ApoPs.append(line_to_add)

with open(ApoP_ORF) as f:
    lines = f.readlines()
    for line in lines:
        line_to_add = line.rstrip()
        to_add = ".".join([line_to_add, "t1"])
        ApoPs.append(to_add)

ApoP_set = set(ApoPs)

print("Dictionaries and list of ApoP hits created")

# -----------------------------------------------------
# Step 3
# Check where two genes are at the same location and preferentially keep ApoP
# -----------------------------------------------------

Replacement_dict = defaultdict(list)
write_dict = defaultdict(list)
Unclear_dict = defaultdict(list)
genes_to_write = []

for item in location_dict.keys():
    genes = location_dict[item]
    if len(genes) > 1:
        for gene in genes:
            if gene in ApoP_set:
                Replacement_dict[item].append(gene)
    else:
        write_dict[item] = location_dict[item]

for item in Replacement_dict.keys():
    genes = Replacement_dict[item]
    if len(genes) == 1:
        write_dict[item] = location_dict[item]
    else:
        Unclear_dict[item] = genes

for item in write_dict.keys():
    gene = write_dict[item]
    for transcript in gene:
        genes_to_write.append(transcript)

print("Genes to write out identified")

# -----------------------------------------------------
# Step 4
# Write out outputs
# -----------------------------------------------------

with open(Out_Gff, 'w') as o:
    for line in input_lines:
        split_line = line.split()
        type = split_line[2]
        if type == 'gene':
            ID = split_line[8].split('=')[-1]
        else:
            ID = split_line[8].split('=')[-1].split('.')[0]
        if ID in genes_to_write:
            o.write(line)
            o.write('\n')

print("Gff written")

if len(Unclear_dict.keys()) > 0:
    print("Some genes are unclear as to which to keep")
    with open(conf.Unclear_genes, 'w') as o:
        for item in Unclear_dict.keys():
            for gene in Unclear_dict[item]:
                Output = "\t".join([item, gene])
                o.write(Output)
                o.write("\n")
