from typing import Optional
from pydantic import BaseModel


class GeoData(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None
    longitude: float
    latitude: float
    model_config = {
        "from_attributes": True,
        "populate_by_name": True,
    }