from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .base import BaseDAO
from ..models import User, Machine, Set, Rep


class UserDAO(BaseDAO):
    model = User
    
    @classmethod
    async def get_user(cls, id: int, session: AsyncSession) -> bool:
        """
        Get user by id

        input:
         - id: int - id of the user

        output:
         - bool: True - exist, False - do not
        """
        query = select(cls.model).where(cls.model.id == id)
        result = await session.execute(query)
        return result.scalar_one_or_none()



class MachineDAO(BaseDAO):
    model = Machine

    @classmethod
    async def get_machines_for_user(cls, user_id: int, session: AsyncSession) -> list:
        query = select(cls.model).where(cls.model.user_id == user_id)
        result = await session.execute(query)
        records = result.scalars().all()
        return records


class SetDAO(BaseDAO):
    model = Set


class RepDAO(BaseDAO):
    model = Rep
