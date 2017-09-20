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

# Get the path of this script
script_dir = os.path.dirname(os.path.abspath(__file__))
exports_dir = os.path.join(script_dir, 'exports')

input_file = ""

# Make sure that modules can be imported
sys.path.append(script_dir)

from libs.export_util import (
    PopenContext,
    versioned_schematic,
    xdotool,
    wait_for_window,
    recorded_xvfb,
)


def usage():
    print("Pass the name of the file to be converted to this script as an argument.")
    print("./export_schematic.py FILE_TO_EXPORT.sch")


def convertFile():
    with PopenContext(['eeschema', input_file], close_fds=True) as eeschema_proc:
        # eeschema_plot_schematic(output_dir)
        wait_for_window('eeschema', '\[')
        # eeschema_proc.terminate()

    # print(exports_dir)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        exit()
    else:
        input_file = sys.argv[1]

    convertFile()