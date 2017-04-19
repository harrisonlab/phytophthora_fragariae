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

tbl6 = numpy.where(tbl5[:,7] != tbl5[:,6])
tbl7 = numpy.where(tbl6[:,7] != tbl6[:,8])
tbl8 = numpy.where(tbl7[:,7] != tbl7[:,9])
tbl9 = numpy.where(tbl8[:,7] != tbl8[:,10])
tbl10 = numpy.where(tbl9[:,7] != tbl9[:,11])

#Print resulting table to a .csv

with open("UK2_polarisation.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(tbl10)
