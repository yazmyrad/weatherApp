from sqlalchemy.ext.asyncio import AsyncSession
from src.models.user import User
from sqlalchemy import select

async def get_or_create_by_google(
        db:  AsyncSession,
        *,
        google_id: str,
        email: str, 
        name: str
    ):
    # try google_id first
    user = await get_by_google_id(db, google_id)
    if user:
        return user

    # then try email (re-link case)
    user = await get_by_email(db, email)
    if user:
        user.google_id = google_id  # re-link
        await db.commit()
        await db.refresh(user)
        return user

    # new user
    user = User(google_id=google_id, email=email, name=name)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_by_email(db: AsyncSession, email: str):
    q = (
        select(User)
        .where(User.email == email)
    )
    return (await db.execute(q)).scalar_one_or_none()

async def get_by_google_id(db: AsyncSession, google_id: str):
    q = (
        select(User)
        .where(User.google_id == google_id)
    )
    return (await db.execute(q)).scalar_one_or_none()