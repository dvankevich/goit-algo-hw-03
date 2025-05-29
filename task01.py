import sys, argparse
from pathlib import PurePath, Path

def main():
    parser = argparse.ArgumentParser(
        description='Recursive file copier.')
    # Required arguments
    parser.add_argument('file', help='The log file')


    parser.epilog = f'Example usage:\n  python {parser.prog} source_dir destination_dir\n'

if __name__ == "__main__":
    main()