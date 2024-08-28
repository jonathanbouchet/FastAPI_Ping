from fastapi import FastAPI
from contextlib import asynccontextmanager
import aiocron
import requests
import datetime

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"start time: {start_time}")
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/", tags=["health check"])
async def root() -> dict[str, str]:
    return {"msg":"Hello World"}


@app.get("/ping", tags=["ping"])
async def ping() -> dict[str, str]:
    return {"msg":"ping"}

# @aiocron.crontab('*/2 * * * *')
# def self_ping() -> None:
#     ping_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(f"ping time: {ping_time}")
#     # response = requests.get(url="http://127.0.0.1:8000/ping")
#     response = requests.get(url="https://fastapi-ping.onrender.com/ping")
#     print(f"ping code: {response.status_code}")
#     print(f"ping code: {response.content}")