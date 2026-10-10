from fastapi import APIRouter

router = APIRouter()

'''
Endpoint to get exact user location (lat & lon) from the city name. 
Used if user refuses to give permission for geo data
'''
@router.get("geo/cityreverse")
def getLocation():
    pass

'''
Endpoint to get geo data - lan & lon 
'''
@router.get("geo/location")
def getCityLocation():
    pass


'''
Endpoint to post location name
'''
@router.post("geo/city")
def postCity():
    pass