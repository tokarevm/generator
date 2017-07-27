#!/usr/bin/env python3

import sys
import os.path
import argparse
import random
import time

size_unit = {
    'byte': 1,
    'word':  2,
    'dword': 4
}

### MAIN ###
arg_parser = argparse.ArgumentParser(description='Process arguments')
arg_parser.add_argument('--count', default=1000, help='count of data (from 1 to 999.999)')
arg_parser.add_argument('--size', default='byte', help='size of one data element (byte,word,dword)')
arg_parser.add_argument('--filename', default='./gendata.lst', help='filename to save data')
args = arg_parser.parse_args()

data_count = int(args.count)
try:
    data_size = size_unit[args.size]
except KeyError as e:
    raise ValueError('Undefined size: {}. Allowed are: byte, word, dword'.format(e.args[0]))

if ( not (data_count > 0 and data_count < 1000000) ):
    print("Size must be great then 0 and less then 1.000.000")
    sys.exit(0)

if ( os.path.isfile(args.filename) ):
    ans = input("{:s} exists. Rewrite it? (Y/n)".format(args.filename))
    if ( not (ans == 'Y' or ans == 'y' or ans == '') ):
        print("Script aborted. Exiting...")
        sys.exit(0)

with open(args.filename, "w+") as outfile:

    print("Generating {} lines with {} byte data length".format(data_count, data_size))

    max_count = 2**(data_size*8)-1
    t0 = time.time()
    outfile.write(''.join(str(random.randint(0, max_count)) + os.linesep for i in range(data_count)))
    d = time.time() - t0
    print( "duration: %.2f s." % d )

