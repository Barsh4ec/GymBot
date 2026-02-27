import logging

from aiogram import Router, types
from aiogram.filters.command import Command

from database.requests import check_if_user_exist, create_user
from keyboards.all_keyboards import main_kb


router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    exist = await check_if_user_exist(user_id)
    if not exist:
        await create_user(id=user_id, chat_id=chat_id)

    await message.answer(
        "Виберіть дію:",
        reply_markup=main_kb(user_id)
    )