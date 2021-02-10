#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata user_init.json
python manage.py runserver 0.0.0.0:8000
