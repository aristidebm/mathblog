SHELL := /usr/bin/bash
.PHONY: test install install-dev run-dev-server check-migrations codestyle help install-tailwind

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

test:
	# launch test
	# python -m unittest discover --start-directory blog --pattern "test_*.py"
	python -m unittest discover -s blog -p "tests.py"

install:
	# install functional requirements
	pip install -r requirements.txt

dev-install:
	# install python dev requirements
	pip install -r requirement-dev.txt

run-dev-server:
	# run flask server in development mode.
	flask run 

check-migrations:
	# check the database migrations

codestyle:
	# check if teh code suite the pep8 requirement
	flake8 blog
	isort --profile black blog
	black --check --diff --color blog
	# check the link below for isort and black compatibility.
	# https://pycqa.github.io/isort/docs/configuration/black_compatibility/#:~:text=For%20projects%20that%20officially%20use,profile%20will%20automatically%20be%20applied.
