import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')

app = Celery("library")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "send_daily_statistic": {
        "task": "user_app.tasks.send_daily_statistic",
        "schedule": crontab(hour=18, minute=0),
    },
    "check_comment_by_admin": {
        "task": "user_app.tasks.check_comment_by_admin",
    }
}