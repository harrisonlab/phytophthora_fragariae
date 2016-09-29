#BUSCO analysis

First stage of constructing a phylogenetic tree for StarBeast, this involves selecting a set of core genes from gene predictions.

Setting variables

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae
scripts=/home/adamst/git_repos/scripts/popgen
```

##Process reference genomes


### Rename sequences in all FASTA files by prefixing with the species name:

```bash
sed -i -e 's/>/>P.fragariae_A4_/' Botrytis_cinerea.ASM83294v1.cds.all.fa
sed -i -e 's/>/>P.fragariae_Bc1/' Fusarium_graminearum.RR.cds.all.fa
sed -i -e 's/>/>P.fragariae_Bc16_/' Fusarium_oxysporum.FO2.cds.all.fa
sed -i -e 's/>/>P.fragariae_Bc23_/' Magnaporthe_oryzae.MG8.cds.all.fa
sed -i -e 's/>/>P.fragariae_Nov27_/' Neonectria_ditissima.R0905_v2.0.cds.all.fa
sed -i -e 's/>/>P.fragariae_Nov5_/' Neurospora_crassa.NC12.cds.all.fa
sed -i -e 's/>/>P.fragariae_Nov71_/' Podospora_anserina_s_mat_.ASM22654v1.cds.all.fa
sed -i -e 's/>/>P.fragariae_Nov77_/' Sordaria_macrospora.ASM18280v2.cds.all.fa
sed -i -e 's/>/>P.fragariae_Nov9_/' Trichoderma_reesei.GCA_000167675.2.cds.all.fa
sed -i -e 's/>/>P.fragariae_ONT3_/' Verticillium_alfalfae_vams_102.ASM15082v1.cds.all.fa
sed -i -e 's/>/>P.fragariae_SCRP25_v2_/' Verticillium_dahliae.ASM15067v2.cds.all.fa
```

### Run BUSCO
for a in *.fa
do
qsub $scripts/sub_BUSCO_fungi.sh $input/$a
done

## Find the intersect of single-copy, complete genes
### Create a list of all fungal BUSCO IDs

pushd /home/sobczm/bin/BUSCO_v1.22/fungi/hmms
ls -1 | sed -e 's/\..*$//' >../all_buscos_fungi
cp ../all_buscos_fungi $input
popd

### Iteratively find the intersect of IDs of all 'complete' BUSCO genes present in the runs in the current directory

#!/bin/bash
cat all_buscos_fungi >temp_ref
for d in $PWD/run*
do
    if test -n "$(find $d -maxdepth 1 -name 'full_table*' -print -quit)"
    then
        awk '$2 == "Complete" { print $1}' $d/full_table* >temp
        grep -Fx -f temp temp_ref >final_list_ssc
        cat final_list_ssc >temp_ref
    else
        echo "There is no full_table result in $d."
    fi
done

## Create FASTA files with separate alignment input for each of the shared BUSCO genes
cat final_list_ssc >align_input_list.txt
perl $scripts/get_alignments.pl
