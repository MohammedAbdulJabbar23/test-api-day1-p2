from fastapi import APIRouter, HTTPException
from models import User
from schemas import UserIn

router = APIRouter()

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await User.filter(id=user_id).first()
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found 404")


