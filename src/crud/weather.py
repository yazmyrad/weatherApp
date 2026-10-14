from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.weather import Weather
from datetime import datetime

async def save_record(
        db: AsyncSession, 
        user_id: int, 
        data: dict
    )->Weather:
    record = Weather(user_id=user_id, **data)
    db.add(record)
    await db.commit()
    await db.refresh(record)
    return record

async def get_latest(
        db: AsyncSession, 
        user_id: int
    )->Weather | None:
    q = (
        select(Weather)
        .where(Weather.user_id == user_id)
        .order_by(Weather.fetch_at.desc())
        .limit(1)
    )
    return (await db.execute(q)).scalar_one_or_none()

async def get_history(
        db: AsyncSession, 
        user_id:int, 
        since: datetime
    )->list[Weather]:
    q = (
        select(Weather)
        .where(Weather.user_id == user_id, Weather.fetched_at >= since)
        .order_by(Weather.fetched_at)
    )
    return list((await db.execute(q)).scalars().all())