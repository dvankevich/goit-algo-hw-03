import os
import sys
import argparse
from pathlib import Path
import errno

def check_paths(src_path, dst_path):
    if src_path.absolute() == dst_path.absolute():
        raise ValueError(f'{src_path} and {dst_path} are the same directory')

    if dst_path.absolute().is_relative_to(src_path.absolute()):
        raise ValueError(f'{dst_path} cannot be inside {src_path.absolute()}')

def validate_source(src_path):
    if not src_path.exists():
        raise FileNotFoundError(errno.ENOENT, f'{src_path} does not exist')

    if not src_path.is_dir():
        raise NotADirectoryError(errno.ENOTDIR, f'{src_path} is not a directory')

def validate_destination(dst_path):
    if dst_path.exists() and not dst_path.is_dir():
        raise NotADirectoryError(errno.ENOTDIR, f'{dst_path} is not a directory')

    if dst_path.exists() and any(dst_path.iterdir()):
        raise OSError(errno.ENOTEMPTY, f'{dst_path} is not empty')

def main():
    parser = argparse.ArgumentParser(description='Recursive file copier.')
    parser.add_argument('srcdir', type=str, help='source dir')
    parser.add_argument('-d', '--dstdir', type=str, default='dist', help='destination dir. dist for default')
    
    parser.epilog = f'Example usage:\n  python {parser.prog} source_dir -d <destination_dir>\n'

    args = parser.parse_args()

    src_path = Path(args.srcdir)
    dst_path = Path(args.dstdir)

    try:
        check_paths(src_path, dst_path)
        validate_source(src_path)
        validate_destination(dst_path)
    except ValueError as ve:
        print(ve)
        sys.exit(1)
    except FileNotFoundError as fe:
        print(fe)
        sys.exit(fe.errno) 
    except NotADirectoryError as nde:
        print(nde)
        sys.exit(nde.errno) 
    except OSError as oe:
        print(oe)
        sys.exit(oe.errno) 

    print(f'Copy files from directory {src_path.absolute()} to directory {dst_path.absolute()}')

if __name__ == "__main__":
    main()