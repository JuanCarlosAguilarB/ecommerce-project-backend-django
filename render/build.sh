# #!/bin/bash

# # # Exit on error
# # set -o errexit

# # pip install -r ./requirements/production.txt

# # # python manage.py collectstatic --no-input

# # echo "---apply database migrations---"
# # # python manage.py makemigrations --settings=core.settings.local
# # python manage.py migrate --settings=core.settings.local

# # # create superuser by default
# # echo "---create superuser---"
# # echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin@gmail.com', 'Admin12345678#')" | python manage.py shell --settings=core.settings.local

# # # runserver
# # echo "---run server---"
# # # python manage.py runserver --settings=core.settings.local 0.0.0.0:8000
# # # gunicorn core.wsgi


# # Check for Redis existence
# if ! command -v redis-server &> /dev/null
# then
#     echo "Downloading Redis..."
#     # Download Redis
#     wget http://download.redis.io/redis-stable.tar.gz
#     tar xvzf redis-stable.tar.gz
#     cd redis-stable
#     make

#     echo "Redis downloaded and compiled successfully."
# else
#     echo "Redis is already installed on the system."
# fi

# # Start Redis
# echo "Starting Redis server..."
# redis-server &



#!/bin/bash
apk add lsb-release curl gpg

curl -fsSL https://packages.redis.io/gpg | gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/redis.list

apk add  redis

snap install redis