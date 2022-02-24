release: python manage.py migrate --noinput
web: gunicorn faker_companies.wsgi:application --log-file -
