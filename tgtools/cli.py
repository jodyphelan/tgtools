import argparse
import tgtools as tg

def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('--input', required = True)
    args = argument_parser.parse_args()

    tg.stats(tg.load(args.input))