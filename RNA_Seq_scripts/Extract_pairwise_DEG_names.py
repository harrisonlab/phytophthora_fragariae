#!/usr/bin/python

'''
This script uses the output of DeSeq2 to produce a list of genes that are
differentially expressed only in a single isolate and add orthogroup ID for
each gene. Only works for three isolates.
'''

import argparse
from collections import defaultdict
import os

ap = argparse.ArgumentParser()
ap.add_argument('--DEG_files', required=True, nargs='+', type=str,
                help='space spererated list of files containing DEG \
                information')
ap.add_argument('--Orthogroup_in', required=True, type=str,
                help='text output file of Orthogroups from OrthoFinder')
ap.add_argument('--Reference_name', required=True, type=str,
                help='Name of organism gene IDs are from in DEG input file')
ap.add_argument('--Min_LFC', required=True, type=float,
                help='Minimum log fold change for a gene to be called a DEG')
ap.add_argument('--Sig_Level', required=True, type=float,
                help='Minimum p-value for a DEG to be considered significant')
ap.add_argument('--Organism_1', required=True, type=str,
                help='Name of isolate 1, three timepoints')
ap.add_argument('--Organism_2', required=True, type=str,
                help='Name of isolate 2, one timepoint')
ap.add_argument('--Organism_3', required=True, type=str,
                help='Name of isolate 3, one timepoint')
ap.add_argument('--OutDir', required=True, type=str,
                help='Directory to write output files to')
ap.add_argument('--RxLRs', required=True, type=str,
                help='File of all RxLR names for aligned genome')
ap.add_argument('--CRNs', required=True, type=str,
                help='File of all CRN names for aligned genome')
ap.add_argument('--ApoP', required=True, type=str,
                help='File of all hits from ApoplastP')
ap.add_argument('--Secreted_CQ', required=True, type=str,
                help='File of all secreted gene models')
ap.add_argument('--Secreted_ORF', required=True, type=str,
                help='File of all secreted ORF fragments')
ap.add_argument('--TFs', required=True, type=str,
                help='File of IDs of TFs/TRs')
conf = ap.parse_args()

# -----------------------------------------------------
# Step 1
# Load input files
# -----------------------------------------------------

LFC = conf.Min_LFC
Sig_Level = conf.Sig_Level

DEG_files = conf.DEG_files
DEG_list = []
LFC_values = defaultdict(float)
P_values = defaultdict(float)
for DEG_file in DEG_files:
    with open(DEG_file) as f:
        filename = DEG_file
        DEG_lines = f.readlines()
        for line in DEG_lines:
            if line.startswith('baseMean'):
                continue
            else:
                split_line = line.split()
                gene_name = split_line[0]
                log_change = float(split_line[2])
                P_val = float(split_line[6])
                if abs(log_change) >= LFC and P_val <= Sig_Level:
                    entryname = "-".join([filename, gene_name])
                    DEG_list.append(entryname)
                    LFC_values[entryname] = log_change
                    P_values[entryname] = P_val

with open(conf.Orthogroup_in) as f:
    Ortho_lines = f.readlines()

reference_name = conf.Reference_name
ortho_dict = defaultdict(str)
for line in Ortho_lines:
    line = line.rstrip()
    split_line = line.split()
    orthogroup = split_line[0]
    orthogroup = orthogroup.replace(":", "")
    genes_in_group = [x for x in split_line if reference_name in x]
    for gene in genes_in_group:
        gene = gene.replace(reference_name, '').replace('|', '')
        ortho_dict[gene] = orthogroup

Org1 = conf.Organism_1
Org2 = conf.Organism_2
Org3 = conf.Organism_3

OutDir = conf.OutDir

cwd = os.getcwd()

print("Input files loaded")

# -----------------------------------------------------
# Step 2
# Create sets for pairwise comaprisons
# -----------------------------------------------------

# Organism1 vs Organism2
Org1_vs_Org2 = []
Org1_vs_Org2_LFC = defaultdict(list)
Org1_vs_Org2_Pval = defaultdict(list)

for item in DEG_list:
    if item.split('/')[-1].split('_')[0] == Org1 and \
            item.split('/')[-1].split('_')[3] == Org2 and \
            item.split('/')[-1].split('_')[5].split('-')[0] == "up.txt":
        transcript_id = item.split('/')[-1].split('-')[1]
        Org1_vs_Org2.append(transcript_id)
        Org1_vs_Org2_LFC[transcript_id].append(LFC_values[item])
        Org1_vs_Org2_Pval[transcript_id].append(P_values[item])
    elif item.split('/')[-1].split('_')[0].split('-')[0] == Org2 and \
            item.split('/')[-1].split('_')[3] == Org1 and \
            item.split('/')[-1].split('_')[5] == "down.txt":
        transcript_id = item.split('/')[-1].split('-')[1]
        Org1_vs_Org2.append(transcript_id)
        Org1_vs_Org2_LFC[transcript_id].append(LFC_values[item])
        Org1_vs_Org2_Pval[transcript_id].append(P_values[item])

Org1_vs_Org2_set = set(Org1_vs_Org2)

# Organism1 vs Organism3
Org1_vs_Org3 = []
Org1_vs_Org3_LFC = defaultdict(list)
Org1_vs_Org3_Pval = defaultdict(list)

for item in DEG_list:
    if item.split('/')[-1].split('_')[0] == Org1 and \
            item.split('/')[-1].split('_')[3] == Org3 and \
            item.split('/')[-1].split('_')[5].split('-')[0] == "up.txt":
        transcript_id = item.split('/')[-1].split('-')[1]
        Org1_vs_Org3.append(transcript_id)
        Org1_vs_Org3_LFC[transcript_id].append(LFC_values[item])
        Org1_vs_Org3_Pval[transcript_id].append(P_values[item])
    elif item.split('/')[-1].split('_')[0].split('-')[0] == Org3 and \
            item.split('/')[-1].split('_')[3] == Org1 and \
            item.split('/')[-1].split('_')[5] == "down.txt":
        transcript_id = item.split('/')[-1].split('-')[1]
        Org1_vs_Org3.append(transcript_id)
        Org1_vs_Org3_LFC[transcript_id].append(LFC_values[item])
        Org1_vs_Org3_Pval[transcript_id].append(P_values[item])

Org1_vs_Org3_set = set(Org1_vs_Org3)

# Organism2 vs Organism1
Org2_vs_Org1 = []
Org2_vs_Org1_LFC = defaultdict(list)
Org2_vs_Org1_Pval = defaultdict(list)

for item in DEG_list:
    if item.split('/')[-1].split('_')[0] == Org2 and \
            item.split('/')[-1].split('_')[3] == Org1 and \
            item.split('/')[-1].split('_')[5].split('-')[0] == "up.txt":
        transcript_id = item.split('/')[-1].split('-')[1]
        Org2_vs_Org1.append(transcript_id)
        Org2_vs_Org1_LFC[transcript_id].append(LFC_values[item])
        Org2_vs_Org1_Pval[transcript_id].append(P_values[item])
    elif item.split('/')[-1].split('_')[0] == Org1 and \
            item.split('/')[-1].split('_')[3] == Org2 and \
            item.split('/')[-1].split('_')[5].split('-')[0] == "down.txt":
        transcript_id = item.split('/')[-1].split('-')[1]
        Org2_vs_Org1.append(transcript_id)
        Org2_vs_Org1_LFC[transcript_id].append(LFC_values[item])
        Org2_vs_Org1_Pval[transcript_id].append(P_values[item])

Org2_vs_Org1_set = set(Org2_vs_Org1)

# Organism2 vs Organism3
Org2_vs_Org3 = []
Org2_vs_Org3_LFC = defaultdict(list)
Org2_vs_Org3_Pval = defaultdict(list)

for item in DEG_list:
    if item.split('/')[-1].split('_')[0] == Org2 and \
            item.split('/')[-1].split('_')[3] == Org3 and \
            item.split('/')[-1].split('_')[5].split('-')[0] == "up.txt":
        transcript_id = item.split('/')[-1].split('-')[1]
        Org2_vs_Org3.append(transcript_id)
        Org2_vs_Org3_LFC[transcript_id].append(LFC_values[item])
        Org2_vs_Org3_Pval[transcript_id].append(P_values[item])
    elif item.split('/')[-1].split('_')[0] == Org3 and \
            item.split('/')[-1].split('_')[3] == Org2 and \
            item.split('/')[-1].split('_')[5].split('-')[0] == "down.txt":
        transcript_id = item.split('/')[-1].split('-')[1]
        Org2_vs_Org3.append(transcript_id)
        Org2_vs_Org3_LFC[transcript_id].append(LFC_values[item])
        Org2_vs_Org3_Pval[transcript_id].append(P_values[item])

Org2_vs_Org3_set = set(Org2_vs_Org3)

# Organism3 vs Organism1
Org3_vs_Org1 = []
Org3_vs_Org1_LFC = defaultdict(list)
Org3_vs_Org1_Pval = defaultdict(list)

for item in DEG_list:
    if item.split('/')[-1].split('_')[0] == Org3 and \
            item.split('/')[-1].split('_')[3] == Org1 and \
            item.split('/')[-1].split('_')[5].split('-')[0] == "up.txt":
        transcript_id = item.split('/')[-1].split('-')[1]
        Org3_vs_Org1.append(transcript_id)
        Org3_vs_Org1_LFC[transcript_id].append(LFC_values[item])
        Org3_vs_Org1_Pval[transcript_id].append(P_values[item])
    elif item.split('/')[-1].split('_')[0] == Org1 and \
            item.split('/')[-1].split('_')[3] == Org3 and \
            item.split('/')[-1].split('_')[5].split('-')[0] == "down.txt":
        transcript_id = item.split('/')[-1].split('-')[1]
        Org3_vs_Org1.append(transcript_id)
        Org3_vs_Org1_LFC[transcript_id].append(LFC_values[item])
        Org3_vs_Org1_Pval[transcript_id].append(P_values[item])

Org3_vs_Org1_set = set(Org3_vs_Org1)

# Organism3 vs Organism2
Org3_vs_Org2 = []
Org3_vs_Org2_LFC = defaultdict(list)
Org3_vs_Org2_Pval = defaultdict(list)

for item in DEG_list:
    if item.split('/')[-1].split('_')[0] == Org3 and \
            item.split('/')[-1].split('_')[3] == Org2 and \
            item.split('/')[-1].split('_')[5].split('-')[0] == "up.txt":
        transcript_id = item.split('/')[-1].split('-')[1]
        Org3_vs_Org2.append(transcript_id)
        Org3_vs_Org2_LFC[transcript_id].append(LFC_values[item])
        Org3_vs_Org2_Pval[transcript_id].append(P_values[item])
    elif item.split('/')[-1].split('_')[0] == Org2 and \
            item.split('/')[-1].split('_')[3] == Org3 and \
            item.split('/')[-1].split('_')[5].split('-')[0] == "down.txt":
        transcript_id = item.split('/')[-1].split('-')[1]
        Org3_vs_Org2.append(transcript_id)
        Org3_vs_Org2_LFC[transcript_id].append(LFC_values[item])
        Org3_vs_Org2_Pval[transcript_id].append(P_values[item])

Org3_vs_Org2_set = set(Org3_vs_Org2)

print("Sets of pairwise comparisons created")

# -----------------------------------------------------
# Step 3
# Create unique sets for DEGs of each isolate
# -----------------------------------------------------

Org1_uniq = []
Org2_uniq = []
Org3_uniq = []

for transcript in Org1_vs_Org2_set:
    if transcript in Org1_vs_Org3_set:
        if transcript not in Org2_vs_Org1_set:
            if transcript not in Org3_vs_Org1_set:
                Org1_uniq.append(transcript)

for transcript in Org2_vs_Org1_set:
    if transcript in Org2_vs_Org3_set:
        if transcript not in Org1_vs_Org2_set:
            if transcript not in Org3_vs_Org2_set:
                Org2_uniq.append(transcript)

for transcript in Org3_vs_Org1_set:
    if transcript in Org3_vs_Org2_set:
        if transcript not in Org1_vs_Org3_set:
            if transcript not in Org2_vs_Org3_set:
                Org3_uniq.append(transcript)

Org1_uniq_set = set(Org1_uniq)
Org2_uniq_set = set(Org2_uniq)
Org3_uniq_set = set(Org3_uniq)

print("Unique sets for each organism created")

# -----------------------------------------------------
# Step 4
# Write out text files for all genes that are uniquely differentially expressed
# -----------------------------------------------------

Org1_file = "_".join([reference_name, Org1, "unique_DEGs.txt"])
Org2_file = "_".join([reference_name, Org2, "unique_DEGs.txt"])
Org3_file = "_".join([reference_name, Org3, "unique_DEGs.txt"])

Org1_out = "/".join([cwd, OutDir, "all_genes", Org1_file])
Org2_out = "/".join([cwd, OutDir, "all_genes", Org2_file])
Org3_out = "/".join([cwd, OutDir, "all_genes", Org3_file])

LFC1 = "_".join(["LFC", Org1])
LFC2 = "_".join(["LFC", Org2])
LFC3 = "_".join(["LFC", Org3])
PV1 = "_".join(["P-value", "adjusted", Org1])
PV2 = "_".join(["P-value", "adjusted", Org2])
PV3 = "_".join(["P-value", "adjusted", Org3])

Header_Org1 = "\t".join(["Gene_ID", "Orthogroup", LFC2, PV2, LFC3, PV3])
Header_Org2 = "\t".join(["Gene_ID", "Orthogroup", LFC1, PV1, LFC3, PV3])
Header_Org3 = "\t".join(["Gene_ID", "Orthogroup", LFC1, PV1, LFC2, PV2])

with open(Org1_out, 'w') as o:
    o.write(Header_Org1)
    o.write("\n")
    for transcript in Org1_uniq_set:
        orthogroup = ortho_dict[transcript]
        LFC2 = str(Org1_vs_Org2_LFC[transcript])
        LFC2 = LFC2.replace("[", "")
        LFC2 = LFC2.replace("]", "")
        PV2 = str(Org1_vs_Org2_Pval[transcript])
        PV2 = PV2.replace("[", "")
        PV2 = PV2.replace("]", "")
        LFC3 = str(Org1_vs_Org3_LFC[transcript])
        LFC3 = LFC3.replace("[", "")
        LFC3 = LFC3.replace("]", "")
        PV3 = str(Org1_vs_Org3_Pval[transcript])
        PV3 = PV3.replace("[", "")
        PV3 = PV3.replace("]", "")
        output = "\t".join([transcript, orthogroup, LFC2, PV2, LFC3, PV3])
        o.write(output)
        o.write("\n")

with open(Org2_out, 'w') as o:
    o.write(Header_Org2)
    o.write("\n")
    for transcript in Org2_uniq_set:
        orthogroup = ortho_dict[transcript]
        LFC1 = str(Org2_vs_Org1_LFC[transcript])
        LFC1 = LFC1.replace("[", "")
        LFC1 = LFC1.replace("]", "")
        PV1 = str(Org2_vs_Org1_Pval[transcript])
        PV1 = PV1.replace("[", "")
        PV1 = PV1.replace("]", "")
        LFC3 = str(Org2_vs_Org3_LFC[transcript])
        LFC3 = LFC3.replace("[", "")
        LFC3 = LFC3.replace("]", "")
        PV3 = str(Org2_vs_Org3_Pval[transcript])
        PV3 = PV3.replace("[", "")
        PV3 = PV3.replace("]", "")
        output = "\t".join([transcript, orthogroup, LFC1, PV1, LFC3, PV3])
        o.write(output)
        o.write("\n")

with open(Org3_out, 'w') as o:
    o.write(Header_Org3)
    o.write("\n")
    for transcript in Org3_uniq_set:
        orthogroup = ortho_dict[transcript]
        LFC2 = str(Org3_vs_Org2_LFC[transcript])
        LFC2 = LFC2.replace("[", "")
        LFC2 = LFC2.replace("]", "")
        PV2 = str(Org3_vs_Org2_Pval[transcript])
        PV2 = PV2.replace("[", "")
        PV2 = PV2.replace("]", "")
        LFC1 = str(Org3_vs_Org1_LFC[transcript])
        LFC1 = LFC1.replace("[", "")
        LFC1 = LFC1.replace("]", "")
        PV1 = str(Org3_vs_Org1_Pval[transcript])
        PV1 = PV1.replace("[", "")
        PV1 = PV1.replace("]", "")
        output = "\t".join([transcript, orthogroup, LFC1, PV1, LFC2, PV2])
        o.write(output)
        o.write("\n")

print("Output files for all genes written")

# -----------------------------------------------------
# Step 5
# Identify RxLRs that are uniquely differentially expressed
# -----------------------------------------------------

with open(conf.RxLRs) as f:
    RxLRs = []
    RxLR_lines = f.readlines()
    for line in RxLR_lines:
        ID = line.rstrip()
        if "contig" in ID:
            ID = ".".join([ID, "t1"])
        RxLRs.append(ID)

RxLR_set = set(RxLRs)
Isolate1_RxLRs = []
Isolate2_RxLRs = []
Isolate3_RxLRs = []

for transcript in Org1_uniq_set:
    if transcript in RxLR_set:
        Isolate1_RxLRs.append(transcript)

for transcript in Org2_uniq_set:
    if transcript in RxLR_set:
        Isolate2_RxLRs.append(transcript)

for transcript in Org3_uniq_set:
    if transcript in RxLR_set:
        Isolate3_RxLRs.append(transcript)

print("Uniquely differentially expressed RxLRs identified")

# -----------------------------------------------------
# Step 6
# Write all uniquely differentially expressed RxLRs to text file
# -----------------------------------------------------

Org1_file = "_".join([reference_name, Org1, "unique_DEGs_RxLRs.txt"])
Org2_file = "_".join([reference_name, Org2, "unique_DEGs_RxLRs.txt"])
Org3_file = "_".join([reference_name, Org3, "unique_DEGs_RxLRs.txt"])

Org1_out = "/".join([cwd, OutDir, "RxLRs", Org1_file])
Org2_out = "/".join([cwd, OutDir, "RxLRs", Org2_file])
Org3_out = "/".join([cwd, OutDir, "RxLRs", Org3_file])

with open(Org1_out, 'w') as o:
    o.write(Header_Org1)
    o.write("\n")
    for transcript in Isolate1_RxLRs:
        orthogroup = ortho_dict[transcript]
        LFC2 = str(Org1_vs_Org2_LFC[transcript])
        LFC2 = LFC2.replace("[", "")
        LFC2 = LFC2.replace("]", "")
        PV2 = str(Org1_vs_Org2_Pval[transcript])
        PV2 = PV2.replace("[", "")
        PV2 = PV2.replace("]", "")
        LFC3 = str(Org1_vs_Org3_LFC[transcript])
        LFC3 = LFC3.replace("[", "")
        LFC3 = LFC3.replace("]", "")
        PV3 = str(Org1_vs_Org3_Pval[transcript])
        PV3 = PV3.replace("[", "")
        PV3 = PV3.replace("]", "")
        output = "\t".join([transcript, orthogroup, LFC2, PV2, LFC3, PV3])
        o.write(output)
        o.write("\n")

with open(Org2_out, 'w') as o:
    o.write(Header_Org2)
    o.write("\n")
    for transcript in Isolate2_RxLRs:
        orthogroup = ortho_dict[transcript]
        LFC1 = str(Org2_vs_Org1_LFC[transcript])
        LFC1 = LFC1.replace("[", "")
        LFC1 = LFC1.replace("]", "")
        PV1 = str(Org2_vs_Org1_Pval[transcript])
        PV1 = PV1.replace("[", "")
        PV1 = PV1.replace("]", "")
        LFC3 = str(Org2_vs_Org3_LFC[transcript])
        LFC3 = LFC3.replace("[", "")
        LFC3 = LFC3.replace("]", "")
        PV3 = str(Org2_vs_Org3_Pval[transcript])
        PV3 = PV3.replace("[", "")
        PV3 = PV3.replace("]", "")
        output = "\t".join([transcript, orthogroup, LFC1, PV1, LFC3, PV3])
        o.write(output)
        o.write("\n")

with open(Org3_out, 'w') as o:
    o.write(Header_Org3)
    o.write("\n")
    for transcript in Isolate3_RxLRs:
        orthogroup = ortho_dict[transcript]
        LFC2 = str(Org3_vs_Org1_LFC[transcript])
        LFC2 = LFC2.replace("[", "")
        LFC2 = LFC2.replace("]", "")
        PV2 = str(Org3_vs_Org1_Pval[transcript])
        PV2 = PV2.replace("[", "")
        PV2 = PV2.replace("]", "")
        LFC3 = str(Org3_vs_Org2_LFC[transcript])
        LFC3 = LFC3.replace("[", "")
        LFC3 = LFC3.replace("]", "")
        PV3 = str(Org3_vs_Org2_Pval[transcript])
        PV3 = PV3.replace("[", "")
        PV3 = PV3.replace("]", "")
        output = "\t".join([transcript, orthogroup, LFC1, PV1, LFC2, PV2])
        o.write(output)
        o.write("\n")

print("Uniquely differentially expressed RxLRs written to text file")

# -----------------------------------------------------
# Step 7
# Identify CRNs that are uniquely differentially expressed
# -----------------------------------------------------

with open(conf.CRNs) as f:
    CRNs = []
    CRN_lines = f.readlines()
    for line in CRN_lines:
        ID = line.rstrip()
        if "contig" in ID:
            ID = ".".join([ID, "t1"])
        CRNs.append(ID)

CRN_set = set(CRNs)
Isolate1_CRNs = []
Isolate2_CRNs = []
Isolate3_CRNs = []

for transcript in Org1_uniq_set:
    if transcript in CRN_set:
        Isolate1_CRNs.append(transcript)

for transcript in Org2_uniq_set:
    if transcript in CRN_set:
        Isolate2_CRNs.append(transcript)

for transcript in Org3_uniq_set:
    if transcript in CRN_set:
        Isolate3_CRNs.append(transcript)

print("Uniquely differentially expressed CRNs identified")

# -----------------------------------------------------
# Step 8
# Write all uniquely differentially expressed CRNs to text file
# -----------------------------------------------------

Org1_file = "_".join([reference_name, Org1, "unique_DEGs_CRNs.txt"])
Org2_file = "_".join([reference_name, Org2, "unique_DEGs_CRNs.txt"])
Org3_file = "_".join([reference_name, Org3, "unique_DEGs_CRNs.txt"])

Org1_out = "/".join([cwd, OutDir, "CRNs", Org1_file])
Org2_out = "/".join([cwd, OutDir, "CRNs", Org2_file])
Org3_out = "/".join([cwd, OutDir, "CRNs", Org3_file])

with open(Org1_out, 'w') as o:
    o.write(Header_Org1)
    o.write("\n")
    for transcript in Isolate1_CRNs:
        orthogroup = ortho_dict[transcript]
        LFC2 = str(Org1_vs_Org2_LFC[transcript])
        LFC2 = LFC2.replace("[", "")
        LFC2 = LFC2.replace("]", "")
        PV2 = str(Org1_vs_Org2_Pval[transcript])
        PV2 = PV2.replace("[", "")
        PV2 = PV2.replace("]", "")
        LFC3 = str(Org1_vs_Org3_LFC[transcript])
        LFC3 = LFC3.replace("[", "")
        LFC3 = LFC3.replace("]", "")
        PV3 = str(Org1_vs_Org3_Pval[transcript])
        PV3 = PV3.replace("[", "")
        PV3 = PV3.replace("]", "")
        output = "\t".join([transcript, orthogroup, LFC2, PV2, LFC3, PV3])
        o.write(output)
        o.write("\n")

with open(Org2_out, 'w') as o:
    o.write(Header_Org2)
    o.write("\n")
    for transcript in Isolate2_CRNs:
        orthogroup = ortho_dict[transcript]
        LFC1 = str(Org2_vs_Org1_LFC[transcript])
        LFC1 = LFC1.replace("[", "")
        LFC1 = LFC1.replace("]", "")
        PV1 = str(Org2_vs_Org1_Pval[transcript])
        PV1 = PV1.replace("[", "")
        PV1 = PV1.replace("]", "")
        LFC3 = str(Org2_vs_Org3_LFC[transcript])
        LFC3 = LFC3.replace("[", "")
        LFC3 = LFC3.replace("]", "")
        PV3 = str(Org2_vs_Org3_Pval[transcript])
        PV3 = PV3.replace("[", "")
        PV3 = PV3.replace("]", "")
        output = "\t".join([transcript, orthogroup, LFC1, PV1, LFC3, PV3])
        o.write(output)
        o.write("\n")

with open(Org3_out, 'w') as o:
    o.write(Header_Org3)
    o.write("\n")
    for transcript in Isolate3_CRNs:
        orthogroup = ortho_dict[transcript]
        LFC2 = str(Org3_vs_Org1_LFC[transcript])
        LFC2 = LFC2.replace("[", "")
        LFC2 = LFC2.replace("]", "")
        PV2 = str(Org3_vs_Org1_Pval[transcript])
        PV2 = PV2.replace("[", "")
        PV2 = PV2.replace("]", "")
        LFC3 = str(Org3_vs_Org2_LFC[transcript])
        LFC3 = LFC3.replace("[", "")
        LFC3 = LFC3.replace("]", "")
        PV3 = str(Org3_vs_Org2_Pval[transcript])
        PV3 = PV3.replace("[", "")
        PV3 = PV3.replace("]", "")
        output = "\t".join([transcript, orthogroup, LFC1, PV1, LFC2, PV2])
        o.write(output)
        o.write("\n")

print("Uniquely differentially expressed CRNs written to text file")

# -----------------------------------------------------
# Step 9
# Identify Apoplastic effectors that are uniquely differentially expressed
# -----------------------------------------------------

with open(conf.ApoP) as f:
    ApoP = []
    ApoP_lines = f.readlines()
    for line in ApoP_lines:
        if "contig" in ID:
            ID = ".".join([ID, "t1"])
        ID = line.rstrip()
        ApoP.append(ID)

ApoP_set = set(ApoP)
Isolate1_ApoP = []
Isolate2_ApoP = []
Isolate3_ApoP = []

for transcript in Org1_uniq_set:
    if transcript in ApoP_set:
        Isolate1_ApoP.append(transcript)

for transcript in Org2_uniq_set:
    if transcript in ApoP_set:
        Isolate2_ApoP.append(transcript)

for transcript in Org3_uniq_set:
    if transcript in ApoP_set:
        Isolate3_ApoP.append(transcript)

print("Uniquely differentially expressed Apoplastic effectors identified")

# -----------------------------------------------------
# Step 10
# Write all uniquely differentially expressed Apoplastic effectors to text file
# -----------------------------------------------------

Org1_file = "_".join([reference_name, Org1, "unique_DEGs_ApoP.txt"])
Org2_file = "_".join([reference_name, Org2, "unique_DEGs_ApoP.txt"])
Org3_file = "_".join([reference_name, Org3, "unique_DEGs_ApoP.txt"])

Org1_out = "/".join([cwd, OutDir, "ApoP", Org1_file])
Org2_out = "/".join([cwd, OutDir, "ApoP", Org2_file])
Org3_out = "/".join([cwd, OutDir, "ApoP", Org3_file])

with open(Org1_out, 'w') as o:
    o.write(Header_Org1)
    o.write("\n")
    for transcript in Isolate1_ApoP:
        orthogroup = ortho_dict[transcript]
        LFC2 = str(Org1_vs_Org2_LFC[transcript])
        LFC2 = LFC2.replace("[", "")
        LFC2 = LFC2.replace("]", "")
        PV2 = str(Org1_vs_Org2_Pval[transcript])
        PV2 = PV2.replace("[", "")
        PV2 = PV2.replace("]", "")
        LFC3 = str(Org1_vs_Org3_LFC[transcript])
        LFC3 = LFC3.replace("[", "")
        LFC3 = LFC3.replace("]", "")
        PV3 = str(Org1_vs_Org3_Pval[transcript])
        PV3 = PV3.replace("[", "")
        PV3 = PV3.replace("]", "")
        output = "\t".join([transcript, orthogroup, LFC2, PV2, LFC3, PV3])
        o.write(output)
        o.write("\n")

with open(Org2_out, 'w') as o:
    o.write(Header_Org2)
    o.write("\n")
    for transcript in Isolate2_ApoP:
        orthogroup = ortho_dict[transcript]
        LFC1 = str(Org2_vs_Org1_LFC[transcript])
        LFC1 = LFC1.replace("[", "")
        LFC1 = LFC1.replace("]", "")
        PV1 = str(Org2_vs_Org1_Pval[transcript])
        PV1 = PV1.replace("[", "")
        PV1 = PV1.replace("]", "")
        LFC3 = str(Org2_vs_Org3_LFC[transcript])
        LFC3 = LFC3.replace("[", "")
        LFC3 = LFC3.replace("]", "")
        PV3 = str(Org2_vs_Org3_Pval[transcript])
        PV3 = PV3.replace("[", "")
        PV3 = PV3.replace("]", "")
        output = "\t".join([transcript, orthogroup, LFC1, PV1, LFC3, PV3])
        o.write(output)
        o.write("\n")

with open(Org3_out, 'w') as o:
    o.write(Header_Org3)
    o.write("\n")
    for transcript in Isolate3_ApoP:
        orthogroup = ortho_dict[transcript]
        LFC2 = str(Org3_vs_Org1_LFC[transcript])
        LFC2 = LFC2.replace("[", "")
        LFC2 = LFC2.replace("]", "")
        PV2 = str(Org3_vs_Org1_Pval[transcript])
        PV2 = PV2.replace("[", "")
        PV2 = PV2.replace("]", "")
        LFC3 = str(Org3_vs_Org2_LFC[transcript])
        LFC3 = LFC3.replace("[", "")
        LFC3 = LFC3.replace("]", "")
        PV3 = str(Org3_vs_Org2_Pval[transcript])
        PV3 = PV3.replace("[", "")
        PV3 = PV3.replace("]", "")
        output = "\t".join([transcript, orthogroup, LFC1, PV1, LFC2, PV2])
        o.write(output)
        o.write("\n")

print("Uniquely differentially expressed Apoplastic effectors written \
to text file")

# -----------------------------------------------------
# Step 11
# Identify Secreted proteins that are uniquely differentially expressed
# -----------------------------------------------------

with open(conf.Secreted_CQ) as f:
    Secreted_CQ = []
    Secreted_CQ_lines = f.readlines()
    for line in Secreted_CQ_lines:
        ID = line.rstrip()
        Secreted_CQ.append(ID)

Secreted_CQ_set = set(Secreted_CQ)
Isolate1_Secreted = []
Isolate2_Secreted = []
Isolate3_Secreted = []

for transcript in Org1_uniq_set:
    if transcript in Secreted_CQ_set:
        Isolate1_Secreted.append(transcript)

for transcript in Org2_uniq_set:
    if transcript in Secreted_CQ_set:
        Isolate2_Secreted.append(transcript)

for transcript in Org3_uniq_set:
    if transcript in Secreted_CQ_set:
        Isolate3_Secreted.append(transcript)

with open(conf.Secreted_ORF) as f:
    Secreted_ORF = []
    Secreted_ORF_lines = f.readlines()
    for line in Secreted_ORF_lines:
        ID = line.rstrip()
        ID_modified = ".".join([ID, "t1"])
        Secreted_ORF.append(ID_modified)

Secreted_ORF_set = set(Secreted_ORF)

for transcript in Org1_uniq_set:
    if transcript in Secreted_ORF_set:
        Isolate1_Secreted.append(transcript)

for transcript in Org2_uniq_set:
    if transcript in Secreted_ORF_set:
        Isolate2_Secreted.append(transcript)

for transcript in Org3_uniq_set:
    if transcript in Secreted_ORF_set:
        Isolate3_Secreted.append(transcript)

print("Uniquely differentially expressed secreted proteins identified")

# -----------------------------------------------------
# Step 12
# Print all uniquely expressed Secreted proteins to text file
# -----------------------------------------------------

Org1_file = "_".join([reference_name, Org1, "unique_DEGs_Secreted.txt"])
Org2_file = "_".join([reference_name, Org2, "unique_DEGs_Secreted.txt"])
Org3_file = "_".join([reference_name, Org3, "unique_DEGs_Secreted.txt"])

Org1_out = "/".join([cwd, OutDir, "Secreted", Org1_file])
Org2_out = "/".join([cwd, OutDir, "Secreted", Org2_file])
Org3_out = "/".join([cwd, OutDir, "Secreted", Org3_file])

with open(Org1_out, 'w') as o:
    o.write(Header_Org1)
    o.write("\n")
    for transcript in Isolate1_Secreted:
        orthogroup = ortho_dict[transcript]
        LFC2 = str(Org1_vs_Org2_LFC[transcript])
        PV2 = str(Org1_vs_Org2_Pval[transcript])
        LFC3 = str(Org1_vs_Org3_LFC[transcript])
        PV3 = str(Org1_vs_Org3_Pval[transcript])
        output = "\t".join([transcript, orthogroup, LFC2, PV2, LFC3, PV3])
        o.write(output)
        o.write("\n")

with open(Org2_out, 'w') as o:
    o.write(Header_Org2)
    o.write("\n")
    for transcript in Isolate2_Secreted:
        orthogroup = ortho_dict[transcript]
        LFC1 = str(Org2_vs_Org1_LFC[transcript])
        PV1 = str(Org2_vs_Org1_Pval[transcript])
        LFC3 = str(Org2_vs_Org3_LFC[transcript])
        PV3 = str(Org2_vs_Org3_Pval[transcript])
        output = "\t".join([transcript, orthogroup, LFC1, PV1, LFC3, PV3])
        o.write(output)
        o.write("\n")

with open(Org3_out, 'w') as o:
    o.write(Header_Org3)
    o.write("\n")
    for transcript in Isolate3_Secreted:
        orthogroup = ortho_dict[transcript]
        LFC2 = str(Org3_vs_Org1_LFC[transcript])
        PV2 = str(Org3_vs_Org1_Pval[transcript])
        LFC3 = str(Org3_vs_Org2_LFC[transcript])
        PV3 = str(Org3_vs_Org2_Pval[transcript])
        output = "\t".join([transcript, orthogroup, LFC1, PV1, LFC2, PV2])
        o.write(output)
        o.write("\n")

print("Uniquely differentially expressed Secreted \
proteins written to text file")

# -----------------------------------------------------
# Step 13
# Identify TFs/TRs that are uniquely differentially expressed
# -----------------------------------------------------

with open(conf.TFs) as f:
    TFs = []
    TF_lines = f.readlines()
    for line in TF_lines:
        ID = line.rstrip()
        TFs.append(ID)

TF_set = set(TFs)
Isolate1_TFs = []
Isolate2_TFs = []
Isolate3_TFs = []

for transcript in Org1_uniq_set:
    if transcript in TF_set:
        Isolate1_TFs.append(transcript)

for transcript in Org2_uniq_set:
    if transcript in TF_set:
        Isolate2_TFs.append(transcript)

for transcript in Org3_uniq_set:
    if transcript in TF_set:
        Isolate3_TFs.append(transcript)

print("Uniquely differentially expressed TFs/TRs identified")

# -----------------------------------------------------
# Step 14
# Write all uniquely differentially expressed TFs to text file
# -----------------------------------------------------

Org1_file = "_".join([reference_name, Org1, "unique_DEGs_TFs.txt"])
Org2_file = "_".join([reference_name, Org2, "unique_DEGs_TFs.txt"])
Org3_file = "_".join([reference_name, Org3, "unique_DEGs_TFs.txt"])

Org1_out = "/".join([cwd, OutDir, "TFs", Org1_file])
Org2_out = "/".join([cwd, OutDir, "TFs", Org2_file])
Org3_out = "/".join([cwd, OutDir, "TFs", Org3_file])

with open(Org1_out, 'w') as o:
    o.write(Header_Org1)
    o.write("\n")
    for transcript in Isolate1_TFs:
        orthogroup = ortho_dict[transcript]
        LFC2 = str(Org1_vs_Org2_LFC[transcript])
        PV2 = str(Org1_vs_Org2_Pval[transcript])
        LFC3 = str(Org1_vs_Org3_LFC[transcript])
        PV3 = str(Org1_vs_Org3_Pval[transcript])
        output = "\t".join([transcript, orthogroup, LFC2, PV2, LFC3, PV3])
        o.write(output)
        o.write("\n")

with open(Org2_out, 'w') as o:
    o.write(Header_Org2)
    o.write("\n")
    for transcript in Isolate2_TFs:
        orthogroup = ortho_dict[transcript]
        LFC1 = str(Org2_vs_Org1_LFC[transcript])
        PV1 = str(Org2_vs_Org1_Pval[transcript])
        LFC3 = str(Org2_vs_Org3_LFC[transcript])
        PV3 = str(Org2_vs_Org3_Pval[transcript])
        output = "\t".join([transcript, orthogroup, LFC1, PV1, LFC3, PV3])
        o.write(output)
        o.write("\n")

with open(Org3_out, 'w') as o:
    o.write(Header_Org3)
    o.write("\n")
    for transcript in Isolate3_TFs:
        orthogroup = ortho_dict[transcript]
        LFC2 = str(Org3_vs_Org1_LFC[transcript])
        PV2 = str(Org3_vs_Org1_Pval[transcript])
        LFC3 = str(Org3_vs_Org2_LFC[transcript])
        PV3 = str(Org3_vs_Org2_Pval[transcript])
        output = "\t".join([transcript, orthogroup, LFC1, PV1, LFC2, PV2])
        o.write(output)
        o.write("\n")

print("Uniquely differentially expressed TFs/TRs written to text file")
