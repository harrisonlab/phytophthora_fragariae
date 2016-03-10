#Analysis of RxLR effectors - Augustus gene models

#Due to the several outputs of RxLR effector prediction from different scripts, the identity of RxLRs were identified from motif and Hmm searches within gene models.

```bash
Strain=A4
"$Strain"AugGff=gene_pred/braker/P.fragariae/$Strain/*/augustus_extracted.gff
InDir=$(ls -d analysis/RxLR_effectors/RxRL_EER_regex_finder/P.fragariae/$Strain)
Source="braker"
Species=P.fragariae
RxLR_motif=$(ls analysis/RxLR_effectors/RxLR_EER_regex_finder/$Species/$Strain/"$Strain"_"$Source"_RxLR_EER_regex.txt)
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
cat $OutDir/"$Strain"_"$Source"_RxLR_EER_motif_hmm_headers.txt $WY_hmm | cut -f1 -d' ' | rev | cut -f2 -d '|' | rev | sort | uniq -d | wc -l
echo ""
cat $GeneGff | grep -w -f $OutDir/"$Strain"_"$Source"_RxLR_EER_motif_hmm_headers.txt > $OutDir/"$Strain"_Aug_RxLR_EER_motif_hmm.gff
```

#Analysis of RxLR effectors - ORF gene models

#Due to the several outputs of RxLR effector prediction from different scripts, the identity of RxLRs were identified from motif and Hmm searches within ORF-finder predictions

```bash
Strain=A4
"$Strain"AugGff=gene_pred/braker/P.fragariae/$Strain/*/augustus_extracted.gff
InDir=$(ls -d analysis/RxLR_effectors/RxRL_EER_regex_finder/P.fragariae/$Strain)
Species=P.fragariae
RxLR_motif=$(ls analysis/RxLR_effectors/RxLR_EER_regex_finder/$Species/$Strain/"$Strain"_ORF_RxLR_EER_regex.txt)
RxLR_hmm=$(ls analysis/RxLR_effectors/hmmer_RxLR/$Species/$Strain/"$Strain"_ORF_RxLR_hmmer_headers.txt)
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
ProgDir=/home/armita/git_repos/emr_repos/tools/seq_tools/feature_annotation
$ProgDir/gene_list_to_gff.pl $OutDir/"$Strain"_ORF_RxLR_EER_motif_hmm_headers.txt $GeneModels RxLR_EER_combined Name Augustus > $OutDir/"$Strain"_ORF_RxLR_EER_motif_hmm.gff
```

#Analysis of RxLR effectors - merging predicted genes with ORF-FINDER output

#Intersection between the coodinates of putative RxLRs from gene models and ORFs were identified to determine the total number of RxLRs predicted in these genomes.

#The RxLR effectors from both Gene models and ORF finding approaches were combined into a single file.

```bash
MergeDir=analysis/RxLR_effectors/combined_evidence/P.fragariae/A4
Strain=A4
Species=P.fragariae
AugGff=$MergeDir/"$Strain"_braker_RxLR_EER_motif_hmm.gff
ORFGff=$MergeDir/"$Strain"_ORF_RxLR_EER_motif_hmm.gff
WY_Aug_hmm=$(ls analysis/RxLR_effectors/hmmer_WY/$Species/$Strain/"$Strain"_*_WY_hmmer_headers.txt | grep -v 'ORF')
WY_ORF_hmm=$(ls analysis/RxLR_effectors/hmmer_WY/$Species/$Strain/"$Strain"_ORF_WY_hmmer_headers.txt)
ORFsInAug=$MergeDir/"$Strain"_ORFsInAug_RxLR_EER_motif_hmm.gff
AugInORFs=$MergeDir/"$Strain"_AugInORFs_RxLR_EER_motif_hmm.gff
ORFsUniq=$MergeDir/"$Strain"_ORFsUniq_RxLR_EER_motif_hmm.gff
AugUniq=$MergeDir/"$Strain"_Aug_Uniq_RxLR_EER_motif_hmm.gff
TotalRxLRsTxt=$MergeDir/"$Strain"_Total_RxLR_EER_motif_hmm.txt
TotalRxLRsGff=$MergeDir/"$Strain"_Total_RxLR_EER_motif_hmm.gff
TotalRxLRsWYTxt=$MergeDir/"$Strain"_Total_RxLR_EER_WY_motif_hmm.txt
TotalRxLRsWYGff=$MergeDir/"$Strain"_Total_RxLR_EER_WY_motif_hmm.gff
TotalRxLRsHeaders=$MergeDir/"$Strain"_Total_RxLR_EER_motif_hmm_headers.txt
bedtools intersect -wa -u -a $ORFGff -b $AugGff > $ORFsInAug
# bedtools intersect -wb -u -a $ORFGff -b $AugGff > $AugInORFs
bedtools intersect -wa -u -a $AugGff -b $ORFGff > $AugInORFs
bedtools intersect -v -wa -a $ORFGff -b $AugGff > $ORFsUniq
bedtools intersect -v -wa -a $AugGff -b $ORFGff > $AugUniq
echo "The number of ORF RxLRs overlapping Braker1 RxLRs:"
cat $ORFsInAug | grep -w 'gene' | wc -l
echo "The number of Braker1 RxLRs overlapping ORF RxLRs:"
cat $AugInORFs | grep -w 'gene' | wc -l
echo "The number of RxLRs unique to ORF models:"
cat $ORFsUniq | grep -w 'transcript' | cut -f9 | cut -f5 -d '=' | wc -l
cat $ORFsUniq | grep -w 'transcript' | cut -f9 | cut -f5 -d '=' >> $TotalRxLRsTxt
echo "The number of RxLRs unique to Braker1 models:"
cat $AugUniq | grep -w 'gene' | wc -l
echo "The total number of putative RxLRs are:"
cat $AugInORFs | grep -w 'gene' | cut -f9 > $TotalRxLRsTxt
cat $AugUniq | grep -w 'gene' | cut -f9 >> $TotalRxLRsTxt
cat $ORFsUniq | grep -w 'transcript' | cut -f9 | cut -f4 -d '=' >> $TotalRxLRsTxt
cat $TotalRxLRsTxt | wc -l
echo "The number of these RxLRs containing WY domains are:"
cat $TotalRxLRsTxt $WY_Aug_hmm $WY_ORF_hmm | cut -f1 -d ' ' | rev | cut -f2 -d '|' | rev | sort | uniq -d > $TotalRxLRsWYTxt
cat $TotalRxLRsWYTxt | wc -l
```

#Fasta sequences for RxLRs were extracted for each isolate

```bash
Fa=gene_pred/braker/*/A4/*/augustus.aa
Strain=$(echo "$AugFa" | rev | cut -f3 -d '/' | rev)
Species=$(echo "$AugFa" | rev | cut -f4 -d '/' | rev)
ORFsFa=$(ls gene_pred/ORF_finder/"$Species"/"$Strain"/"$Strain".aa_cat.fa)
MergeDir=analysis/RxLR_effectors/combined_evidence/$Species/$Strain
TotalRxLRsHeaders=$MergeDir/"$Strain"_Total_RxLR_EER_motif_hmm_headers.txt
RxLRsFa=$MergeDir/"$Strain"_Total_RxLR_EER_motif_hmm_headers.fa
ProgDir=~/git_repos/emr_repos/tools/seq_tools/feature_annotation
$ProgDir/unwrap_fasta.py --inp_fasta $AugFa | grep -A1 -w -f $TotalRxLRsHeaders | grep -v -E '^--$' > $RxLRsFa
ProgDir=/home/armita/git_repos/emr_repos/tools/gene_prediction/ORF_finder
$ProgDir/extract_from_fasta.py --fasta $ORFsFa --headers $TotalRxLRsHeaders >> $RxLRsFa
echo "$Strain"
echo "The number of sequences extracted is"
cat $RxLRsFa | grep '>' | wc -l
```
