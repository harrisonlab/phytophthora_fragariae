#!/usr/bin/python

'''
This script uses the output of DeSeq2 to produce a list of genes that are differntially expressed only in a single isolate and add orthogroup ID for each gene
'''

import sys,argparse
from collections import defaultdict
import numpy as np
import json
from sets import Set

ap = argparse.ArgumentParser()
ap.add_argument('--DEG_files',required=True,nargs='+',type=str,help='space spererated list of files containing DEG information')
ap.add_argument('--Orthogroup_in',required=True,type=str,help='text output file of Orthogroups from OrthoFinder')
ap.add_argument('--Organism_name',required=True,type=str,help='Name of organism gene IDs are from in FPKM input file')
ap.add_argument('--Output_1',required=True,type=str,help='Output text file for isolate 1, three timepoints')
ap.add_argument('--Output_2',required=True,type=str,help='Output text file for isolate 2, one timepoint')
ap.add_argument('--Output_3',required=True,type=str,help='Output text file for isolate 3, one timepoint')
conf = ap.parse_args()
