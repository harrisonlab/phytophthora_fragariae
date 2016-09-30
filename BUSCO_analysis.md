#BUSCO analysis

First stage of constructing a phylogenetic tree for StarBeast, this involves selecting a set of core genes from gene predictions.

Setting variables

```bash
input=/home/groups/harrisonlab/project_files/phytophthora_fragariae/phylogeny
scripts=/home/adamst/git_repos/scripts/popgen/phylogenetics
```

##Process reference genomes

###Copy gene prediction FASTAs to new directory

```bash
for CDS in $(ls gene_pred/codingquary/*/*/final/final_genes_combined.cdna.fasta)
do
    Strain=$(echo $CDS | rev | cut -d '/' -f3 | rev)
    mkdir -p phylogeny
    cp $CDS phylogeny/"$Strain"_final_genes_combined.cdna.fasta
done
```

### Rename sequences in all FASTA files by prefixing with the species name:

```bash
sed -i -e 's/>/>P.fragariae_A4_/' phylogeny/A4_final_genes_combined.cdna.fasta
sed -i -e 's/>/>P.fragariae_Bc1/' phylogeny/Bc1_final_genes_combined.cdna.fasta
sed -i -e 's/>/>P.fragariae_Bc16_/' phylogeny/Bc16_final_genes_combined.cdna.fasta
sed -i -e 's/>/>P.fragariae_Bc23_/' phylogeny/Bc23_final_genes_combined.cdna.fasta
sed -i -e 's/>/>P.fragariae_Nov27_/' phylogeny/Nov27_final_genes_combined.cdna.fasta
sed -i -e 's/>/>P.fragariae_Nov5_/' phylogeny/Nov5_final_genes_combined.cdna.fasta
sed -i -e 's/>/>P.fragariae_Nov71_/' phylogeny/Nov71_final_genes_combined.cdna.fasta
sed -i -e 's/>/>P.fragariae_Nov77_/' phylogeny/Nov77_final_genes_combined.cdna.fasta
sed -i -e 's/>/>P.fragariae_Nov9_/' phylogeny/Nov9_final_genes_combined.cdna.fasta
sed -i -e 's/>/>P.fragariae_ONT3_/' phylogeny/ONT3_final_genes_combined.cdna.fasta
sed -i -e 's/>/>P.fragariae_SCRP25_v2_/' phylogeny/SCRP245_v2_final_genes_combined.cdna.fasta
```

### Run BUSCO

```bash
for CDS in $input/*.fasta
do
    echo $CDS
    qsub $scripts/sub_BUSCO.sh $CDS
done
```

## Find the intersect of single-copy, complete genes
### Create a list of all fungal BUSCO IDs

```bash
pushd /home/sobczm/bin/BUSCO_v1.22/eukaryota/hmms
ls -1 | sed -e 's/\..*$//' >$input/all_buscos_eukaryota
popd
```

### Iteratively find the intersect of IDs of all 'complete' BUSCO genes present in the runs in the current directory

```bash
cat all_buscos_eukaryota >temp_ref
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
```

## Create FASTA files with separate alignment input for each of the shared BUSCO genes
cat final_list_ssc >align_input_list.txt
perl $scripts/get_alignments.pl
