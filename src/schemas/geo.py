from typing import Optional
from pydantic import BaseModel, model_validator


class GeoDataOut(BaseModel):
    city: str
    country: str
    latitude: float
    longitude: float
    
    model_config = {
        "from_attributes": True,
    }

class GeoDataInLocation(BaseModel):
    latitude: float 
    longitude: float

class GeoDataInAddress(BaseModel):
    city: str 
    country: str 