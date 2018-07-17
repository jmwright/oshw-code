#!/usr/bin/env python
import os.path
import sys
import cmd
import argparse
from subprocess import call

parser = argparse.ArgumentParser(description='Helps maintain Sliderule OSHW projects.')
csv_template = ["static content,your changes will be kept\n", "**********,**********\n", "autogenerated dynamic content,your changes will be deleted\n"]
readme_template = ["# " + os.path.basename(os.path.normpath(os.getcwd())) + "\n\n", "## Introduction\n", "TODO: Write something about this project.\n\nDocumentation is [here](docs/index.md)\n\n", "## Contributing\n" "TODO: Add contributing guide.\n\n", "## License\n", "TODO: Add license information."]
index_template = ["The index will be auto-generated later when doing 'sr update'.\n\nAny changes made to this file manually will be overwritten.\n"]

# TODO: For sub commands
# subparsers = parser.add_subparsers()
# init = subparsers.add_parser('init')

parser.add_argument('init')

args = parser.parse_args()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def createComponents():
    print("Creating blank components directory.")

    # Create the components directory
    os.makedirs("./components")


def createDocs():
    print("Creating docs directory from template.")

    # Create the documentation directory
    os.makedirs("./docs")

    # Create a index.md file that will be autogenerated later
    index_file = open("./docs/index.md", "w+")
    index_file.writelines(index_template)
    index_file.close()


def createReadme():
    print("Creating README.md from template.")

    # Create the file and write a few template lines into it
    readme_file = open("./README.md", "w+")
    readme_file.writelines(readme_template)
    readme_file.close()


"""
Generates a BoM from scratch based on a template to show the user what they can enter manually, vs what is autogenerated
"""
def createBoM():
    print("Creating bill of materials (BoM) from template.")

    # Create the file and write a few template lines into it
    csv_file = open("./BoM.csv", "w+")
    csv_file.writelines(csv_template)
    csv_file.close()


def main():
    # The user wants to initialize a Sliderule project inside an existing directory
    if 'init' in args:
        print("Initializing current directory as a new Sliderule project.")
        print()

        # Check if the user has already initialized this directory as a git repo
        if os.path.isdir("./.git"):
            print(bcolors.WARNING + "WARNING: This directory is already set up as a git repository. To change the remote, please do so directly with git commands." + bcolors.ENDC)
        else:
            print("Initializing git repo.")

            # The user will have to do the initial setup of their repos themselves
            main_repo = input("Enter URL of git repository: ")

            # Set up root git repo
            call(["git", "init"])
            call(["git", "remote", "add", "origin", main_repo])
            print("Done initializing root git repo")

        # If a BoM file doesn't already exist, create it
        if not os.path.isfile("./BoM.csv"):
            print()
            print("BoM does not exist.")

            createBoM()
        else:
            print()
            print(bcolors.WARNING + "WARNING: BoM.csv exists, refusing to overwrite to prevent loss of data." + bcolors.ENDC)

        if not os.path.isdir('./components'):
            print()
            print("components directory does not exist")

            createComponents()
        else:
            print()
            print(bcolors.WARNING + "WARNING: components directory exists, refusing to overwrite to prevent loss of data." + bcolors.ENDC)

        # If a readme doesn't exist, create it
        if not os.path.isfile("./README.md"):
            print()
            print("README.md does not exist.")

            createReadme()
        else:
            print()
            print(bcolors.WARNING + "WARNING: README.md exists, refusing to overwrite to prevent loss of data." + bcolors.ENDC)

        # If the docs directory doesn't exist, created it and the index.md file
        if not os.path.isdir("./docs"):
            print()
            print("docs directory does not exist.")
            createDocs()
        else:
            print()
            print(bcolors.WARNING + "WARNING: docs directory exists, refusing to overwrite to prevent loss of data." + bcolors.ENDC)

        print()
        print("Done initializing new Sliderule project.")


if __name__ == "__main__":
    main()