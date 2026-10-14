from datetime import datetime
from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(
          String(255), unique=True, nullable=False, index=True
        )
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
    google_id: Mapped[str] = mapped_column(String(255), index=True, unique=True)