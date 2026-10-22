from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from authlib.integrations.base_client import OAuthError
from typing import Annotated
import logging

from src.crud.user import get_or_create_by_google
from src.core.security import create_access_token, verify_token
from src.core.oauth import oauth
from src.core.database import get_db
from src.core.config import get_settings
from src.models.user import User

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/auth/google", tags=["authentication"])
settings = get_settings()

@router.get("/login")
async def google_login(request: Request):
    """Redirect to Google login page"""
    redirect_uri = settings.google.redirect_url
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/callback")
async def google_callback(request: Request, db: Annotated[AsyncSession, Depends(get_db)]):
    try:
        token = await oauth.google.authorize_access_token(request)
        
        # Get user info from token
        user_info = token.get("userinfo")
        
        if not user_info:
            raise HTTPException(status_code=400, detail="Failed to get user info")
        
        # Extract user data
        google_id = user_info.get("sub")
        email = user_info.get("email")
        name = user_info.get("name", "")

        if not email:
            raise HTTPException(status_code=400, detail="Email not provided by Google")
        
        user = await get_or_create_by_google(db, google_id, email, name)
        
        # Create token and redirect
        access_token = create_access_token(user_id=user.id, expires_delta=timedelta(days=1))
        redirect_url = f"{settings.domain.url}/docs?token={access_token}"
        
        return RedirectResponse(url=redirect_url, status_code=302)
        
    except OAuthError as e:
        # only catch the specific authlib failure
        raise HTTPException(status_code=400, detail=f"OAuth exchange failed: {str(e)}")