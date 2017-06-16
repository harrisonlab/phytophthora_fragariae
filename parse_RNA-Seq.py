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
# Import variables, load input files & create set of genes
# If using a different number of files, arguments & appending to list of genes will need to be changed
#-----------------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument('--input_1',required=True,type=str,help='text file of genes')
ap.add_argument('--input_2',required=True,type=str,help='text file of genes')
ap.add_argument('--input_3',required=True,type=str,help='text file of genes')
ap.add_argument('--out_dir',required=True,type=str,help='the tsv file where the count table is output to')
conf = ap.parse_args()

with open(conf.input_1) as f1:
    inp1_lines = f1.readlines()[1:]
    genes_list = []
    for x in inp1_lines:
        genes_list.append(x.split('\t')[0])

with open(conf.input_2) as f2:
    inp2_lines = f2.readlines()[1:]
    for x in inp2_lines:
        genes_list.append(x.split('\t')[0])

with open(conf.input_3) as f3:
    inp3_lines = f3.readlines()[1:]
    for x in inp3_lines:
        genes_list.append(x.split('\t')[0])

genes = set(genes_list)

#-----------------------------------------------------
# Step 2
# Load gene names to a numpy array and reshape array to size required for analysis
# If doing with a different number of files, change the number in the numpy.reshape() command
#-----------------------------------------------------
