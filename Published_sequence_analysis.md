An assembly has been published by a Chinese group and is available on Genbank, but the assembly looks of low quality and he paper is poorly written so confirming that it definitely is _Phytophthora fragariae_. BLAST analysis has shown β-tubulin to have the _P. fragariae_ type SNP, and ITS was not found by BLAST.

#Assembly downloaded from Genbank

```bash
mkdir -p assembly/downloaded/P.fragariae/309.62
cd assembly/downloaded/P.fragariae/309.62
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/686/205/GCA_000686205.3_ASM68620v3/GCA_000686205.3_ASM68620v3_genomic.fna.gz
gunzip GCA_000686205.3_ASM68620v3_genomic.fna.gz
```

#Promer alignment of Assemblies

##against _Phytophthora fragariae_ BC-16 genome

MUMmer was run to align assemblies against the reference genome.

```bash
Reference=repeat_masked/P.fragariae/Bc16/filtered_contigs_repmask/95m_contigs_softmasked_repeatmasker_TPSI_appended.fa
Query=assembly/downloaded/P.fragariae/309.62/GCA_000686205.3_ASM68620v3_genomic.fna
Strain=$(echo $Query | rev | cut -f2 -d '/' | rev)
Organism=$(echo $Query | rev | cut -f3 -d '/' | rev)
echo "$Organism - $Strain"
Prefix="$Strain"_vs_Bc16
OutDir=analysis/genome_alignment/mummer/$Organism/$Strain/$Prefix
ProgDir=/home/adamst/git_repos/tools/seq_tools/genome_alignment/promer
qsub $ProgDir/sub_MUMmer.sh $Reference $Query $Prefix $OutDir
```

The number of bases of the reference covered with aligned reads were identified. The script below converts any base involved in an alignment to a 'Q' and then counts the number of Qs in each fasta sequence.

Reference=$(ls repeat_masked/*/*/*/*_contigs_hardmasked_repeatmasker_TPSI_appended.fa | grep -w 'Fus2_canu_new')
# for Coordinates in $(ls analysis/genome_alignment/mummer/F*/*/*/*_vs_Fus2_coords.tsv | grep -e 'ncbi' -e 'Fus2_canu_new' -e '4287_chromosomal' -e 'fo47' | grep -e '4287_chromosomal' -e 'fo47'); do
for Coordinates in $(ls analysis/genome_alignment/mummer/F*/*/*/*_vs_Fus2_coords.tsv | grep -e 'ncbi' -e 'Fus2_canu_new' -e '4287_chromosomal' -e 'fo47'); do
Strain=$(echo $Coordinates | rev | cut -f3 -d '/' | rev)
Organism=$(echo $Coordinates | rev | cut -f4 -d '/' | rev)
echo "$Organism - $Strain"
OutFile=$(echo $Coordinates | sed 's/_coords.tsv/_results.tsv/g')
Out10kb=$(echo $Coordinates | sed 's/_coords.tsv/_results_10kb.tsv/g')
ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/genome_alignment/promer
$ProgDir/mummer_ls_regions.py --coord $Coordinates --fasta $Reference --out_contig $OutFile --out_10kb $Out10kb
done
paste analysis/genome_alignment/mummer/F*/*/*/*_vs_Fus2_results.tsv > analysis/genome_alignment/mummer/vs_Fus2_canu_new.tsv
Sequences tend to show 50-70% of bp being covered by an aligned sequence in core contigs whereas 1-35% seem to represent regions which are LS. The weakness of this methodology is shown by mitochondrial sequence being absent as that seems to have not assembled in the majority of assemblies and with the long contigs of the reference genome seeming to have poorer alignment stats than MiSeq assemblies.

5.2 against FoL genome

Reference=$(ls repeat_masked/*/*/*/*_contigs_hardmasked_repeatmasker_TPSI_appended.fa | grep -w '4287_chromosomal')
for Query in $(ls repeat_masked/*/*/*/*_contigs_hardmasked_repeatmasker_TPSI_appended.fa | grep -w -e 'Fus2_canu_new' -e 'ncbi_submission' -e '4287_chromosomal' -e 'fo47'); do
Strain=$(echo $Query | rev | cut -f3 -d '/' | rev)
Organism=$(echo $Query | rev | cut -f4 -d '/' | rev)
echo "$Organism - $Strain"
Prefix="$Strain"_vs_FoL
OutDir=analysis/genome_alignment/mummer/$Organism/$Strain/$Prefix
ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/genome_alignment/promer
qsub $ProgDir/sub_MUMmer.sh $Reference $Query $Prefix $OutDir
done
The number of bases of the reference covered with aligned reads were identified. The script below converts any base involved in an alignment to a 'Q' and then counts the number of Qs in each fasta sequence.

Reference=$(ls repeat_masked/*/*/*/*_contigs_hardmasked_repeatmasker_TPSI_appended.fa | grep -w '4287_chromosomal')
for Coordinates in $(ls analysis/genome_alignment/mummer/F*/*/*/*_vs_FoL_coords.tsv | grep -e 'ncbi' -e 'Fus2_canu_new' -e '4287_chromosomal' -e 'fo47'); do
  Strain=$(echo $Coordinates | rev | cut -f3 -d '/' | rev)
  Organism=$(echo $Coordinates | rev | cut -f4 -d '/' | rev)
  echo "$Organism - $Strain"
  OutFile=$(echo $Coordinates | sed 's/_coords.tsv/_results.tsv/g')
  Out10kb=$(echo $Coordinates | sed 's/_coords.tsv/_results_10kb.tsv/g')
  ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/genome_alignment/promer
  $ProgDir/mummer_ls_regions.py --coord $Coordinates --fasta $Reference --out_contig $OutFile --out_10kb $Out10kbdone
paste analysis/genome_alignment/mummer/F*/*/*/*_vs_FoL_results.tsv > analysis/genome_alignment/mummer/vs_FoL_canu_new.tsv
