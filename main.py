#!/usr/bin/env python

# main is lame name, you want to change it after checking out

import argparse
import sys
sys.path.append('./lib/')
from pyskel import *

# http://docs.python.org/library/argparse.html
def parse_arguments():
    parser = argparse.ArgumentParser(description='Skeleton code for small Python application.')
    # mandatory argument
    #parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')

    #optional arguments
    parser.add_argument("-v", "--verbosity", help="increase the verbosity level of the output", action="store_true")
    args = parser.parse_args()
    #print args.accumulate(args.integers)

    # Process the command line arguments
    if args.verbosity:
        print "verbosity enabled..."

def run_pyskel():
    ps = PySkel()
    print ps.foo()

if __name__ == '__main__':
    parse_arguments()
    run_pyskel()
