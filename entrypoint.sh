#!/bin/bash -x

python manage.py makemigrations
python manage.py migrate
exec "$@"
