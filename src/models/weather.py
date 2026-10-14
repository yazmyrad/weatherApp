from typing import Dict, Any, Optional
from datetime import time
from sqlalchemy import ForeignKey, JSON, Time
from sqlalchemy import Integer, Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Weather(Base):
    __tablename__ = "weather"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    condition: Mapped[Dict[str, Any]] = mapped_column(JSON)
    datetime: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    datetime_epoch: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    temp: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    feelslike: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    humidity: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    dew: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    precip: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    precipprob: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    snow: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    snowdepth: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    preciptype: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)

    windgust: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    windspeed: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    winddir: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    pressure: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    visibility: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    cloudcover: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    solarradiation: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    solarenergy: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    uvindex: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    severerisk: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    conditions: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    icon: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    stations: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    source: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)

    sunrise: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    sunrise_epoch: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    sunset: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    sunset_epoch: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    moonphase: Mapped[Optional[float]] = mapped_column(Float, nullable=True)