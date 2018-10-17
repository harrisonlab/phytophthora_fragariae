#!/usr/bin/python

'''
This script extracts Interproscan annotations for genes and builds Fisher
contigency tables showing number of annotated genes in a specified set
in comparison to a second set of genes.
'''

import argparse
import numpy
for collections import defaultdict
from operator import itemgetter

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

#-----------------------------------------------------
# Step 1
# Create dictionaries of the number of genes for each IPR annotation
#-----------------------------------------------------

Genes_set1 = conf.Set1_Genes
Genes_set2 = conf.Set2_Genes
IPRs = conf.Interpro

Genes_1 = []
Genes_2 = []

with open(Set1_Genes) as f:
    lines = f.readlines()
    for line in lines:
        Genes_1.append(line)

with open(Set2_Genes) as f:
    lines = f.readlines()
    for line in lines:
        Genes_2.append(line)

Genes_1s = set(Genes_1)
Genes_2s = set(Genes_2)
