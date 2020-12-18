"""this is reader's keyboards handler."""

from aiogram.types import CallbackQuery

from bot import dp

from handlers.callback_handler import callback
from handlers.senders.reader_books_sender import send_reader_books_by_item_id
from handlers.senders.readers_sender import send_readers_with_pages

from models.reader import Readers


@dp.callback_query_handler(text_contains='reader_page_')
async def handle_reader_page(call: CallbackQuery):
    """Genre's page handler."""
    current_page = callback(call).replace('reader_page_', '')
    # keyboard reader
    await send_readers_with_pages(call, int(current_page))


@dp.callback_query_handler(text_contains='reader_id_book_page_')
async def handle_reader_id_and_book_page(call: CallbackQuery):
    """Reader's id and book's page number handler."""
    reader_id_and_book_page = callback(call).replace('reader_id_book_page_', '') \
                                            .split('/')
    reader_id = reader_id_and_book_page[0]
    current_page = reader_id_and_book_page[1]
    await send_reader_books_by_item_id(call, int(reader_id),
                                       int(current_page), Readers.id)
