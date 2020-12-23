"""this is readers sender."""

from aiogram.types import CallbackQuery

from db.db_queries.count_page_query import get_count_page
from db.db_queries.table_query import create_query_table

from keyboards.readers_keyboards import create_readers_keyboard

from models.reader import Readers


async def send_readers_with_pages(
                                  call: CallbackQuery,
                                  current_page: int):
    """Submit readers."""
    readers_list = create_query_table(Readers, current_page,
                                      Readers.name)
    # keyboard readers
    count_page = get_count_page(Readers)
    reader_keyboard = create_readers_keyboard(readers_list, current_page,
                                              count_page)
    await call.message.answer(
                              text='Выберите исполнителя. \n'
                                   'Если передумали - вернитесь в меню',
                              reply_markup=reader_keyboard)
