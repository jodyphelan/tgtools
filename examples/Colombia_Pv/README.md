# P. vivax from Colombia

## Background 

We also demonstrate the use of TGV with genetic relatedness graphs frequently used to look at malaria parasite transmission16. Detecting segments of shared ancestry (identity by descent (IBD)) is a fundamental estimation of genetic relatedness. Hidden Markov models (HMM) provide a framework to infer pairwise IBD segments from genetic data, and are commonly used in studies of malaria transmission dynamics and relatedness. Using a binary matrix of 112,816 high-quality genome-wide biallelic SNPs, hmmIBD was applied to 54 monoclonal P. vivax isolates of Colombian origin. For each pair of isolates, the fraction of sites called identical was estimated with the Viterbi algorithm. Values are reported between 0 and 1, where clonal isolate pairs have a relatedness estimate of 1 and completely unrelated isolate pairs have an estimate of 0. Tgtools was used to convert the IBD matrix into trjson format. Highly related isolate pairs were classified using an arbitrary threshold of 0.2. The IBD graph was visualised with TGV (Figure 4), and shows that the majority of the clustered isolates are from the Tierralta region of Colombia.

## Converting output to JSON

The output of the analysis can be converted to JSON format using the following command:

```bash
tgtools import hmmIBD -i colombia_fract_vit_ibd.txt -o graph.json -d 0.15
```

This will create a JSON file with the relatedness probabilities in the format required by the TGV visualisation tool. The `-d` flag specifies the threshold probability for relatedness to be included in the output.

## Visualisation in TGV

The JSON file can be visualised using the TGV tool. Navigate to [https://jodyphelan.github.io/tgv/](https://jodyphelan.github.io/tgv/) and upload the JSON file to view the relatedness network. Additional refinement of the relatedness can be done interactively in the TGV tool.

The node_metadata.csv file contains the metadata for each node in the graph. A column named "Node" should be present and contain the same IDs as present in the .json graph. All further columns can contain data that can be used to colour the nodes by the metadata value.