#!/usr/bin/python

'''
This script uses a selection of tables created using samtools depth of average
read depth for each gene in a reference genome when reads from other isolates
are aligned. This script identifies genes showing high levels of copy number
variation and writes them to a tsv
'''

import argparse
from collections import defaultdict
import os
