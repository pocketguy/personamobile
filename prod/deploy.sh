#!/bin/bash


git pull
docker-compose pull -q
docker-compose up -d --scale backend=3 --scale web=3
docker-compose run --rm backend ./manage.py migrate
docker-compose run --rm backend ./manage.py collectstatic --noinput
