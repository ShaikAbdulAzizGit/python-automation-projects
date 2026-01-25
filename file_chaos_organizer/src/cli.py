import argparse
from pathlib import Path

def parse_cli_args()->argparse.Namespace:
    '''
    Parse and validate command line arguments 
    Returns:
        args(argpase.Namespace): Parsed CLI Arguments
    '''

    parser=argparse.ArgumentParser(description='safely organize files in a directory')

    parser.add_argument('--path',type=Path,help='Target directory to organize ')

    parser.add_argument('--recursive',action='store_true',help='scan directory recursively')

    
    parser.add_argument('--undo',action='store_true',help='undo the last organizaton operation')

    parser.add_argument('--dry-run',action='store_true',help='Preview operations without performing them')

    args=parser.parse_args()

    if args.path and args.undo:
        parser.error('--undo cannot be used with --path')
    
    if not args.path and not args.undo:
        parser.error('Either --path or --undo must be provided')
    
    return args