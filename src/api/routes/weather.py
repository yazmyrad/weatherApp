#src/api/routes/weather.py
from fastapi import APIRouter
from src.services import weather
router = APIRouter()

'''
Endpoint to get current weather conditions
'''
@router.get("weather/current")
async def currentWeather():
    return await weather.fetch_current_from_db()

'''
Endpoint to get past 7 days weather conditions
'''
@router.get("weather/history")
async def weatherHistory():
    return await weather.fetch_history()

'''
Endpoint to get weather conditions for tomorrow
'''
@router.get("weather/forecast")
async def forecast():
    return await weather.fetch_forecast()
