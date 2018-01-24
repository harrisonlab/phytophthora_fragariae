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
