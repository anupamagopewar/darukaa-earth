from datetime import datetime

from pydantic import BaseModel


class AnalyticsCreate(BaseModel):
    site_id: int
    date: datetime
    carbon_value: float | None = None
    biodiversity_score: float | None = None
    vegetation_index: float | None = None
    performance_score: float | None = None


class AnalyticsResponse(BaseModel):
    id: int
    site_id: int
    date: datetime
    carbon_value: float | None
    biodiversity_score: float | None
    vegetation_index: float | None
    performance_score: float | None

    class Config:
        from_attributes = True