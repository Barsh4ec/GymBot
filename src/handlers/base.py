import logging

from aiogram import Bot, Dispatcher, types

from .bot_config import settings
from handlers import basic_handlers


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = settings.get_bot_token()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(basic_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)