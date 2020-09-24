import logging
from aiogram.types import Message, CallbackQuery
from bot import dp, bot
from handlers.keyboards import click_callback, create_start_menu_keyboard
from db.db import DB


# стартовая клавиатура в ответ на команду '/start'
@dp.message_handler(commands=['start'])
async def show_items(message: Message):
    menu_keyboard = create_start_menu_keyboard()
    await message.answer(text="В этом боте вы можете выбрать аудиокнигу.", reply_markup=menu_keyboard)
