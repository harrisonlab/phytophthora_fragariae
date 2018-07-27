# Commands to prepare gene annotations and raw reads for submission to NCBI

This appears to be a complex procedure, following Andy's commands.
Bioprojects & Biosamples have already been created.
This is for *P. fragariae* and *P. rubi*

## Submission steps

Fasta files were uploaded initially to allow for contamination screen
(See Genbank_corrections.md), however as the MiSeq genomes were submitted as a
batch submission, I have been advised there is no way to update them and the
whole submission has to be repeated.

### Make a table for locus tags

```bash
printf "PF001 SAMN07449679 A4
PF002 SAMN07449680 BC-1
PF003 SAMN07449681 BC-16
PF004 SAMN07449682 BC-23
PF005 SAMN07449683 NOV-27
PF006 SAMN07449684 NOV-5
PF007 SAMN07449685 NOV-71
PF008 SAMN07449686 NOV-77
PF009 SAMN07449687 NOV-9
PF010 SAMN07449688 ONT-3
PF011 SAMN07449689 SCRP245
PR001 SAMN07449690 SCRP249
PR002 SAMN07449691 SCRP324
PR003 SAMN07449692 SCRP333" > genome_submission/Pf_Pr_locus_tags.txt
```
