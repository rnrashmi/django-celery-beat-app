
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from dj_celery import settings
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_celery.settings')

app = Celery('dj_celery')

app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')

# Set the broker URL (Redis in your case)
app.config_from_object('django.conf:settings', namespace='CELERY')


# Load task modules from all registered Django apps.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# app.autodiscover_tasks()
# CELERY_BEAT_SCHEDULE_FILE = None  # Ensure the file-based scheduler is not used
# CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# celery -A dj_celery beat  -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler




