#!/usr/bin/python

'''
This script parses functional annotations from interproscan and swissprot.
Using gene lists of all genes and differentially expressed genes, it will output a table of functionally enriched annotations
'''

#-----------------------------------------------------
# Stage 1
# Import variables and load input files
#-----------------------------------------------------

import sys
import argparse
import re
from sets import Set
from collections import defaultdict
from operator import itemgetter
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('--gff_format',required=True,type=str,choices=['gff3', 'gtf'],help='Gff file format')
ap.add_argument('--gene_gff',required=True,type=str,help='Gff file of predicyted gene models')
ap.add_argument('--InterPro',required=True,type=str,help='The Interproscan functional annotation .tsv file')
ap.add_argument('--Swissprot',required=True,type=str,help='A parsed table of BLAST results against the Swissprot database. Note - must have been parsed with swissprot_parser.py')
ap.add_argument('--upreg_1',required=True,type=str,help='text file of genes upregulated at 24hrs')
ap.add_argument('--upreg_2',required=True,type=str,help='text file of genes upregulated at 48hrs')
ap.add_argument('--upreg_3',required=True,type=str,help='text file of genes upregulated at 96hrs')
ap.add_argument('--downreg_1',required=True,type=str,help='text file of genes downregulated at 24hrs')
ap.add_argument('--downreg_2',required=True,type=str,help='text file of genes downregulated at 48hrs')
ap.add_argument('--downreg_3',required=True,type=str,help='text file of genes downregulated at 96hrs')

conf = ap.parse_args()

with open(conf.gene_gff) as f:
    gene_lines = f.readlines()

with open(conf.InterPro) as f:
    InterPro_lines = f.readlines()

with open(conf.Swissprot) as f:
    swissprot_lines = f.readlines()

with open(conf.upreg_1) as f:
    up1_lines = f.readlines()[1:]

with open(conf.upreg_2) as f:
    up2_lines = f.readlines()[1:]

with open(conf.upreg_3) as f:
    up3_lines = f.readlines()[1:]

with open(conf.downreg_1) as f:
    down1_lines = f.readlines()[1:]

with open(conf.downreg_2) as f:
    down2_lines = f.readlines()[1:]

with open(conf.downreg_3) as f:
    down3_lines = f.readlines()[1:]
