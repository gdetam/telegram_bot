"""this is bot initialization file."""

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)
