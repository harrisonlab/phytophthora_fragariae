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
ap.add_argument('--orthogroups',required=True,type=str,help='text file output of OrthoMCL orthogroups')
ap.add_argument('--out_dir',required=True,type=str,help='the tsv file where the count table is output to')
conf = ap.parse_args()
