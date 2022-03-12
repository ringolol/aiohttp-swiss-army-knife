# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.users_request import UsersRequest
from openapi_server.models.users_response import UsersResponse


async def test_create_users(client):
    """Test case for create_users

    Returns a list of users.
    """
    body = {
  "username" : "username"
}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

