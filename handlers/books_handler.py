"""this is book's keyboards handler."""

from aiogram.types import CallbackQuery

from bot import dp

from handlers.callback_handler import callback
from handlers.senders.books_sender import send_book_by_book_id


@dp.callback_query_handler(text_contains='book_id_')
async def handle_book_id_and_book_url(call: CallbackQuery):
    """Book's id and book's url handler."""
    book_id = callback(call).replace('book_id_', '')
    await send_book_by_book_id(call, book_id)
