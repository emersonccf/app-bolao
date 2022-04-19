#!/usr/bin/env bash
python manage.py migrate
python manage.py loaddata app-bolao-data.json # populate bd
python manage.py collectstatic --noinput
python manage.py createsuperuser