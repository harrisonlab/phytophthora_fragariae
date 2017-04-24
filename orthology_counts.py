#Import modules

import numpy
import csv
import glob

#Import tsv into numpy

Orthology_tbl = numpy.loadtxt(fname="All_Strains_count_table.tsv", dtype=object, delimiter='\t')

#Run calculations for UK1

hits = []

for rows in Orthology_tbl:
    a = float(column[2] + column[6]) / 2
    b = float(column[1] + column[5] + column[3] + column[7] + column[9]) / 5
    if a > b:
        hits.append(column[0])

print 'UK1'
print hits


#Run calculations for UK2

hits = []

for rows in Orthology_tbl:
    a = float(column[1] + column[3]) / 2
    b = float(column[2] + column[5] + column[6] + column[7] + column[9]) / 5
    if a > b:
        hits.append(column[0])

print 'UK2'
print hits

#Run calculations for UK3

hits = []

for rows in Orthology_tbl:
    a = float(column[5] + column[7] + column[9]) / 3
    b = float(column[2] + column[1] + column[6] + column[3]) / 4
    if a > b:
        hits.append(column[0])

print 'UK3'
print hits
