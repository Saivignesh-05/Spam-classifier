#!/bin/bash
docker rm $(docker container ls -a -q)
