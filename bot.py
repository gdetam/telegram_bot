"""this is bot initialization file."""

from aiogram import Bot, Dispatcher, types

from config import bot_token


bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
