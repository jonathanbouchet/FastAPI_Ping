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

@aiocron.crontab('*/2 * * * *')
@app.get("/", tags=["ping"])
async def self_ping():
    ping_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"ping time: {ping_time}")
    response = requests.get(url="http://127.0.0.1:8000")
    print(f"Health check response: {response.status_code}")