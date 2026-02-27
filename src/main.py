from asyncio import run

from handlers.base import main


#########
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.requests import create_user, get_all_users, check_if_user_exist, delete_user_by_id, create_machine, get_all_machines_for_user
from database.schemas import UserPydantic, MachinePydantic


machines = run(get_all_machines_for_user(user_id=775179074))
print(machines)
for machine in machines:
    machine_pydantic = MachinePydantic.model_validate(machine)
    print(machine_pydantic.model_dump())

# users = run(get_all_users())
# for user in users:
#     user_pydantic = UserPydantic.model_validate(user)
#     print(user_pydantic.model_dump())

##############


if __name__ == "__main__":
    run(main())
