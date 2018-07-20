import os.path
import sys
import cmd
from subprocess import call

csv_template = ["static content,your changes will be kept\n", "**********,**********\n", "autogenerated dynamic content,your changes will be deleted\n"]
readme_template = ["# " + os.path.basename(os.path.normpath(os.getcwd())) + "\n\n", "## Introduction\n", "TODO: Write something about this project.\n\nDocumentation is [here](docs/index.md)\n\n", "## Contributing\n" "TODO: Add contributing guide.\n\n", "## License\n", "TODO: Add license information."]
index_template = ["The index will be auto-generated later when doing 'sr update'.\n\nAny changes made to this file manually will be overwritten.\n"]

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


"""
Creates the directories and files that are required for the Sliderule project
"""
def initialize():
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


"""
Does the git commit step for this project
"""
def commit(message):
    # TODO: Check git status here to see if there are any changes to commit/push
    print("Adding files to git.")
    call(["git", "add", "."])
    print("Creating commit with provided message.")
    call(["git", "commit", "-m", message])

    push()


"""
Does the git push step for this project
"""
def push():
    print("Pushing to git.")
    call(["git", "push", "origin", "master"])


"""
Does a recursive git pull to grab all the changes to the root project 
and all its components.
"""
def pull():
    print("Pulling changes from git.")
    call(["git", "pull", "origin", "master"])
    call(["git", "submodule", "update", "--recursive", "--remote"])


"""
Adds a component as a git submodule.
"""
def add_submodule(url):
    print("Adding component as submodule.")

    component_names = url.split("/")
    print(len(component_names))
    component_name = component_names[len(component_names) - 1]
    print("git submodule add " + url + " components/" + component_name)
    # call(["git", "submodule", "add", url, "components/" + component_name])
    # print(url)
    # git submodule add git@mygithost:billboard lib/billboard


"""
Remove a git submodule
"""
def remove_submodule(url):
    print("Removing component.")
    print(url)