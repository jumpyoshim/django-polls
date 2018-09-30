release: python3 manage.py migrate && python3 manage.py collectstatic --noinput
web: cd mysite && gunicorn mysite.wsgi --log-file -
