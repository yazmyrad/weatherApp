from datetime import datetime, timedelta, timezone
import jwt
from src.core.config import get_settings
import logging

settings = get_settings()

logger = logging.getLogger(__name__)

def create_access_token(user_id: int, expires_delta: timedelta | None = None) -> str:
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=settings.jwt.token_expire))
    payload = {"sub": str(user_id), "exp": expire, "iat": datetime.now(timezone.utc)}
    return jwt.encode(payload, settings.jwt.secret_key.get_secret_value(), algorithm=settings.jwt.crypto_algo)

def verify_token(token: str) -> dict | None:
    try:
        return jwt.decode(
            token,
            settings.jwt.secret_key.get_secret_value(),
            algorithms=[settings.jwt.crypto_algo],
        )
    except jwt.ExpiredSignatureError:
        logger.error("Token expired")
        return None
    except jwt.PyJWTError:
        logger.warning("Invalid token")
        return None

def create_refresh_token(user_id: int) -> str:
    expire = datetime.now(timezone.utc) + timedelta(days=1) 
    payload = {
        "sub": str(user_id), 
        "exp": expire, 
        "iat": datetime.now(timezone.utc), 
        "type": "refresh"
    }
    return jwt.encode(payload, settings.jwt.secret_key.get_secret_value(), algorithm=settings.jwt.crypto_algo)