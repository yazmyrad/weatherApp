from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, Query
from typing import Annotated, List
from src.api.deps import get_current_user
from src.core.config import Settings, get_settings
from src.core.database import get_db
from src.models.user import User
from src.models.weather import Weather
from src.schemas.weather import CurrentWeatherSchema
from src.services import weather
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(prefix="/weather", tags=["weather"])


'''
Endpoint to get current weather conditions
'''
@router.get("/current", response_model=CurrentWeatherSchema)
async def current_weather(
    settings: Annotated[Settings, Depends(get_settings)],
    user: Annotated[User, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(get_db)]
    ):
    return await weather.fetch_current_from_db(settings, user, db)

'''
Endpoint to get past 7 days weather conditions
'''
@router.get("/history", response_model=List[CurrentWeatherSchema])
async def weather_history(
    user: Annotated[User, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(get_db)],
    days: int = Query(7, ge=1, le=30)
):
    since = datetime.now(timezone.utc) - timedelta(days=days)
    return await weather.fetch_history(user, db, since)

'''
Endpoint to get weather conditions for tomorrow
'''
@router.get("/forecast", response_model=CurrentWeatherSchema)
async def forecast(
    user: Annotated[User, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(get_db)],
    settings: Annotated[Settings, Depends(get_settings)]
):
    return await weather.fetch_weather_tomorrow(db, user, settings=settings)
