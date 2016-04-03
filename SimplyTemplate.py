#!/usr/bin/env python

import os
import argparse
import sys
from Common import TaskController

def cli_parser():
    parser = argparse.ArgumentParser(add_help=False, description='''
        Builds out full emails for an OP.
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

def TaskManger():
    # Get all the options passed and pass it to the TaskConducter, this will
    # keep all the processioning on the side.
    # need to pass the store true somehow to tell printer to restrict output
    cli_list, cli_verbose = cli_parser()
    Task = TaskController.Conducter()
    if cli_list:
        Task.ListModules()
        sys.exit(0)
    Task.TaskSelector()

def main():
    # instantiate the class
    TaskManger()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print '\n [!] Interrupted'
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
