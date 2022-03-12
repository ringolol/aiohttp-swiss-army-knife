# coding: utf-8

import pytest
import json
from aiohttp import web



async def test_ping(client):
    """Test case for ping

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

