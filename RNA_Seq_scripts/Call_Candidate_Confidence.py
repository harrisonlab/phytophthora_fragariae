#!/usr/bin/python

'''
This script takes outputs from Expression presence/absence and differently DEGs to create a sorted table of candidates with a score of 1-9, 9 being best
'''

import sys,argparse
from collections import defaultdict
from sets import Set
import os

ap = argparse.ArgumentParser()
