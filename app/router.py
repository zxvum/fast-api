from fastapi import APIRouter

router = APIRouter()

@router.post('/login')
async def index():
    return {"message": "pong"}