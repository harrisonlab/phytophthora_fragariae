import numpy
import csv

results = numpy.loadtxt(fname="genome_vs_region_hits.tbl", dtype=object)

new_col_list = []

for row in results:
    value_a = float(row[3])
    value_b = float(row[14])
    new_col_list.append(value_a / value_b)

new_col_int = numpy.array(new_col_list)
new_col = numpy.reshape(new_col_int, (33685, 1))
# this reshaping command MUST be changed depending on the dimensions
# of the BLAST hits dataset.

new_results = numpy.append(results, new_col, 1)

w = numpy.where((new_results[:, 15] > 0.25) | (new_results[:, 15] == 0.25))[0]
# The value can be changed by preference.
# Only bitwise logical operators may be used.

filtered_results = new_results[w, :]

with open("filtered_contigs.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(filtered_results)
