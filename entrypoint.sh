#!/bin/ash

echo "Apply migration"

cd ./ciphers_project
python3 manage.py migrate
python manage.py runserver 0.0.0.0:8000

exec"$@"