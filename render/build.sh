#!/bin/bash

# Exit on error
set -o errexit

pip install -r ./requirements/production.txt

# python manage.py collectstatic --no-input

echo "---apply database migrations---"
# python manage.py makemigrations --settings=core.settings.local
python manage.py migrate --settings=core.settings.local

# create superuser by default
echo "---create superuser---"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin@gmail.com', 'Admin12345678#')" | python manage.py shell --settings=core.settings.local
