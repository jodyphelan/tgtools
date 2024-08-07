# _Mycobacterium tuberculosis_ transmission analysis

## Background

To demonstrate the use of this tool, we analysed a publicly available dataset of M. tuberculosis whole genome sequence data collected from all TB culture-positive individuals from the Republic of Moldova between January 2018 and December 2019 first described by Yang et al1. High quality short-read sequence public datasets were available for 2,770 culture-positive TB individuals. Demographic, epidemiological and disease data, including age, sex, location, and smear status, were collected for everyone.

Raw sequencing reads were downloaded from the ENA (accession: PRJNA736718) and aligned to the H37Rv reference strain (NCBI accession no. NC_000962.3) using bwa mem8, with sorted binary alignment files created using samtools software (v.1.10) 9. TB lineage and in silico antimicrobial resistance profiles were predicted using TB-Profiler software10. Variant calling was carried out with GATK11 (v. 4.1) to identify SNPs, with low-quality variants removed and mixed calls assigned as the majority allele if more than 80% of reads were called as the nucleotide. SNPs found in pe/ppe genes, repetitive regions, and at known antimicrobial-resistance conferring sites were also removed. High-likelihood mixed infection samples identified by MixInfect12 were also removed from further analysis, resulting in a final dataset consisting of 1,834 individuals. 

The probability of direct transmission between individuals with TB in the population was inferred using the multi-input tree implementation of TransPhylo13,14. First, broad clusters were identified by linking sequences in groups with a pairwise distance of ≤ 50 SNPs. Next, a timed phylogeny was built for each of these clusters using BEAST215 with the HKY nucleotide substitution model, a strict clock model, and constant population size. Models were run for 2.5x108 MCMC iterations or until convergence and 50 trees for each cluster were drawn from the posterior distributions, after a 20% burn-in, to be used as input for TransPhylo. The TransPhylo infer_multittree_share_param function was used to reconstruct transmission from the phylogenies using a prior gamma generation time (k = 1.3,  = 3.33) and sampling time (k = 1.1,  = 2.75) distribution, a beta sampling density distribution (α = 20, ß = 8), and a fixed within-host coalescent rate of 100/365. Models were run for 105 MCMC iterations and prior parameters shared across the 50 independent runs per cluster. Finally, we used the computeMatWIW function to calculate the posterior probability of directed transmission between individuals in each cluster and imputed a zero probability of transmission between those not in the same cluster. Tgtools was used to convert the probability matrix into trjson format. The transmission clusters were visualised and annotated with TGV (Figure 3). The output highlights the transmission of MDR-TB and XDR-TB within the largest 5 clusters of M. tuberculosis.

## Converting output to JSON

The output of the analysis can be converted to JSON format using the following command:

```bash
tgtools import transphylo -i MoldovaTB_transmissionProbs.txt -o graph.json -p 0.3
```

This will create a JSON file with the transmission probabilities in the format required by the TGV visualisation tool. The `-p` flag specifies the threshold probability for transmission to be included in the output.

## Visualisation in TGV

The JSON file can be visualised using the TGV tool. Navigate to [https://jodyphelan.github.io/tgv/](https://jodyphelan.github.io/tgv/) and upload the JSON file to view the transmission network. Additional refinement of the probabilities can be done interactively in the TGV tool.

The node_data.csv file contains the metadata for each node in the graph. A column named "Node" should be present and contain the same IDs as present in the .json graph. All further columns can contain data that can be used to colour the nodes by the metadata value.