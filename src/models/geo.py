from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Geo(Base):
    __tablename__ = "geo"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    latitude: Mapped[float]
    longitude: Mapped[float]
    city: Mapped[str] = mapped_column(String(30))
    country: Mapped[str] = mapped_column(String(30))