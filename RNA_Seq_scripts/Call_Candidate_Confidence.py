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
conf = ap.parse_args()

#-----------------------------------------------------
# Step 1
# Load input files
#-----------------------------------------------------

Uniq_Exp_Files = conf.Unique_Expression_Files
gene_IDs = []
Org1_Uniq_Exp = []
Org2_Uniq_Exp = []
Org3_Uniq_Exp = []
for Uniq_Exp_File in Uniq_Exp_Files:
    with open(Uniq_Exp_File) as f:
        if Uniq_Exp_File.split('/')[-1].split('_')[0] == Org1 and Uniq_Exp_File.split('/')[-1].split('_')[1] == Ref_Name:
            gene_lines = f.readlines()[1:]
            transcript_ID = gene_lines.split('\t')[0]
            Org1_Uniq_Exp.append(transcipt_ID)
        elif Uniq_Exp_File.split('/')[-1].split('_')[0] == Org2 and Uniq_Exp_File.split('/')[-1].split('_')[1] == Ref_Name:
            gene_lines = f.readlines()[1:]
            transcript_ID = gene_lines.split('\t')[0]
            Org2_Uniq_Exp.append(transcipt_ID)
        elif Uniq_Exp_File.split('/')[-1].split('_')[0] == Org3 and Uniq_Exp_File.split('/')[-1].split('_')[1] == Ref_Name:
            gene_lines = f.readlines()[1:]
            transcript_ID = gene_lines.split('\t')[0]
            Org3_Uniq_Exp.append(transcipt_ID)
        else:
            sys.exit("Error, incorrect expression files provided")

Org1_Uniq_Exp_set = set(Org1_Uniq_Exp)
Org2_Uniq_Exp_set = set(Org2_Uniq_Exp)
Org3_Uniq_Exp_set = set(Org3_Uniq_Exp)
