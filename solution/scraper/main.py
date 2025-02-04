from typing import List
from fastapi import FastAPI, BackgroundTasks
from routes import upload
from settings import database
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(upload.router, prefix="/api",  tags=["Upload"])
