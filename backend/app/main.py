# main.py
'''Main File for LogiNet'''

import asyncio
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.redis import redis_client
from app.core.logging import setup_logging
from app.middleware import LoggingMiddleware, WebSocketLoggingMiddleware
from app.routers import users

setup_logging()
startup_logger = logging.getLogger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    startup_logger.info("Starting LogiNet...")
    await redis_client.connect()
    yield
    startup_logger.info("Shutting down LogiNet...")
    await redis_client.close_redis()

app = FastAPI(
    title="Foxhole LogiNet",
    description="Regiment logistics coordination for Foxhole",
    version="0.0.1",
    lifespan=lifespan,
)

app.add_middleware(                                     
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(LoggingMiddleware)
app.add_middleware(WebSocketLoggingMiddleware)

app.include_router(users.router)

@app.get("/health")
async def health():
    return {"status": "ok", "service": "Foxhole LogiNet"}
