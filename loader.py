"""this is file activate telegram bot."""

from aiogram import executor

from config import inserter_flag
from db.db_inserter import books_handler
from bot import dp
import handlers.loader_handlers


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    books_handler(inserter_flag)
