#!/bin/bash

echo "Wait starting database..."

while ! nc -z db 5432; do
  sleep 1
done

echo "Database done. Starting API..."

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata immoble_data.json announcement_data.json reserve_data.json
python manage.py runserver 0.0.0.0:8000