from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.enums.parse_mode import ParseMode

from database.models import MachineCategory, WeightType
from database.requests import create_machine
from keyboards.all_keyboards import (
    machine_kb,
    machine_categories_kb, 
    machine_weight_type_kb, 
    without_photo_option_kb,
    check_machine_data_kb,
    remove_kb
)


class Form(StatesGroup):
    name = State()
    category = State()
    weight_type = State()
    pic_path = State()
    check_state = State()


def create_text(name: str, category: str, weight_type: str, pic_path: str | None) -> str:
    text = f"Новий тренажер/вправа: \n" \
            f"<b>Назва</b>: {name}\n" \
            f"<b>Категорія</b>: {category}\n" \
            f"<b>тип</b>: {weight_type}"
    return text


router = Router()


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
        "Виберіть категорію тренажера зі списку ⬇️",
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
            "Будь ласка, виберіть категорію зі списку",
            reply_markup=machine_categories_kb()
        )
        return

    await state.update_data(category=category)
    await message.answer(
        "Виберіть тип тренажера зі списку ⬇️",
        reply_markup=machine_weight_type_kb()
    )
    await state.set_state(Form.weight_type)


@router.message(F.text, Form.weight_type)
async def capture_weight_type(message: Message, state: FSMContext):
    weight_type = message.text

    try:
        WeightType(weight_type)
    except ValueError:
        await message.reply(
            "Будь ласка, виберіть тип тренажера зі списку",
            reply_markup=machine_weight_type_kb()
        )
        return
    
    await state.update_data(weight_type=weight_type)
    await message.answer(
        'Відправте фото тренажера або нажміть кнопку "Без фото"',
        reply_markup=without_photo_option_kb()
    )
    await state.set_state(Form.pic_path)


@router.message(F.photo, Form.pic_path)
async def capture_photo(message: Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(pic_path=photo_id)

    data = await state.get_data()
    text = create_text(**data)

    await message.answer_photo(
        photo=data.get("pic_path"), 
        caption=text, 
        parse_mode=ParseMode.HTML,
        reply_markup=check_machine_data_kb()
    )
    await state.set_state(Form.check_state)


@router.message(F.text=="Без фото", Form.pic_path)
async def capture_photo(message: Message, state: FSMContext):
    await state.update_data(pic_path=None)

    data = await state.get_data()
    text = create_text(**data)

    await message.answer(text, parse_mode=ParseMode.HTML, reply_markup=check_machine_data_kb())
    await state.set_state(Form.check_state)



@router.callback_query(F.data == "correct", Form.check_state)
async def start_questionnaire_process(call: CallbackQuery, state: FSMContext):
    await call.answer("Тренажер/вправу збережено")
    await call.message.edit_reply_markup(reply_markup=machine_kb())
    await state.clear()


@router.callback_query(F.data == "incorrect", Form.check_state)
async def start_questionnaire_process(call: CallbackQuery, state: FSMContext):
    await call.answer("Звповніть дані наново")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("Введіть назву тренажера або вправи", reply_markup=machine_kb)
    await state.set_state(Form.name)