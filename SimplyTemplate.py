#!/usr/bin/env python

import os
import argparse
import sys

def cli_parser():
    parser = argparse.ArgumentParser(add_help=False, description='''
        Build's out full emails for an OP.
        ''')
    parser.add_argument(
        "-l", action='store_true', help="List the current Modules Loaded")
    parser.add_argument(
        "-v", action='store_true', help="Set this switch for verbose output of modules")
    parser.add_argument('-h', '-?', '--h', '-help',
                        '--help', action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.h:
        parser.print_help()
        sys.exit()
    return args.l, args.v

def TaskController():
  

def main():
    # instatiate the class
    orc = TaskController.Conducter()
    orc.title()
    orc.title_screen()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print 'Interrupted'
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
