#!/usr/bin/env python

# main is lame name, you want to change it after checking out

import argparse
import sys
sys.path.append('./lib/')
from pyskel import *

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    args = parser.parse_args()
    print args.accumulate(args.integers)

def run_pyskel():
    ps = PySkel()
    ps.foo()

if __name__ == '__main__':
    #parse_arguments()
    run_pyskel()
