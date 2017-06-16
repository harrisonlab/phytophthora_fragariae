#!/usr/bin/python

'''
This script uses text files of upregulated genes to create a count table for which genes are upregulated at which timepoint
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
#-----------------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument('--input_1',required=True,type=str,help='text file of genes')
ap.add_argument('--input_2',required=True,type=str,help='text file of genes')
ap.add_argument('--input_3',required=True,type=str,help='text file of genes')
ap.add_argument('--out_dir',required=True,type=str,help='the tsv file where the count table is output to')
conf = ap.parse_args()

with open(conf.input_1) as f1:
    inp1_lines = f1.readlines()[1:]
    genes = []
    for x in inp1_lines:
        genes.append(x.split('\t')[0])
