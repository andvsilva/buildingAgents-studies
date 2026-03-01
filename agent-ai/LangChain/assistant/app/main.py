from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings
from app.core.logging import setup_logging

setup_logging(settings.DEBUG)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

app.include_router(router)