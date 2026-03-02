import logging

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import BotCommand, BotCommandScopeDefault

from .bot_config import settings
from handlers import basic_handlers, machine_management, machine_creation_fsm


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = settings.get_bot_token()
REDIS_URL = settings.get_redis_url()

bot = Bot(token=BOT_TOKEN)
storage = RedisStorage.from_url(REDIS_URL)
dp = Dispatcher(storage=storage)


async def set_commands():
    commands = [BotCommand(command="start", description="Старт")]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def main():
    dp.include_router(basic_handlers.router)
    dp.include_router(machine_management.router)
    dp.include_router(machine_creation_fsm.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)