#!/usr/bin/python

'''
This script uses an orthology group txt file output from OrthoMCL to create a count table for the number of genes per strain in each orthogroup
'''

from sets import Set
import sys,argparse
from collections import defaultdict
import re

#-----------------------------------------------------
# Step 1
# Import variables & load input files
#-----------------------------------------------------
