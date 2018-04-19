#!/usr/bin/python

'''
This script will count the number of RxLRs, CRNs, ApoplastP hits and combined
effector genes in a coexpressed module compared to and the rest of the genome
'''

import argparse
import numpy
from collections import defaultdict
import os

# -----------------------------------------------------
# Step 1
# Import variables and load input files
# -----------------------------------------------------
