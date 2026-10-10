# router.py
'''Users Router for Loginet'''

from fastapi import APIRouter, Depends

from sqlmodel import Session
from redis.asyncio import Redis

from app.database import get_session
from app.core.redis import get_redis_client

router = APIRouter(
    prefix="/users", 
    tags=["users"]
)

# TODO Temporary path to test router.
@router.get("/health")
async def health(
    *, 
    session: Session = Depends(get_session), 
    redis: Redis = Depends(get_redis_client)
):
    try:
        await redis.ping()
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}, 503
    
    return {"status": "ok", "service": "Foxhole LogiNet Users"}
