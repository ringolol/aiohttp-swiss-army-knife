from typing import List, Dict
from aiohttp import web
import asyncpg

from dramatiq_tasks import tasks

from openapi_server.models.users_request import UsersRequest
from openapi_server.models.users_response import UsersResponse
from openapi_server import util


async def create_users(request: web.Request, body) -> web.Response:
    """Returns a list of users.

    Optional extended description in CommonMark or HTML.

    :param body:
    :type body: dict | bytes

    """
    async with request.config_dict["pool"].acquire() as conn:
        conn: asyncpg.Connection
        num = await conn.fetchval("select 5")
    body = UsersRequest.from_dict(body)
    tasks.add.send(2, 3)
    return web.json_response(
        status=200, data=UsersResponse(name=body.username + str(num)).to_dict()
    )
