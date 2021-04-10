import asyncio
from asyncio import gather, StreamReader, StreamWriter
from collections import deque, defaultdict
from typing import Deque, DefaultDict
from msgproto import read_msg, send_msg

SUBSCRIBERS: DefaultDict[bytes, Deque] = defaultdict(deque)


async def client(reader: StreamReader, writer: StreamWriter) -> None:
    peername = writer.get_extra_info("peername")
    subscribe_channel = await read_msg(reader)
    SUBSCRIBERS[subscribe_channel].append(writer)
    print(f"Remote {peername} subscribed to {subscribe_channel}")
    try:
        while channel_name := await read_msg(reader):
            data = await read_msg(reader)
            print(f"Sending to {channel_name}: {data[:19]}...")
            conns = SUBSCRIBERS[channel_name]
            if conns and channel_name.startswith(b"/queue"):
                conns.rotate()
                conns = [conns[0]]
            await gather(*[send_msg(c, data) for c in conns])
    except asyncio.CancelledError:
        print(f"Remote {peername} closing connection.")
        writer.close()
        await writer.wait_closed()
    except asyncio.IncompleteReadError:
        print(f"Remote {peername} disconnected")
    finally:
        print(f"Remote {peername} closed")
        SUBSCRIBERS[subscribe_channel].remove(writer)


async def server_main(*args, **kwargs):
    server = await asyncio.start_server(*args, **kwargs)
    async with server:
        await server.serve_forever()


try:
    asyncio.run(server_main(client, host="127.0.0.1", port="25000"))
except KeyboardInterrupt:
    print("Bye!")
