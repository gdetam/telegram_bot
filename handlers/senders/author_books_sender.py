"""this is author's books sender."""

from aiogram.types import CallbackQuery

from db.db_querys.author_books_query import get_author_books_by_item_id
from db.db_querys.count_books_pages_query import get_count_books_pages_by_item_id

from keyboards.books_keyboards import create_books_keyboard_by_author

from sqlalchemy import Column


async def send_author_books_by_item_id(
                                       call: CallbackQuery,
                                       item_id: int,
                                       current_page: int,
                                       column_name: Column):
    """Submit books and item_id."""
    books_list = get_author_books_by_item_id(item_id, current_page)
    # keyboard book
    count_page = get_count_books_pages_by_item_id(item_id, column_name)
    book_keyboard = create_books_keyboard_by_author(books_list, current_page,
                                                    count_page, item_id)
    await call.message.answer(
                              text='Выберите аудиокнигу. \n'
                                   'Если передумали - вернитесь в меню',
                              reply_markup=book_keyboard)
