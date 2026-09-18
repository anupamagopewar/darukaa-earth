from datetime import datetime

from sqlalchemy import DateTime, String
from geoalchemy2 import Geometry
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150))
    description: Mapped[str | None] = mapped_column(
        String(500), nullable=True
    )
    project_type: Mapped[str] = mapped_column(String(100))
    created_by: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )


class Site(Base):
    __tablename__ = "sites"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    project_id: Mapped[int]
    name: Mapped[str] = mapped_column(String(150))
    description: Mapped[str | None] = mapped_column(
        String(500), nullable=True
    )
    area: Mapped[float | None] = mapped_column(nullable=True)
    geometry = mapped_column(Geometry("POLYGON", srid=4326))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )


class SiteAnalytics(Base):
    __tablename__ = "site_analytics"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    site_id: Mapped[int]
    date: Mapped[datetime] = mapped_column(DateTime)

    carbon_value: Mapped[float | None] = mapped_column(nullable=True)
    biodiversity_score: Mapped[float | None] = mapped_column(nullable=True)
    vegetation_index: Mapped[float | None] = mapped_column(nullable=True)
    performance_score: Mapped[float | None] = mapped_column(nullable=True)