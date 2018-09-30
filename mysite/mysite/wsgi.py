"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

DJANGO_SETTINGS_MODULE = os.environ['DJANGO_SETTINGS_MODULE']

application = get_wsgi_application()
