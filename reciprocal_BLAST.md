#Run a reciprocal BLAST of every RxLR that shows evidence of expression against the genomes of race 1 and 3 isolates. Use a python script from external developers: https://github.com/peterjc/galaxy_blast/blob/master/tools/blast_rbh/blast_rbh.py

Cite the following if this is used for any publication:
NCBI BLAST+ integrated into Galaxy. P.J.A. Cock, J.M. Chilton, B. Gruening, J.E. Johnson, N. Soranzo GigaScience 2015, 4:39 DOI: http://dx.doi.org/10.1186/s13742-015-0080-7

You should also cite the NCBI BLAST+ tools:

BLAST+: architecture and applications. C. Camacho et al. BMC Bioinformatics 2009, 10:421. DOI: http://dx.doi.org/10.1186/1471-2105-10-421

##Set up directory with required fasta files

```bash
WorkDir=analysis/Reciprocal_BLAST
mkdir -p $WorkDir
RxLRDir=analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/
cat $RxLRDir/Bc16_expressed_RxLR_headers.txt | sed 's/.t1//g' > $WorkDir/Bc16_expressed_RxLR_headers_parsed.txt
RxLRs=$WorkDir/Bc16_expressed_RxLR_headers_parsed.txt
for Strain in Bc1 Nov5
do
    Assembly=repeat_masked/P.fragariae/$Strain/deconseq_Paen_repmask/"$Strain"_contigs_unmasked.fa
    cat $Assembly | sed "s/>/>"$Strain"_/g" >> $WorkDir/UK1_genomes.fa
done
for Strain in Nov71 Nov9 Nov27
do
    Assembly=repeat_masked/P.fragariae/$Strain/deconseq_Paen_repmask/"$Strain"_contigs_unmasked.fa
    cat $Assembly | sed "s/>/>"$Strain"_/g" >> $WorkDir/UK3_genomes.fa
done
ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
Genome=gene_pred/annotation/P.fragariae/Bc16/Bc16_genes_incl_ORFeffectors.gene.fasta
$ProgDir/extract_from_fasta.py --fasta $Genome --headers $RxLRs > $WorkDir/Bc16_expressed_RxLR.fa
```

##Run python script from external developers

```bash
WorkDir=analysis/Reciprocal_BLAST
GeneDir=gene_pred/annotation/P.fragariae/Bc16
/home/adamst/git_repos/scripts/blast_rbh.py -a nucl -t blastn -o $WorkDir/Bc16_vs_UK1.tsv $GeneDir/Bc16_genes_incl_ORFeffectors.gene.fasta $WorkDir/UK1_genomes.fa

WorkDir=analysis/Reciprocal_BLAST
/home/adamst/git_repos/scripts/blast_rbh.py -a nucl -t blastn -o $WorkDir/Bc16_vs_UK3.tsv $GeneDir/Bc16_genes_incl_ORFeffectors.gene.fasta $WorkDir/UK3_genomes.fa
```
