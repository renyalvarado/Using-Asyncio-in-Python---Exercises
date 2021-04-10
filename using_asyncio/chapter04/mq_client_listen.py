import argparse
import asyncio
import uuid
from msgproto import read_msg, send_msg


async def main_client(args):
    me = uuid.uuid4().hex[:8]
    print(f"Starting up {me}")
    reader, writer = await asyncio.open_connection(args.host, args.port)
    print(f"I am {writer.get_extra_info('sockname')}")
    channel = args.listen.encode()
    await send_msg(writer, channel)
    try:
        while data := await read_msg(reader):
            print(f"Received by {me}: {data[:20]}")
        print("Connection ended.")
    except asyncio.IncompleteReadError:
        print("Server closed.")
    finally:
        writer.close()
        await writer.wait_closed()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=25000)
    parser.add_argument("--listen", default="/topic/foo")
    try:
        asyncio.run(main_client(parser.parse_args()))
    except KeyboardInterrupt:
        print("Client - Bye!")
