from sqlalchemy.ext.asyncio import AsyncSession
from asyncio import run

from .dao.dao import UserDAO
from .engine import connection
from .models import User


@connection
async def create_user(id: int, chat_id: int, session: AsyncSession) -> int:
    """
    Create new user instance
    Input:
     - id: int - telegram id of user
     - chat_id: int -  telegram chat id
    
    Output:
     - id: int - id of the user
    """
    user = await UserDAO.add(id=id, chat_id=chat_id, session=session)
    return user.id

@connection
async def check_if_user_exist(id: int, session: AsyncSession) -> bool:
    """
    Check if user exist by id
    Input:
     - id: int - user telegram id

    Output:
     - result: bool - If exists - True, else False
    """
    user = await UserDAO.get_user(id=id, session=session)
    if user:
        return True
    else: 
        return False


@connection
async def delete_user_by_id(id: int, session: AsyncSession) -> None:
    user = await UserDAO.get_user(id=id, session=session)

    await session.delete(user)
    await session.commit()


@connection
async def get_all_users(session: AsyncSession) -> list:
    return await UserDAO.getall(session=session)



