from typing import List, Dict
from aiohttp import web
from celery_main import tasks

from openapi_server.models.users_request import UsersRequest
from openapi_server.models.users_response import UsersResponse
from openapi_server import util


async def create_users(request: web.Request, body) -> web.Response:
    """Returns a list of users.

    Optional extended description in CommonMark or HTML.

    :param body:
    :type body: dict | bytes

    """
    body = UsersRequest.from_dict(body)
    res = tasks.add.delay(4, 4).wait()
    return web.json_response(status=200, data=UsersResponse(name=body.username + str(res)).to_dict())
