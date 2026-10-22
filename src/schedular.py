from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import logging

from src.core.config import get_settings
from src.core.database import SessionLocal
from src.models.user import User
from src.models.geo import Geo
from src.crud.weather import save_record
from src.services.weather import fetch_current

logger = logging.getLogger(__name__)

async def fetch_all_users_with_location(db: AsyncSession) -> list[tuple[int, float, float]]:
    subq_geo = (
        select(User.id, Geo.latitude, Geo.longitude)
        .join(Geo, Geo.user_id == User.id)
    )

    result = await db.execute(subq_geo)
    return list(result.all())

async def fetch_current_weather_for_users():
    
    async with SessionLocal() as db:
        users = await fetch_all_users_with_location(db)
        for id, lat, lon in users:
            try:
                weather = await fetch_current(lat, lon, settings=get_settings())
                await save_record(db, id, weather)
            except Exception:
                logger.exception(f"Weather featch failed for user with id {id}")
