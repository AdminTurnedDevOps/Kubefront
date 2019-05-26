# Pre-reqs;
# 1. You will need a docker folder holding your Dockerfile in a place of your choosing
# 2. You will need a directory within your directly holding your Dockerfile that has the (continued)
# Kubefront git repo AND you will need your cache folder, http-cache folder, and config FROM your .kube (continued)
# directory in the SAME directory that you just created for your Dockerfile and your Kubefront repo

FROM ubuntu:18.04

MAINTAINER Mike Levan

RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

RUN apt-get update -y

RUN pip3 install Flask
RUN pip3 install Kubernetes
RUN pip3 install more_itertools

RUN apt-get install curl -y
RUN apt-get update && apt-get install -y apt-transport-https -y
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list
RUN apt-get update -y
RUN apt-get install -y kubectl

COPY Kubefront /home

RUN mkdir /root/.kube

RUN cp -r /home/cache /root/.kube
RUN cp -r /home/http-cache /root/.kube
RUN cp /home/config /root/.kube