#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install pipenv

pipenv install

pipenv run python manage.py collectstatic --no-input
pipenv run python manage.py migrate
