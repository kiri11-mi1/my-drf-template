import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(packages=['apps'])


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    from apps.users.tasks import test_task_for_example
    sender.add_periodic_task(20.0, test_task_for_example.s())
