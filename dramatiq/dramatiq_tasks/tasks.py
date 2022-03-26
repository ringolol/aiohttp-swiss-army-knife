from pytz import utc

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

from dramatiq_tasks import oneshot_tasks
from dramatiq_tasks import periodic_tasks


rabbitmq_broker = RabbitmqBroker(host="rabbitmq")
dramatiq.set_broker(rabbitmq_broker)


@dramatiq.actor
def ping(*args, **kwargs):
    periodic_tasks.ping_task.run(*args, **kwargs)


@dramatiq.actor
def add(*args, **kwargs):
    oneshot_tasks.add_task.run(*args, **kwargs)


if __name__ == "__main__":
    print('starting scheduler')
    scheduler = BlockingScheduler(timezone=utc)
    scheduler.add_job(
        ping.send,
        CronTrigger.from_crontab("* * * * *"),
    )
    try:
        scheduler.start()
    except Exception as exc:
        print(f'scheduler error \n{exc}')
    finally:
        print('stopping scheduler')
