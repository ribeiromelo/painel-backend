release: python manage.py collectstatic --noinput
web: gunicorn painel_cereais.wsgi:application --bind 0.0.0.0:$PORT
release: python manage.py migrate
