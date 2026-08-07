from fastapi import FastAPI

from app.config import settings
from app.routes.health import router as health_router

app = FastAPI(
    title="testing-repo",
    docs_url=f"{settings.api_prefix}/docs",
    redoc_url=f"{settings.api_prefix}/redoc",
    openapi_url=f"{settings.api_prefix}/openapi.json",
)
# this is a test3
app.include_router(health_router, prefix=settings.api_prefix)


