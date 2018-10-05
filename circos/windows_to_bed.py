#!/usr/bin/python

'''
This script converts the 100kb windows gff for circos to bed format
'''

import argparse

ap = argparse.ArgumentParser()
ap.add_argument('--gff_in', required=True, type=str,
                help='Gff file to be converted to a bed file')
ap.add_argument('--out_dir', required=True, type=str,
                help='Output directory to write bed file to')
conf = ap.parse_args()

with open(conf.gff_in) as f:
    lines = f.readlines()
    for line in lines:
        split_line = line.split()
        contig = split_line[0]
        start = split_line[3]
        stop =  split_line[4]
        line_out = "\t".join([contig, start, stop])
        print(line_out)
