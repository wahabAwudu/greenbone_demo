#!/bin/bash

set -e

python manage.py collectstatic --no-input

python manage.py migrate --no-input

celery -A gb_demo.celery_app worker --beat --scheduler django --loglevel=info --without-mingle --detach

exec gunicorn --bind 0.0.0.0:8000 gb_demo.wsgi:application

"$@"
