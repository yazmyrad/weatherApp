from fastapi import APIRouter
from src.services.geodata import fetch_geo_from_ip, fetch_geo_from_city_name

router = APIRouter(prefix="geo", tags=["geo data"])

'''
Endpoint to get exact user location (lat & lon) from the city name. 
Used if user refuses to give permission for geo data
'''
@router.get("/citytolocation")
async def get_location():
    return await fetch_geo_from_city_name()

'''
Endpoint to post geo data - lan & lon and get city name
'''
@router.get("/locationtocity")
async def get_city_location():
    return await fetch_geo_from_ip()
