"""this is menu's keyboards handler."""

import random

from aiogram.types import CallbackQuery, Message

from bot import dp

from db.db_querys.count_books_query import get_count_books

from handlers.callback_handler import callback
from handlers.senders.books_sender import send_book_by_book_id

from keyboards.menu_keyboards import create_authors_and_genres_menu, \
                                     create_start_menu


@dp.message_handler(commands=['start'])
async def show_menu(message: Message):
    """Start keyboard in response to '/ start' command."""
    start_menu = create_start_menu()
    await message.answer(
                         text='В этом боте вы можете выбрать аудиокнигу.',
                         reply_markup=start_menu)


@dp.callback_query_handler(text_contains='select_book')
async def handle_select_book(call: CallbackQuery):
    """Select audiobook button handler."""
    callback(call)
    authors_and_genres_menu = create_authors_and_genres_menu()
    # keyboard authors and genres
    await call.message.answer(
                              text='Выберите аудиокнигу по автору, жанру или исполнителю. \n'
                                   'Если передумали - вернитесь в меню',
                              reply_markup=authors_and_genres_menu)


@dp.callback_query_handler(text_contains='random_book')
async def handle_random_book(call: CallbackQuery):
    """Select a 'Random audiobook' button handler."""
    callback(call)
    count_books = get_count_books()
    random_book_id = random.randint(1, count_books)
    await send_book_by_book_id(call, random_book_id)


@dp.callback_query_handler(text='menu')
async def handle_menu(call: CallbackQuery):
    """Menu handler with response in notification popup."""
    await call.answer('Вы вернулись в меню!', show_alert=True)
    # Submitting the start keyboard
    await show_menu(call.message)
