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

class GoogleAuth(BaseModel):
    model_config = SettingsConfigDict(populate_by_name=True)

    google_id: SecretStr
    client_secret: SecretStr
    redirect_url: str

class JWT(BaseModel):
    model_config = SettingsConfigDict(populate_by_name=True)

    secret_key: SecretStr
    crypto_algo: str
    token_expire: int

class Domain(BaseModel):
    model_config = SettingsConfigDict(populate_by_name=True)

    url: str

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_nested_delimiter="__", extra='forbid')

    database: DatabaseSettings

    weather: WeatherApiSettings

    geo: GeoApiSettings

    google: GoogleAuth

    jwt: JWT

    domain: Domain

@lru_cache
def get_settings()->Settings:
    return Settings()
