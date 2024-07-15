from typing import Sequence

from core.models import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_all_users(session: AsyncSession) -> Sequence[User]:
    stmt = select(User)
    result = await session.scalars(stmt)
    return result.all()
