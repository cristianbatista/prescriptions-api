from datetime import datetime

from fastapi import APIRouter

start_time = datetime.now()

router = APIRouter()


@router.get("")
async def health():
    return {"message": "I'm alive and kicking!"}
