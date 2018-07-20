#!/usr/bin/env python
import argparse
import sliderule_impl

parser = argparse.ArgumentParser(description='Helps maintain Sliderule OSHW projects.')
subparsers = parser.add_subparsers(dest='command')
init = subparsers.add_parser('init')
update = subparsers.add_parser('update')
upload = subparsers.add_parser('upload')
upload.add_argument('-m')
component = subparsers.add_parser('component')
component.add_argument('action', nargs='?')
component.add_argument('url')

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
    # The user wants to add a component
    elif args.command == 'component':
        print(args)
        if args.action == 'add':
            sliderule_impl.add_submodule(args.url)
        elif args.action == 'remove':
            sliderule_impl.remove_submodule(args.url)
        else:
            print("ERROR: You have to 'add' or 'remove' a component.")


if __name__ == "__main__":
    main()