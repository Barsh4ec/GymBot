import logging

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand, BotCommandScopeDefault

from .bot_config import settings
from handlers import basic_handlers, machine_management


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = settings.get_bot_token()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


async def set_commands():
    commands = [BotCommand(command="start", description="Старт")]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def main():
    dp.include_router(basic_handlers.router)
    dp.include_router(machine_management.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)