from contextlib import asynccontextmanager

import uvicorn
from api import router
from core import settings
from core.models import db_helper
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from loguru import logger


def setup_logger():
    logger.add(f"{settings.base_dir}/logs/log.log", level="ERROR", rotation="00:00", retention="7 days")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info(f"Start FastAPI on {settings.run.host}:{settings.run.port}")
    yield
    # Shutdown
    await db_helper.dispose()
    logger.info(f"Stop FastAPI")


def create_app():
    app = FastAPI(lifespan=lifespan, default_response_class=ORJSONResponse)
    app.include_router(router)

    return app


if __name__ == "__main__":
    setup_logger()

    uvicorn.run(
        "main:create_app",
        factory=True,
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.debug,
        workers=settings.run.workers
    )
