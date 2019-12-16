#!/bin/bash
docker build -t flask-host ./flask_host
docker build -t flask-number ./flask_generator_number
docker build -t flask-letter ./flask_generator_letter
docker build -t flask-sequence ./flask_generator_sequence
docker rmi $(docker images -f "dangling=true" -q)
