#Import modues

import numpy
import csv
import glob

#Import dataset to numpy

Inital_tbl = numpy.loadtxt(fname="Parsed_Polarising_95m_contigs_unmasked.tbl", dtype=object)

#Cut down table to give equal variants

tbl2 = Inital_tbl[Inital_tbl[:,7] == Inital_tbl[:,5]]
tbl3 = tbl2[tbl2[:,7] == tbl2[:,12]]
tbl4 = tbl3[tbl3[:,7] == tbl3[:,13]]
tbl5 = tbl4[tbl4[:,7] == tbl4[:,14]]

#Further cut down for different variants

tbl6 = tbl5[tbl5[:,7] != tbl5[:,6]]
tbl7 = tbl6[tbl6[:,7] != tbl6[:,8]]
tbl8 = tbl7[tbl7[:,7] != tbl7[:,9]]
tbl9 = tbl8[tbl8[:,7] != tbl8[:,10]]
tbl10 = tbl9[tbl9[:,7] != tbl9[:,11]]

#Print resulting table to a .csv

with open("UK2_polarisation.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(tbl2)
