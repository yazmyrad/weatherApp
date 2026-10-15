from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.deps import get_current_user
from src.core.config import Settings, get_settings
from src.core.database import get_db
from src.schemas.geo import GeoDataOut, GeoDataIn
from src.services.geodata import upsert_location, fetch_geo
from src.models.user import User

router = APIRouter(prefix="/geo", tags=["geo data"])

@router.get("/location", response_model=GeoDataOut)
async def get_location(
    db: Annotated[AsyncSession, Depends(get_db)], 
    user: Annotated[User, Depends(get_current_user)]
)->GeoDataOut:
    return await fetch_geo(db, user)

@router.post("/location", status_code=200)
async def set_location(
    db: Annotated[AsyncSession, Depends(get_db)],
    user: Annotated[User, Depends(get_current_user)],
    payload: GeoDataIn,
    settings: Annotated[Settings, Depends(get_settings)]
) -> GeoDataOut:
    return await upsert_location(db, user, payload, settings)