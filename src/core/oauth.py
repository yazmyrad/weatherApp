from authlib.integrations.starlette_client import OAuth
from src.core.config import get_settings

oauth = OAuth()
settings = get_settings()
oauth.register(
    name="google",
    client_id=settings.google.google_id.get_secret_value(),
    client_secret=settings.google.client_secret.get_secret_value(),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        "scope": "openid email profile",
    },
)