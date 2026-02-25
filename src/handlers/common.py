from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from .bot_config import settings


BOT_TOKEN = settings.get_bot_token()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)