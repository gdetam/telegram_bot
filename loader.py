"""this is file activate telegram bot."""

from aiogram import executor

from handlers.commands_handler import dp

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
