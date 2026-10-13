import httpx
from fastapi import Depends
from pydantic import IPvAnyAddress
from src.core import Settings, get_settings
import asyncio

async def fetch_geo_from_ip(ip: IPvAnyAddress, settings: Settings):
    params = {
        "apiKey": settings.geo.api_key.get_secret_value(),
    }
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(f"{settings.geo.base_url}/ipinfo?", params=params)

    if response.status_code != 200:
        return Exception("Non run")
    
    data = response.json()
    parsed_data = {
        'city_name': data['city']['name'],
        'country_name': data['country']['name'],
        'city_flag': data['country']['flag'],
        'latitude': data['location']['latitude'],
        'longitude': data['location']['longitude'],
        'ip': data['ip'],
    }
    return parsed_data

async def fetch_geo_from_city_name(city:str, country:str, settings: Settings):
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
        'latitude': data['lat'],
        'longitude': data['lon'],
    }

    return parsed_data

#asyncio.run(fetch_geo_from_city_name("Berlin", "Germany", get_settings()))