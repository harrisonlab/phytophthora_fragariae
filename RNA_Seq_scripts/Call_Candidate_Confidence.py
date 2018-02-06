#!/usr/bin/python

'''
This script takes outputs from Expression presence/absence and differently DEGs to create a sorted table of candidates with a score of 1-9, 9 being best
'''

import sys,argparse
from collections import defaultdict
from sets import Set
import os

ap = argparse.ArgumentParser()
ap.add_argument('--Unique_Expression_Files',required=True,nargs='+',type=str,help='Space separated list of files containing uniquely expressed genes')
ap.add_argument('--Differently_DEG_File',required=True,nargs='+',type=str,help='Space separated list of files containing unique differently differentially expressed genes')
ap.add_argument('--Organism_1',required=True,type=str,help='ID of organism 1')
ap.add_argument('--Organism_2',required=True,type=str,help='ID of organism 2')
ap.add_argument('--Organism_3',required=True,type=str,help='ID of organism 3')
ap.add_argument('--Reference_name',required=True,type=str,help='ID of isolate to score candidates of')
ap.add_argument('--RxLRs',required=True,type=str,help='File of all RxLR names for aligned genome')
ap.add_argument('--CRNs',required=True,type=str,help='File of all CRN names for aligned genome')
ap.add_argument('--ApoP',required=True,type=str,help='File of all hits from ApoplastP')
ap.add_argument('--Secreted_CQ',required=True,type=str,help='File of all secreted gene models')
ap.add_argument('--Secreted_ORF',required=True,type=str,help='File of all secreted ORF fragments')
ap.add_argument('--OutDir',required=True,type=str,help='Directory to write output files to')
