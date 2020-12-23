"""this is books sender."""

from aiogram.types import CallbackQuery

from db.db_queries.book_by_id_query import get_book_by_id

from keyboards.books_keyboards import create_book_keyboard_by_list


async def send_book_by_book_id(
                               call: CallbackQuery,
                               book_id: int):
    """Send books and book id."""
    books_list = get_book_by_id(book_id)
    book_keyboard = create_book_keyboard_by_list(books_list)
    await call.message.answer(
                              text='Нажмите на аудиокнигу, чтобы воспроизвести. \n'
                                   'Если передумали - вернитесь в меню',
                              reply_markup=book_keyboard)
