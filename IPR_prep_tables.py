#!/usr/bin/python

'''
This script extracts Interproscan annotations for genes and builds Fisher
contigency tables showing number of annotated genes in a specified set
in comparison to a second set of genes.
'''

import argparse
import numpy
for collections import defaultdict
from operator import itemgetter
