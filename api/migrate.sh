
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"admin@gmail.com"}
SUPERUSER=${DJANGO_SUPERUSER_USERNAME:-"admin"}


/opt/venv/bin/python manage.py migrate --noinput
/opt/venv/bin/python manage.py createsuperuser --username $SUPERUSER --email $SUPERUSER_EMAIL --noinput || true