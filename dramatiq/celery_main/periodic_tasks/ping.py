import os

import asyncpg


async def run():
    conn = await asyncpg.connect(database=os.environ['POSTGRES_DB'],
                                            user=os.environ['POSTGRES_USER'],
                                            password=os.environ['POSTGRES_PASSWORD'],
                                            host='db')
    await conn.execute('INSERT INTO test.table (data) VALUES (\'ping\')')
    print('ping')
