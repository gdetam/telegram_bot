"""this is genre's keyboards handler."""

from aiogram.types import CallbackQuery

from bot import dp

from handlers.callback_handler import callback
from handlers.senders.genre_books_sender import send_genre_books_by_item_id
from handlers.senders.genres_sender import send_genres_with_pages

from models.genre import Genres


@dp.callback_query_handler(text_contains='genre_page_')
async def handle_genre_page(call: CallbackQuery):
    """Genre's page handler."""
    current_page = callback(call).replace('genre_page_', '')
    # keyboard genres
    await send_genres_with_pages(call, int(current_page))


@dp.callback_query_handler(text_contains='genre_id_book_page_')
async def handle_genre_id_and_book_page(call: CallbackQuery):
    """Genre's id and book's page number handler."""
    genre_id_and_book_page = callback(call).replace('genre_id_book_page_', '') \
                                           .split('/')
    genre_id = genre_id_and_book_page[0]
    current_page = genre_id_and_book_page[1]
    await send_genre_books_by_item_id(call, int(genre_id),
                                      int(current_page), Genres.id)
