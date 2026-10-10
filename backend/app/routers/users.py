# router.py
'''Users Router for Loginet'''

from fastapi import APIRouter

router = APIRouter(
    prefix="/users", 
    tags=["users"]
)

# TODO Temporary path to test router.
@router.get("/health")
async def health():
    return {"status": "ok", "service": "Foxhole LogiNet Users"}