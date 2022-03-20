from celery.schedules import crontab

from celery_main.celery import app
from celery_main import oneshot_tasks
from celery_main import periodic_tasks
from celery_main import utils


app.conf.timezone = 'UTC'

app.conf.beat_schedule = {
    'add-every-minute': {
        'task': 'celery_main.tasks.ping',
        'schedule': crontab(),
        'args': (),
    },
}


@app.task
@utils.async_to_sync
async def ping(*args, **kwargs):
    await periodic_tasks.ping.run(*args, **kwargs)


@app.task
@utils.async_to_sync
async def add(*args, **kwargs):
    await oneshot_tasks.add_task.run(*args, **kwargs)
