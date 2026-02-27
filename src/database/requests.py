from sqlalchemy.ext.asyncio import AsyncSession
from asyncio import run

from .dao.dao import UserDAO, MachineDAO
from .engine import connection
from .models import User, Machine
from .schemas import MachinePydantic


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
    """
    Delete user by id
    Input:
     - id: int - user telegram id
    """
    user = await UserDAO.get_user(id=id, session=session)

    await session.delete(user)
    await session.commit()


@connection
async def get_all_users(session: AsyncSession) -> list:
    """
    Get all users

    Output:
     - result: list - List with users
    """
    return await UserDAO.getall(session=session)


@connection
async def create_machine(
        name: str, 
        category: str, 
        weight_type: str, 
        pic_path: str | None, 
        user_id: int, 
        session: AsyncSession
    ) -> int:
    """
    Create new machine
    Input:
     - name: str - name of the machine
     - category: str - category of exercise/machine (груди, руки, спина, ноги)
     - weight_type: str - weight type (стек, вільна вага)
     - pic_path: str - id of the picture
     - user_id: int - id of the user who is creating machine

    Output:
     - id: int - id of created machine
    """
    machine = await MachineDAO.add(
        name=name, 
        category=category, 
        weight_type=weight_type, 
        pic_path=pic_path, 
        user_id=user_id, 
        session=session
    )
    return machine.id


@connection
async def get_all_machines_for_user(user_id: int, session: AsyncSession) -> list:
    machines = await MachineDAO.get_machines_for_user(user_id=user_id, session=session)
    list_machines = []
    for machine in machines:
        machine_pydantic = MachinePydantic.model_validate(machine)
        list_machines.append(machine_pydantic.model_dump())
    return list_machines
