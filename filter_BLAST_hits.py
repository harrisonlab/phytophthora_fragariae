import numpy

results = numpy.loadtxt(fname=/home/adamst/blast_output/genome_vs_region.csv)

new_col = (float(my_data[:,6])/my_data[:,2])[...,None]

new_results = numpy.append(results, new_col, 1)
