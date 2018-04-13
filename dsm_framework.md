DSM commands were set up, but no longer relevant for my analysis.
Keep here for others use.

## B) Counting kmers with dsm-framework

Before running add the following line to your profile:

```bash
export DSM_FRAMEWORK_PATH=/home/adamst/prog/dsm-framework
```

### B.1) Pre-processing of fasta files

```bash
for File in $(ls promotor_id/*.fasta)
do
    ProgDir=/home/adamst/git_repos/tools/seq_tools/kmer_enrichment
    File_ID=$(echo $File | cut -f2 -d "/")
    qsub $ProgDir/sub_dsm_preprocessing.sh $File
done
```

### B.2) Initialise server

Create text file containing the names of input files

```bash
for Set in all all_comparison_set highconfidence highconfidence_comparison_set \
highexpressed highexpressed_comparison_set
do
    Name="$Set"_upstream3000
    Txt_File=sample-names_"$Set".txt
    WorkDir=promotor_id
    echo $Name > $WorkDir/$Txt_File
done
```

Ensure that the fasta, fmi and sample-names files for each comparison \
are in their own directory

```bash
for Set in all highconfidence highexpressed
do
    mkdir -p promotor_id/$Set
    fasta=promotor_id/"$Set"_upstream3000.fasta
    index=promotor_id/"$Set"_upstream3000.fasta.fmi
    sample_names=promotor_id/sample-names_"$Set".txt
    mv $fasta promotor_id/$Set/.
    mv $index promotor_id/$Set/.
    mv $sample_names promotor_id/$Set/.
done
```

Now initialise the server-side processes

Parallel processes can be set at 4, 16 or 64

#### Set "all"

```bash
Set=all
WorkDir=promotor_id/$Set
tmp_dir=$WorkDir/tmp_dsmframework_"$Set"_config
mkdir -p $tmp_dir
ProgDir=/home/adamst/git_repos/tools/seq_tools/kmer_enrichment
sample_IDs=$WorkDir/sample-names_"$Set".txt
Parallel_processes=4
$ProgDir/server_set_up.sh $sample_IDs $tmp_dir $Parallel_processes $WorkDir $Set
```

Now run the client side processes

IMPORTANT: Ensure all the server side processes are running first

```bash
Set=all
Sample_Names=promotor_id/$Set/sample-names_"$Set".txt
ScriptDir=/home/adamst/git_repos/tools/seq_tools/kmer_enrichment
ProjDir=/home/groups/harrisonlab/project_files/phytophthora_fragariae
tmp_dir=$ProjDir/promotor_id/$Set/tmp_dsmframework_"$Set"_config
WorkDir=$ProjDir/promotor_id/$Set/
$ScriptDir/client_execution.sh $Sample_Names $tmp_dir $WorkDir
```
