#!/usr/bin/python

'''
This script uses candidates identified by Call_Candidate_Confidence.py and
extracts details from tables created by pacbio_anntoation_tables_modified.py
or pacbio_anntoation_tables_modified_no_coexp.py depending on isolate examined
'''

import argparse
import os
from collections import defaultdict

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
# Load candidate file and create a list of candidate genes and their score
# -----------------------------------------------------

score_dict = defaultdict(float)
transcripts = []
candidates_file = conf.candidates
with open(candidates_file) as f:
    candidate_lines = f.readlines()[1:]
    for line in candidate_lines:
        split_line = line.split()
        transcript_ID = split_line[0]
        transcripts.append(transcript_ID)
        score = split_line[-1]
        score_dict[transcript_ID] = score

print("Candidate gene list loaded")

# -----------------------------------------------------
# Step 2
# Identify lines in annotation table to keep and add to list
# -----------------------------------------------------

Output_lines = []
annotation_table = conf.annotation_table
with open(annotation_table) as f:
    annotation_lines = f.readlines()
    annotation_set = set(annotation_lines)
    Header = annotation_lines[0]
    Header_split = Header.split()
    Header_split = Header_split.append("Score")
    Header = "\t".join(Header_split)
    for transcript_ID in transcripts:
        for annotation_line in annotation_set:
            if annotation_line.startswith(transcript_ID):
                score = score_dict[transcript_ID]
                annotation_split = annotation_line.split()
                annotation_split = annotation_split.append(score)
                Final_line = "\t".join(annotation_split)
                Output_lines.append(Final_line)

print("Lines of annotation table to keep identified")

# -----------------------------------------------------
# Step 3
# Write out lines to keep to TSV file
# -----------------------------------------------------

outfile = conf.out_file
cwd = os.getcwd()
Output = "/".join([cwd, outfile])

with open(Output, 'w') as o:
    o.write(Header)
    for line in Output_lines:
        o.write(line)

print("Output file created")
