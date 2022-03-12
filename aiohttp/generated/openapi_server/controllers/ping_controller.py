from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def ping(request: web.Request, ) -> web.Response:
    """ping

    


    """
    return web.Response(status=200)
