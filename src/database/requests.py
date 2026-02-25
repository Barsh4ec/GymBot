from sqlalchemy.ext.asyncio import AsyncSession
from asyncio import run

from .dao.dao import UserDAO
from .engine import connection
from .models import User


@connection
async def create_user_example(user_id: int, chat_id: int, session: AsyncSession) -> int:
    """
    Create new user instance
    Input:
     - user_id: int - telegram id of user
     - chat_id: int -  telegram chat id
    
    Output:
     - id: int - id of the user
    """
    user = await UserDAO.add(user_id=user_id, chat_id=chat_id, session=session)
    return user.id


@connection
async def get_all_users(session: AsyncSession) -> list:
    users = await UserDAO.getall(session=session)
    return users



