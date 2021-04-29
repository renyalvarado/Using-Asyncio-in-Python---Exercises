import asyncio
import zmq
from zmq.asyncio import Context

context = Context()
loop = asyncio.get_event_loop()


async def client(i):
    print("Connecting to server")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    request = f"Hello {i}"
    print(f"Sending request: {request}")
    socket.send(request.encode("utf8"))
    response = await socket.recv()
    print(f"request ({request}), response ({response})\n")
    socket.close()


clients = asyncio.gather(*[client(i) for i in range(10)])
loop.run_until_complete(clients)
loop.close()
