import asyncio
import asyncpg


async def run():
    conn = await asyncpg.connect(
        user="postgres",
        password="postgres",
        database="asyncio_example",
        host="127.0.0.1"
    )
    values = await conn.fetch(
        "SELECT * FROM Animal WHERE id =1"
    )
    print(values)
    await conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
