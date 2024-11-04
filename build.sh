#!/usr/bin/env bash

# Exit on error
set -o errexit

pipenv install --deploy --ignore-pipfile

# Convert static asset files
python probless/manage.py collectstatic --no-input

# Apply any outstanding database migrations
python probless/manage.py migrate
