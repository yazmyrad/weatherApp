from typing import Dict, Any
from datetime import date
from sqlalchemy import ForeignKey, Date, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Weather(Base):
    __tablename__ = "weather"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    condition: Mapped[Dict[str, Any]] = mapped_column(JSON)
    data:  Mapped[date] = mapped_column(DateTime)
    #user: Mapped["User"] = relationship(back_populates="weather_records")