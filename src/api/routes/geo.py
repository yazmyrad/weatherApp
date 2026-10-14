from fastapi import APIRouter, Depends
from typing import Annotated

from pydantic import IPvAnyAddress
from src.core.config import Settings, get_settings
from src.services.geodata import fetch_geo_from_ip, fetch_geo_from_city_name

router = APIRouter(prefix="/geo", tags=["geo data"])

'''
Endpoint to get exact user location (lat & lon) from the city name. 
Used if user refuses to give permission for geo data
'''
@router.get("/citytolocation")
async def get_location_from_city(city: str, country: str, settings: Annotated[Settings, Depends(get_settings)]):
    return await fetch_geo_from_city_name(city=city, country=country, settings=settings)

'''
Endpoint to post geo data - lan & lon and get city name
'''
@router.get("/locationtocity")
async def get_city_location_from_ip(ip: IPvAnyAddress, settings: Annotated[Settings, Depends(get_settings)]):
    return await fetch_geo_from_ip(ip=ip, settings=settings)
