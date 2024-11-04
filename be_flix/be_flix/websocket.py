
import asyncio
from websockets.asyncio.server import serve


async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)


async def main():
    async with serve(echo, "localhost", 5001):
        await asyncio.get_running_loop().create_future() # fun forever


print("Starting websocket")
asyncio.run(main())

