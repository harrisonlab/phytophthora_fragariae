#!/usr/bin/python

'''
This script converts from samtools bedcov format to a circos friendly format
'''

#-----------------------------------------------------
# Step 1
# Import variables, input files and modules
#-----------------------------------------------------

import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('--cov_in',required=True,type=str,help='A file output from samtools bedcov')
ap.add_argument('--per_X_bp',required=False, default=1000, type=float, help='The number of bp over which you want to report the number of features eg. reads per 1000bp')

conf = ap.parse_args()
multiplier = conf.per_X_bp

with open(conf.cov_in) as f:
    cov_lines = f.readlines()

#-----------------------------------------------------
# Step 2
# Extract feature start and stop positions, and coverage
# per Kb and print before parsing into circos format.
#-----------------------------------------------------

for line in cov_lines:
    line = line.rstrip()
    split_line = line.split("\t")
    contig = split_line[0]
    start = split_line[1]
    stop = split_line[2]
    reads = float(split_line[6])
    lgth = float(stop) - float(start)
    # print (str(reads) + "\t" + str(lgth))
    reads_per_bp = np.divide(reads, lgth)
    # print(reads_per_bp)
    reads_per_kb = np.multiply(reads_per_bp, multiplier)
    reads_per_kb = int(np.round_(reads_per_kb, decimals=0,out=None))
    feature = "\t".join([str(contig), str(start), str(stop), str(reads_per_kb)])
    print(feature)
