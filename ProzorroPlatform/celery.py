import os

from celery import Celery
from celery.schedules import crontab
from MonitoringService.tasks import check_tender

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProzorroPlatform.settings')

app = Celery('ProzorroPlatform')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

@app.on_after_configure.connect
def periodic_task(sender, **kwargs):
    sender.add_periodic_task(
        crontab(),
        check_tender
    )










