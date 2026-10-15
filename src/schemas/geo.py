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

class GeoDataIn(BaseModel):
    latitude: float
    longitude: float
    city: str | None = None
    country: str | None = None

    @model_validator(mode="after")
    def _require_one_source(self):
        has_coords = self.latitude is not None and self.longitude is not None
        has_city = self.city is not None
        if not (has_coords or has_city):
            raise ValueError("Provide either (latitude, longitude) or city")
        if has_coords and has_city:
            raise ValueError("Provide either coordinates OR city, not both")
        return self