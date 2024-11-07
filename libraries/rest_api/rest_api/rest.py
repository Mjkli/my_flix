
# FastAPI Library to handle serving differnt apis given by the user


import uvicorn
import asyncio


async def serve(handles):
    config = uvicorn.Config(handles, host="127.0.0.1", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    from fastapi import FastAPI
    app = FastAPI()
    asyncio.run(server(app))

