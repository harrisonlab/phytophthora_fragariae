#!/usr/bin/python

'''
This script renames header files of predicted effectors (and secreted etc.)
that were used to create final GFFs, in order to match gene names submitted to
NCBI
'''

from collections import defaultdict
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('--Feature_File', type=str, required=True, help='File \
containing predictions of effector genes from older analyses')
ap.add_argument('--Conversion_File', type=str, required=True, help='File \
containing old and new gene IDs')
ap.add_argument('--Out_File', type=str, required=True, help='File for new gene \
names predicted as specific effector type')
