import numbers
from dramatiq_tasks import utils


@utils.task_logger
@utils.async_to_sync
async def run(x: numbers.Number, y: numbers.Number):
    print(x + y)
