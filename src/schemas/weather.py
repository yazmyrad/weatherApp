from typing import Optional
from datetime import time
from pydantic import BaseModel


class CurrentWeatherSchema(BaseModel):
    datetime: Optional[time] = None
    datetimeEpoch: Optional[int] = None

    temp: Optional[float] = None
    feelslike: Optional[float] = None
    humidity: Optional[float] = None
    dew: Optional[float] = None
    precip: Optional[float] = None
    precipprob: Optional[float] = None
    snow: Optional[float] = None
    snowdepth: Optional[float] = None
    preciptype: Optional[str] = None

    windgust: Optional[float] = None
    windspeed: Optional[float] = None
    winddir: Optional[float] = None

    pressure: Optional[float] = None
    visibility: Optional[float] = None
    cloudcover: Optional[float] = None

    solarradiation: Optional[float] = None
    solarenergy: Optional[float] = None
    uvindex: Optional[float] = None
    severerisk: Optional[float] = None

    conditions: Optional[str] = None
    icon: Optional[str] = None
    stations: Optional[str] = None
    source: Optional[str] = None

    sunrise: Optional[time] = None
    sunriseEpoch: Optional[int] = None
    sunset: Optional[time] = None
    sunsetEpoch: Optional[int] = None

    moonphase: Optional[float] = None

    model_config = {
        "from_attributes": True,
        "populate_by_name": True,
    }