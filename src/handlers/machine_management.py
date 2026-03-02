from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from database.requests import get_all_machines_for_user
from keyboards.all_keyboards import machine_kb

router = Router()


@router.message(F.text=="Керувати тренажерами")
async def manage_machines(message: Message):
    user_id = message.from_user.id
    machines = await get_all_machines_for_user(user_id=user_id)
    await message.answer(
        "Введіть назву вправи або тренажера щоб створити новий або виберіть тренажер зі списку",
        reply_markup=machine_kb(user_id, machines)
    )


