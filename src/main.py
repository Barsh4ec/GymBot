from asyncio import run

from database.requests import create_user_example, get_all_users
from database.schemas import UserPydantic, MachinePydantic


users = run(get_all_users())
for user in users:
    user_pydantic = UserPydantic.model_validate(user)
    print(user_pydantic)