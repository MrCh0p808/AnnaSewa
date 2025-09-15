from fastapi import APIRouter
from app.config.db import engine
from sqlalchemy import text
from app.config import settings

router = APIRouter()

@router.get("/status")
def status():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))  # quick db check
        db_status = "connected"
    except Exception:
        db_status = "not_connected"
    return {"api_version": settings.API_VERSION, "db_status": db_status}

