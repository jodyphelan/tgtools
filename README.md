# tgtools

This is a command-line tool to help manipulate transjson files which are used to store transmission/relatedness networks.

## Installation

```bash
pip install git+https://github.com/jodyphelan/tgtools.git
```

## Usage

```bash
usage: tgtools [-h] {import} ...

positional arguments:
  {import}
    import    Convert different formats to .trjson
```

## Import

You can use the `import` function to convert data from different formats to .trjson. The following formats are currently supported:

### snp-distance
This is a tab-delimited matrix of pairwise SNP distances. The first row and column should be sample names. The rest of the matrix should be the SNP distances between samples.

```bash
usage: tgtools import snp-distance [-h] -i INPUT -o OUTPUT -d MAX_DIST

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input file
  -o OUTPUT, --output OUTPUT
                        output file
  -d MAX_DIST, --max-dist MAX_DIST
                        Maximum snp distance
```
### transphylo

This is a transmission probability matrix which is output by the TransPhylo tool. The first row and column should be sample names. The rest of the matrix should be the transmission probabilities between samples.

```bash
usage: tgtools import transphylo [-h] -i INPUT -o OUTPUT -p MIN_PROBABILITY

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input file
  -o OUTPUT, --output OUTPUT
                        output file
  -p MIN_PROBABILITY, --min-probability MIN_PROBABILITY
                        Minimum probability for edge
```
