#Import modules

import numpy
import csv
import glob

#Import tsv into numpy

Othology_tbl = numpy.loadtxt(fname="All_Strains_count_table.tsv", dtype=object, delimiter='\t')
