#!/bin/bash

set -eu

if [ ! -f .env ]; then
    echo ".env not exists; create one";
    exit 1
else
    export $(cat .env | xargs)
fi



docker-compose down -v
docker-compose up --build -d
docker-compose run --rm api find api/migrations -name "0???_*.py" -exec rm -f {} \;
docker-compose run --rm api ./manage.py makemigrations
docker-compose run --rm api ./manage.py migrate
docker-compose run --rm api ./manage.py collectstatic --noinput
echo "\
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('admin', 'admin@myproject.com', 'password')
" | docker-compose run --rm -T api ./manage.py shell
echo "\
mc config host add minio http://storage:9000 '$STORAGE_ACCESS_KEY' '$STORAGE_SECRET_KEY'
mc policy set download minio/django
" | docker run -i --rm --entrypoint=/bin/sh --network=personamobile_default minio/mc 

