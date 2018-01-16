#!/usr/bin/python

'''
This script uses the tsv file produced by parsing RNA-Seq with a previous python script to extract only DEGs above a certain threshold
'''

import sys,argparse
from collections import defaultdict
