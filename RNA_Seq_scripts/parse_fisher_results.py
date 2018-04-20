#!/usr/bin/python

'''
This script will analyse results from a Fishers Exact Test on enrichment
for RxLRs, CRNs, ApoplastP hits and combined Effectors vs the genome
With significance thresholds of: 0.1, 0.05, 0.01 and 0.001
'''

import argparse
from collections import defaultdict
import os
