#!/usr/bin/python

'''
This script takes outputs from Expression presence/absence and differently DEGs
to create a sorted table of candidates with a score of 0-6, 6 being best
'''

import sys
import argparse
from collections import defaultdict
import os

ap = argparse.ArgumentParser()
ap.add_argument('--Unique_Expression_Files', required=True, nargs='+',
                type=str, help='Space separated list of files containing \
                uniquely expressed genes')
ap.add_argument('--Differently_DEG_File', required=True, nargs='+', type=str,
                help='Space separated list of files containing unique \
                differently differentially expressed genes')
ap.add_argument('--Orthogroup_in', required=True, type=str, help='Text output \
file of Orthogroups from OrthoFinder')
ap.add_argument('--Organism_1', required=True, type=str, help='ID of organism \
1')
ap.add_argument('--Organism_2', required=True, type=str, help='ID of organism \
2')
ap.add_argument('--Organism_3', required=True, type=str, help='ID of organism \
3')
ap.add_argument('--Race_isolates', required=True, nargs='+', type=str,
                help='Space separated list of isolates of the race of interest \
                ')
ap.add_argument('--Reference_name', required=True, type=str, help='ID of \
isolate to score candidates of')
ap.add_argument('--RxLRs', required=True, type=str, help='File of all RxLR \
names for aligned genome')
ap.add_argument('--CRNs', required=True, type=str, help='File of all CRN names \
for aligned genome')
ap.add_argument('--ApoP', required=True, type=str, help='File of all hits from \
ApoplastP')
ap.add_argument('--Secreted_CQ', required=True, type=str, help='File of all \
secreted gene models')
ap.add_argument('--Secreted_ORF', required=True, type=str, help='File of all \
secreted ORF fragments')
ap.add_argument('--TFs', required=True, type=str, help='File of all genes \
identified as possible TFs/TRs')
ap.add_argument('--OutDir', required=True, type=str, help='Directory to write \
output files to')
conf = ap.parse_args()

# -----------------------------------------------------
# Step 1
# Load input files
# -----------------------------------------------------

Org1 = conf.Organism_1
Org2 = conf.Organism_2
Org3 = conf.Organism_3
Ref_Name = conf.Reference_name

Uniq_Exp_Files = conf.Unique_Expression_Files
Org1_Uniq_Exp = []
Org2_Uniq_Exp = []
Org3_Uniq_Exp = []

for Uniq_Exp_File in Uniq_Exp_Files:
    with open(Uniq_Exp_File) as f:
        if (Uniq_Exp_File.split('/')[-1].split('_')[0] == Org1 and
           Uniq_Exp_File.split('/')[-1].split('_')[1] == Ref_Name):
            gene_lines = f.readlines()[1:]
            for gene in gene_lines:
                transcript_ID = gene.split('\t')[0]
                Org1_Uniq_Exp.append(transcript_ID)
        elif (Uniq_Exp_File.split('/')[-1].split('_')[0] == Org2 and
              Uniq_Exp_File.split('/')[-1].split('_')[1] == Ref_Name):
            gene_lines = f.readlines()[1:]
            for gene in gene_lines:
                transcript_ID = gene.split('\t')[0]
                Org2_Uniq_Exp.append(transcript_ID)
        elif (Uniq_Exp_File.split('/')[-1].split('_')[0] == Org3 and
              Uniq_Exp_File.split('/')[-1].split('_')[1] == Ref_Name):
            gene_lines = f.readlines()[1:]
            for gene in gene_lines:
                transcript_ID = gene.split('\t')[0]
                Org3_Uniq_Exp.append(transcript_ID)
        else:
            sys.exit("Error, incorrect expression files provided")

Org1_Uniq_Exp_set = set(Org1_Uniq_Exp)
Org2_Uniq_Exp_set = set(Org2_Uniq_Exp)
Org3_Uniq_Exp_set = set(Org3_Uniq_Exp)

Uniq_DEG_Files = conf.Differently_DEG_File
Org1_Uniq_DEG = []
Org2_Uniq_DEG = []
Org3_Uniq_DEG = []
for Uniq_DEG_File in Uniq_DEG_Files:
    with open(Uniq_DEG_File) as f:
        if (Uniq_DEG_File.split('/')[-1].split('_')[0] == Org1 and
           Uniq_DEG_File.split('/')[-1].split('_')[1] == Ref_Name):
            gene_lines = f.readlines()[1:]
            for gene in gene_lines:
                transcript_ID = gene.split('\t')[0]
                Org1_Uniq_DEG.append(transcript_ID)
        elif (Uniq_DEG_File.split('/')[-1].split('_')[0] == Org2 and
              Uniq_DEG_File.split('/')[-1].split('_')[1] == Ref_Name):
            gene_lines = f.readlines()[1:]
            for gene in gene_lines:
                transcript_ID = gene.split('\t')[0]
                Org2_Uniq_DEG.append(transcript_ID)
        elif (Uniq_DEG_File.split('/')[-1].split('_')[0] == Org3 and
              Uniq_DEG_File.split('/')[-1].split('_')[1] == Ref_Name):
            gene_lines = f.readlines()[1:]
            for gene in gene_lines:
                transcript_ID = gene.split('\t')[0]
                Org3_Uniq_DEG.append(transcript_ID)
        else:
            sys.exit("Error, incorrect DEG files provided")

Org1_Uniq_DEG_set = set(Org1_Uniq_DEG)
Org2_Uniq_DEG_set = set(Org2_Uniq_DEG)
Org3_Uniq_DEG_set = set(Org3_Uniq_DEG)

ortho_dict = defaultdict(list)
with open(conf.Orthogroup_in) as f:
    Ortho_lines = f.readlines()
    for line in Ortho_lines:
        line = line.rstrip()
        split_line = line.split()
        orthogroup = split_line[0]
        orthogroup = orthogroup.replace(":", "")
        genes_in_group = [x for x in split_line if 'OG' not in x]
        ortho_dict[orthogroup] = genes_in_group

RxLRs = []
with open(conf.RxLRs) as f:
    RxLR_lines = f.readlines()
    for line in RxLR_lines:
        ID = line.rstrip()
        if "contig" in ID:
            ID = ".".join([ID, "t1"])
        RxLRs.append(ID)

CRNs = []
with open(conf.CRNs) as f:
    CRN_lines = f.readlines()
    for line in CRN_lines:
        ID = line.rstrip()
        if "contig" in ID:
            ID = ".".join([ID, "t1"])
        CRNs.append(ID)

ApoPs = []
with open(conf.ApoP) as f:
    ApoP_lines = f.readlines()
    for line in ApoP_lines:
        ID = line.rstrip()
        if "contig" in ID:
            ID = ".".join([ID, "t1"])
        ApoPs.append(ID)

Sec = []
with open(conf.Secreted_CQ) as f:
    Sec_CQ_lines = f.readlines()
    for line in Sec_CQ_lines:
        ID = line.rstrip()
        Sec.append(ID)

with open(conf.Secreted_ORF) as f:
    Sec_ORF_lines = f.readlines()
    for line in Sec_ORF_lines:
        ID = line.rstrip()
        ID_modified = ".".join([ID, "t1"])
        Sec.append(ID_modified)

TFs = []
with open(conf.TFs) as f:
    TF_lines = f.readlines()
    for line in TF_lines:
        ID = line.rstrip()
        TFs.append(ID)

RxLR_set = set(RxLRs)
CRN_set = set(CRNs)
ApoP_set = set(ApoPs)
Sec_set = set(Sec)
TF_set = set(TFs)

print("Files loaded and prepared")

# -----------------------------------------------------
# Step 2
# Create dictionaries listing gene IDs in each expressed set as keys with
# orthogroup ID as values -- slow step
# -----------------------------------------------------

Race_IDs = conf.Race_isolates

Org1_ID_dict = defaultdict(list)
Isolates_per_group = defaultdict(list)
OGs = []

for transcript_ID in Org1_Uniq_Exp_set:
    ID_to_search = "|".join([Org1, transcript_ID])
    orthogroups = [OG for OG, genes in ortho_dict.items() if ID_to_search in
                   genes]
    for orthogroup in orthogroups:
        OGs.append(orthogroup)
        for item in ortho_dict[orthogroup]:
            Isolate = item.split('|')[0]
            Isolates_per_group[orthogroup].append(Isolate)

OGs_set = set(OGs)
for orthogroup in OGs_set:
    if set(Race_IDs).issubset(set(Isolates_per_group[orthogroup])):
        Org1_ID_dict[transcript_ID] = orthogroup

print("Dictionary of orthogroups created")

# -----------------------------------------------------
# Step 3
# Loop through genes from isolate of interest
# ID genes from other analysed genomes in same OG
# -----------------------------------------------------

Org1_Org2_dict = defaultdict(list)
Org1_Org3_dict = defaultdict(list)

for transcript_ID in Org1_ID_dict.keys():
    orthogroup = Org1_ID_dict[transcript_ID]
    OG_genes = ortho_dict[orthogroup]
    for gene_ID in OG_genes:
        if gene_ID.split('|')[0] == Org2:
            Org1_Org2_dict[transcript_ID].append(gene_ID.split('|')[1])
        elif gene_ID.split('|')[0] == Org3:
            Org1_Org3_dict[transcript_ID].append(gene_ID.split('|')[1])

print("Genes in the same orthogroup as candidates identified")

# -----------------------------------------------------
# Step 4
# Loop through each ID to be written to table and create dictionaries for
# writing to each field of the table
# -----------------------------------------------------

Org1_Exp_to_print = []
Org2_Exp_to_print = []
Org3_Exp_to_print = []
Org1_DEG_to_print = []
Org2_DEG_to_print = []
Org3_DEG_to_print = []
RxLR_to_print = []
CRN_to_print = []
ApoP_to_print = []
Sec_to_print = []
TF_to_print = []
Score_dict = defaultdict(float)

for transcript_ID in Org1_ID_dict.keys():
    if transcript_ID in Org1_Uniq_Exp_set:
        Org1_Exp_to_print.append(transcript_ID)
    gene_list = Org1_Org2_dict[transcript_ID]
    for gene in gene_list:
        if gene in Org2_Uniq_Exp_set:
            Org2_Exp_to_print.append(transcript_ID)
    gene_list = Org1_Org3_dict[transcript_ID]
    for gene in gene_list:
        if gene in Org3_Uniq_Exp_set:
            Org3_Exp_to_print.append(transcript_ID)
    if transcript_ID in Org1_Uniq_DEG_set:
        Org1_DEG_to_print.append(transcript_ID)
    gene_list = Org1_Org2_dict[transcript_ID]
    for gene in gene_list:
        if gene in Org2_Uniq_DEG_set:
            Org2_DEG_to_print.append(transcript_ID)
    gene_list = Org1_Org3_dict[transcript_ID]
    for gene in gene_list:
        if gene in Org3_Uniq_DEG_set:
            Org3_DEG_to_print.append(transcript_ID)
    if transcript_ID in RxLR_set:
        RxLR_to_print.append(transcript_ID)
    if transcript_ID in CRN_set:
        CRN_to_print.append(transcript_ID)
    if transcript_ID in ApoP_set:
        ApoP_to_print.append(transcript_ID)
    if transcript_ID in Sec_set:
        Sec_to_print.append(transcript_ID)
    if transcript_ID in TF_set:
        TF_to_print.append(transcript_ID)

for transcript_ID in Org1_ID_dict.keys():
    if (transcript_ID in RxLR_to_print or transcript_ID in CRN_to_print or
       transcript_ID in ApoP_to_print or transcript_ID in Sec_to_print
       or transcript_ID in TF_to_print):
        feat_list = []
        if transcript_ID in Org1_Exp_to_print:
            feat_list.append('O1E')
        if transcript_ID in Org2_Exp_to_print:
            feat_list.append('O2E')
        if transcript_ID in Org3_Exp_to_print:
            feat_list.append('O3E')
        if transcript_ID in Org1_DEG_to_print:
            feat_list.append('O1D')
        if transcript_ID in Org2_DEG_to_print:
            feat_list.append('O2D')
        if transcript_ID in Org3_DEG_to_print:
            feat_list.append('O3D')
        Score = len(feat_list)
        Score_dict[transcript_ID] = Score
    else:
        Score_dict[transcript_ID] = float('0')

print("Features identified")

# -----------------------------------------------------
# Step 5
# Write out file
# -----------------------------------------------------

OutDir = conf.OutDir
cwd = os.getcwd()

OutFile = "_".join([Ref_Name, "candidate", "avrs.tsv"])
Output = "/".join([cwd, OutDir, OutFile])

Org1_gene_Head = "_".join([Org1, "transcript", "ID"])
Org2_gene_Head = "_".join([Org2, "transcript", "ID"])
Org3_gene_Head = "_".join([Org3, "transcript", "ID"])
Org1_DEG_Head = "_".join([Org1, "different", "DEG"])
Org2_DEG_Head = "_".join([Org2, "different", "DEG"])
Org3_DEG_Head = "_".join([Org3, "different", "DEG"])
Org1_exp_Head = "_".join([Org1, "uniquely", "expressed"])
Org2_exp_Head = "_".join([Org2, "uniquely", "expressed"])
Org3_exp_Head = "_".join([Org3, "uniquely", "expressed"])

Header = "\t".join([Org1_gene_Head, Org2_gene_Head, Org3_gene_Head,
                    "Orthogroup", Org1_DEG_Head, Org2_DEG_Head, Org3_DEG_Head,
                    Org1_exp_Head, Org2_exp_Head, Org3_exp_Head, "RxLR", "CRN",
                    "ApoplastP", "Secreted", "TFs/TRs", "Score"])

with open(Output, 'w') as o:
    o.write(Header)
    o.write("\n")
    for transcript_ID in Org1_ID_dict.keys():
        if transcript_ID in Org1_Exp_to_print:
            Org1_Exp = "Yes"
        else:
            Org1_Exp = ""
        if transcript_ID in Org2_Exp_to_print:
            Org2_Exp = "Yes"
        else:
            Org2_Exp = ""
        if transcript_ID in Org3_Exp_to_print:
            Org3_Exp = "Yes"
        else:
            Org3_Exp = ""
        if transcript_ID in Org1_DEG_to_print:
            Org1_DEG = "Yes"
        else:
            Org1_DEG = ""
        if transcript_ID in Org2_DEG_to_print:
            Org2_DEG = "Yes"
        else:
            Org2_DEG = ""
        if transcript_ID in Org3_DEG_to_print:
            Org3_DEG = "Yes"
        else:
            Org3_DEG = ""
        if transcript_ID in RxLR_to_print:
            RxLR = "Yes"
        else:
            RxLR = ""
        if transcript_ID in CRN_to_print:
            CRN = "Yes"
        else:
            CRN = ""
        if transcript_ID in ApoP_to_print:
            ApoP = "Yes"
        else:
            ApoP = ""
        if transcript_ID in Sec_to_print:
            Sec = "Yes"
        else:
            Sec = ""
        if transcript_ID in TF_to_print:
            TF = "Yes"
        else:
            TF = ""
        Org2_IDs = ",".join(str(ID) for ID in Org1_Org2_dict[transcript_ID])
        Org3_IDs = ",".join(str(ID) for ID in Org1_Org3_dict[transcript_ID])
        Orthogroup = str(Org1_ID_dict[transcript_ID])
        Score = str(Score_dict[transcript_ID])
        To_Write = "\t".join([transcript_ID, Org2_IDs, Org3_IDs, Orthogroup,
                             Org1_Exp, Org2_Exp, Org3_Exp, Org1_DEG, Org2_DEG,
                             Org3_DEG, RxLR, CRN, ApoP, Sec, TF, Score])
        o.write(To_Write)
        o.write("\n")

print("Output written to file")
