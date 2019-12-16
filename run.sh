#!/bin/bash
docker rm -f $(docker ps -qa)
docker run -d -e MYSQL_DB_TEST="proj2_test" -e SECRET_KEY="qqwertyuiop[asdfghjklzxcvbnn4567" -e MYSQL_DB="proj2" -e MYSQL_HOST="35.228.128.140" -e MYSQL_PASSWORD="Pame121295" -e MYSQL_USER="root" -p 5000:5000 --name flask-host flask-host
docker run -d -e MYSQL_DB_TEST="proj2_test" -e SECRET_KEY="qqwertyuiop[asdfghjklzxcvbnn4567" -e MYSQL_DB="proj2" -e MYSQL_HOST="35.228.128.140" -e MYSQL_PASSWORD="Pame121295" -e MYSQL_USER="root" -p 5001:5000 --name flask-number flask-number
docker run -d -e MYSQL_DB_TEST="proj2_test" -e SECRET_KEY="qqwertyuiop[asdfghjklzxcvbnn4567" -e MYSQL_DB="proj2" -e MYSQL_HOST="35.228.128.140" -e MYSQL_PASSWORD="Pame121295" -e MYSQL_USER="root" -p 5002:5000 --name flask-letter flask-letter
docker run -d -e MYSQL_DB_TEST="proj2_test" -e SECRET_KEY="qqwertyuiop[asdfghjklzxcvbnn4567" -e MYSQL_DB="proj2" -e MYSQL_HOST="35.228.128.140" -e MYSQL_PASSWORD="Pame121295" -e MYSQL_USER="root" -p 5003:5000 --name flask-sequence flask-sequence
