"""this is genres sender."""

from aiogram.types import CallbackQuery

from db.db_queries.count_page_query import get_count_page
from db.db_queries.table_query import create_query_table

from keyboards.genres_keyboards import create_genres_keyboard

from models.genre import Genres


async def send_genres_with_pages(
                                 call: CallbackQuery,
                                 current_page: int):
    """Submit genres."""
    genres_list = create_query_table(Genres, current_page,
                                     Genres.name)
    # keyboard genres
    count_page = get_count_page(Genres)
    genre_keyboard = create_genres_keyboard(genres_list, current_page,
                                            count_page)
    await call.message.answer(
                              text='Выберите жанр. \n'
                                   'Если передумали - вернитесь в меню',
                              reply_markup=genre_keyboard)
