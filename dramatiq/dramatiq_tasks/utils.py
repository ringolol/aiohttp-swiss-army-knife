import asyncio
import functools
import typing
import logging

import dramatiq

logger = logging.getLogger("dramatiq")


def async_to_sync(fun: typing.Callable[..., dramatiq.Message]) -> dramatiq.Message:
    @functools.wraps(fun)
    def dec(*args, **kwargs):
        return asyncio.run(fun(*args, **kwargs))

    return dec


def task_logger(fun: typing.Callable[..., dramatiq.Message]) -> dramatiq.Message:
    @functools.wraps(fun)
    def dec(*args, **kwargs):
        logger.info(
            f'calling task {fun.__module__}.{fun.__name__}({", ".join(map(str, args))}, '
            f'{", ".join(f"{k}={v}" for k, v in kwargs)})'
        )
        try:
            task_info = fun(*args, **kwargs)
        except Exception:
            logger.exception(
                f"task {fun.__module__}.{fun.__name__} finishid with exception"
            )
            raise
        logger.info(f"task {fun.__module__}.{fun.__name__} finished")
        return task_info

    return dec
