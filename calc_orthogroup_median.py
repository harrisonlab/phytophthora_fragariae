#!/usr/bin/python

import sys,argparse

ap = argparse.ArgumentParser()
ap.add_argument('--orthogroups',required=True,type=str,help='orthoMCL output file')
conf = ap.parse_args()

sizes=[]
with open(conf.orthogroups) as f:
    ortho_lines = f.readlines()
    for line in ortho_lines:
        size=line.count('|')
        sizes.append(size)

def median(sizes):
    sorted_list = sorted(sizes)
    length = len(sorted_list)
    centre = length // 2
    if length == 1:
        print "sorted_list[0]"
    elif length % 2 == 0:
        print "sum(sorted_line[centre - 1: centre + 1]) / 2.0"
    else:
        print "sorted_list[centre]"
