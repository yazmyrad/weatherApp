from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.geo import Geo
from src.schemas.geo import GeoData

async def save_location(
        db: AsyncSession, 
        user_id: int, 
        data: GeoData
    )->Geo:
    exists = await get_location(db, user_id)
    if exists:
        for key, value in data.model_dump().items():
            setattr(exists, key, value)
    else:
        exists = Geo(user_id=user_id, **data.model_dump())
        db.add(exists)
    await db.commit()
    await db.refresh(exists)
    return exists

async def get_location(
        db: AsyncSession, 
        user_id: int
    )->Geo | None:
    q = (
        select(Geo)
        .where(Geo.user_id == user_id)
    )
    return (await db.execute(q)).scalar_one_or_none()