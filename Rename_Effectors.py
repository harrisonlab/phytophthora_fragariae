#!/usr/bin/python

'''
This script renames header files of predicted effectors (and secreted etc.)
that were used to create final GFFs, in order to match gene names submitted to
NCBI
'''

from collections import defaultdict
import os
import argparse
