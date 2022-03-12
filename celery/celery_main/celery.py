from celery import Celery

app = Celery('celery_main',
             broker='pyamqp://guest@rabbitmq//',
             backend='rpc://',
             include=['celery_main.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
