#!/usr/bin/python

'''
This script takes three gene tables produced by pacbio_anntoation_tables_modified.py as input and outputs text files with a list of uniquely differentially expressed genes, based on gene ID in BC-16.
'''

import sys,argparse

#-----------------------------------------------------
# Step 1
# Import variables, load input files and create lists of gene names
#-----------------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument('--input_1',required=True,type=str,help='Gene table for reference isolate transcripts')
ap.add_argument('--input_2',required=True,type=str,help='Gene table for transcripts of non-reference isolate #1')
ap.add_argument('--input_3',required=True,type=str,help='Gene table for transcripts of non-reference isolate #2')
ap.add_argument('--output_1',required=True,type=str,help='Text file for output of reference isolate candidates')
ap.add_argument('--output_2',required=True,type=str,help='Text file for output of non-reference isolate #1')
ap.add_argument('--output_3',required=True,type=str,help='Text file for output of non-reference isolate #2')
conf = ap.parse_args()
