import numpy
import csv

results = numpy.loadtxt(fname="genome_vs_region_hits.tbl", dtype=object)

new_col = []

for row in results:
    value_a = float(row[3])
    value_b = float(row[13])
    new_col.append(value_a / value_b)

new_results = numpy.append(results, new_col, 1)

w1 = numpy.where((new_results[:,0]) and ((new_results[:,14] > 0.5) or (new_results[:,14] == 0.5)))

filtered_results = new_results[:, w1]

with open("filtered_contigs.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(filtered_results)

filtered_results.shape

names ="ID,Sequence,Sequence_lgth,No_hits,Hit,E-value,Hit_lgth,Per_length,Per_ID,Hit_strand,Hit_start,Hit_end,Hit_seq"
