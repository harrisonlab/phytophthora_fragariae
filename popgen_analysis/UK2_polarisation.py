import argparse
import numpy
import csv
import glob

parser = argparse.ArgumentParser(description='Choose a tbl file to analyse')
parser.add_argument('tbl',required=True,type=str,help='tbl file to be analysed by script')
conf = parser.parse_args()
