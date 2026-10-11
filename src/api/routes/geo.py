from fastapi import APIRouter
from src.services.geodata import geo_data
router = APIRouter()

'''
Endpoint to get exact user location (lat & lon) from the city name. 
Used if user refuses to give permission for geo data
'''
@router.get("geo/citytolocation")
async def getLocation():
    return await geo_data()

'''
Endpoint to post geo data - lan & lon and get city name
'''
@router.get("geo/locationtocity")
async def getCityLocation():
    return await geo_data()


'''
Endpoint to post location name
'''
@router.post("geo/city")
async def postCity():
    return await geo_data()