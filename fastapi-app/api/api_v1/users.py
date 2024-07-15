from typing import Annotated

from core import settings
from core.models import db_helper
from core.schemas import UserRead
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .db_api import users as users_crud

router = APIRouter(prefix=settings.api.v1.users, tags=["Users"])


@router.get("/", response_model=list[UserRead])
async def get_users(
        session: Annotated[AsyncSession, Depends(db_helper.get_session)],
):
    users = await users_crud.get_all_users(session)
    return users
