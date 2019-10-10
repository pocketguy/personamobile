#!/bin/bash

set -eu

docker-compose run --rm api ./manage.py test
