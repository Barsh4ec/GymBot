from asyncio import run

from handlers.base import main


#########
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.requests import create_user, get_all_users, check_if_user_exist, delete_user_by_id
from database.schemas import UserPydantic, MachinePydantic


# user = run(delete_user_by_id(775179074))
# print(user)

# users = run(get_all_users())
# for user in users:
#     user_pydantic = UserPydantic.model_validate(user)
#     print(user_pydantic.model_dump())

##############


if __name__ == "__main__":
    run(main())
