#!/usr/bin/env python
# This was created on Ubuntu 16.04 64-bit with FreeCAD stable installed from the PPA
# https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-stable
# Tested with FreeCAD 0.16, Libs: 0.16R6710 (Git) and Python 2.7.12 (FreeCAD is still Python 2)
# License: Apache 2.0

import sys

# Make sure that the FreeCAD library is accessible
FREECADPATH = '/usr/lib/freecad/lib/'
sys.path.append(FREECADPATH)

def convert_fcstd(filename):
    try:
        import FreeCAD
    except ValueError:
        print("Could not load the FreeCAD library")
    else:
        import Part

        # Export the STEP to the same directory
        step_filename = filename.replace(".fcstd", ".step")

        doc = FreeCAD.open(filename)
        objects = doc.Objects
        for object in objects:
            if object.Type[:4] == 'Part':
                shape = object.Shape
                shape.exportStep(step_filename)

        print("Exported " + step_filename)


def main():
    # Of course, this will need to be changed to whatever path the file is at
    convert_fcstd('/home/jwright/Downloads/Cube.fcstd')


if __name__ == '__main__':
    main()