#Runs commands from Maria to analyse output from SNP calling

##Filter inital vcf output

```bash
vcf=SNP_calling/95m_contigs_unmasked.vcf
script=/home/adamst/git_repos/scripts/popgen/snp/sub_vcf_parser.sh
qsub $script $vcf
```