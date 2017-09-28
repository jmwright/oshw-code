# KiCAD to SVG Converter

This converter is in pre-alpha release condition and will change a lot as development progresses.

## Installing

The following packages need to be installed before using this script. The following commands assume Ubuntu Server.

```bash
sudo apt-get install kicad xvfb xdotool imagemagick
```

The following commands also need to be run to set up the virtual display for the EESchema GUI. They can be added to `.bash_profile` or `.bashrc` to make them permanent.

```bash
Xvfb :0 -screen - 1280x1024x16&
export DISPLAY=":0.0"
```

## Usage

1. Put a KiCAD project's *.pro, *-cache.lib and *.sch files in the `to_convert` directory.
2. Run the `export_schematic.py` script, passing the name of the .sch file as an argument.

```bash
./export_schematic.py to_convert/sample.sch
```

## Troubleshooting

In order to see what is happening in the GUI on the server, it is useful to set up remote access.

### Server-Side

Install the pre-requisites.
```bash
sudo apt-get install x11vnc
# Optional in case you want a window manager running
sudo apt-get install fluxbox
```
If you want a window manager to be running when you remote in, run the following line on the server.
```bash
fluxbox &
```
Do a one-time setup of the password for the VNC connection.
```bash
x11vnc -storepasswd
```
Start the x11vnc server that will accept incoming connections over the network with password protection.
```bash
x11vnc -display :0.0 -usepw
```

### Client-Side

Install vncviewer
```bash
sudo apt-get install vncviewer
```
Run the following to connect to the server using VNC, substituting the IP address of the server. You'll need to enter the password you set for x11vnc on the server.
```bash
vncviewer <server_ip_address>
```
