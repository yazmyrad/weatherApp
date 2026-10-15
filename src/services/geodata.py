import httpx
from fastapi import Depends, HTTPException
from pydantic import IPvAnyAddress
from src.core import Settings, get_settings
from src.crud.geo import get_location, save_location
from src.models.user import User
from src.schemas.geo import GeoDataOut, GeoDataIn
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio

async def fetch_geo_from_location(
        lat: float, 
        lon: float, 
        settings: Settings
)->GeoDataOut:
    params = {
        "lat": lat,
        "lon": lon,
        "limit": 1,
        "format": "json",
        "apiKey": settings.geo.api_key.get_secret_value(),
    }
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(f"{settings.geo.base_url}/geocode/reverse", params=params)

    if response.status_code != 200:
        return Exception("Non run")
    
    data = response.json()
    parsed_data = {
        'city': data['features'][0]['properties']['city'],
        'country': data['features'][0]['properties']['country'],
        'latitude': lat,
        'longitude': lon,
    }
    return parsed_data

async def fetch_geo_from_city_name(
        city:str, 
        country:str, 
        settings: Settings
)->GeoDataOut:
    params = {
        "city": city,
        "state": country,
        "format": "json",
        "limit": 1,
        "apiKey": settings.geo.api_key.get_secret_value(),
    }
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(f"{settings.geo.base_url}/geocode/search?", params=params)

    if response.status_code != 200:
        return Exception("Non run")
    
    data = response.json()["results"][0]

    parsed_data = {
        "city": city,
        "country": country,
        'latitude': data['lat'],
        'longitude': data['lon'],
    }

    return parsed_data

async def upsert_location(
        db: AsyncSession, 
        user: User, 
        data: GeoDataIn, 
        settings: Settings
)->GeoDataOut:
    if data.city:
        result = await fetch_geo_from_city_name(data.city, data.country, settings)
    elif data.latitude is not None and data.longitude is not None:
        result = await fetch_geo_from_location(data.latitude, data.longitude, settings)
    geo = await save_location(db, user.id, result)
    return GeoDataOut.model_validate(geo)

async def fetch_geo(
        db: AsyncSession, 
        user: User
)->GeoDataOut:
    geo = await get_location(db, user.id)
    if geo is None:
        raise HTTPException(404, "No location set")
    return GeoDataOut.model_validate(geo)

#asyncio.run(fetch_geo_from_city_name("Berlin", "Germany", get_settings()))