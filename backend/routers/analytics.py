from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import SiteAnalytics
from schemas.analytics import AnalyticsCreate, AnalyticsResponse


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.post("/", response_model=AnalyticsResponse)
def create_analytics(
    analytics: AnalyticsCreate,
    db: Session = Depends(get_db)
):
    new_analytics = SiteAnalytics(
        site_id=analytics.site_id,
        date=analytics.date,
        carbon_value=analytics.carbon_value,
        biodiversity_score=analytics.biodiversity_score,
        vegetation_index=analytics.vegetation_index,
        performance_score=analytics.performance_score
    )

    db.add(new_analytics)
    db.commit()
    db.refresh(new_analytics)

    return new_analytics


@router.get("/{site_id}", response_model=list[AnalyticsResponse])
def get_site_analytics(
    site_id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(SiteAnalytics)
        .filter(SiteAnalytics.site_id == site_id)
        .order_by(SiteAnalytics.date)
        .all()
    )