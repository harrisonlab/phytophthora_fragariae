##Analysis of RxLR effectors

#11 Phytophthora fragariae strains (A4, BC-1, BC-16, BC-23, NOV-27, NOV-5, NOV-71, NOV-77, NOV-9, ONT-3, SCRP245_v2) have had effectors predicted via various means, using Braker1 models. These commands combine the datasets for orthology analysis.

```bash
A4Braker1Gff=gene_pred/braker/P.fragariae/A4/P.fragariae_A4_braker/augustus_extracted.gff
Bc1Braker1Gff=gene_pred/braker/P.fragariae/Bc1/P.fragariae_Bc1_braker/augustus_extracted.gff
Bc16Braker1Gff=gene_pred/braker/P.fragariae/Bc16/P.fragariae_Bc16_braker/augustus_extracted.gff
Bc23Braker1Gff=gene_pred/braker/P.fragariae/Bc23/P.fragariae_Bc23_braker/augustus_extracted.gff
Nov27Braker1Gff=gene_pred/braker/P.fragariae/Nov27/P.fragariae_Nov27_braker/augustus_extracted.gff
Nov5Braker1Gff=gene_pred/braker/P.fragariae/Nov5/P.fragariae_Nov5_braker/augustus_extracted.gff
Nov71Braker1Gff=gene_pred/braker/P.fragariae/Nov71/P.fragariae_Nov71_braker/augustus_extracted.gff
Nov77Braker1Gff=gene_pred/braker/P.fragariae/Nov77/P.fragariae_Nov77_braker/augustus_extracted.gff
Nov9Braker1Gff=gene_pred/braker/P.fragariae/Nov9/P.fragariae_Nov9_braker/augustus_extracted.gff
ONT3Braker1Gff=gene_pred/braker/P.fragariae/ONT3/P.fragariae_ONT3_braker/augustus_extracted.gff
SCRP245_v2Braker1Gff=gene_pred/braker/P.fragariae/SCRP245_v2/P.fragariae_SCRP245_v2_braker/augustus_extracted.gff
for GeneGff in $A4Braker1Gff $Bc1Braker1Gff $Bc16Braker1Gff $Bc23Braker1Gff $Nov27Braker1Gff $Nov5Braker1Gff $Nov71Braker1Gff $Nov77Braker1Gff $Nov9Braker1Gff $ONT3Braker1Gff $SCRP245_v2Braker1Gff
do
    echo "$GeneGff"
    Strain=$(echo "$GeneGff" | rev | cut -f3 -d '/' | rev)
    Species=$(echo "$GeneGff" | rev | cut -f4 -d '/' | rev)
    InDir=$(ls -d analysis/RxLR_effectors/RxLR_EER_regex_finder/$Species/$Strain)
    Source="Braker1"
    RxLR_motif=$(ls analysis/RxLR_effectors/RxLR_EER_regex_finder/$Species/$Strain/"$Strain"_braker_RxLR_EER_regex.txt)
    RxLR_hmm=$(ls analysis/RxLR_effectors/hmmer_RxLR/$Species/$Strain/"$Strain"_pub_RxLR_hmmer_headers.txt)
    WY_hmm=$(ls analysis/RxLR_effectors/hmmer_WY/$Species/$Strain/"$Strain"_pub_WY_hmmer_headers.txt)
    echo "$Species - $Strain"
    echo "Total number of RxLRs in predicted genes:"
    cat $RxLR_motif $RxLR_hmm | cut -f1 -d' ' | sort | uniq | wc -l
    echo "Total number of RxLRs shared between prediction sources:"
    cat $RxLR_motif $RxLR_hmm | cut -f1 -d' ' | sort | uniq -d | wc -l
    OutDir=analysis/RxLR_effectors/combined_evidence/$Species/$Strain
    mkdir -p $OutDir
    cat $RxLR_motif $RxLR_hmm | cut -f1 -d' ' | sort | uniq | rev | cut -f2 -d '|' | rev > $OutDir/"$Strain"_"$Source"_RxLR_EER_motif_hmm_headers.txt
    echo "The number of combined RxLR containing proteins containing WY domains are:"
    cat $OutDir/"$Strain"_Braker1_RxLR_EER_motif_hmm_headers.txt $WY_hmm | cut -f1 -d' ' | rev | cut -f2 -d '|' | rev | sort | uniq -d | wc -l
    echo ""
    cat $GeneGff | grep -w -f $OutDir/"$Strain"_"$Source"_RxLR_EER_motif_hmm_headers.txt > $OutDir/"$Strain"_"$Source"_RxLR_EER_motif_hmm.gff
done
```

```
P.fragariae - A4
Total number of RxLRs in predicted genes:
356
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing proteins containing WY domains are:
0

P.fragariae - Bc1
Total number of RxLRs in predicted genes:
399
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing proteins containing WY domains are:
85

P.fragariae - Bc16
Total number of RxLRs in predicted genes:
371
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing proteins containing WY domains are:
81

P.fragariae - Bc23
Total number of RxLRs in predicted genes:
337
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing proteins containing WY domains are:
74

P.fragariae - Nov27
Total number of RxLRs in predicted genes:
359
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing proteins containing WY domains are:
78

P.fragariae - Nov5
Total number of RxLRs in predicted genes:
373
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing proteins containing WY domains are:
80

P.fragariae - Nov71
Total number of RxLRs in predicted genes:
396
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing proteins containing WY domains are:
86

P.fragariae - Nov77
Total number of RxLRs in predicted genes:
359
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing proteins containing WY domains are:
2

P.fragariae - Nov9
Total number of RxLRs in predicted genes:
377
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing proteins containing WY domains are:
80

P.fragariae - ONT3
Total number of RxLRs in predicted genes:
369
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing proteins containing WY domains are:
79

P.fragariae - SCRP245_v2
Total number of RxLRs in predicted genes:
331
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing proteins containing WY domains are:
1
```

##Analysis of RxLR effectors - ORF gene models

#Due to RxLR effectors being predicted from a number of sources, the number of unique RxLRs were identified using these commands

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    InDir=analysis/RxLR_effectors/RxLR_EER_regex_finder/P.fragariae/$Strain
    Strain=$(echo "$InDir" | rev | cut -f1 -d '/' | rev)
    Species=$(echo "$InDir" | rev | cut -f2 -d '/' | rev)
    RxLR_motif=$(ls analysis/RxLR_effectors/RxLR_EER_regex_finder/$Species/$Strain/"$Strain"_ORF_RxLR_EER_regex.txt)
    RxLR_motif=$(ls analysis/RxLR_effectors/RxLR_EER_regex_finder/$Species/$Strain/"$Strain"_ORF_RxLR_EER_regex.txt)
    WY_hmm=$(ls analysis/RxLR_effectors/hmmer_WY/$Species/$Strain/"$Strain"_ORF_WY_hmmer_headers.txt)
    echo "$Species - $Strain"
    echo "Total number of RxLRs in predicted ORFs:"
    cat $RxLR_motif $RxLR_hmm | cut -f1 -d' ' | sort | uniq | wc -l
    echo "Total number of RxLRs shared between prediction sources:"
    cat $RxLR_motif $RxLR_hmm | cut -f1 -d' ' | sort | uniq -d | wc -l
    OutDir=analysis/RxLR_effectors/combined_evidence/$Species/$Strain
    mkdir -p $OutDir
    cat $RxLR_motif $RxLR_hmm | cut -f1 -d' ' | sort | uniq > $OutDir/"$Strain"_ORF_RxLR_EER_motif_hmm_headers.txt
    echo "The number of combined RxLR containing ORFs containing WY domains are:"
    cat $OutDir/"$Strain"_ORF_RxLR_EER_motif_hmm_headers.txt $WY_hmm | cut -f1 -d' ' | sort | uniq -d | wc -l
    echo ""
    GeneModels=$(ls gene_pred/ORF_finder/$Species/$Strain/"$Strain"_ORF_corrected.gff3)
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
    $ProgDir/gene_list_to_gff.pl $OutDir/"$Strain"_ORF_RxLR_EER_motif_hmm_headers.txt $GeneModels RxLR_EER_combined Name Augustus > $OutDir/"$Strain"_ORF_RxLR_EER_motif_hmm.gff
done
```

```
P.fragariae - A4
Total number of RxLRs in predicted ORFs:
419
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing ORFs containing WY domains are:
88

P.fragariae - Bc1
Total number of RxLRs in predicted ORFs:
420
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing ORFs containing WY domains are:
89

P.fragariae - Bc16
Total number of RxLRs in predicted ORFs:
418
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing ORFs containing WY domains are:
89

P.fragariae - Bc23
Total number of RxLRs in predicted ORFs:
397
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing ORFs containing WY domains are:
82

P.fragariae - Nov27
Total number of RxLRs in predicted ORFs:
421
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing ORFs containing WY domains are:
89

P.fragariae - Nov5
Total number of RxLRs in predicted ORFs:
419
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing ORFs containing WY domains are:
89

P.fragariae - Nov71
Total number of RxLRs in predicted ORFs:
417
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing ORFs containing WY domains are:
91

P.fragariae - Nov77
Total number of RxLRs in predicted ORFs:
406
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing ORFs containing WY domains are:
76

P.fragariae - Nov9
Total number of RxLRs in predicted ORFs:
417
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing ORFs containing WY domains are:
90

P.fragariae - ONT3
Total number of RxLRs in predicted ORFs:
433
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing ORFs containing WY domains are:
95

P.fragariae - SCRP245_v2
Total number of RxLRs in predicted ORFs:
396
Total number of RxLRs shared between prediction sources:
0
The number of combined RxLR containing ORFs containing WY domains are:
80
```

##Analysis of RxLR effectors - merger of Augustus / published genes with ORFs

#Intersection between the RxLRs from gene models and ORFs were identified to determine the total number of RxLRs in these genomes.

#The RxLR effectors from both Gene models and ORF finding approaches were combined into a single file.

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    MergeDir=analysis/RxLR_effectors/combined_evidence/P.fragariae/$Strain
    Strain=$(echo "$MergeDir" | rev | cut -f1 -d '/' | rev)
    Species=$(echo "$MergeDir" | rev | cut -f2 -d '/' | rev)
    Braker1Gff=$MergeDir/"$Strain"_Braker1_RxLR_EER_motif_hmm.gff
    ORFGff=$MergeDir/"$Strain"_ORF_RxLR_EER_motif_hmm.gff
    WY_Braker1_hmm=$(ls analysis/RxLR_effectors/hmmer_WY/$Species/$Strain/"$Strain"_pub_WY_hmmer_headers.txt | grep -v 'ORF')
    WY_ORF_hmm=$(ls analysis/RxLR_effectors/hmmer_WY/$Species/$Strain/"$Strain"_ORF_WY_hmmer_headers.txt)
    ORFsInBraker1=$MergeDir/"$Strain"_ORFsInBraker1_RxLR_EER_motif_hmm.gff
    Braker1InORFs=$MergeDir/"$Strain"_Braker1InORFs_RxLR_EER_motif_hmm.gff
    ORFsUniq=$MergeDir/"$Strain"_ORFsUniq_RxLR_EER_motif_hmm.gff
    Braker1Uniq=$MergeDir/"$Strain"_Braker1_Uniq_RxLR_EER_motif_hmm.gff
    TotalRxLRsTxt=$MergeDir/"$Strain"_Total_RxLR_EER_motif_hmm.txt
    TotalRxLRsGff=$MergeDir/"$Strain"_Total_RxLR_EER_motif_hmm.gff
    TotalRxLRsWYTxt=$MergeDir/"$Strain"_Total_RxLR_EER_WY_motif_hmm.txt
    TotalRxLRsWYGff=$MergeDir/"$Strain"_Total_RxLR_EER_WY_motif_hmm.gff
    TotalRxLRsHeaders=$MergeDir/"$Strain"_Total_RxLR_EER_motif_hmm_headers.txt
    bedtools intersect -wa -u -a $ORFGff -b $Braker1Gff > $ORFsInBraker1
    bedtools intersect -wa -u -a $Braker1Gff -b $ORFGff > $Braker1InORFs
    bedtools intersect -v -wa -a $ORFGff -b $Braker1Gff > $ORFsUniq
    bedtools intersect -v -wa -a $Braker1Gff -b $ORFGff > $Braker1Uniq
    echo "$Species - $Strain"
    echo "The number of ORF RxLRs overlapping Braker1 RxLRs:"
    cat $ORFsInBraker1 | grep -w 'gene' | wc -l
    echo "The number of Braker1 RxLRs overlapping ORF RxLRs:"
    cat $Braker1InORFs | grep -w 'gene' | wc -l
    echo "The number of RxLRs unique to ORF models:"
    cat $ORFsUniq | grep -w 'transcript' | cut -f9 | cut -f5 -d '=' | wc -l
    cat $ORFsUniq | grep -w 'transcript' | cut -f9 | cut -f5 -d '=' >> $TotalRxLRsTxt
    echo "The number of RxLRs unique to Braker1 models:"
    cat $Braker1Uniq | grep -w 'gene' | wc -l
    echo "The total number of putative RxLRs are:"
    cat $Braker1InORFs | grep -w 'gene' | cut -f9 > $TotalRxLRsTxt
    cat $Braker1Uniq | grep -w 'gene' | cut -f9 >> $TotalRxLRsTxt
    cat $ORFsUniq | grep -w 'transcript' | cut -f9 | cut -f4 -d '=' >> $TotalRxLRsTxt
    cat $TotalRxLRsTxt | wc -l
    echo "The number of these RxLRs containing WY domains are:"
    cat $TotalRxLRsTxt $WY_Braker1_hmm $WY_ORF_hmm | cut -f1 -d ' ' | rev | cut -f2 -d '|' | rev | sort | uniq -d > $TotalRxLRsWYTxt
    cat $TotalRxLRsWYTxt | wc -l
    cat $Braker1InORFs $Braker1Uniq $ORFsUniq | grep -w -f $TotalRxLRsTxt > $TotalRxLRsGff
    cat $Braker1InORFs $Braker1Uniq $ORFsUniq | grep -w -f $TotalRxLRsWYTxt > $TotalRxLRsWYGff
done
```

```
P.fragariae - A4
The number of ORF RxLRs overlapping Braker1 RxLRs:
52
The number of Braker1 RxLRs overlapping ORF RxLRs:
0
The number of RxLRs unique to ORF models:
166
The number of RxLRs unique to Braker1 models:
170
The total number of putative RxLRs are:
336
The number of these RxLRs containing WY domains are:
53
P.fragariae - Bc1
The number of ORF RxLRs overlapping Braker1 RxLRs:
193
The number of Braker1 RxLRs overlapping ORF RxLRs:
190
The number of RxLRs unique to ORF models:
52
The number of RxLRs unique to Braker1 models:
3
The total number of putative RxLRs are:
245
The number of these RxLRs containing WY domains are:
90
P.fragariae - Bc16
The number of ORF RxLRs overlapping Braker1 RxLRs:
179
The number of Braker1 RxLRs overlapping ORF RxLRs:
171
The number of RxLRs unique to ORF models:
64
The number of RxLRs unique to Braker1 models:
2
The total number of putative RxLRs are:
237
The number of these RxLRs containing WY domains are:
89
P.fragariae - Bc23
The number of ORF RxLRs overlapping Braker1 RxLRs:
172
The number of Braker1 RxLRs overlapping ORF RxLRs:
166
The number of RxLRs unique to ORF models:
50
The number of RxLRs unique to Braker1 models:
0
The total number of putative RxLRs are:
216
The number of these RxLRs containing WY domains are:
81
P.fragariae - Nov27
The number of ORF RxLRs overlapping Braker1 RxLRs:
180
The number of Braker1 RxLRs overlapping ORF RxLRs:
172
The number of RxLRs unique to ORF models:
66
The number of RxLRs unique to Braker1 models:
0
The total number of putative RxLRs are:
238
The number of these RxLRs containing WY domains are:
87
P.fragariae - Nov5
The number of ORF RxLRs overlapping Braker1 RxLRs:
186
The number of Braker1 RxLRs overlapping ORF RxLRs:
179
The number of RxLRs unique to ORF models:
58
The number of RxLRs unique to Braker1 models:
1
The total number of putative RxLRs are:
238
The number of these RxLRs containing WY domains are:
87
P.fragariae - Nov71
The number of ORF RxLRs overlapping Braker1 RxLRs:
191
The number of Braker1 RxLRs overlapping ORF RxLRs:
189
The number of RxLRs unique to ORF models:
51
The number of RxLRs unique to Braker1 models:
2
The total number of putative RxLRs are:
242
The number of these RxLRs containing WY domains are:
91
P.fragariae - Nov77
The number of ORF RxLRs overlapping Braker1 RxLRs:
49
The number of Braker1 RxLRs overlapping ORF RxLRs:
1
The number of RxLRs unique to ORF models:
160
The number of RxLRs unique to Braker1 models:
164
The total number of putative RxLRs are:
325
The number of these RxLRs containing WY domains are:
55
P.fragariae - Nov9
The number of ORF RxLRs overlapping Braker1 RxLRs:
187
The number of Braker1 RxLRs overlapping ORF RxLRs:
181
The number of RxLRs unique to ORF models:
55
The number of RxLRs unique to Braker1 models:
1
The total number of putative RxLRs are:
237
The number of these RxLRs containing WY domains are:
89
P.fragariae - ONT3
The number of ORF RxLRs overlapping Braker1 RxLRs:
181
The number of Braker1 RxLRs overlapping ORF RxLRs:
173
The number of RxLRs unique to ORF models:
77
The number of RxLRs unique to Braker1 models:
1
The total number of putative RxLRs are:
251
The number of these RxLRs containing WY domains are:
93
P.fragariae - SCRP245_v2
The number of ORF RxLRs overlapping Braker1 RxLRs:
26
The number of Braker1 RxLRs overlapping ORF RxLRs:
1
The number of RxLRs unique to ORF models:
173
The number of RxLRs unique to Braker1 models:
155
The total number of putative RxLRs are:
329
The number of these RxLRs containing WY domains are:
61
```

#FASTA sequences for RxLRs were extracted for each isolate

```bash
A4Fa=gene_pred/braker/P.fragariae/A4/P.fragariae_A4_braker/augustus.aa
Bc1Fa=gene_pred/braker/P.fragariae/Bc1/P.fragariae_Bc1_braker/augustus.aa
Bc16Fa=gene_pred/braker/P.fragariae/Bc16/P.fragariae_Bc16_braker/augustus.aa
Bc23Fa=gene_pred/braker/P.fragariae/Bc23/P.fragariae_Bc23_braker/augustus.aa
Nov27Fa=gene_pred/braker/P.fragariae/Nov27/P.fragariae_Nov27_braker/augustus.aa
Nov5Fa=gene_pred/braker/P.fragariae/Nov5/P.fragariae_Nov5_braker/augustus.aa
Nov71Fa=gene_pred/braker/P.fragariae/Nov71/P.fragariae_Nov71_braker/augustus.aa
Nov77Fa=gene_pred/braker/P.fragariae/Nov77/P.fragariae_Nov77_braker/augustus.aa
Nov9Fa=gene_pred/braker/P.fragariae/Nov9/P.fragariae_Nov9_braker/augustus.aa
ONT3Fa=gene_pred/braker/P.fragariae/ONT3/P.fragariae_ONT3_braker/augustus.aa
SCRP245_v2Fa=gene_pred/braker/P.fragariae/SCRP245_v2/P.fragariae_SCRP245_v2_braker/augustus.aa

for Braker1Fa in $A4Fa $Bc1Fa $Bc16Fa $Bc23Fa $Nov27Fa $Nov5Fa $Nov71Fa $Nov77Fa $Nov9Fa $ONT3Fa $SCRP245_v2Fa
do
    Strain=$(echo "$Braker1Fa" | rev | cut -f3 -d '/' | rev)
    Species=$(echo "$Braker1Fa" | rev | cut -f4 -d '/' | rev)
    ORFsFa=$(ls gene_pred/ORF_finder/"$Species"/"$Strain"/"$Strain".aa_cat.fa)
    MergeDir=analysis/RxLR_effectors/combined_evidence/$Species/$Strain
    TotalRxLRsHeaders=$MergeDir/"$Strain"_Total_RxLR_EER_motif_hmm_headers.txt
    RxLRsFa=$MergeDir/"$Strain"_Total_RxLR_EER_motif_hmm_headers.fa
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
    $ProgDir/unwrap_fasta.py --inp_fasta $Braker1Fa | grep -A1 -w -f $TotalRxLRsTxt | grep -v -E '^--$' > $RxLRsFa
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    $ProgDir/extract_from_fasta.py --fasta $ORFsFa --headers $TotalRxLRsTxt >> $RxLRsFa
    echo "$Strain"
    echo "The number of sequences extracted is:"
    cat $RxLRsFa | grep '>' | wc -l
done
```

```
```

##Expression of RxLRs

#RNAseq data from P.cactorum 10300 was used to approximate expression support with Braker1.

#This was done by intersecting the location of RxLRs with the RNAseq data aligned to the genomes of the 11 strains.

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    MergeDir=analysis/RxLR_effectors/combined_evidence/P.fragariae/$Strain
    Strain=$(echo "$MergeDir" | rev | cut -f1 -d '/' | rev)
    TotalRxLRsGff=$MergeDir/"$Strain"_Total_RxLR_EER_motif_hmm_headers.gff

    cufflinks -o tmp -p 16 -G gene_pred/braker/P.fragariae/$Strain/P.fragariae*/augustus_extracted.gff alignment/P.fragariae/$Strain/accepted_hits.bam
    bedtools intersect -s -u -a tmp/transcripts.gtf -b $TotalRxLRsGff  > analysis/RxLR_effectors/combined_evidence/P.fragariae/$Strain/"$Strain"_Total_RxLR_EER_motif_hmm_expressed.gtf
    echo "The top 20 expressed RxLRs are:"
    cat analysis/RxLR_effectors/combined_evidence/P.fragariae/$Strain/"$Strain"_Total_RxLR_EER_motif_hmm_expressed.gtf | grep -w 'transcript' | sort -r -n -k 14 -t '"' | cut -f2,14 -d '"' --output-delimite " - " |  head -n 20
    echo "The total number of RxLRs was:"
    cat analysis/RxLR_effectors/combined_evidence/P.fragariae/$Strain/"$Strain"_Total_RxLR_EER_motif_hmm_expressed.gtf | grep -w 'transcript' | wc -l
    echo "The number of RxLRs with 1x coverage or greater was:"
    cat analysis/RxLR_effectors/combined_evidence/P.fragariae/$Strain/"$Strain"_Total_RxLR_EER_motif_hmm_expressed.gtf | grep -w 'transcript' | sort -r -n -k 14 -t '"' | cut -f14 -d '"' | grep -v -E '0\.' | wc -l
    echo "The number of RxLRs with 0x coverage was:"
    cat analysis/RxLR_effectors/combined_evidence/P.fragariae/$Strain/"$Strain"_Total_RxLR_EER_motif_hmm_expressed.gtf | grep -w 'transcript' | sort -r -n -k 14 -t '"' | cut -f14 -d '"' | grep -E '0\.00' | wc -l
done
```

```
```

##Functional annotation of RxLRs

#Interproscan annotations and swissprot similarities were identified for RxLRs from each strain.

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    MergeDir=analysis/RxLR_effectors/combined_evidence/P.fragariae/$Strain
    for Gene in $(cat $MergeDir/"$Strain"_Total_RxLR_EER_motif_hmm_expressed.gtf | grep -w 'transcript' | sort -r -n -k 14 -t '"' | cut -f4,14 -d '"' --output-delimite " - " | cut -f1 -d '.')
    do
        echo "$Gene"
        cat gene_pred/interproscan/P.fragariae/$Strain/"$Strain"_interproscan.tsv | grep '$Gene'
        cat gene_pred/swissprot/P.fragariae/$Strain/swissprot_v2015_10_hits.tbl | grep '$Gene'
        echo ""
    done
done
```

##Analysis of Crinkler effectors - merger of Braker1 genes with ORFs

#Intersection between the putative CRNs from gene models and ORFs were identified to determine the total number of CRNs in these genomes.

#The CRN effectors from both Gene models and ORF finding approaches were combined into a single file.

```bash
A4Braker1Gff=gene_pred/braker/P.fragariae/A4/P.fragariae_A4_braker/augustus_extracted.gff
Bc1Braker1Gff=gene_pred/braker/P.fragariae/Bc1/P.fragariae_Bc1_braker/augustus_extracted.gff
Bc16Braker1Gff=gene_pred/braker/P.fragariae/Bc16/P.fragariae_Bc16_braker/augustus_extracted.gff
Bc23Braker1Gff=gene_pred/braker/P.fragariae/Bc23/P.fragariae_Bc23_braker/augustus_extracted.gff
Nov27Braker1Gff=gene_pred/braker/P.fragariae/Nov27/P.fragariae_Nov27_braker/augustus_extracted.gff
Nov5Braker1Gff=gene_pred/braker/P.fragariae/Nov5/P.fragariae_Nov5_braker/augustus_extracted.gff
Nov71Braker1Gff=gene_pred/braker/P.fragariae/Nov71/P.fragariae_Nov71_braker/augustus_extracted.gff
Nov77Braker1Gff=gene_pred/braker/P.fragariae/Nov77/P.fragariae_Nov77_braker/augustus_extracted.gff
Nov9Braker1Gff=gene_pred/braker/P.fragariae/Nov9/P.fragariae_Nov9_braker/augustus_extracted.gff
ONT3Braker1Gff=gene_pred/braker/P.fragariae/ONT3/P.fragariae_ONT3_braker/augustus_extracted.gff
SCRP245_v2Braker1Gff=gene_pred/braker/P.fragariae/SCRP245_v2/P.fragariae_SCRP245_v2_braker/augustus_extracted.gff
for GeneGff in $A4Braker1Gff $Bc1Braker1Gff $Bc16Braker1Gff $Bc23Braker1Gff $Nov27Braker1Gff $Nov5Braker1Gff $Nov71Braker1Gff $Nov77Braker1Gff $Nov9Braker1Gff $ONT3Braker1Gff $SCRP245_v2Braker1Gff
do
    echo "$GeneGff"
    Strain=$(echo "$GeneGff" | rev | cut -f3 -d '/' | rev)
    Species=$(echo "$GeneGff" | rev | cut -f4 -d '/' | rev)
    CrnDir=$(ls -d analysis/CRN_effectors/hmmer_CRN/$Species/$Strain)
    Source="pred"
    CRN_hmm_txt=analysis/CRN_effectors/hmmer_CRN/$Species/$Strain/"$Strain"_braker1_CRN_hmmer.txt
    CRN_hmm_gff=analysis/CRN_effectors/hmmer_CRN/$Species/$Strain/"$Strain"_braker1_CRN_hmmer.gff
    echo "$Species - $Strain"
    cat $GeneGff | grep -w -f $CRN_hmm_txt > $CRN_hmm_gff
done
```

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    MergeDir=analysis/CRN_effectors/hmmer_CRN/P.fragariae/$Strain
    Strain=$(echo "$MergeDir" | rev | cut -f1 -d '/' | rev)
    Species=$(echo "$MergeDir" | rev | cut -f2 -d '/' | rev)
    Braker1Gff=$MergeDir/"$Strain"_braker1_CRN_hmmer.gff
    ORFGff=$MergeDir/"$Strain"_CRN_merged_hmmer.gff3
    ORFsInBraker1=$MergeDir/"$Strain"_ORFsInBraker1_CRN_hmmer.bed
    Braker1InORFs=$MergeDir/"$Strain"_Braker1InORFs_CRN_hmmer.bed
    ORFsUniq=$MergeDir/"$Strain"_ORFsUniq_CRN_hmmer.bed
    Braker1Uniq=$MergeDir/"$Strain"_Braker1_Uniq_CRN_hmmer.bed
    TotalCRNsTxt=$MergeDir/"$Strain"_Total_CRN.txt
    TotalCRNsGff=$MergeDir/"$Strain"_Total_CRN.gff
    TotalCRNsHeaders=$MergeDir/"$Strain"_Total_CRN_headers.txt
    bedtools intersect -wa -u -a $ORFGff -b $Braker1Gff > $ORFsInBraker1
    bedtools intersect -wa -u -a $Braker1Gff -b $ORFGff > $Braker1InORFs
    bedtools intersect -v -wa -a $ORFGff -b $Braker1Gff > $ORFsUniq
    bedtools intersect -v -wa -a $Braker1Gff -b $ORFGff > $Braker1Uniq
    echo "$Species - $Strain"
    echo "The number of ORF CRNs overlapping Braker1 CRNs:"
    cat $ORFsInBraker1 | grep -w 'gene' | wc -l
    cat $ORFsInBraker1 | grep -w 'gene' > $TotalCRNsTxt
    echo "The number of Braker1 CRNs overlapping ORF CRNs:"
    cat $Braker1InORFs | grep -w 'gene' | wc -l
    cat $Braker1InORFs | grep -w 'gene' >> $TotalCRNsTxt
    echo "The number of CRNs unique to ORF models:"
    cat $ORFsUniq | grep -w 'transcript' | cut -f9 | cut -f5 -d '=' | wc -l
    cat $ORFsUniq | grep -w 'transcript' | cut -f9 | cut -f5 -d '=' >> $TotalCRNsTxt
    echo "The number of CRNs unique to Braker1 models:"
    cat $Braker1Uniq | grep -w 'gene' | wc -l
    cat $Braker1Uniq | grep -w 'gene' >> $TotalCRNsTxt
    cat $Braker1InORFs $Braker1Uniq $ORFsUniq | grep -w -f $TotalCRNsTxt > $TotalCRNsGff
    echo "The total number of CRNs are:"
    cat $TotalCRNsGff | grep 'AUGUSTUS' | cut -f9 > $TotalCRNsHeaders
    cat $TotalCRNsGff | grep -o -E -e 'Name=.*$' -e 'name ".*";' | sed -e 's/^Name=//g' | sed 's/^name "//g' | sed 's/";$//g' | sort | uniq >> $TotalCRNsHeaders
    cat $TotalCRNsHeaders | wc -l
done
```

```
```

#FASTA sequences for CRNs were extracted from each strain

```bash
A4Braker1Gff=gene_pred/braker/P.fragariae/A4/P.fragariae_A4_braker/augustus_extracted.gff
Bc1Braker1Gff=gene_pred/braker/P.fragariae/Bc1/P.fragariae_Bc1_braker/augustus_extracted.gff
Bc16Braker1Gff=gene_pred/braker/P.fragariae/Bc16/P.fragariae_Bc16_braker/augustus_extracted.gff
Bc23Braker1Gff=gene_pred/braker/P.fragariae/Bc23/P.fragariae_Bc23_braker/augustus_extracted.gff
Nov27Braker1Gff=gene_pred/braker/P.fragariae/Nov27/P.fragariae_Nov27_braker/augustus_extracted.gff
Nov5Braker1Gff=gene_pred/braker/P.fragariae/Nov5/P.fragariae_Nov5_braker/augustus_extracted.gff
Nov71Braker1Gff=gene_pred/braker/P.fragariae/Nov71/P.fragariae_Nov71_braker/augustus_extracted.gff
Nov77Braker1Gff=gene_pred/braker/P.fragariae/Nov77/P.fragariae_Nov77_braker/augustus_extracted.gff
Nov9Braker1Gff=gene_pred/braker/P.fragariae/Nov9/P.fragariae_Nov9_braker/augustus_extracted.gff
ONT3Braker1Gff=gene_pred/braker/P.fragariae/ONT3/P.fragariae_ONT3_braker/augustus_extracted.gff
SCRP245_v2Braker1Gff=gene_pred/braker/P.fragariae/SCRP245_v2/P.fragariae_SCRP245_v2_braker/augustus_extracted.gff

for Braker1Fa in $A4Braker1Gff $Bc1Braker1Gff $Bc16Braker1Gff $Bc23Braker1Gff $Nov27Braker1Gff $Nov5Braker1Gff $Nov71Braker1Gff $Nov77Braker1Gff $Nov9Braker1Gff $ONT3Braker1Gff $SCRP245_v2Braker1Gff
do
    Strain=$(echo "$Braker1Fa" | rev | cut -f3 -d '/' | rev)
    Species=$(echo "$Braker1Fa" | rev | cut -f4 -d '/' | rev)
    ORFsFa=$(ls gene_pred/ORF_finder/"$Species"/"$Strain"/"$Strain".aa_cat.fa)
    MergeDir=analysis/CRN_effectors/hmmer_CRN/$Species/$Strain
    TotalCRNsHeaders=$MergeDir/"$Strain"_Total_CRN_headers.txt
    CRNsFa=$MergeDir/"$Strain"_Total_CRN.fa
    ProgDir=/home/adamst/git_repos/tools/seq_tools/feature_annotation
    $ProgDir/unwrap_fasta.py --inp_fasta $Braker1Fa | grep -A1 -w -f $TotalCRNsHeaders | grep -v -E '^--$' > $CRNsFa
    ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
    $ProgDir/extract_from_fasta.py --fasta $ORFsFa --headers $TotalCRNsHeaders >> $CRNsFa
    echo "$Strain"
    echo "The number of sequences extracted is:"
    cat $CRNsFa | grep '>' | wc -l
done
```

##Expression of CRN genes

#Expression data from P.cactorum 10300 was used to estimate expression in each strain.

#This was done by intersecting the location of CRNs with the RNAseq data aligned to each genome.

```bash
for Strain in A4 Bc1 Bc16 Bc23 Nov27 Nov5 Nov71 Nov77 Nov9 ONT3 SCRP245_v2
do
    MergeDir=analysis/CRN_effectors/hmmer_CRN/P.fragariae/$Strain
    Strain=$(echo "$MergeDir" | rev | cut -f1 -d '/' | rev)
    TotalCRNsGff=$MergeDir/"$Strain"_Total_CRN.gff
    cufflinks -o tmp -p 16 -G gene_pred/braker/P.fragariae/$Strain/P.fragariae_"$Strain"_braker/augustus_extracted.gff alignment/P.fragariae/$Strain/accepted_hits.bam
    bedtools intersect -s -u -a tmp/transcripts.gtf -b $TotalCRNsGff  > $MergeDir/"$Strain"_Total_CRN_expressed.gtf
    echo "The top 20 expressed CRNs are:"
    cat $MergeDir/"$Strain"_Total_CRN_expressed.gtf | grep -w 'transcript' | sort -r -n -k 14 -t '"' | cut -f4,14 -d '"' --output-delimite " - " |  head -n 20
    echo "The total number of CRNs was:"
    cat $MergeDir/"$Strain"_Total_CRN_expressed.gtf | grep -w 'transcript' | wc -l
    echo "The number of CRNs with 1x coverage or greater was:"
    cat $MergeDir/"$Strain"_Total_CRN_expressed.gtf | grep -w 'transcript' | sort -r -n -k 14 -t '"' | cut -f14 -d '"' | grep -v -E '0\.' | wc -l
    echo "The number of CRNs with 0x coverage was:"
    cat $MergeDir/"$Strain"_Total_CRN_expressed.gtf | grep -w 'transcript' | sort -r -n -k 14 -t '"' | cut -f14 -d '"' | grep -E '0\.00' | wc -l
done
```

```
```

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
