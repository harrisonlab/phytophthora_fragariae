#!/usr/bin/python

'''
This script will analyse results from each repetition of DREME and extract
motifs present in 90% of runs
'''

import argparse
from collections import defaultdict

# -----------------------------------------------------
# Step 1
# Import variables
# -----------------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument('--inputs', required=True, type=str, help='Lists of files \
from repeated runs of DREME')
ap.add_argument(--'output', required=True, type=str, help='Location to output \
results to')
conf = ap.parse_args()
