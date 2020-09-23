import logging
from aiogram.types import Message, CallbackQuery
from bot import dp, bot
from handlers.keyboards import click_callback, create_start_menu_keyboard, \
    create_select_audiobook_keyboard, create_authors_keyboard, create_genres_keyboard
from db.db import DB


# стартовая клавиатура в ответ на команду '/start'
@dp.message_handler(commands=['start'])
async def show_items(message: Message):
    menu_keyboard = create_start_menu_keyboard()
    await message.answer(text="В этом боте вы можете выбрать аудиокнигу.", reply_markup=menu_keyboard)


# обработчик кнопки 'Выбрать аудиокнигу'
@dp.callback_query_handler(text_contains='select_audiobook')
async def select_audiobook(call: CallbackQuery):
    await call.answer(cache_time=6)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    select_audiobook_keyboard = create_select_audiobook_keyboard()
    # клавиатура 'авторы и жанры'
    await call.message.answer(text="Выберите аудиокнигу по автору или жанру. \n"
                                   "Если передумали - жмите отмену", reply_markup=select_audiobook_keyboard)


@dp.callback_query_handler(text_contains='author_page_')
async def handle_author_page(call: CallbackQuery):
    await call.answer(cache_time=6)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    current_page = callback_data.replace('author_page_', '')
    # клавиатура 'авторы'
    await send_authors_with_pages(call, int(current_page))


@dp.callback_query_handler(text_contains='genre_page_')
async def handle_genre_page(call: CallbackQuery):
    await call.answer(cache_time=6)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    current_page = callback_data.replace('genre_page_', '')
    # клавиатура 'жанры'
    await send_genres_with_pages(call, int(current_page))


@dp.callback_query_handler(text="cancel")
async def handle_cancel(call: CallbackQuery):
    # Ответим в окошке с уведомлением!
    await call.answer("Вы вернулись в меню!", show_alert=True)

    # Отправляем стартовую клавиатуру
    menu_keyboard = create_start_menu_keyboard()
    await call.message.answer(text="В этом боте вы можете выбрать аудиокнигу.", reply_markup=menu_keyboard)


async def send_authors_with_pages(call: CallbackQuery, current_page: int):
    authors = DB.get_authors(current_page)
    # клавиатура 'авторы'
    count_page = DB.get_count_page("authors")
    author_keyboard = create_authors_keyboard(authors, count_page)
    await call.message.answer(text="Выберите автора. \n"
                                   "Если передумали - жмите отмену", reply_markup=author_keyboard)


async def send_genres_with_pages(call: CallbackQuery, current_page: int):
    genres = DB.get_genres(current_page)
    # клавиатура 'жанры'
    count_page = DB.get_count_page("genres")
    genre_keyboard = create_genres_keyboard(genres, count_page)
    await call.message.answer(text="Выберите жанр. \n"
                                   "Если передумали - жмите отмену", reply_markup=genre_keyboard)

