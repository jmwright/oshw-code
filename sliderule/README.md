# Sliderule

## Introduction
This is a reference implementation for the open [sliderule methodology](https://github.com/Mach30/sliderule) being developed by [Mach 30](http://mach30.org/).

This has currently only been tested on Linux, but should run on MacOS or Windows if git and Python 2.7+ are installed.

This is in the very early stages of development, and is not ready for widespread use.

## Usage

An `sr` symlink can be created to sr.py for convenience, otherwise run these commands as `sr.py`.

### Current Commands
- `sr init` - Initializes a directory as a new Sliderule project, creating files and directories as needed to match the methodology.
- `sr upload -m [message]` - Commits and pushes a project to git recursively, assuming the master branch. _Future:_ It will commit and push all components recursively, dealing with only the components/repos the user has access to.

### Future Commands
- `sr clone [URL]` - Clones a Sliderule project recursively,downloading all components.
- `sr update` - Updates a Sliderule project recursively, building BoMs and running any extra commands specified in the `sliderule.py` files found throughout the directory structure.
- `sr component` - Has subcommands that allow the addition, removal and modification of components in the directory tree. Components are treated as git submodules of the main project.
  - `sr component add [url]` - Adds the component via its URL. Note that the URL must exist prior to running this command. The git repo for the component is not created automatically at this time.
  - `sr component remove [name]` - Removes a component from a project (deletes its submodule).
