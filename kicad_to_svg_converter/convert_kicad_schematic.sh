#!/bin/bash
# NOTE
# the -u (unbuffered flag) in the below is very important without it, KiCAD
# may manage to get some stdout junking up output when stdout is used.
if [ -z "$1" ]; then
   echo "************************"
   echo "KiCAD Schematic to SVG Conversion Docker Image"
   echo "************************"
   echo "Usage: docker run kicad-converter convert [options]"
   echo "Examples:"
   echo " Read a schematic from stdin, write output to stdout"
   echo ""
   echo "    cat sample.sch | sudo docker run -i kicad-converter:latest --in_spec stdin --out_spec stdout > sample.svg"
   echo " "
   echo " Mount a directory, and write results into the local directory"
   echo ""
   echo "    sudo docker run -i -v /home/user/kicad_to_svg_converter/samples:/home/conv/src dcowden/cadquery:latest --in_spec /home/conv/src/sample.sch --out_spec /home/conv/src/sample.svg"
   echo ""
   exec python -u /opt/kicad-converter/convert_kicad_schematic.py -h
   exit 1
fi;
if [ "$1" == "convert" ]; then
   exec python -u /opt/kicad-converter/convert_kicad_schematic.py "${@:2}"
fi;