from celery.schedules import crontab

from celery_main.celery import app
from celery_main import oneshot_tasks
from celery_main import periodic_tasks


app.conf.timezone = 'UTC'

app.conf.beat_schedule = {
    'add-every-minute': {
        'task': 'celery_main.tasks.ping',
        'schedule': crontab(),
        'args': (),
    },
}


@app.task
def ping(*args, **kwargs):
    periodic_tasks.ping.run(*args, **kwargs)


@app.task
def add(*args, **kwargs):
    oneshot_tasks.add_task.run(*args, **kwargs)
