#!/usr/bin/env python3

import argparse
import sys
from gmusic import *
from spotify import *

def main(argv):
    """ Main driver, use to transfer (at the moment) playlist from GM to SP"""

    

def parse_command_line(argv):
    """
    Parse command line and return a Namespace of the appropriate variables
    """
    parser = argparse.ArgumentParser(prog=argv[0])
    #if len(argv) == 1:
    #    return argparse.Namespace(max_threads=10, outfile=sys.stdout)
    parser.add_argument('-g', dest='playlist_name', type=str)
    return parser.parse_args(argv[1:])

if __name__ == "__main__":
    main(sys.argv)
