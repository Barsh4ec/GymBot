from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database.requests import get_all_machines_for_user
from database.models import MachineCategory
from keyboards.all_keyboards import machine_kb, machine_categories_kb


class Form(StatesGroup):
    name = State()
    category = State()


router = Router()


@router.message(F.text=="Керувати тренажерами")
async def manage_machines(message: Message):
    user_id = message.from_user.id
    machines = await get_all_machines_for_user(user_id=user_id)
    await message.answer(
        "Введіть назву вправи або тренажера щоб створити новий або виберіть тренажер зі списку",
        reply_markup=machine_kb(user_id, machines)
    )


@router.message(F.text=="➕ Додати вправу/тренажер")
async def start_creating_machine_process(message: Message, state: FSMContext):
    await message.answer(
        "Введіть назву тренажера або вправи"
    )
    await state.set_state(Form.name)


@router.message(F.text, Form.name)
async def capture_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(
        "Виберіть тип тренажера зі списку",
        reply_markup=machine_categories_kb()
    )
    await state.set_state(Form.category)


@router.message(F.text, Form.category)
async def capture_category(message: Message, state: FSMContext):
    category = message.text

    try:
        MachineCategory(category)
    except ValueError:
        await message.reply(
            "Будь ласка виберіть категорію зі списку",
            reply_markup=machine_categories_kb()
        )
        return

    await state.update_data(category=category)

    data = await state.get_data()
    msg_text = f"Назва тренажера - {data.get('name')}, Категорія тренажера - {data.get('category')}"
    
    await message.answer(msg_text)
    await state.clear()

