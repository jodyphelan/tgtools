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

### Isorelate

This importer parses the file output by the Isorelate tool. 

```bash
usage: tgtools import isorelate [-h] -i INPUT -o OUTPUT -d MIN_IBD

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input file
  -o OUTPUT, --output OUTPUT
                        output file
  -d MIN_IBD, --min-ibd MIN_IBD
                        Minimum IBD value
```


## Development

Additional format parsers can be added by creating a new file in the `tgtools/io` directory. This file should create import the `Importer` base class and implement the `import_data`, `register_subparser` and `cli` methods. The implemented subclass should then be imported into the `tgtools/io/__init__.py` file.

### register_subparser

This method should take a subparser object and add a new subparser for the new format. Any required arguments should be added to the subparser. An example of this is shown below:

```python
def register_subparser(self, subparsers):
    parser = subparsers.add_parser("myformat", help="Import data from my format")
    parser.add_argument("-i", "--input", required=True, help="input file")
    parser.add_argument("-o", "--output", required=True, help="output file")
    parser.add_argument("-d", "--min-distance", required=True, help="Minimum distance for edge")
    parser.set_defaults(func=self.cli)
```

The `set_defaults` method should be set to the `cli` method of the class.

### cli

This method should take the parsed arguments and call the `import_data` method with the required arguments. An example of this is shown below:

```python
def cli(self, args):
    self.import_data(args.input, args.output, args.min_distance)
```

### import_data

This method is called by `cli` and should take the input file, output file and any other required arguments. It should read the input file and return a dictionary with the required data. An example of this is shown below:

```python
def import_data(self, input_file, output_file, min_distance):
    data = {}
    with open(input_file) as f:
        # Read data from file
    with open(output_file, "w") as f:
        json.dump(data, f)
```

This method should return a dictionary with the following structure:

```python
{
    "nodes": [
        {"id": "sample1", "metadata": {"location": "UK"}},
        {"id": "sample2", "metadata": {"location": "USA"}}
    ],
    "edges": [
        {"source": "sample1", "target": "sample2", "metadata": {"probability": 0.5}}
    ]
}
```