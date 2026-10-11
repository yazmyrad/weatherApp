from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, Field, BaseModel
from functools import lru_cache

@lru_cache
def get_settings()->Settings:
    return Settings()

class DatabaseSettings(BaseModel):
    model_config = SettingsConfigDict(populate_by_name=True)
    url: str = Field(validation_alias="DATABASE_URL")

class WeatherApiSettings(BaseModel):
    model_config = SettingsConfigDict(populate_by_name=True)

    base_url: str = Field(validation_alias="WEATHER_BASE_URL")
    api_key: SecretStr = Field(validation_alias="WEATHER_API_KEY")

class GeoApiSettings(BaseModel):
    model_config = SettingsConfigDict(populate_by_name=True)

    base_url: str = Field(validation_alias="GEO_BASE_URL")
    api_key: SecretStr = Field(validation_alias="GEO_API_KEY")

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra='forbid')

    db: DatabaseSettings

    weather: WeatherApiSettings

    geo: GeoApiSettings