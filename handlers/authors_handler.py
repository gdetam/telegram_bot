"""this is author's keyboards handler."""

from aiogram.types import CallbackQuery

from bot import dp

from handlers.callback_handler import callback
from handlers.senders.author_books_sender import send_author_books_by_item_id
from handlers.senders.authors_sender import send_authors_with_pages

from models.book import Books


@dp.callback_query_handler(text_contains='author_page_')
async def handle_author_page(call: CallbackQuery):
    """Author's page handler."""
    current_page = callback(call).replace('author_page_', '')
    # keyboard authors
    await send_authors_with_pages(call, int(current_page))


@dp.callback_query_handler(text_contains='author_id_book_page_')
async def handle_author_id_and_book_page(call: CallbackQuery):
    """Author's id and book's page number handler."""
    author_id_and_book_page = callback(call).replace('author_id_book_page_', '') \
                                            .split('/')
    author_id = author_id_and_book_page[0]
    current_page = author_id_and_book_page[1]
    await send_author_books_by_item_id(call, int(author_id),
                                       int(current_page), Books.author_id)
