all: clean build
	docker run -d --name test-celery-psql --rm -e POSTGRES_DB=celery postgres:9.5
	docker run -d --name test-celery-redis --rm redis
	docker run -p 8080:15672 -d --link test-celery-redis --link test-celery-psql --name test-celery-rabbitmq --rm -ti rabbitmq:3-management
	docker run --rm -ti -v `pwd`:/app --link test-celery-redis --link test-celery-psql --link test-celery-rabbitmq test-celery bash


shell: build
	docker run --rm -ti -v `pwd`:/app --link test-celery-redis --link test-celery-psql --link test-celery-rabbitmq test-celery bash

build:
	docker build -t test-celery .

clean:
	docker rm -f test-celery-psql || echo
	docker rm -f test-celery-redis || echo
	docker rm -f test-celery-rabbitmq || echo
	docker rm -f test-celery || echo
