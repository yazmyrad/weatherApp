from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
import logging

from src.core.database import get_db
from src.core.security import verify_token
from src.models.user import User

logger = logging.getLogger(__name__)

security = HTTPBearer(auto_error=True, scheme_name="BearerAuth")

async def get_current_user(
    db: Annotated[AsyncSession, Depends(get_db)],
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
) -> User:
    """Get current user from JWT token"""
    
    token = credentials.credentials
    payload = verify_token(token)
    
    if not payload:
        logger.error("❌ Invalid token")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Get user_id from token
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    user = await db.get(User, int(user_id))
    if user is None:
        raise HTTPException(status_code=401, detail="User not found or inactive")

    return user