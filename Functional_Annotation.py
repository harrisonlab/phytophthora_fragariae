#!/usr/bin/python

'''
This script parses functional annotations from interproscan and swissprot.
Using gene lists of all genes and differentially expressed genes, it will output a table of functionally enriched annotations
'''

#-----------------------------------------------------
# Stage 1
# Import variables and load input files
#-----------------------------------------------------

import sys
import argparse
import re
from sets import Set
from collections import defaultdict
from operator import itemgetter
import numpy as np
