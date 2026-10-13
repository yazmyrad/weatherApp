import httpx
from fastapi import Depends
from src.core.config import Settings, get_settings
import asyncio
from datetime import datetime, timedelta

async def fetch_current(lat:float, long:float, settings: Settings):
    current_time = datetime.now().isoformat(timespec='seconds')
    params = {
        "contentType": "json",
        "include": "current",
        "unitGroup": "metric",
        "key": settings.weather.api_key.get_secret_value(),
    }
    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(f"{settings.weather.base_url}/{lat},{long}/{current_time}?", params=params)
    
    data = response.json()

    return data["currentConditions"]

async def fetch_current_from_db(settings: Settings):
    pass

async def fetch_history():
    pass

async def fetch_forecast(lat:float, long:float, settings: Settings):
    tomorrow = datetime.now() + timedelta(days=1)
    forecast = tomorrow.isoformat(timespec='seconds')
    params = {
        "contentType": "json",
        "include": "current",
        "unitGroup": "metric",
        "key": settings.weather.api_key.get_secret_value(),
    }
    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(f"{settings.weather.base_url}/{lat},{long}/{forecast}?", params=params)
    
    data = response.json()

    return data["currentConditions"]
