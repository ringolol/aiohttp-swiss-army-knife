# coding: utf-8

import pytest
import json
from aiohttp import web



async def test_users_get(client):
    """Test case for users_get

    Returns a list of users.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

