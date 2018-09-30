release: cd mysite && python manage.py migrate && python manage.py collectstatic --noinput
web: cd mysite && gunicorn mysite.wsgi --log-file -
