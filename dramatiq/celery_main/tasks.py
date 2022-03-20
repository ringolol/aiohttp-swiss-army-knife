import dramatiq
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from dramatiq.brokers.rabbitmq import RabbitmqBroker

from celery_main import oneshot_tasks
from celery_main import periodic_tasks
from celery_main import utils


rabbitmq_broker = RabbitmqBroker(url="amqp://localhost")
dramatiq.set_broker(rabbitmq_broker)


@dramatiq.actor
@utils.task_logger
@utils.async_to_sync
async def ping(*args, **kwargs):
    await periodic_tasks.ping.run(*args, **kwargs)


@dramatiq.actor
@utils.task_logger
@utils.async_to_sync
async def add(*args, **kwargs):
    await oneshot_tasks.add_task.run(*args, **kwargs)


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(
        ping.send,
        CronTrigger.from_crontab("* * * * *"),
    )
    try:
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown()


