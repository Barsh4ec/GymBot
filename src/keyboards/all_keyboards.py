from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from database.models import MachineCategory


def main_kb(user_id: int) -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()

    builder.row(
        KeyboardButton(text="Почати тренування")
    )
    builder.row(
        KeyboardButton(text="Керувати тренажерами"),
        KeyboardButton(text="Керувати блінами")
    )
    builder.row(
        KeyboardButton(text="Статистика"),
        KeyboardButton(text="Розрахунок блінів")
    )
    # if user_id in admins:
    #     builder.row(
    #         KeyboardButton(text="Адмін панель")
    #     )

    return builder.as_markup(
        resize_keyboard=True, 
        one_time_keyboard=True,
        input_field_placeholder="Використайте меню"
    )


def machine_kb(user_id: int, machines: list) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    
    for machine in machines:
        builder.row(
            KeyboardButton(text=machine["name"])
        )

    builder.row(
        KeyboardButton(text="➕ Додати вправу/тренажер")
    )

    return builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True,
    )


def machine_categories_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    categories = [category.value for category in MachineCategory]

    for category in categories:
        builder.row(
            KeyboardButton(text=category)
        )
    builder.adjust(2, 2)

    return builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True
    )
