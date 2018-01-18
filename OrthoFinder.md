#Maria has suggested a new tool to try for orthology analysis, run it in parallel with orthomcl as a comparison.

##Setting of variables

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/analysis/orthology/OrthoFinder
scripts=/home/adamst/git_repos/scripts/popgen/clock/motif_discovery
```

##Copy files of all protein sequences to one directory

```bash
mkdir -p $input
cp -r analysis/orthology/orthomcl/All_Strains_plus_rubi_no_removal/formatted $input
```

###Runs orthofinder

```bash
screen -a
qlogin -pe smp 24
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/analysis/orthology/OrthoFinder
scripts=/home/adamst/git_repos/scripts/popgen/clock/motif_discovery
cd $input
IsolateAbrv=All_Strains_plus_rubi_no_removal
orthofinder -f formatted -t 24
```

```
Best outgroup(s) for species tree
---------------------------------
Observed 250 duplications. 228 support the best root and 22 contradict it.
Best outgroup for species tree:
SCRP249, SCRP333, SCRP324

OrthoFinder assigned 469036 genes (97.9% of total) to 38179 orthogroups. Fifty percent of all genes were in orthogroups
with 14 or more genes (G50 was 14) and were contained in the largest 12233 orthogroups (O50 was 12233). There were 17388
orthogroups with all species present and 13444 of these consisted entirely of single-copy genes.
```
