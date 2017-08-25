#BLASTs the 205 high confidence RxLRs, merged with the expressed low confidence RxLRs.

##Create a fasta file of the genes required for BLAST

Extract fasta from text file created manually by inspecting FPKM values

```bash
ProgDir=/home/adamst/git_repos/tools/gene_prediction/ORF_finder
mkdir -p analysis/reciprocal_BLAST
$ProgDir/extract_from_fasta.py --fasta analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_final_RxLR.fa --headers analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_expressed_low_confidence_RxLRs.txt > analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_expressed_low_confidence_RxLRs.fa
```

Create a merged file

```bash
cat analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_final_RxLR_EER.fa > analysis/reciprocal_BLAST/Bc16_RxLRs.fa
cat analysis/RxLR_effectors/combined_evidence/P.fragariae/Bc16/Bc16_expressed_low_confidence_RxLRs.fa >> analysis/reciprocal_BLAST/Bc16_RxLRs.fa
```
