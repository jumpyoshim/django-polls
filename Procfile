release: python manage.py migrate
web: python manage.py collectstatic --noinput && gunicorn mysite.wsgi --log-file -
