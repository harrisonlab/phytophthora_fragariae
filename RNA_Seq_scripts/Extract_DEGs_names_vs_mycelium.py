#!/usr/bin/python

'''
This script uses the output of DeSeq2 to produce a list of genes that are differntially expressed only in a single isolate and add orthogroup ID for each gene. For aligning multiple isolates RNA to one reference.
'''

import sys,argparse
from collections import defaultdict
import json
from sets import Set
