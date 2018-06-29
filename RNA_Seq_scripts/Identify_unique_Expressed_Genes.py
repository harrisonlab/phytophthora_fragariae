#!/usr/bin/python

'''
This script uses the output of DeSeq2 to produce a list of genes that are
expressed only in a single isolate and add orthogroup ID for each gene,
also identifies and classifies unique genes
'''

import argparse
from collections import defaultdict
import numpy as np
import os

ap = argparse.ArgumentParser()
ap.add_argument('--FPKM_in', required=True, type=str,
                help='text output file from DeSeq2 commands of non-normalised \
                FPKM values')
ap.add_argument('--Orthogroup_in', required=True, type=str,
                help='text output file of Orthogroups from OrthoFinder')
ap.add_argument('--Reference_name', required=True, type=str,
                help='Name of organism gene IDs are from in FPKM input file')
ap.add_argument('--Organism_1', required=True, type=str,
                help='Name of isolate 1, must have only three timepoints')
ap.add_argument('--Organism_2', required=True, type=str,
                help='Name of isolate 2, must have only one timepoint')
ap.add_argument('--Organism_3', required=True, type=str,
                help='Name of isolate 3, must have only one timepoint')
ap.add_argument('--FPKM_min', required=True, type=float,
                help='Minimum FPKM value to accept as evidence of expression')
ap.add_argument('--RxLRs', required=True, type=str,
                help='File of all RxLR names for aligned genome')
ap.add_argument('--CRNs', required=True, type=str,
                help='File of all CRN names for aligned genome')
ap.add_argument('--ApoP', required=True, type=str,
                help='File of all hits from ApoplastP for aligned genome')
ap.add_argument('--Secreted_CQ', required=True, type=str,
                help='File of all secreted gene models for aligned genome')
ap.add_argument('--Secreted_ORF', required=True, type=str,
                help='File of all secreted ORF fragments for aligned genome')
ap.add_argument('--TFs', required=True, type=str,
                help='File of all predicted transcription factors or \
                transcriptional regulators for aligned genome')
ap.add_argument('--OutDir', required=True, type=str,
                help='Directory to write output files to')
conf = ap.parse_args()

# -----------------------------------------------------
# Step 1
# Load input files
# -----------------------------------------------------

cwd = os.getcwd()

with open(conf.FPKM_in) as f:
    fpkm_lines = f.readlines()[1:]

with open(conf.Orthogroup_in) as f:
    Ortho_lines = f.readlines()

Org1 = conf.Organism_1
Org2 = conf.Organism_2
Org3 = conf.Organism_3

OutDir = conf.OutDir

print("Input files loaded")

# -----------------------------------------------------
# Step 2
# Build dictonaries of count data and of orthogroups
# -----------------------------------------------------

Isolate1_dict = defaultdict(list)
Isolate2_dict = defaultdict(list)
Isolate3_dict = defaultdict(list)
transcript_list = []

for line in fpkm_lines:
    split_lines = line.split()
    transcript_id = split_lines[0]
    transcript_list.append(transcript_id)
    time_a_list = []
    time_a_list.append(float(split_lines[1]))
    time_a_list.append(float(split_lines[2]))
    time_a_list.append(float(split_lines[3]))
    time_a = np.mean(time_a_list)
    time_b_list = []
    time_b_list.append(float(split_lines[4]))
    time_b_list.append(float(split_lines[5]))
    time_b_list.append(float(split_lines[6]))
    time_b = np.mean(time_b_list)
    time_c_list = []
    time_c_list.append(float(split_lines[7]))
    time_c_list.append(float(split_lines[8]))
    time_c_list.append(float(split_lines[9]))
    time_c = np.mean(time_c_list)
    Isolate1_dict[transcript_id] = [float(time_a), float(time_b),
                                    float(time_c)]
    time_d_list = []
    time_d_list.append(float(split_lines[10]))
    time_d_list.append(float(split_lines[11]))
    time_d_list.append(float(split_lines[12]))
    time_d = np.mean(time_d_list)
    Isolate2_dict[transcript_id] = float(time_d)
    time_e_list = []
    time_e_list.append(float(split_lines[13]))
    time_e_list.append(float(split_lines[14]))
    time_e_list.append(float(split_lines[15]))
    time_e = np.mean(time_e_list)
    Isolate3_dict[transcript_id] = float(time_e)

Reference_name = conf.Reference_name
ortho_dict = defaultdict(list)
for line in Ortho_lines:
    line = line.rstrip()
    split_line = line.split()
    orthogroup = split_line[0]
    orthogroup = orthogroup.replace(":", "")
    genes_in_group = [x for x in split_line if Reference_name in x]
    for gene in genes_in_group:
        gene = gene.replace(Reference_name, '').replace('|', '')
        ortho_dict[gene] = orthogroup

print("FPKM & Orthogroup libraries built")

# -----------------------------------------------------
# Step 3
# Iterate over dictionaries to keep only those with FPKM > 5
# -----------------------------------------------------

Isolate1_candidates = defaultdict(list)
Isolate2_candidates = defaultdict(list)
Isolate3_candidates = defaultdict(list)
FPKM = conf.FPKM_min

for transcript, fpkm in Isolate1_dict.items():
    if any(value >= FPKM for value in fpkm):
        if transcript in ortho_dict.keys():
            orthogroup = ortho_dict[transcript]
            Isolate1_candidates[transcript] = orthogroup
        else:
            Isolate1_candidates[transcript] = "None"

for transcript, fpkm in Isolate2_dict.items():
    if fpkm >= FPKM:
        if transcript in ortho_dict.keys():
            orthogroup = ortho_dict[transcript]
            Isolate2_candidates[transcript] = orthogroup
        else:
            Isolate2_candidates[transcript] = "None"

for transcript, fpkm in Isolate3_dict.items():
    if fpkm >= FPKM:
        if transcript in ortho_dict.keys():
            orthogroup = ortho_dict[transcript]
            Isolate3_candidates[transcript] = orthogroup
        else:
            Isolate3_candidates[transcript] = "None"

print("Expressed genes identified")

# -----------------------------------------------------
# Step 4
# Print text files of expressed genes using dictionaries
# -----------------------------------------------------

Org1_file = "_".join([Reference_name, Org1, "expressed.txt"])
Org2_file = "_".join([Reference_name, Org2, "expressed.txt"])
Org3_file = "_".join([Reference_name, Org3, "expressed.txt"])

Org1_out = "/".join([cwd, OutDir, Org1_file])
Org2_out = "/".join([cwd, OutDir, Org2_file])
Org3_out = "/".join([cwd, OutDir, Org3_file])

Header = "\t".join(["Gene_ID", "Orthogroup", "FPKM"])

with open(Org1_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    keys = Isolate1_candidates.keys()
    for item in keys:
        FPKM = str(Isolate1_dict[item])
        FPKM = FPKM.replace('[', '')
        FPKM = FPKM.replace(']', '')
        orthogroup = Isolate1_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

with open(Org2_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    keys = Isolate2_candidates.keys()
    for item in keys:
        FPKM = str(Isolate2_dict[item])
        orthogroup = Isolate2_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

with open(Org3_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    keys = Isolate3_candidates.keys()
    for item in keys:
        FPKM = str(Isolate3_dict[item])
        orthogroup = Isolate3_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

print("Initial output files created for all genes")

# -----------------------------------------------------
# Step 5
# Identify genes that are uniquely expressed
# -----------------------------------------------------

Isolate1_set = set(Isolate1_candidates.keys())
Isolate1_uniq = []
Isolate2_set = set(Isolate2_candidates.keys())
Isolate2_uniq = []
Isolate3_set = set(Isolate3_candidates.keys())
Isolate3_uniq = []

for transcript in Isolate1_set:
    if transcript not in Isolate2_set:
        if transcript not in Isolate3_set:
            Isolate1_uniq.append(transcript)

for transcript in Isolate2_set:
    if transcript not in Isolate1_set:
        if transcript not in Isolate3_set:
            Isolate2_uniq.append(transcript)

for transcript in Isolate3_set:
    if transcript not in Isolate2_set:
        if transcript not in Isolate1_set:
            Isolate3_uniq.append(transcript)

Isolate1_uniq_set = set(Isolate1_uniq)
Isolate2_uniq_set = set(Isolate2_uniq)
Isolate3_uniq_set = set(Isolate3_uniq)

print("Unique lists created")

# -----------------------------------------------------
# Step 6
# Print all uniquely expressed genes to text file
# -----------------------------------------------------

Org1_file = "_".join([Reference_name, Org1, "expressed_unique.txt"])
Org2_file = "_".join([Reference_name, Org2, "expressed_unique.txt"])
Org3_file = "_".join([Reference_name, Org3, "expressed_unique.txt"])

Org1_out = "/".join([cwd, OutDir, "all_genes", Org1_file])
Org2_out = "/".join([cwd, OutDir, "all_genes", Org2_file])
Org3_out = "/".join([cwd, OutDir, "all_genes", Org3_file])

with open(Org1_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate1_uniq:
        FPKM = str(Isolate1_dict[item])
        FPKM = FPKM.replace('[', '')
        FPKM = FPKM.replace(']', '')
        orthogroup = Isolate1_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

with open(Org2_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate2_uniq:
        FPKM = str(Isolate2_dict[item])
        orthogroup = Isolate2_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

with open(Org3_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate3_uniq:
        FPKM = str(Isolate3_dict[item])
        orthogroup = Isolate3_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

print("Output files created for all uniquely expressed genes")

# -----------------------------------------------------
# Step 7
# Identify RxLRs that are uniquely expressed
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

for transcript in Isolate1_uniq_set:
    if transcript in RxLR_set:
        Isolate1_RxLRs.append(transcript)

for transcript in Isolate2_uniq_set:
    if transcript in RxLR_set:
        Isolate2_RxLRs.append(transcript)

for transcript in Isolate3_uniq_set:
    if transcript in RxLR_set:
        Isolate3_RxLRs.append(transcript)

print("Unqiuely expressed RxLRs identified")

# -----------------------------------------------------
# Step 8
# Print all uniquely expressed RxLRs to text file
# -----------------------------------------------------

Org1_file = "_".join([Reference_name, Org1, "expressed_unique_RxLRs.txt"])
Org2_file = "_".join([Reference_name, Org2, "expressed_unique_RxLRs.txt"])
Org3_file = "_".join([Reference_name, Org3, "expressed_unique_RxLRs.txt"])

Org1_out = "/".join([cwd, OutDir, "RxLRs", Org1_file])
Org2_out = "/".join([cwd, OutDir, "RxLRs", Org2_file])
Org3_out = "/".join([cwd, OutDir, "RxLRs", Org3_file])

with open(Org1_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate1_RxLRs:
        FPKM = str(Isolate1_dict[item])
        FPKM = FPKM.replace('[', '')
        FPKM = FPKM.replace(']', '')
        orthogroup = Isolate1_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

with open(Org2_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate2_RxLRs:
        FPKM = str(Isolate2_dict[item])
        orthogroup = Isolate2_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

with open(Org3_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate3_RxLRs:
        FPKM = str(Isolate3_dict[item])
        orthogroup = Isolate3_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

print("Output files created for all uniquely expressed RxLRs")

# -----------------------------------------------------
# Step 9
# Identify CRNs that are uniquely expressed
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

for transcript in Isolate1_uniq_set:
    if transcript in CRN_set:
        Isolate1_CRNs.append(transcript)

for transcript in Isolate2_uniq_set:
    if transcript in CRN_set:
        Isolate2_CRNs.append(transcript)

for transcript in Isolate3_uniq_set:
    if transcript in CRN_set:
        Isolate3_CRNs.append(transcript)

print("Unqiuely expressed CRNs identified")

# -----------------------------------------------------
# Step 10
# Print all uniquely expressed CRNs to text file
# -----------------------------------------------------

Org1_file = "_".join([Reference_name, Org1, "expressed_unique_CRNs.txt"])
Org2_file = "_".join([Reference_name, Org2, "expressed_unique_CRNs.txt"])
Org3_file = "_".join([Reference_name, Org3, "expressed_unique_CRNs.txt"])

Org1_out = "/".join([cwd, OutDir, "CRNs", Org1_file])
Org2_out = "/".join([cwd, OutDir, "CRNs", Org2_file])
Org3_out = "/".join([cwd, OutDir, "CRNs", Org3_file])

with open(Org1_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate1_CRNs:
        FPKM = str(Isolate1_dict[item])
        FPKM = FPKM.replace('[', '')
        FPKM = FPKM.replace(']', '')
        orthogroup = Isolate1_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

with open(Org2_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate2_CRNs:
        FPKM = str(Isolate2_dict[item])
        orthogroup = Isolate2_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

with open(Org3_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate3_CRNs:
        FPKM = str(Isolate3_dict[item])
        orthogroup = Isolate3_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

print("Output files created for all uniquely expressed CRNs")

# -----------------------------------------------------
# Step 11
# Identify apoplastic effectors that are uniquely expressed
# -----------------------------------------------------

with open(conf.ApoP) as f:
    ApoP = []
    ApoP_lines = f.readlines()
    for line in ApoP_lines:
        ID = line.rstrip()
        if "contig" in ID:
            ID = ".".join([ID, "t1"])
        ApoP.append(ID)

ApoP_set = set(ApoP)
Isolate1_ApoP = []
Isolate2_ApoP = []
Isolate3_ApoP = []

for transcript in Isolate1_uniq_set:
    if transcript in ApoP_set:
        Isolate1_ApoP.append(transcript)

for transcript in Isolate2_uniq_set:
    if transcript in ApoP_set:
        Isolate2_ApoP.append(transcript)

for transcript in Isolate3_uniq_set:
    if transcript in ApoP_set:
        Isolate3_ApoP.append(transcript)

print("Unqiuely expressed apoplastic effectors identified")

# -----------------------------------------------------
# Step 12
# Print all uniquely expressed apoplastic effectors to text file
# -----------------------------------------------------

Org1_file = "_".join([Reference_name, Org1, "expressed_unique_ApoP.txt"])
Org2_file = "_".join([Reference_name, Org2, "expressed_unique_ApoP.txt"])
Org3_file = "_".join([Reference_name, Org3, "expressed_unique_ApoP.txt"])

Org1_out = "/".join([cwd, OutDir, "ApoP", Org1_file])
Org2_out = "/".join([cwd, OutDir, "ApoP", Org2_file])
Org3_out = "/".join([cwd, OutDir, "ApoP", Org3_file])

with open(Org1_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate1_ApoP:
        FPKM = str(Isolate1_dict[item])
        FPKM = FPKM.replace('[', '')
        FPKM = FPKM.replace(']', '')
        orthogroup = Isolate1_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

with open(Org2_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate2_ApoP:
        FPKM = str(Isolate2_dict[item])
        orthogroup = Isolate2_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

with open(Org3_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate3_ApoP:
        FPKM = str(Isolate3_dict[item])
        orthogroup = Isolate3_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

print("Output files created for all uniquely expressed Apoplastic effectors")

# -----------------------------------------------------
# Step 13
# Identify secreted proteins that are uniquely expressed
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

for transcript in Isolate1_uniq_set:
    if transcript in Secreted_CQ_set:
        Isolate1_Secreted.append(transcript)

for transcript in Isolate2_uniq_set:
    if transcript in Secreted_CQ_set:
        Isolate2_Secreted.append(transcript)

for transcript in Isolate3_uniq_set:
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

for transcript in Isolate1_uniq_set:
    if transcript in Secreted_ORF_set:
        Isolate1_Secreted.append(transcript)

for transcript in Isolate2_uniq_set:
    if transcript in Secreted_ORF_set:
        Isolate2_Secreted.append(transcript)

for transcript in Isolate3_uniq_set:
    if transcript in Secreted_ORF_set:
        Isolate3_Secreted.append(transcript)


print("Unqiuely expressed secreted proteins identified")

# -----------------------------------------------------
# Step 14
# Print all uniquely expressed Secreted proteins to text file
# -----------------------------------------------------

Org1_file = "_".join([Reference_name, Org1, "expressed_unique_secreted.txt"])
Org2_file = "_".join([Reference_name, Org2, "expressed_unique_secreted.txt"])
Org3_file = "_".join([Reference_name, Org3, "expressed_unique_secreted.txt"])

Org1_out = "/".join([cwd, OutDir, "Secreted", Org1_file])
Org2_out = "/".join([cwd, OutDir, "Secreted", Org2_file])
Org3_out = "/".join([cwd, OutDir, "Secreted", Org3_file])

with open(Org1_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate1_Secreted:
        FPKM = str(Isolate1_dict[item])
        FPKM = FPKM.replace('[', '')
        FPKM = FPKM.replace(']', '')
        orthogroup = Isolate1_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

with open(Org2_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate2_Secreted:
        FPKM = str(Isolate2_dict[item])
        orthogroup = Isolate2_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

with open(Org3_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate3_Secreted:
        FPKM = str(Isolate3_dict[item])
        orthogroup = Isolate3_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

print("Output files created for all uniquely expressed Secreted proteins")

# -----------------------------------------------------
# Step 15
# Identify TFs/TRs that are uniquely expressed
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

for transcript in Isolate1_uniq_set:
    if transcript in TF_set:
        Isolate1_TFs.append(transcript)

for transcript in Isolate2_uniq_set:
    if transcript in TF_set:
        Isolate2_TFs.append(transcript)

for transcript in Isolate3_uniq_set:
    if transcript in TF_set:
        Isolate3_TFs.append(transcript)

print("Unqiuely expressed TFs identified")

# -----------------------------------------------------
# Step 16
# Print all uniquely expressed RxLRs to text file
# -----------------------------------------------------

Org1_file = "_".join([Reference_name, Org1, "expressed_unique_TFs.txt"])
Org2_file = "_".join([Reference_name, Org2, "expressed_unique_TFs.txt"])
Org3_file = "_".join([Reference_name, Org3, "expressed_unique_TFs.txt"])

Org1_out = "/".join([cwd, OutDir, "TFs", Org1_file])
Org2_out = "/".join([cwd, OutDir, "TFs", Org2_file])
Org3_out = "/".join([cwd, OutDir, "TFs", Org3_file])

with open(Org1_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate1_TFs:
        FPKM = str(Isolate1_dict[item])
        FPKM = FPKM.replace('[', '')
        FPKM = FPKM.replace(']', '')
        orthogroup = Isolate1_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

with open(Org2_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate2_TFs:
        FPKM = str(Isolate2_dict[item])
        orthogroup = Isolate2_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

with open(Org3_out, 'w') as o:
    o.write(Header)
    o.write("\n")
    for item in Isolate3_TFs:
        FPKM = str(Isolate3_dict[item])
        orthogroup = Isolate3_candidates[item]
        output = "\t".join([item, orthogroup, FPKM])
        o.write(output)
        o.write("\n")

print("Output files created for all uniquely expressed TFs")
