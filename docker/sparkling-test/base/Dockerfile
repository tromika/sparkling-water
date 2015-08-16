FROM ubuntu:precise

ENV VERSION 0.23.0
ENV PKG_RELEASE 1.0

# Repo
#RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
# Java 7 installation from Oracle
RUN apt-get update
RUN apt-get -y install python-software-properties
RUN add-apt-repository ppa:webupd8team/java

# Upgrade package index
RUN apt-get update
# RUN apt-get -y upgrade

# automatically accept oracle license
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

# and install java 7 oracle jdk
RUN apt-get -y install oracle-java7-installer && apt-get clean
RUN apt-get -y install oracle-java7-set-default

# Install additional tools
RUN apt-get -y install \
  less \
  curl \
  vim-tiny \
  sudo \
  openssh-server \
  unzip

# Install Spark 1.4.1
RUN curl -s http://www.eu.apache.org/dist/spark/spark-1.4.1/spark-1.4.1-bin-hadoop2.6.tgz | tar -xz -C /opt && \
    ln -s /opt/spark-1.4.1-bin-hadoop2.6 /opt/spark && \
    mkdir /opt/spark/work && \
    chmod 0777 /opt/spark/work

# Install Sparkling water latest version
RUN curl -s http://h2o-release.s3.amazonaws.com/sparkling-water/master/103/sparkling-water-0.2.103.zip --output sw.zip && \
  unzip sw.zip -d /opt/ && \
  ln -s /opt/sparkling-water-0.2.103 /opt/sparkling-water && \
  rm -f sw.zip

  WORKDIR /tmp
  RUN \
    curl -s -O https://downloads.mesosphere.io/master/ubuntu/14.04/mesos_${VERSION}-${PKG_RELEASE}.ubuntu1404_amd64.deb && \
    dpkg --unpack mesos_${VERSION}-${PKG_RELEASE}.ubuntu1404_amd64.deb && \
    apt-get install -f -y && \
    rm mesos_${VERSION}-${PKG_RELEASE}.ubuntu1404_amd64.deb && \
    apt-get clean



# Setup environment
ENV SPARK_HOME /opt/spark
ENV SPARKLING_WATER_HOME /opt/sparkling-water

WORKDIR ${SPARKLING_WATER_HOME}
