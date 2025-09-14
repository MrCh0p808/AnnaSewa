"""
Health and Status endpoints (kept minimal for Phase 1).
- GET /health -> simple liveness check
- GET /status -> returns API version and DB status
"""
from fastapi import APIRouter, Request
from app.utils.db import check_db_connection
from app.config import settings
from app.utils.logger import logger

router = APIRouter()

@router.get("/health", summary="Liveness probe", tags=["health"])
async def health(request: Request):
    # Log a timestamped event for this request — middleware logs too, but this is explicit
    logger.info({
        "event": "health_check",
        "client": request.client.host if request.client else None,
        "path": str(request.url.path)
    })
    return {"status": "ok"}

@router.get("/status", summary="Service status including db", tags=["health"])
async def status():
    # Check DB connectivity (non-blocking quick check)
    db_status = check_db_connection()
    return {"api_version": settings.API_VERSION, "db_status": db_status}

