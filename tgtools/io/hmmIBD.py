from .base import Importer
import argparse
from tqdm import tqdm
import csv

class hmmIBDImporter(Importer):
    name = "hmmIBD"

    def cli(self,args: argparse.Namespace):
        self.graph = self.import_data(args.input, args.min_ibd)
        self.json_dump(args.output)
        
    def import_data(self, infile:str, min_ibd: int) -> dict:

        sample_names = set()
        edges = []
        F = open(infile, 'r')
        for row in tqdm(csv.DictReader(F, delimiter='\t')):
            sample_names.add(row['sample1'])
            sample_names.add(row['sample2'])
            if float(row['fract_vit_sites_IBD']) >= min_ibd:
                edges.append({'source': row['sample1'], 'target': row['sample2'], 'properties': {'IBD':row['fract_vit_sites_IBD']}})

        nodes = []
        for s in sample_names:
            nodes.append({'id': s, 'properties': {}})
             
        return {"nodes":nodes, "edges":edges}
        

    def register_subparser(self, subparsers):
        parser = subparsers.add_parser(self.name, help='import snp-distance help')
        parser.add_argument('-i','--input', type=str, help='input file', required=True)
        parser.add_argument('-o','--output', type=str, help='output file', required=True)
        parser.add_argument('-d','--min-ibd', type=float, help='Minimum IBD value', required=True)
        parser.set_defaults(func=self.cli)
        return parser