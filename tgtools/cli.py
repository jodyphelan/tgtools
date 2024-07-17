import argparse
import json
from tgtools.io import get_importer_names, get_available_importers

def convert(args):
    importer = next(importer for importer in get_available_importers() if importer.name == args.type)
    dict_graph = importer().import_data(args.input)
    print(dict_graph)
    print(type(dict_graph))

    json.dump(dict_graph,open(args.output, 'w'))


def main():
    top_level_parser = argparse.ArgumentParser()
    
    # add subparsers
    top_level_subparsers = top_level_parser.add_subparsers(dest='subparser_name')

    # create the parser for the "import" command
    import_parser = top_level_subparsers.add_parser('import', help='Convert different formats to .trjson')
    # create subparser for each importer
    import_subparsers = import_parser.add_subparsers(dest='type')
    # add subparser for each importer
    for importer in get_available_importers():
        importer().register_subparser(import_subparsers)



    args = top_level_parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        top_level_parser.print_help()

