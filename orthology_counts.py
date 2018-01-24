#Import modules

import numpy

#Import tsv into numpy

Orthology_tbl = numpy.loadtxt(fname="count_table.tsv", dtype=object, delimiter='\t', skiprows=1)

#Run calculations for UK1

hits = []

for row in Orthology_tbl:
    if float(row[2]) > float(row[1]) and float(row[2]) > float(row[3]) and float(row[2]) > float(row[5]) and float(row[2]) > float(row[7]) and float(row[2]) > float(row[9]) and float(row[6]) > float(row[1]) and float(row[6]) > float(row[3]) and float(row[6]) > float(row[5]) and float(row[6]) > float(row[7]) and float(row[6]) > float(row[9]) and float(row[2]) > 0 and float(row[6]) > 0:
        hits.append(row[0])

with open("UK1_expanded.txt", "w") as f:
    for o in hits:
        f.write(str(o) + '\n')

#Run calculations for UK2

hits = []

for row in Orthology_tbl:
    if float(row[1]) > float(row[2]) and float(row[1]) > float(row[5]) and float(row[1]) > float(row[6]) and float(row[1]) > float(row[7]) and float(row[1]) > float(row[9]) and float(row[3]) > float(row[2]) and float(row[3]) > float(row[5]) and float(row[3]) > float(row[6]) and float(row[3]) > float(row[7]) and float(row[3]) > float(row[9]) and float(row[1]) > 0 and float(row[3]) > 0:
        hits.append(row[0])

with open("UK2_expanded.txt", "w") as f:
    for o in hits:
        f.write(str(o) + '\n')

#Run calculations for UK3

hits = []

for row in Orthology_tbl:
    if float(row[5]) > float(row[1]) and float(row[5]) > float(row[2]) and float(row[5]) > float(row[3]) and float(row[5]) > float(row[6]) and float(row[7]) > float(row[1]) and float(row[7]) > float(row[2]) and float(row[7]) > float(row[3]) and float(row[7]) > float(row[6]) and float(row[9]) > float(row[1]) and float(row[9]) > float(row[2]) and float(row[9]) > float(row[3]) and float(row[9]) > float(row[6]) and float(row[5]) > 0 and float(row[7]) > 0 and float(row[9]) > 0:
        hits.append(row[0])

with open("UK3_expanded.txt", "w") as f:
    for o in hits:
        f.write(str(o) + '\n')
