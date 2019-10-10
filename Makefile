test:
	pipenv run quotedb test -v 2
build:
	docker-compose build
migrate:
	pipenv run quotedb migrate
run: migrate
	pipenv run quotedb runserver

shell: migrate
	pipenv run quotedb shell

reset:
	pipenv run quotedb migrate quotedb zero
	git clean -f quotedb/migrations
	pipenv run quotedb makemigrations
	pipenv run quotedb migrate
