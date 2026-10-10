# router.py
'''Users Router for Loginet'''

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database import get_session

router = APIRouter(
    prefix="/users", 
    tags=["users"]
)

# TODO Temporary path to test router.
@router.get("/health")
async def health(*, session: Session = Depends(get_session)):
    return {"status": "ok", "service": "Foxhole LogiNet Users"}