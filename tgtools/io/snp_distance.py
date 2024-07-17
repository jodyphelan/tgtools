from .base import Importer
import argparse
from tqdm import tqdm

class SNPDistanceImporter(Importer):
    name = "snp-distance"

    def cli(self,args: argparse.Namespace):
        self.graph = self.import_data(args.input, args.max_dist)
        self.json_dump(args.output)
        
    def import_data(self, infile:str, max_dist: int) -> dict:
        F = open(infile, 'r')
        header = F.readline().strip().split()
        nodes = [{'id':n,'properties':{}} for n in header[1:]]
        edges = []
        for i,l in tqdm(enumerate(F)):
            row = l.strip().split()
            for j in range(1, len(row)-1):
                if int(row[j]) <= max_dist:
                    edges.append({
                        "source":header[i], 
                        "target":header[j-1], 
                        "properties":{"snp-dist":row[j]}
                    })
                    
        return {"nodes":nodes, "edges":edges}
        

    def register_subparser(self, subparsers):
        parser = subparsers.add_parser(self.name, help='import snp-distance help')
        parser.add_argument('-i','--input', type=str, help='input file', required=True)
        parser.add_argument('-o','--output', type=str, help='output file', required=True)
        parser.add_argument('-d','--max-dist', type=int, help='Maximum snp distance', required=True)
        parser.set_defaults(func=self.cli)
        return parser