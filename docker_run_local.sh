#!/bin/bash
docker system prune -f
docker stop api 2>&1
docker rm api 2>&1
docker build -f Dockerfile -t api  .
docker run \
-v ./:/app/ -p5000:5000 --name api api 