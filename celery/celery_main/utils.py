import asyncio


def async_to_sync(fun):
    def dec(*args, **kwargs):
        return asyncio.run(fun(*args, **kwargs))
    return dec
