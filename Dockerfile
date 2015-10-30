FROM stackbrew/ubuntu:saucy
MAINTAINER Ted Chen <tedlchen@gmail.com>

# Enable the necessary sources and upgrade to latest
RUN echo "deb http://archive.ubuntu.com/ubuntu saucy main universe" > /etc/apt/sources.list && \
  apt-get update && \
  apt-get upgrade -y -o DPkg::Options::=--force-confold

# Install python modules
RUN apt-get update && apt-get install python-twisted python-autobahn -y

# Cleanup
RUN apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/*

ADD ./server.py /opt/app/server.py

ENTRYPOINT ["python", "/opt/app/server.py"]
CMD ["80"]
