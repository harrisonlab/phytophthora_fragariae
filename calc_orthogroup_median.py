#!/usr/bin/python

import sys,argparse
import statistics

ap = argparse.ArgumentParser()
ap.add_argument('--orthogroups',required=True,type=str,help='orthoMCL output file')
conf = ap.parse_args()

sizes=[]
with open(conf.orthogroups) as f:
    ortho_lines = f.readlines()
    for line in ortho_lines:
        size=line.count('|')
        sizes.append(size)

median=statistics.median(sizes)
print "median"
