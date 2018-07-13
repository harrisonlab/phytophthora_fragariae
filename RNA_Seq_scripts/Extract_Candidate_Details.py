#!/usr/bin/python

'''
This script uses candidates identified by Call_Candidate_Confidence.py and
extracts details from tables created by pacbio_anntoation_tables_modified.py
or pacbio_anntoation_tables_modified_no_coexp.py depending on isolate examined
'''

import sys
import argparse
import os
