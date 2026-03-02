from aiogram.types import (
    KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from database.models import MachineCategory, WeightType


def remove_kb():
    return ReplyKeyboardRemove()


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
        input_field_placeholder="Використайте меню"
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
        one_time_keyboard=True,
        input_field_placeholder="Виберіть категорію"
    )


def machine_weight_type_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    weight_types = [w_type.value for w_type in WeightType]

    for w_type in weight_types:
        builder.row(
            KeyboardButton(text=w_type)
        )
    builder.adjust(2)

    return builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Виберіть тип"
    )


def without_photo_option_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Без фото")
    )
    return builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder='Надішліть фото або виберіть опцію "Без фото" в меню'
    )


def check_machine_data_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="✅Все правильно", callback_data="correct"),
        InlineKeyboardButton(text="❌Неправильно", callback_data="incorrect")
    )
    return builder.as_markup()
