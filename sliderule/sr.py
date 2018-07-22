#!/usr/bin/env python
import os
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
clone = subparsers.add_parser('clone')
clone.add_argument('url')

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

        # Walk through the components in the directory tree, committing as necessary
        for dirname, dirnames, filenames in os.walk('./components'):
            for subdirname in dirnames:
                os.chdir("./components/" + subdirname)

                sliderule_impl.commit(None)
                sliderule_impl.push()
                
                os.chdir("../")
    # The user wants to pull changes to a Sliderul project from git
    elif args.command == 'update':
        sliderule_impl.pull()
    # The user wants to add a component
    elif args.command == 'component':
        if args.action == 'add':
            sliderule_impl.add_component(args.url)
        elif args.action == 'remove':
            sliderule_impl.remove_component(args.url)
        elif args.action == 'create':
            sliderule_impl.create_component(args.url)
        else:
            print("ERROR: You have to 'add' or 'remove' a component.")
    elif args.command == 'clone':
        sliderule_impl.clone(args.url)


if __name__ == "__main__":
    main()