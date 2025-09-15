"""
FastAPI application root:
- mounts health router
- request-logging middleware that logs timestamp, path, method, duration
- global exception handlers for HTTP and generic exceptions
- CORS middleware for frontend <-> backend communication
"""
import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.api import health as health_module  # router defined in app/api/health.py
from app.utils.logger import logger
from app.config import settings

app = FastAPI(title="AnnaSewa API", version=settings.API_VERSION)

# ✅ CORS configuration (allow frontend to call backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # React dev server
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request logging middleware: logs start + end with duration and timestamp
@app.middleware("http")
async def request_logging_middleware(request: Request, call_next):
    start_ts = time.time()
    logger.info({
        "event": "request_start",
        "method": request.method,
        "path": request.url.path,
        "client": request.client.host if request.client else None,
        "start_ts": start_ts
    })
    response = None
    try:
        response = await call_next(request)
        return response
    except Exception as exc:
        logger.error({"event": "exception_during_request", "error": str(exc)})
        raise
    finally:
        duration_ms = int((time.time() - start_ts) * 1000)
        status_code = getattr(response, "status_code", 500) if response is not None else 500
        logger.info({
            "event": "request_end",
            "method": request.method,
            "path": request.url.path,
            "status_code": status_code,
            "duration_ms": duration_ms
        })

# Exception handler for HTTP errors (including 404)
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    logger.warning({
        "event": "http_exception",
        "path": request.url.path,
        "status_code": exc.status_code,
        "detail": str(exc.detail)
    })
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

# Generic exception handler (500)
@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.error({
        "event": "unhandled_exception",
        "path": request.url.path,
        "error": str(exc)
    })
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

# Routers
app.include_router(health_module.router)

