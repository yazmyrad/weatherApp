import json
from typing import List

import httpx
from fastapi import Depends, HTTPException
from src.core.config import Settings
import asyncio
from datetime import datetime, timedelta

from src.crud.weather import get_history, get_latest, save_record
from src.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.weather import Weather
from src.schemas.weather import CurrentWeatherSchema
from src.services.geodata import fetch_geo

async def fetch_current(
        lat:float, 
        lon:float, 
        settings: Settings
    )->CurrentWeatherSchema:
    current_time = datetime.now().isoformat(timespec='seconds')
    params = {
        "contentType": "json",
        "include": "current",
        "unitGroup": "metric",
        "key": settings.weather.api_key.get_secret_value(),
    }
    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(f"{settings.weather.base_url}/{lat},{lon}/{current_time}?", params=params)

    if response.status_code != 200:
        raise HTTPException(502, f"Weather API error: {response.status_code}")

    data = response.json()["currentConditions"]
    result = CurrentWeatherSchema(
        temp=data["temp"],
        humidity=data["humidity"],
        windspeed=data["windspeed"],
        conditions=data["conditions"]
    )
    return result

async def fetch_current_from_db(
        settings: Settings,
        user: User,
        db: AsyncSession, 
    )->CurrentWeatherSchema:
    weather = await get_latest(db, user.id, False)
    if weather is None:
        location = await fetch_geo(db, user)
        data = await fetch_current(location.latitude, location.longitude, settings)
        await save_record(db, user.id, data)
        weather = await get_latest(db, user.id, False)
    return CurrentWeatherSchema.model_validate(weather)

async def fetch_history(    
        user: User,
        db: AsyncSession, 
        since: datetime
    )->List[CurrentWeatherSchema]|str:
    historical_data = await get_history(db, user.id, since)
    if not historical_data:
        raise HTTPException(404, "No historical data")
    return [CurrentWeatherSchema.model_validate(w) for w in historical_data]

async def fetch_forecast(
        lat:float, 
        lon:float, 
        settings: Settings
    )->CurrentWeatherSchema:
    tomorrow = datetime.now() + timedelta(days=1)
    forecast = tomorrow.isoformat(timespec='seconds')
    params = {
        "contentType": "json",
        "include": "current",
        "unitGroup": "metric",
        "key": settings.weather.api_key.get_secret_value(),
    }
    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(f"{settings.weather.base_url}/{lat},{lon}/{forecast}?", params=params)

    if response.status_code != 200:
        raise HTTPException(502, f"Weather API error: {response.status_code}")

    data = response.json()["currentConditions"]

    result = CurrentWeatherSchema(
        temp=data["temp"],
        humidity=data["humidity"],
        windspeed=data["windspeed"],
        conditions=data["conditions"]
    )
    return result
