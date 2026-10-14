from typing import List, Optional
from datetime import date, datetime
from sqlalchemy import Date, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from .weather import Weather

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(
          String(255), unique=True, nullable=False
        )
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
    #weather_records: Mapped[list["Weather"]] = relationship(back_populates="user")