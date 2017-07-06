#The ortholog groups that these genes belonged to were investigated:

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for Gene in $(cat $MergeDir/"$Strain"_Total_CRN_expressed.gtf | grep -w 'transcript' | sort -r -n -k 14 -t '"' | cut -f4,14 -d '"' --output-delimite " - " |  head -n 20 | cut -f1 -d '.')
    do
        echo "$Gene"
        cat analysis/orthology/orthomcl/P.fragariae/P.fragariae_orthogroups.txt | grep -w "$Gene"
        echo ""
    done
done
```

##Functional annotation of CRNs

#Interproscan annotations and swissprot similarities were identified for CRNs of all strains.

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    for Gene in $(cat $MergeDir/"$Strain"_Total_CRN_expressed.gtf | grep -w 'transcript' | sort -r -n -k 14 -t '"' | cut -f4,14 -d '"' --output-delimite " - " | cut -f1 -d '.')
    do
        echo "$Gene"
        cat gene_pred/interproscan/P.fragariae/$Strain/"$Strain"_interproscan.tsv | grep '$Gene'
        cat gene_pred/swissprot/P.fragariae/$Strain/"$Strain"_swissprot_v2015_10_hits.tbl  | grep '$Gene'
        echo ""
    done
done
```

#Now feed into orthmcl shell script
