#!/usr/bin/python

'''
This script uses candidates identified by Call_Candidate_Confidence.py and
extracts details from tables created by pacbio_anntoation_tables_modified.py
or pacbio_anntoation_tables_modified_no_coexp.py depending on isolate examined
'''

import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument('--candidates', required=True, type=str,
                help='TSV file of candidate genes explaning the phenotypic \
                differences')
ap.add_argument('--annotation_table', required=True, type=str,
                help='TSV file containing gene expression details and other \
                information')
ap.add_argument('--out_file', required=True, type=str,
                help='File to write output files to')
conf = ap.parse_args()

# -----------------------------------------------------
# Step 1
# Load candidate file and create a list of candidate genes
# -----------------------------------------------------

transcripts = []
candidates_file = conf.candidates
candidate_lines = candidates_file.readlines[1:]
for line in candidate_lines:
    split_line = line.split()
    transcript_ID = split_line[0]
    transcripts.append(transcript_ID)

# -----------------------------------------------------
# Step 2
# Identify lines in annotation table to keep and add to list
# -----------------------------------------------------

Output_lines = []
annotation_table = conf.annotation_table
annotation_lines = annotation_table.readlines[1:]
for transcript_ID in transcripts:
    for annotation_line in annotation_lines:
        if annotation_line.startswih(transcript_ID):
            Output_lines.append(annotation_line)

# -----------------------------------------------------
# Step 3
# Write out lines to keep to TSV file
# -----------------------------------------------------

outfile = conf.out_file
cwd = os.getcwd()
Output = "/".join([cwd, outfile])

Header = annotation_table.readlines[0]

with open(Output, 'w') as o:
    o.write(Header)
    o.write("\n")
    for line in Output_lines:
        o.write(line)
        o.write("\n")
