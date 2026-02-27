import logging

from aiogram import Router, types, F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters.command import Command

from database.requests import check_if_user_exist, create_user, get_all_machines_for_user
from keyboards.all_keyboards import machine_kb


router = Router()

@router.message(F.text=="Керувати тренажерами")
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    machines = await get_all_machines_for_user(user_id=user_id)
    await message.answer(
        "Введіть назву вправи або тренажера щоб створити новий або виберіть тренажер зі списку",
        reply_markup=machine_kb(user_id, machines)
        )
