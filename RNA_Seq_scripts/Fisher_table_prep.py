#!/usr/bin/python

'''
This script will count the number of RxLRs, CRNs, ApoplastP hits and combined
effector genes in a coexpressed module compared to and the rest of the genome
'''

import argparse
import os

# -----------------------------------------------------
# Step 1
# Import command line arguments
# -----------------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument('--Module_RxLRs', required=True, type=str, help='List of RxLRs \
in a coexpression module')
ap.add_argument('--Module_CRNs', required=True, type=str, help='List of CRNs \
in a coexpression module')
ap.add_argument('--Module_ApoP', required=True, type=str, help='List of ApoP \
hits in a coexpression module')
ap.add_argument('--Module_Effectors', required=True, type=str, help='List of Effectors \
in a coexpression module')
ap.add_argument('--Module_Genes', required=True, type=str, help='Complete list \
of genes in a coexpression module')
ap.add_argument('--Module_Name', required=True, type=str, help='Name of the \
module being analysed')
ap.add_argument('--Genome_RxLRs', required=True, type=float, help='Number of \
total RxLRs in the genome')
ap.add_argument('--Genome_CRNs', required=True, type=float, help='Number of \
total CRNs in the genome')
ap.add_argument('--Genome_ApoP', required=True, type=float, help='Number of \
total ApoP hits in the genome')
ap.add_argument('--Genome_Effectors', required=True, type=float, help='Number of \
total Effectorss in the genome')
ap.add_argument('--Genome_Genes', required=True, type=float, help='Number of \
total genes in the genome')
ap.add_argument('--OutDir', required=True, type=str, help='Directory to write \
output files to')
conf = ap.parse_args()

# -----------------------------------------------------
# Step 2
# Load inputs into python variables
# -----------------------------------------------------

RxLRs = []
with open(conf.Module_RxLRs) as f:
    for line in f.readlines():
        RxLRs.append(line)

RxLR_Set = set(RxLRs)

CRNs = []
with open(conf.Module_CRNs) as f:
    for line in f.readlines():
        CRNs.append(line)

CRN_Set = set(CRNs)

ApoP = []
with open(conf.Module_ApoP) as f:
    for line in f.readlines():
        ApoP.append(line)

ApoP_Set = set(ApoP)

Effectors = []
with open(conf.Module_Effectors) as f:
    for line in f.readlines():
        Effectors.append(line)

Effector_Set = set(Effectors)

Genes = []
with open(conf.Module_Genes) as f:
    for line in f.readlines():
        Genes.append(line)

Gene_Set = set(Genes)

Module_Name = conf.Module_Name
Genome_RxLRs = conf.Genome_RxLRs
Genome_CRNs = conf.Genome_CRNs
Genome_ApoP = conf.Genome_ApoP
Genome_Effectors = conf.Genome_Effectors
Genome_Genes = conf.Genome_Genes
OutDir = conf.OutDir
cwd = os.getcwd()

# -----------------------------------------------------
# Step 3
# Obtain counts for all gene types in module and rest of genome
# -----------------------------------------------------

# Modules

Mod_RxLR_Num = len(RxLR_Set)
Mod_CRN_Num = len(CRN_Set)
Mod_ApoP_Num = len(ApoP_Set)
Mod_Effector_Num = len(Effector_Set)
Mod_Gene_Num = len(Gene_Set)

# Genome

Gen_RxLR_Num = Genome_RxLRs - Mod_RxLR_Num
Gen_CRN_Num = Genome_CRNs - Mod_CRN_Num
Gen_ApoP_Num = Genome_ApoP - Mod_ApoP_Num
Gen_Effector_Num = Genome_Effectors - Mod_Effector_Num
Gen_Gene_Num = Genome_Genes - Mod_Gene_Num

# -----------------------------------------------------
# Step 4
# Write output files
# -----------------------------------------------------

RxLR_File = "_".join([Module_Name, "RxLR_Fishertable.txt"])
RxLR_Out = "/".join([cwd, OutDir, RxLR_File])

with open(RxLR_Out, "w") as o:
    Gen_RxLR = Gen_RxLR_Num - Mod_RxLR_Num
    Line1 = "\t".join(["RxLR", str(Mod_RxLR_Num), str(Gen_RxLR)]) + "\n"
    Mod_Genes = Mod_Gene_Num - Mod_RxLR_Num
    Gen_Genes = Gen_Gene_Num - Mod_Gene_Num - Gen_RxLR_Num
    Line2 = "\t".join(["Other Genes", str(Mod_Genes), str(Gen_Genes)]) + "\n"
    o.write("".join([Line1, Line2]))
    o.close()

CRN_File = "_".join([Module_Name, "CRN_Fishertable.txt"])
CRN_Out = "/".join([cwd, OutDir, CRN_File])

with open(CRN_Out, "w") as o:
    Gen_CRN = Gen_CRN_Num - Mod_CRN_Num
    Line1 = "\t".join(["CRN", str(Mod_CRN_Num), str(Gen_CRN)]) + "\n"
    Mod_Genes = Mod_Gene_Num - Mod_CRN_Num
    Gen_Genes = Gen_Gene_Num - Mod_Gene_Num - Gen_CRN_Num
    Line2 = "\t".join(["Other Genes", str(Mod_Genes), str(Gen_Genes)]) + "\n"
    o.write("".join([Line1, Line2]))
    o.close()

ApoP_File = "_".join([Module_Name, "ApoP_Fishertable.txt"])
ApoP_Out = "/".join([cwd, OutDir, ApoP_File])

with open(ApoP_Out, "w") as o:
    Gen_ApoP = Gen_ApoP_Num - Mod_ApoP_Num
    Line1 = "\t".join(["ApoP", str(Mod_ApoP_Num), str(Gen_ApoP)]) + "\n"
    Mod_Genes = Mod_Gene_Num - Mod_ApoP_Num
    Gen_Genes = Gen_Gene_Num - Mod_Gene_Num - Gen_ApoP_Num
    Line2 = "\t".join(["Other Genes", str(Mod_Genes), str(Gen_Genes)]) + "\n"
    o.write("".join([Line1, Line2]))
    o.close()

Effector_File = "_".join([Module_Name, "Effector_Fishertable.txt"])
Effector_Out = "/".join([cwd, OutDir, Effector_File])

with open(Effector_Out, "w") as o:
    Gen_Effector = Gen_Effector_Num - Mod_Effector_Num
    Line1 = "\t".join(["Effector", str(Mod_Effector_Num), str(Gen_Effector)]) \
        + "\n"
    Mod_Genes = Mod_Gene_Num - Mod_Effector_Num
    Gen_Genes = Gen_Gene_Num - Mod_Gene_Num - Gen_Effector_Num
    Line2 = "\t".join(["Other Genes", str(Mod_Genes), str(Gen_Genes)]) + "\n"
    o.write("".join([Line1, Line2]))
    o.close()
