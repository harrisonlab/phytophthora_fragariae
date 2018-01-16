#!/usr/bin/python

'''
This script uses the tsv file produced by parsing RNA-Seq with a previous python script to extract only DEGs above a certain threshold
'''

import sys,argparse
from collections import defaultdict

ap = argparse.ArgumentParser()
ap.add_argument('--input',required=True,type=str,help='tsv file of binary presence table of DEGs')
ap.add_argument('--output',reuqired=True,type=str,help='Output text file of gene names')
