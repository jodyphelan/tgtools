from .base import Importer
from .snp_distance import SNPDistanceImporter
from .transphylo import TransPhyloImporter

def get_available_importers():
    return Importer.__subclasses__()

def get_importer_names() -> list:
    return [importer.name for importer in get_available_importers()]


    
    
    