FROM python:3.6-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN pip install --upgrade pip && pip install pipenv
RUN pipenv install --system --deploy

WORKDIR /code/mysite/
CMD gunicorn --build 0.0.0.0:8000 mysite.wsgi
