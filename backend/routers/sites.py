from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from geoalchemy2.shape import from_shape, to_shape
from shapely.geometry import shape

from database import get_db
from models import Site
from schemas.site import SiteCreate, SiteResponse


router = APIRouter(
    prefix="/sites",
    tags=["Sites"]
)


@router.post("/", response_model=SiteResponse)
def create_site(
    site: SiteCreate,
    db: Session = Depends(get_db)
):
    polygon = shape(site.geometry)

    new_site = Site(
        project_id=site.project_id,
        name=site.name,
        description=site.description,
        area=site.area,
        geometry=from_shape(polygon, srid=4326)
    )

    db.add(new_site)
    db.commit()
    db.refresh(new_site)

    return {
        "id": new_site.id,
        "project_id": new_site.project_id,
        "name": new_site.name,
        "description": new_site.description,
        "area": new_site.area,
        "geometry": site.geometry
    }


@router.get("/", response_model=list[SiteResponse])
def get_sites(
    db: Session = Depends(get_db)
):
    sites = db.query(Site).all()

    return [
        {
            "id": site.id,
            "project_id": site.project_id,
            "name": site.name,
            "description": site.description,
            "area": site.area,
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [point[0], point[1]]
                       for point in to_shape(site.geometry).exterior.coords
                    ]
                ]
            }
        }
        for site in sites
    ]