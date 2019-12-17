#!/bin/bash
docker rm -f flask-host
docker rm -f flask-number
docker rm -f flask-letter
docker rm -f flask-sequence

docker build -t flask-host ./flask_host
docker build -t flask-number ./flask_generator_number
docker build -t flask-letter ./flask_generator_letter
docker build -t flask-sequence ./flask_generator_sequence
docker rmi $(docker images -f "dangling=true" -q)
