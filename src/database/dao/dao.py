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


class SetDAO(BaseDAO):
    model = Set


class RepDAO(BaseDAO):
    model = Rep
