#!/usr/bin/Rscript

sub cluster_diff_expressed_transcripts {
    my ($diff_expr_matrix_file) = @_;

    my $R_script = "$diff_expr_matrix_file.R";

    open (my $ofh, ">$R_script") or die "Error, cannot write to $R_script";

    print $ofh "library(cluster)\n";
    print $ofh "library(gplots)\n";
    print $ofh "library(Biobase)\n";
    print $ofh "library(ctc)\n";
    print $ofh "library(ape)\n";

    print $ofh "data = read.table(\"$diff_expr_matrix_file\", header=T, com=\'\', sep=\"\\t\")\n";
    print $ofh "rownames(data) = data[,1] # set rownames to gene identifiers\n";
        ;
    print $ofh "data = data[,2:length(data[1,])] # remove the gene column since its now the rowname value\n";
        ;
    print $ofh "data = as.matrix(data) # convert to matrix\n";
        ;
    ## generate correlation matrix
    print $ofh "cr = cor(data, method='spearman')\n";


    ## log2 transform, mean center rows
    print $ofh "data = log2(data+1)\n";
    print $ofh "centered_data = t(scale(t(data), scale=F)) # center rows, mean substracted\n";
        ;

    #print $ofh "hc_genes = agnes(centered_data, diss=FALSE, metric=\"euclidean\") # cluster genes\n";


    if ($gene_dist =~ /spearman|pearson/) {
        if ($gene_dist eq "spearman") {
            print $ofh "gene_cor = cor(t(centered_data), method='spearman')\n";
        }
        else {
            print $ofh "gene_cor = cor(t(centered_data), method='spearman')\n";
        }
        print $ofh "gene_dist = as.dist(1-gene_cor)\n";
    }
    else {
        print $ofh "gene_dist = dist(centered_data, method=\'$gene_dist\')\n";
    }

    print $ofh "hc_genes = hclust(gene_dist, method=\'$gene_clust\')\n";

    print $ofh "hc_samples = hclust(as.dist(1-cr), method=\"complete\") # cluster conditions\n";
    print $ofh "myheatcol = redgreen(75)\n";
    print $ofh "gene_partition_assignments <- cutree(as.hclust(hc_genes), k=6);\n";
    print $ofh "partition_colors = rainbow(length(unique(gene_partition_assignments)), start=0.4, end=0.95)\n";
    print $ofh "gene_colors = partition_colors[gene_partition_assignments]\n";
    print $ofh "save(list=ls(all=TRUE), file=\"${R_script}.all.RData\")\n";



#    print $ofh <<_EOTEXT;

#    ordered_genes_file = paste("$diff_expr_matrix_file", ".ordered_gene_matrix", sep='');
#    ordered_genes = hc_genes\$data;
#    write.table(ordered_genes, file=ordered_genes_file, quote=F, sep="\t");
#
#    gene_tree = hc2Newick(hc_genes);
#    gene_tree_filename = paste("$diff_expr_matrix_file", ".gene_tree", sep='');
#    write(gene_tree, file=gene_tree_filename);

    # get rid of the distances since these can sometimes cause problems with other software tools.
#    gene_nodist_tree_filename = paste("$diff_expr_matrix_file", ".gene_nodist_tree", sep='');
#    t = read.tree(text=gene_tree);
#    t\$edge.length = NULL;
#    write.tree(t, file=gene_nodist_tree_filename);
#
#    sample_tree = hc2Newick(hc_samples);
#    sample_tree_filename = paste("$diff_expr_matrix_file", ".sample_tree", sep='');
#    write(sample_tree, file=sample_tree_filename);

#_EOTEXT

        ;

    ## write plots

    #print $ofh "postscript(file=\"$diff_expr_matrix_file.heatmap.eps\", horizontal=FALSE, width=7, height=10, paper=\"special\");\n";

    print $ofh "pdf(\"$diff_expr_matrix_file.heatmap.pdf\")\n";

    print $ofh "heatmap.2(centered_data, dendrogram='both', Rowv=as.dendrogram(hc_genes), Colv=as.dendrogram(hc_samples), col=myheatcol, RowSideColors=gene_colors, scale=\"none\", density.info=\"none\", trace=\"none\", key=TRUE, keysize=1.2, cexCol=1, lmat=rbind(c(5,0,4,0),c(3,1,2,0)), lhei=c(1.5,5),lwid=c(1.5,0.2,2.5,2.5), margins=c(12,5))\n";

    #print $ofh "try(heatmap.2(cr, col = redgreen(75), scale='none', symm=TRUE, key=TRUE,density.info='none', trace='none', symkey=FALSE, Colv=TRUE,margins=c(10,10), cexCol=1, cexRow=1))\n";
    print $ofh "try(heatmap.2(cr, col = cm.colors(256), scale='none', symm=TRUE, key=TRUE,density.info='none', trace='none', symkey=FALSE, Colv=TRUE,margins=c(10,10), cexCol=1, cexRow=1))\n";


    print $ofh "dev.off()\n";


    close $ofh;

    eval {
        &process_cmd("R --vanilla -q < $R_script");
    };
    if ($@) {
        print STDERR "$@\n";
        ## keep on going...
    }


    return;


=notes from zehua regarding heatmap.2

you need to change the margin of the heatmap in the command heatmap.2:

margins=c(8,8),

The first number is the margin on the bottom (column name), and the second number is for the margin on the right (i.e., the row names). So you can increase the second number and you should get larger space for row names.

If you want to use a column order as you specified, then you can just turn off the ordering of the column by setting the following options in the heatmap.2 command:

dendrogram='row', Colv=FALSE

This will allow you to have a heatmap with column order from the data you provided.

=cut



}
