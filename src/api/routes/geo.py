from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.deps import get_current_user
from src.core.config import Settings, get_settings
from src.core.database import get_db
from src.schemas.geo import GeoDataOut, GeoDataInLocation, GeoDataInAddress
from src.services.geodata import upsert_location_city, upsert_location_coords, fetch_geo
from src.models.user import User

router = APIRouter(prefix="/geo/location", tags=["geo data"])

@router.get("/fetch", response_model=GeoDataOut)
async def get_location(
    db: Annotated[AsyncSession, Depends(get_db)], 
    user: Annotated[User, Depends(get_current_user)]
)->GeoDataOut:
    return await fetch_geo(db, user)

@router.post("/coords", status_code=200)
async def set_location(
    db: Annotated[AsyncSession, Depends(get_db)],
    user: Annotated[User, Depends(get_current_user)],
    payload: GeoDataInLocation,
    settings: Annotated[Settings, Depends(get_settings)]
) -> GeoDataOut:
    return await upsert_location_coords(db, user, payload, settings)

@router.post("/city", status_code=200)
async def set_location(
    db: Annotated[AsyncSession, Depends(get_db)],
    user: Annotated[User, Depends(get_current_user)],
    payload: GeoDataInAddress,
    settings: Annotated[Settings, Depends(get_settings)]
) -> GeoDataOut:
    return await upsert_location_city(db, user, payload, settings)