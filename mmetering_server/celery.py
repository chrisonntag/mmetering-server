from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings
from django.apps import apps

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmetering_server.settings')

app = Celery('mmetering_server')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
