VENV = venv
PYTHON = ${VENV}/bin/python3
PIP = ${VENV}/bin/pip3


.PHONY: help venv install flake8 isort black runserver makemigrations migrate shell_plus createsuperuser flush_db reset_db

venv:
	python3 -m venv venv

install: venv roas_app/requirements/base.txt roas_app/requirements/dev.txt roas_app/requirements/lint.txt
	${PIP} install -r roas_app/requirements/base.txt -r roas_app/requirements/dev.txt -r roas_app/requirements/lint.txt

makemigrations: install
	${PYTHON} roas_app/manage.py makemigrations

migrate: install
	${PYTHON} roas_app/manage.py migrate

createsuperuser: migrate
	${PYTHON} roas_app/manage.py create_superuser

runserver: createsuperuser
	${PYTHON} roas_app/manage.py runserver

test: install
	${PYTHON} -m pytest roas_app

format: install
	${PYTHON} -m black .

lint: install
	${PYTHON} -m flake8 roas_app/.

isort: install
	${PYTHON} -m isort .

load_data: install
	${PYTHON} roas_app/manage.py load_data campaigns.csv --ad_groups adgroups.csv --search_terms search_terms.csv

shell_plus: install
	${PYTHON} roas_app/manage.py shell_plus

reset_db: install
	${PYTHON} roas_app/manage.py reset_db

flush_db: install
	${PYTHON} roas_app/manage.py flush --database=default --noinput
