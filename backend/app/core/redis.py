# redis.py
'''Redis Manager for LogiNet'''

from redis.asyncio import Redis, ConnectionPool
from contextlib import asynccontextmanager

from app.config import settings


class RedisClient:
    def __init__(self):
        self.pool: ConnectionPool | None = None
        self.client: Redis | None = None

    async def connect(self):
        self.pool = ConnectionPool.from_url(
            settings.redis_url,
            max_connections=100,
            decode_responses=True
        )
        self.client = Redis(connection_pool=self.pool)

    async def close_redis(self):
        if self.client:
            await self.client.close()
        if self.pool:
            await self.pool.disconnect()

    async def get_redis(self) -> Redis:
        return self.client
    
redis_client = RedisClient()

async def get_redis_client() -> Redis:
    return await redis_client.get_redis()
