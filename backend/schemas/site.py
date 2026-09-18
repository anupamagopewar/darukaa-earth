from pydantic import BaseModel


class SiteCreate(BaseModel):
    project_id: int
    name: str
    description: str | None = None
    area: float | None = None
    geometry: dict


class SiteResponse(BaseModel):
    id: int
    project_id: int
    name: str
    description: str | None
    area: float | None
    geometry: dict

    class Config:
        from_attributes = True