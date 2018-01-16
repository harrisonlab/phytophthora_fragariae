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
