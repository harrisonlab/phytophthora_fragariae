#Import modules

import numpy
import csv
import glob

#Import tsv into numpy

Orthology_tbl = numpy.loadtxt(fname="All_Strains_count_table.tsv", dtype=object, delimiter='\t', skiprows=1)

#Run calculations for UK1

hits = []

for row in Orthology_tbl:
    a = float(row[2] + row[6]) / 2
    b = float(row[1] + row[5] + row[3] + row[7] + row[9]) / 5
    if a > b and float(row[2]) > 0 and float(row[6]) > 0:
        hits.append(row[0])

print 'UK1'
print hits


#Run calculations for UK2

hits = []

for row in Orthology_tbl:
    a = float(row[1] + row[3]) / 2
    b = float(row[2] + row[5] + row[6] + row[7] + row[9]) / 5
    if a > b and row[1] > 0 and row[3] > 0:
        hits.append(row[0])

print 'UK2'
print hits

#Run calculations for UK3

hits = []

for row in Orthology_tbl:
    a = float(row[5] + row[7] + row[9]) / 3
    b = float(row[2] + row[1] + row[6] + row[3]) / 4
    if a > b and row[5] > 0 and row[7] > 0 and row[9] > 0:
        hits.append(row[0])

print 'UK3'
print hits
