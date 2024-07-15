from core import settings
from fastapi import APIRouter

from .users import router as users_router

router = APIRouter(prefix=settings.api.v1.prefix)

router.include_router(users_router)
