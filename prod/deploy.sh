#!/bin/bash


docker-compose pull -q
docker-compose up -d
docker-compose run --rm backend ./manage.py migrate
docker-compose run --rm backend ./manage.py collectstatic --noinput
