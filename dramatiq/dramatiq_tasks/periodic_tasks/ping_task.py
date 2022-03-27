import os

import asyncpg

from dramatiq_tasks import utils


@utils.task_logger
@utils.async_to_sync
async def run():
    conn = await asyncpg.connect(
        database=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        host=os.environ["POSTGRES_ADDRESS"],
    )
    await conn.execute("INSERT INTO test.table (data) VALUES ('ping')")
    print("ping")
