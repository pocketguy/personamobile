$(shell touch .env)
include .env
export $(shell sed 's/=.*//' .env)

define rand
$(shell cat /dev/urandom | head -c 24 | base64)
endef

define DOTNENV_CONTENT =
API_SECRET_KEY=$(rand)
DB_PASSWORD=$(rand)
STORAGE_ACCESS_KEY=$(rand)
STORAGE_SECRET_KEY=$(rand)
endef

export DOTNENV_CONTENT

default:
	@echo "call 'make create_dotenv' to create .env file"
	@echo "call 'make clean' to fresh install"

create_dotenv:
	@echo "$$DOTNENV_CONTENT" > .env

require_dotenv:
	test -s .env || { echo ".env not exits; call 'make create_dotenv'"; exit 1;}

docker-down:
	docker-compose down -v

docker-up:
	docker-compose up --build -d

removemigrations:
	docker-compose exec api find api/migrations -name "0???_*.py" -exec rm -f {} \;

makemigrations:
	docker-compose exec api python manage.py makemigrations

migrate:
	docker-compose exec api python manage.py migrate

createsuperuser:
	bash -c "echo \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password') \" | docker-compose exec -T api python manage.py shell"

collectstatic:
	docker-compose exec api python manage.py collectstatic --noinput

add_minio_permissions:
	@echo "mc config host add minio http://storage:9000 '$$STORAGE_ACCESS_KEY' '$$STORAGE_SECRET_KEY' && mc policy set download minio/django " | docker run -i --rm --entrypoint=/bin/sh --network=personamobile_default minio/mc 

clean: require_dotenv docker-down docker-up removemigrations makemigrations migrate createsuperuser collectstatic add_minio_permissions
	@echo "clean done"
