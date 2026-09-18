# router.py
'''Core API Router for Loginet'''

from fastapi import APIRouter

from app.api.v1 import router as v1_router

router = APIRouter(prefix="/api", tags=["api"])
#router.include_router(v1_router)

@router.get("/health")
async def health():
    return {"status": "ok", "service": "Foxhole LogiNet API"}