
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

clean: docker-down docker-up removemigrations makemigrations migrate createsuperuser collectstatic