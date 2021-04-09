import asyncio


async def echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    print("New connection")
    try:
        while data := await reader.readline():
            writer.write(data.upper())
            await writer.drain()
        print("Leaving connection!")
    except asyncio.CancelledError:
        print("Connection Dropped!")


async def main_server_function(host="127.0.0.1", port=8888):
    server = await asyncio.start_server(echo, host, port)
    async with server:
        await server.serve_forever()


try:
    asyncio.run(main_server_function())
except KeyboardInterrupt:
    print("Bye!")
