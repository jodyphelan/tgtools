from .base import Importer
import argparse
from tqdm import tqdm

class TransPhyloImporter(Importer):
    name = "transphylo"

    def cli(self,args: argparse.Namespace):
        self.graph = self.import_data(args.input, args.min_probability)
        self.json_dump(args.output)
        
    def import_data(self, infile:str, min_prob: float) -> dict:
        F = open(infile, 'r')
        header = F.readline().strip().split()

        edges = []
        for i,l in tqdm(enumerate(F)):
            row = l.strip().split()
            for j in range(1, len(row)-1):
                if float(row[j])>min_prob:
                    edges.append({'source':header[i], 'target':header[j-1], 'properties':{'probability':round(float(row[j]),2)}})

        nodes = []
        for sample in header:
            nodes.append({"id": sample,"properties":{}})
        
        return {"nodes":nodes, "edges":edges,"directed":True}
                

    def register_subparser(self, subparsers):
        parser = subparsers.add_parser(self.name, help='import transphylo help')
        parser.add_argument('-i','--input', type=str, help='input file', required=True)
        parser.add_argument('-o','--output', type=str, help='output file', required=True)
        parser.add_argument('-p','--min-probability', type=float, help='Minimum probability for edge', required=True)
        parser.set_defaults(func=self.cli)
        return parser