from datetime import datetime
from sqlalchemy import ForeignKey,func
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Weather(Base):
    __tablename__ = "weather"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    temp: Mapped[float]
    humidity: Mapped[float]
    windspeed: Mapped[float]
    conditions: Mapped[str] = mapped_column(String(255))
    fetched_at: Mapped[datetime] = mapped_column(server_default=func.now(), index=True)
    is_forecast: Mapped[bool] = mapped_column(default=False)