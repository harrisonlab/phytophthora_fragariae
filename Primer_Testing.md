qPCR primers have been designed in geneious using my local machine, but require testing. A genome for Hapil has been provided, but my local machine has too limited CPU capacity. Run bowtie on the cluster instead and then visualise the .bam files in geneious on my local machine.

```bash
for Primer_Dir in $(ls | grep -v "hapil_a.lines.fasta" | grep -v "script")
do
    PrimerF=$Primer_Dir/*F.fa
    PrimerR=$Primer_Dir/*R.fa
    Assembly=hapil_a.lines.fasta
    OutDir="$Primer_Dir"_aligned
    mkdir $OutDir
    ProgDir=script
    qsub $ProgDir/sub_bowtie_test_primers.sh $Assembly $PrimerF $PrimerR $OutDir
done
```
