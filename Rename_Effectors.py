#!/usr/bin/python

'''
This script renames header files of predicted effectors (and secreted etc.)
that were used to create final GFFs, in order to match gene names submitted to
NCBI
'''

from collections import defaultdict
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('--Feature_File', type=str, required=True, help='File \
containing predictions of effector genes from older analyses')
ap.add_argument('--Conversion_File', type=str, required=True, help='File \
containing old and new gene IDs')
ap.add_argument('--Out_File', type=str, required=True, help='File for new gene \
names predicted as specific effector type')
conf = ap.parse_args()

# Load features file to a set

Old_Genes = []

with open(conf.Feature_File) as f:
    lines = f.readlines()
    for line in lines:
        stripped_line = line.rstrip()
        if '.' in stripped_line:
            Old_Genes.append(stripped_line)
        else:
            gene_id = '.'.join([stripped_line, 't1'])
            Old_Genes.append(gene_id)

Old_Set = set(Old_Genes)

print "Old gene IDs loaded and parsed"

# Load conversion file into a dictionary

conversion_dict = defaultdict(str)

with open(conf.Conversion_File) as f:
    lines = f.readlines()
    for line in lines:
        stripped_line = line.rstrip()
        split_line = stripped_line.split()
        Old_ID = split_line[0]
        New_ID = split_line[2]
        conversion_dict[Old_ID] = New_ID

print "Conversion file loaded and parsed"

# Create set of new IDs

New_IDs = []

for Old_Gene in Old_Set:
    split_gene = Old_Gene.split(".")
    ID_search_for = split_gene[0]
    Transcript_Number = split_gene[1]
    New_Gene = conversion_dict[ID_search_for]
    New_Transcript = ".".join([New_Gene, Transcript_Number])
    New_IDs.append(New_Transcript)

New_Set = set(New_IDs)
New_Set.discard(".t1")

print "New gene IDs generated"

# Write out new IDs

with open(conf.Out_File, 'w') as o:
    for gene in New_Set:
        o.write(gene)
        o.write('\n')

print "New headers file written"
