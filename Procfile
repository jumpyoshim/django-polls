release: python mysite/manage.py migrate && python mysite/manage.py collectstatic --noinput
web: gunicorn mysite.mysite.wsgi --log-file -
