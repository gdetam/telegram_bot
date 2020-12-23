"""this is authors sender."""

from aiogram.types import CallbackQuery

from db.db_queries.count_page_query import get_count_page
from db.db_queries.table_query import create_query_table

from keyboards.authors_keyboards import create_authors_keyboard

from models.author import Authors


async def send_authors_with_pages(
                                  call: CallbackQuery,
                                  current_page: int):
    """Submit Authors."""
    authors_list = create_query_table(Authors, current_page, Authors.name)
    # keyboard authors
    count_page = get_count_page(Authors)
    author_keyboard = create_authors_keyboard(authors_list, current_page,
                                              count_page)
    await call.message.answer(
                              text='Выберите автора. \n'
                                   'Если передумали - вернитесь в меню',
                              reply_markup=author_keyboard)
