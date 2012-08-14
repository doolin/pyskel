#!/usr/bin/env python

# main is lame name, you want to change it after checking out

import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    args = parser.parse_args()
    print args.accumulate(args.integers)

if __name__ == '__main__':
    parse_arguments()
