"""this is commands and keyboards handler."""

import logging
import random

from aiogram.types import CallbackQuery, Message

from bot import dp

from db.authors import authors
from db.books import books
from db.data_base import DB
from db.genres import genres

from handlers.keyboards import create_authors_and_genres_menu, \
    create_authors_keyboard, create_book_keyboard_by_list, \
    create_books_keyboard, create_genres_keyboard, create_start_menu

from sqlalchemy import Column


def callback(call: CallbackQuery):
    """Callback handler."""
    call.answer(cache_time=6)
    callback_data = call.data
    logging.info(f'{callback_data=}')
    return callback_data


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
        text='Выберите аудиокнигу по автору или жанру. \n'
        'Если передумали - вернитесь в меню',
        reply_markup=authors_and_genres_menu)


@dp.callback_query_handler(text_contains='random_book')
async def handle_random_book(call: CallbackQuery):
    """Select a 'Random audiobook' button handler."""
    callback(call)
    count_books = DB.get_count_books()
    random_book_id = random.randint(1, count_books)
    await send_book_by_book_id(call, random_book_id)


@dp.callback_query_handler(text_contains='author_page_')
async def handle_author_page(call: CallbackQuery):
    """Handler for authors page ."""
    current_page = callback(call).replace('author_page_', '')
    # keyboard authors
    await send_authors_with_pages(call, int(current_page))


@dp.callback_query_handler(text_contains='author_id_book_page_')
async def handle_author_id_and_book_page(call: CallbackQuery):
    """Handler for author id and book page number."""
    author_id_and_book_page = callback(call)\
        .replace('author_id_book_page_', '')\
        .split('/')
    author_id = author_id_and_book_page[0]
    current_page = author_id_and_book_page[1]
    await send_books_by_item_id(call, int(author_id),
                                int(current_page), books.c.author_id)


@dp.callback_query_handler(text_contains='genre_page_')
async def handle_genre_page(call: CallbackQuery):
    """Genre page handler."""
    current_page = callback(call).replace('genre_page_', '')
    # keyboard genres
    await send_genres_with_pages(call, int(current_page))


@dp.callback_query_handler(text_contains='genre_id_book_page_')
async def handle_genre_id_and_book_page(call: CallbackQuery):
    """Genre id and book page number handler."""
    genre_id_and_book_page = callback(call)\
        .replace('genre_id_book_page_', '')\
        .split('/')
    genre_id = genre_id_and_book_page[0]
    current_page = genre_id_and_book_page[1]
    await send_books_by_item_id(call, int(genre_id),
                                int(current_page), books.c.genre_id)


@dp.callback_query_handler(text_contains='book_id_')
async def handle_book_id_and_book_url(call: CallbackQuery):
    """Book's id and book's url handler."""
    book_id = callback(call).replace('book_id_', '')
    await send_book_by_book_id(call, book_id)


@dp.callback_query_handler(text='menu')
async def handle_menu(call: CallbackQuery):
    """Menu handler with response in notification popup."""
    await call.answer('Вы вернулись в меню!', show_alert=True)
    # Submitting the start keyboard
    await show_menu(call.message)


async def send_authors_with_pages(
        call: CallbackQuery,
        current_page: int):
    """Submit Authors."""
    authors_list = DB.create_query_table(authors, current_page,
                                         authors.c.last_name)
    # keyboard authors
    count_page = DB.get_count_page(authors)
    author_keyboard = create_authors_keyboard(authors_list, current_page,
                                              count_page)
    await call.message.answer(
        text='Выберите автора. \n'
        'Если передумали - вернитесь в меню',
        reply_markup=author_keyboard)


async def send_genres_with_pages(
        call: CallbackQuery,
        current_page: int):
    """Submit genres."""
    genres_list = DB.create_query_table(genres, current_page,
                                        genres.c.name)
    # keyboard genres
    count_page = DB.get_count_page(genres)
    genre_keyboard = create_genres_keyboard(genres_list, current_page,
                                            count_page)
    await call.message.answer(
        text='Выберите жанр. \n'
        'Если передумали - вернитесь в меню',
        reply_markup=genre_keyboard)


async def send_books_by_item_id(
        call: CallbackQuery,
        item_id: int,
        current_page: int,
        column_name: Column):
    """Submit books and item_id."""
    books_list = DB.get_books_by_item_id(item_id, current_page, column_name)
    # keyboard book
    count_page = DB.get_count_books_pages_by_item_id(item_id, column_name)
    book_keyboard = create_books_keyboard(books_list, current_page,
                                          count_page, item_id)
    await call.message.answer(
        text='Выберите аудиокнигу. \n'
        'Если передумали - вернитесь в меню',
        reply_markup=book_keyboard)


async def send_book_by_book_id(
        call: CallbackQuery,
        book_id: int):
    """Send books and book id."""
    books_list = DB.get_book_by_id(book_id)
    book_keyboard = create_book_keyboard_by_list(books_list)
    await call.message.answer(
        text='Нажмите на аудиокнигу, чтобы воспроизвести. \n'
        'Если передумали - вернитесь в меню',
        reply_markup=book_keyboard)
