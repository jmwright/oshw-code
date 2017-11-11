FROM ubuntu:16.04

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

ENV CONV_HOME=/opt/kicad-converter
ENV DISPLAY=":0.0"

# install supporting tools
RUN apt-get update --fix-missing && \
    apt-get install -y software-properties-common wget curl

# install kicad and supporting packages
RUN apt-get install -y kicad xvfb xdotool imagemagick

# make the data directories
RUN mkdir -p $CONV_HOME
RUN mkdir -p $CONV_HOME/build_data
VOLUME $CONV_HOME/build_data

COPY convert_kicad_schematic.py convert_kicad_schematic.sh $CONV_HOME/
COPY libs $CONV_HOME/libs

RUN chmod +x $CONV_HOME/convert_kicad_schematic.sh
RUN useradd -ms /bin/bash conv
USER conv
WORKDIR /home/conv

# start the app entrypoint when the container runs
# CMD /app/entrypoint.sh
ENTRYPOINT [ "/opt/kicad-converter/convert_kicad_schematic.sh" ]
