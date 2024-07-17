from abc import ABC, abstractmethod
import json


class Importer(ABC):
    @abstractmethod
    def import_data(self, filename: str) -> dict:
        """
        Import data from filename and return a dictionary with the graph
        """
        pass

    @abstractmethod
    def register_subparser(self, subparsers):
        """
        Register a subparser for the importer
        """
        pass

    @abstractmethod
    def cli(self, args):
        """
        Command line interface for the importer
        """
        pass

    def json_dump(self, filename: str) -> None:
        """
        Dump the graph to a json file
        """
        json.dump(self.graph,open(filename, 'w'))