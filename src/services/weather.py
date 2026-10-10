import httpx
from pathlib import Path
from src.core.config import settings

async def fetch_current(lat:float, long:float):
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

async def fetch_current_from_db():
    pass

async def fetch_history():
    pass

async def fetch_forecast():
    pass

