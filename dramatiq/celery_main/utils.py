import logging

import asyncio


logger = logging.getLogger("dramatiq")


def async_to_sync(fun):
    def dec(*args, **kwargs):
        return asyncio.run(fun(*args, **kwargs))
    return dec


def task_logger(fun):
    def dec(*args, **kwargs):
        logger.info(
            f'calling task {fun.__name__}({", ".join(args)}, '
            f'{", ".join(f"{k}={v}" for k, v in kwargs)})'
        )
        try:
            res = fun(*args, **kwargs)
        except Exception:
            logger.exception(f'task {fun.__name__} finishid with exception')
            raise
        logger.info(f'task {fun.__name__} finished with result {res}')

        return res

    return dec
