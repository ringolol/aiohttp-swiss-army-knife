import os

import asyncpg

from dramatiq_tasks import utils


@utils.task_logger
@utils.async_to_sync
async def run():
    conn = await asyncpg.connect(database=os.environ['POSTGRES_DB'],
                                            user=os.environ['POSTGRES_USER'],
                                            password=os.environ['POSTGRES_PASSWORD'],
                                            host='db')
    await conn.execute(
        'CREATE SCHEMA IF NOT EXISTS test; '
        'CREATE TABLE IF NOT EXISTS test.table (id serial, data text); '
        'INSERT INTO test.table (data) VALUES (\'ping\')'
    )
    print('ping')
