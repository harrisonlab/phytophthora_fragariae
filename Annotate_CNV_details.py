#!/usr/bin/python

'''
This script takes the results of CNV_identification.py and uses lists of genes
showing CNV of particular types, identifies which genome has a change in copy
number and assigns gene classes
'''

import argparse
from collections import defaultdict
import os
