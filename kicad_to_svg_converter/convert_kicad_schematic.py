#!/usr/bin/env python
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import os
import sys
import time
import argparse

# Get the path of this script
script_dir = os.path.dirname(os.path.abspath(__file__))
exports_dir = os.path.join(script_dir, 'output')

# Make sure that modules can be imported
sys.path.append(script_dir)

from libs.export_util import (
    PopenContext,
    xdotool,
    wait_for_window,
)


def usage():
    print("Pass the name of the file to be converted to this script as an argument.")
    print("./convert_kicad_schematic.py input/FILE_TO_EXPORT.sch")


def convertFile(args):
    input_file = args.in_spec

    with PopenContext(['eeschema', input_file], close_fds=True) as eeschema_proc:
        wait_for_window('eeschema', 'kicad_to_svg_converter')

        time.sleep(5)

        xdotool(['search', '--name', 'kicad_to_svg_converter', 'windowfocus'])

        xdotool(['key', 'alt+f'])
        xdotool(['key', 'p'])
        xdotool(['key', 'p'])

        wait_for_window('plot', 'Plot')
        xdotool(['search', '--name', 'Plot', 'windowfocus'])

        xdotool(['type', exports_dir])

        xdotool([
            'key',
            'Tab',
            'Tab',
            'Tab',
            'Tab',
            'Tab',
            'Up',
            'Up',
            'space',
        ])

        xdotool(['key', 'Return'])

        time.sleep(2)

        eeschema_proc.terminate()

    # print(exports_dir)

if __name__ == '__main__':
    desc = """
    Converts a KiCAD schematic to SVG format for display and diff-ing.
    A schematic can be provided as a file or as standard input.
    The svg is written the supplied output directory.
        """
    filename_pattern_help = """
    Filename pattern to use when creating output files.
    The sequential file number and the format are available.
    Default: schematic-%%(counter)d.%%(format)s
    Use stdout to write to stdout
        """
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("--format", action="store", default="SVG",
                        help="Output schematic file format (SVG)")
    parser.add_argument("--in_spec", action="store", required=True,
                        help="Input file path. Use stdin to read standard in")
    parser.add_argument("--out_spec", action="store",
                        default="./schematic-%(counter)d.%(format)s",
                        help=filename_pattern_help)
    args = parser.parse_args()

    convertFile(args)