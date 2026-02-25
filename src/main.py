from asyncio import run

from database.requests import create_user_example, get_all_users



users = run(get_all_users())
for user in users:
    print(user.to_dict())