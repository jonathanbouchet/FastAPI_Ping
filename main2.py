from fastapi import FastAPI
import asyncio
import httpx
from contextlib import asynccontextmanager
import datetime

@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(cyclic_func())
    yield
    task.cancel()

async def cyclic_func():
    while True:
        try:
            async with httpx.AsyncClient() as client:
                await client.get("https://fastapi-ping.onrender.com/ping")
                await asyncio.sleep(120)  # 15 minutes
        except Exception as e:
            print(f"Error in cyclic_func: {e}")
            await asyncio.sleep(60)  # wait a minute before retrying

app = FastAPI(lifespan=lifespan)

@app.get("/ping")
async def ping() -> None:
    ping_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"ping time: {ping_time}")