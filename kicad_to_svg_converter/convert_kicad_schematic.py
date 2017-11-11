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
import subprocess
import time

# Get the path of this script
script_dir = os.path.dirname(os.path.abspath(__file__))
exports_dir = os.path.join(script_dir, 'output')

input_file = ""

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


def convertFile():
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
    if len(sys.argv) != 2:
        usage()
        exit()
    else:
        input_file = sys.argv[1]

    convertFile()