#!/usr/bin/python

'''
Sometimes an ORF fragment is classified as an ApoplastP hit when the
overlapping Augustus gene is not. Prioritise the gene with an effector
prediction.
'''

import argparse
from collections import defaultdict
import os
