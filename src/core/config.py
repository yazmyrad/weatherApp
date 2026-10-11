from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, Field, BaseModel
from functools import lru_cache

class DatabaseSettings(BaseModel):
    model_config = SettingsConfigDict(populate_by_name=True)
    url: str

class WeatherApiSettings(BaseModel):
    model_config = SettingsConfigDict(populate_by_name=True)

    base_url: str
    api_key: SecretStr

class GeoApiSettings(BaseModel):
    model_config = SettingsConfigDict(populate_by_name=True)

    base_url: str
    api_key: SecretStr

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_nested_delimiter="__", extra='forbid')

    database: DatabaseSettings

    weather: WeatherApiSettings

    geo: GeoApiSettings

@lru_cache
def get_settings()->Settings:
    return Settings()
