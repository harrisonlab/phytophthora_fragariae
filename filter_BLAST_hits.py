import numpy
import csv

results = numpy.loadtxt(fname="genome_vs_region.csv", dtype=str, delimiter=",", skiprows=1)

new_col = (float(my_data[:,6])/float(my_data[:,2]))[...,None]

new_results = numpy.append(results, new_col, 1)

w1 = numpy.where((new_results[0,:]) and ((new_results[13,:] > 0.5) or (new_results[13,:] == 0.5)))

filtered_results = new_results[:, w1]

with open("filtered_contigs.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(filtered_results)

filtered_results.shape
