from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

from celery.schedules import crontab

# setting the Django settings module.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventPlanner.settings')

app = Celery('eventPlanner')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks()


# schedule
from celery.schedules import crontab

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-minute-hour-day4/thursday': {
        'task': 'task.generate_pdf',
        'schedule': crontab(hour='*', minute='*', day_of_week=4),
    },
    'generate-every-10-seconds-bibin-3': {
        'task': 'task.generate_pdf',  # give what's shown in celery list discovered tasks.
        'schedule': 10.0,
        'options': {
            'expires': 15.0,
        },
    },
}