FROM ubuntu:18.04

RUN apt-get clean && apt-get update
ENV DEBIAN_FRONTEND noninteractive

# Install required software
RUN apt-get install -y apt-utils && \
    apt-get install -y sudo && \
    apt-get install -y wget && \
 sed -i 's/^mesg n$/tty -s \&\& mesg n/g' /root/.profile


ENV LANG            en_US.UTF-8
ENV LC_ALL          en_US.UTF-8


RUN apt-get install apt-transport-https

# Install Python 3.7
RUN apt-get install -y python3-pip && \
    apt-get install -y python-pip && \
    apt-get update && \
    apt-get install -y software-properties-common vim && \
    sudo apt-get update && \
    sudo apt-get install python3.7 -y

RUN pip3 install pytest && \
    pip3 install pytest-html && \
    pip3 install --user -U nltk

# Install git
RUN apt-get update && apt-get install -y git







