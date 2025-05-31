import os, sys, argparse
from pathlib import PurePath, Path

def main():
    parser = argparse.ArgumentParser(
        description='Recursive file copier.')
    # Required arguments
    parser.add_argument('srcdir', type=str, help='source dir')
    # optional argument
    parser.add_argument('-d','--dstdir', type=str, default='dist', help='destination dir. dist for default')
    
    parser.epilog = f'Example usage:\n  python {parser.prog} source_dir -d <destination_dir>\n'

    # Parse the command line arguments
    args = parser.parse_args()

    print(args)
    src_path = Path(args.srcdir)
    dst_path = Path(args.dstdir)

    print(src_path.absolute(), dst_path.absolute())
    # print(dst_path.absolute().is_relative_to(src_path.absolute()))


    if src_path.absolute() == dst_path.absolute():
        print(f'{src_path} and {dst_path} are the same directory')
        sys.exit(1) # 1 Operation not permitted

    if dst_path.absolute().is_relative_to(src_path.absolute()):
        print(f'{dst_path} cannot be inside {src_path.absolute()}')
        sys.exit(1) # 1 Operation not permitted

    if not src_path.exists():
        print(f'{src_path} not exist')
        sys.exit(2) # 2 No such file or directory

    if not src_path.is_dir():
        print(f'{src_path} is not a directory')
        sys.exit(20) # 20 Not a directory

    if not dst_path.exists():
        print(f'{dst_path} not exist')
        sys.exit(2) # 2 No such file or directory

    if not dst_path.is_dir():
        print(f'{dst_path} is not a directory')
        sys.exit(20) # 20 Not a directory

    # print(list(dst_path.iterdir()))
    # print(any(dst_path.iterdir()))

    if any(dst_path.iterdir()):
        print(f'{dst_path} is not empty')
        sys.exit(39) # 39 Directory not empty


    print(f'copy files from directory {src_path.absolute()} to directory {dst_path.absolute()}')



    sys.exit()

if __name__ == "__main__":
    main()