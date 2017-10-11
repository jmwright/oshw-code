FROM ubuntu:16.04

# install supporting tools
RUN apt update && \
    apt install -y software-properties-common wget curl

# install kicad and supporting packages
RUN apt install -y kicad xvfb xdotool imagemagick

# make the data directories
RUN mkdir /input /output

# start the app entrypoint when the container runs
CMD /app/entrypoint.sh
