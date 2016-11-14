An assembly has been published by a Chinese group and is available on Genbank, but the assembly looks of low quality and he paper is poorly written so confirming that it definitely is _Phytophthora fragariae_. BLAST analysis has shown β-tubulin to have the _P. fragariae_ type SNP, and ITS was not found by BLAST.

#Assembly downloaded from Genbank

```bash
mkdir -p assembly/downloaded/P.fragariae/309.62
cd assembly/downloaded/P.fragariae/309.62
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/686/205/GCA_000686205.3_ASM68620v3/GCA_000686205.3_ASM68620v3_genomic.fna.gz
gunzip GCA_000686205.3_ASM68620v3_genomic.fna.gz
```

#Promer alignment of Assemblies

##against _Phytophthora fragariae_ BC-1 genome

MUMmer was run to align assemblies against the reference genome.

```bash
Reference=repeat_masked/P.fragariae/Bc1/filtered_contigs_repmask/Bc1_contigs_softmasked_repeatmasker_TPSI_appended.fa
Query=assembly/downloaded/P.fragariae/309.62/GCA_000686205.3_ASM68620v3_genomic.fna
Strain=$(echo $Query | rev | cut -f2 -d '/' | rev)
Organism=$(echo $Query | rev | cut -f3 -d '/' | rev)
echo "$Organism - $Strain"
Prefix="$Strain"_vs_Bc1
OutDir=analysis/genome_alignment/mummer/$Organism/$Strain/$Prefix
ProgDir=/home/adamst/git_repos/tools/seq_tools/genome_alignment/promer
qsub $ProgDir/sub_MUMmer.sh $Reference $Query $Prefix $OutDir
```

The number of bases of the reference covered with aligned reads were identified. The script below converts any base involved in an alignment to a 'Q' and then counts the number of Qs in each fasta sequence.

```bash
Reference=repeat_masked/P.fragariae/Bc1/filtered_contigs_repmask/Bc1_contigs_softmasked_repeatmasker_TPSI_appended.fa
Coordinates=analysis/genome_alignment/mummer/P.fragariae/309.62/309.62_vs_Bc1/*_vs_Bc1_coords.tsv
Strain=$(echo $Coordinates | rev | cut -f3 -d '/' | rev)
Organism=$(echo $Coordinates | rev | cut -f4 -d '/' | rev)
echo "$Organism - $Strain"
OutFile=$(echo $Coordinates | sed 's/_coords.tsv/_results.tsv/g')
Out10kb=$(echo $Coordinates | sed 's/_coords.tsv/_results_10kb.tsv/g')
ProgDir=/home/adamst/git_repos/tools/seq_tools/genome_alignment/promer
$ProgDir/mummer_ls_regions.py --coord $Coordinates --fasta $Reference --out_contig $OutFile --out_10kb $Out10kb
paste analysis/genome_alignment/mummer/P*/*/*/*_vs_Bc1_results.tsv > analysis/genome_alignment/mummer/vs_Bc1_new.tsv
```

##against SCRP333 genome

```bash
Reference=../phytophthora_rubi/repeat_masked/spades/P.rubi/SCRP333/filtered_contigs_repmask/SCRP333_contigs_softmasked_repeatmasker_TPSI_appended.fa
Query=assembly/downloaded/P.fragariae/309.62/GCA_000686205.3_ASM68620v3_genomic.fna
Strain=$(echo $Query | rev | cut -f2 -d '/' | rev)
Organism=$(echo $Query | rev | cut -f3 -d '/' | rev)
echo "$Organism - $Strain"
Prefix="$Strain"_vs_SCRP333
OutDir=analysis/genome_alignment/mummer/$Organism/$Strain/$Prefix
ProgDir=/home/adamst/git_repos/tools/seq_tools/genome_alignment/promer
qsub $ProgDir/sub_MUMmer.sh $Reference $Query $Prefix $OutDir
```

The number of bases of the reference covered with aligned reads were identified. The script below converts any base involved in an alignment to a 'Q' and then counts the number of Qs in each fasta sequence.

```bash
Reference=../phytophthora_rubi/repeat_masked/spades/P.rubi/SCRP333/filtered_contigs_repmask/SCRP333_contigs_softmasked_repeatmasker_TPSI_appended.fa
Coordinates=analysis/genome_alignment/mummer/P.fragariae/309.62/309.62_vs_SCRP333/*_vs_SCRP333_coords.tsv
Strain=$(echo $Coordinates | rev | cut -f3 -d '/' | rev)
Organism=$(echo $Coordinates | rev | cut -f4 -d '/' | rev)
echo "$Organism - $Strain"
OutFile=$(echo $Coordinates | sed 's/_coords.tsv/_results.tsv/g')
Out10kb=$(echo $Coordinates | sed 's/_coords.tsv/_results_10kb.tsv/g')
ProgDir=/home/adamst/git_repos/tools/seq_tools/genome_alignment/promer
$ProgDir/mummer_ls_regions.py --coord $Coordinates --fasta $Reference --out_contig $OutFile --out_10kb $Out10kb
paste analysis/genome_alignment/mummer/P*/*/*/*_vs_SCRP333_results.tsv > analysis/genome_alignment/mummer/vs_SCRP333_new.tsv
```
