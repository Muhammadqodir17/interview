.ONESHELL:

install:
	poetry install --with dev --no-root

migrate:
	python -B manage.py migrate

collectstatic:
	python -B manage.py collectstatic --noinput

run: migrate collectstatic
	python -B manage.py runserver 0.0.0.0:8000

up:
	docker compose up -d

down:
	docker compose down