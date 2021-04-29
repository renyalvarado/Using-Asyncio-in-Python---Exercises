import asyncio
import zmq
from zmq.asyncio import Context

context = Context()


async def server():
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        message = await socket.recv()
        await asyncio.sleep(1)
        print(f"Received request: {message}")
        response = f"World -> {message}"
        socket.send(response.encode("utf-8"))


asyncio.run(server())
