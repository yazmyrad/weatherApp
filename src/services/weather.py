import httpx
from fastapi import Depends
from src.core.config import Settings

async def fetch_current(lat:float, long:float, settings: Settings):
    params = {
        "lat": lat,
        "lon": long,
        "units": 'metric', 
        "appid": '',
    }
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(f"{settings.weather_base_url}/weather?", params=params)

    if response.status_code != 200:
        return Exception()

    return response.json()

async def fetch_current_from_db(settings: Settings):
    pass

async def fetch_history():
    pass

async def fetch_forecast(settings: Settings):
    pass

