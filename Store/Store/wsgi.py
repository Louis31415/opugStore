"""
WSGI config for Store project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Store.settings")

#Following line added to let Apache2 & WSGI find module named 'Store'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

application = get_wsgi_application()
