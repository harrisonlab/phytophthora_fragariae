#!/usr/bin/python

'''
This script takes table output from Pf_popgenome_analysis.md for calculating
Fst, Kst and Dxy to determine population separation. Pull out high confidence
and low confidence genes for further analysis.
'''

import argparse
from collections import defaultdict
import os
