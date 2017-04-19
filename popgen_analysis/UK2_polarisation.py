#Import modues

import argparse
import numpy
import csv
import glob

#Import arguments

parser = argparse.ArgumentParser(description='Choose a tbl file to analyse')
parser.add_argument('--tbl',required=True,type=str,help='tbl file to be analysed by script')
conf = parser.parse_args()

#Import dataset to numpy

Inital_tbl = numpy.loadtxt(fname="conf.tbl", dtype=object)

#Cut down table to give equal variants

tbl2 = numpy.where(Inital_tbl[:,7] == Inital_tbl[:,5])
tbl3 = numpy.where(tbl2[:,7] == tbl2[:,12])
tbl4 = numpy.where(tbl3[:,7] == tbl3[:,13])
tbl5 = numpy.where(tbl4[:,7] == tbl4[:,14])

#Further cut down for different variants

tbl
