from typing import List, Dict
from aiohttp import web

from openapi_server.models.inline_object import InlineObject
from openapi_server.models.inline_response200 import InlineResponse200
from openapi_server import util


async def users_post(request: web.Request, body) -> web.Response:
    """Returns a list of users.

    Optional extended description in CommonMark or HTML.

    :param body: 
    :type body: dict | bytes

    """
    body = InlineObject.from_dict(body)
    return web.json_response(data=InlineResponse200(body.username), status=200)
