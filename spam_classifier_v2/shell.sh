#!/bin/bash
export DOCKER_BUILDKIT=1
# DOCKER_BUILDKIT=1 docker build . # enables build kit (--mount option in pip install -r requirments)
docker build -t ${1} .
# enter the tagname for the container for ${1}