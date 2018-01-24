#!/usr/bin/python

'''
This script takes three gene tables produced by pacbio_anntoation_tables_modified.py as input and outputs text files with a list of uniquely differentially expressed genes, based on orthogroup.
'''

from sets import Set
import sys,argparse
from collections import defaultdict

#-----------------------------------------------------
# Step 1
# Import variables, load input files and create sets of orthogroup names
#-----------------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument('--input_1',required=True,type=str,help='gene table for isolate #1')
ap.add_argument('--input_2',required=True,type=str,help='gene table for isolate #2')
ap.add_argument('--input_3',required=True,type=str,help='gene table for isolate #3')
ap.add_argument('--output_1',required=True,type=str,help='text file for output of isolate #1 candidates')
ap.add_argument('--output_2',required=True,type=str,help='text file for output of isolate #2 candidates')
ap.add_argument('--output_3',required=True,type=str,help='text file for output of isolate #3 candidates')
conf = ap.parse_args()
