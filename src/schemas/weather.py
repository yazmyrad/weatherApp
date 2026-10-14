from pydantic import BaseModel

class CurrentWeatherSchema(BaseModel):
    temp: float
    humidity: float
    windspeed: float
    conditions: str

    model_config = {
        "from_attributes": True,
    }