from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from database import get_db
from routers.auth import router as auth_router
from routers.projects import router as projects_router
from routers.sites import router as sites_router
from routers.analytics import router as analytics_router
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(projects_router)
app.include_router(sites_router)
app.include_router(analytics_router)
@app.get("/")
def home():
    return {"message": "Darukaa.Earth Backend is running!"}


@app.get("/test-db")
def test_database(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))

    return {
        "message": "Database connected successfully!",
        "result": result.scalar()
    }