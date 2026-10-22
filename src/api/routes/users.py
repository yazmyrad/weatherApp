from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from src.api.deps import get_current_user
from src.core.database import get_db
from src.models.user import User
from src.schemas.user import UserResponse

router = APIRouter(prefix='/auth')

@router.get("/me", response_model=UserResponse)
async def me(user: Annotated[User, Depends(get_current_user)]):
    return user

