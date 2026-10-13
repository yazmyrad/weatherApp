#src/api/routes/weather.py
from fastapi import APIRouter, Depends
from typing import Annotated
from src.core.config import Settings, get_settings

from src.services import weather

router = APIRouter(prefix="/weather", tags=["weather"])


'''
Endpoint to get current weather conditions
'''
@router.get("/current")
async def current_weather(settings: Annotated[Settings, Depends(get_settings)]):
    return await weather.fetch_current_from_db(settings)

'''
Endpoint to get past 7 days weather conditions
'''
@router.get("/history")
async def weather_history():
    return await weather.fetch_history()

'''
Endpoint to get weather conditions for tomorrow
'''
@router.get("/forecast")
async def forecast(lat:float, lon: float, settings: Annotated[Settings, Depends(get_settings)]):
    return await weather.fetch_forecast(lat=lat, lon=lon, settings=settings)
