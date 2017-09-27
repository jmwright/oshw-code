# KiCAD to SVG Converter

This converter is in pre-alpha release condition and will change a lot as development progresses.

## Installing

The following packages need to be installed before using this script. The following commands assume Ubuntu Server.

```bash
sudo apt-get install kicad
sudo apt-get install xvfb
sudo apt-get install xdotool
sudo apt-get install imagemagick
```

The following commands also need to be run to set up the virtual display for the EESchema GUI. They can be added to `.bash_profile` or `.bashrc` to make them permanent.

```bash
Xvfb :0 -screen - 1280x1024x16&
export DISPLAY=":0.0"
```

## Usage

1. Put a KiCAD project's .pro and .sch files in the `to_convert` directory.
2. Run the `export_schematic.py` script, passing the name of the .sch file as an argument.

```bash
./export_schematic.py to_convert/sample.sch
```
