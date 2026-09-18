from pydantic import BaseModel


class ProjectCreate(BaseModel):
    name: str
    description: str | None = None
    project_type: str


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str | None
    project_type: str
    created_by: int

    class Config:
        from_attributes = True