#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -pe smp 1
#$ -l virtual_free=1G
#$ -M andrew.armitage@emr.ac.uk
#$ -m abe

# Script to prepare rna for downstream applications.
# Will filter poor quality reads, perform trimming and
# remove illumina adapters.
# To be run from the project directory. Usage:
# rna_qc_fastq-mcf <RNASeq_F.fq> <illumina_adapters.fa> [DNA/RNA]

#######  Step 1	 ########
# Initialise values	#
#########################


CUR_PATH=$PWD
WORK_DIR=$TMPDIR/rna_qc

F_IN=$CUR_PATH/$1
ILLUMINA_ADAPTERS=$2
SEQ_TYPE=$3

LIBRARY_TYPE=$(echo $F_IN | rev | cut -d "/" -f5 | rev)
ORGANISM=$(echo $F_IN | rev | cut -d "/" -f4 | rev)
STRAIN=$(echo $F_IN | rev | cut -d "/" -f3 | rev)

F_FILE=$(echo $F_IN | rev | cut -d "/" -f1 | rev | sed 's/.gz//')

F_OUT=$(echo "$F_FILE" | sed 's/.fq/_trim.fq/g' | sed 's/.fastq/_trim.fq/g')


echo "your compressed forward read is: $F_IN"
	echo ""
echo "your forward read is: $F_FILE"
	echo ""
echo "your qc outfiles will be given the prefix: $QC_OUTFILE"
	echo ""
echo "illumina adapters are stored in the file: $ILLUMINA_ADAPTERS"
	echo ""
echo "you are providing Sequence data as (DNA/RNA): $SEQ_TYPE"


#######  Step 2	 ########
# 	unzip reads			#
#########################

mkdir -p "$WORK_DIR"/F
cd "$WORK_DIR"

cat "$F_IN" | gunzip -fc > "$F_FILE"

#######  Step 4	 ########
# 	Quality trim		#
#########################

fastq-mcf $ILLUMINA_ADAPTERS $F_FILE -o F/"$F_OUT" -C 1000000 -u -k 20 -t 0.01 -q 30 -p 5

#gzip "$WORK_DIR/*/$QC_OUTFILE"_*
SEQ_TYPE=$(echo "$SEQ_TYPE" | tr "[:upper:]" "[:lower:]")
OUTDIR="$CUR_PATH"/qc_"$SEQ_TYPE"/"$LIBRARY_TYPE"/"$ORGANISM"/"$STRAIN"
gzip F/"$F_OUT"
mkdir -p "$OUTDIR"/F
cp -r F/"$F_OUT".gz "$OUTDIR"/F/"$F_OUT".gz

#cat F/"$QC_OUTFILE"_F.fastq | gzip -cf > $CUR_PATH/qc_$SEQ_TYPE/paired/$ORGANISM/$STRAIN/F/"$QC_OUTFILE"_F.fastq.gz
#cat R/"$QC_OUTFILE"_R.fastq | gzip -cf > $CUR_PATH/qc_$SEQ_TYPE/paired/$ORGANISM/$STRAIN/R/"$QC_OUTFILE"_R.fastq.gz
#cp -r $WORK_DIR/F/* $CUR_PATH/qc_$SEQ_TYPE/paired/$ORGANISM/$STRAIN/F/.
#cp -r $WORK_DIR/R/* $CUR_PATH/qc_$SEQ_TYPE/paired/$ORGANISM/$STRAIN/R/.

#######  Step 8  ########
#       Cleanup         #
#########################

rm -r $WORK_DIR/
