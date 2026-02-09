#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files (if you use them)
python manage.py collectstatic --noinput

# Run migrations to create your database tables
python manage.py migrate
