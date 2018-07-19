#!/usr/bin/env python
import argparse
import sliderule_impl

parser = argparse.ArgumentParser(description='Helps maintain Sliderule OSHW projects.')
subparsers = parser.add_subparsers(dest='command')
init = subparsers.add_parser('init')
update = subparsers.add_parser('update')
upload = subparsers.add_parser('upload')
upload.add_argument('-m')

# Example of optional argument
# parser.add_argument('init', nargs='?')

args = parser.parse_args()

def main():
    # The user wants to initialize a Sliderule project inside an existing directory
    if args.command == 'init':
        sliderule_impl.initialize()
    # The user wants to push changes to a Sliderule project to git
    elif args.command == 'upload':
        sliderule_impl.commit(args.m)
        sliderule_impl.push()
    # The user wants to pull changes to a Sliderul project from git
    elif args.command == 'update':
        sliderule_impl.pull()


if __name__ == "__main__":
    main()