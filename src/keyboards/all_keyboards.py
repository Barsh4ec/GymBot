from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


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


def machine_kb(user_id: int, machines: list) -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    
    for machine in machines:
        builder.row(
            KeyboardButton(text=f"{machine['name']}")
        )

    builder.row(
        KeyboardButton(text="➕")
    )

    return builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True,
    )
