"""this is genre's keyboards creator."""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.paginations.pagination_keyboards import add_pagination


def create_genres_keyboard(
                           genres: list,
                           current_page: int,
                           count_page: int):
    """Keyboard in response to the 'genres' button."""
    genre_keyboard = InlineKeyboardMarkup(row_width=2)
    for genre in genres:
        genre_button = InlineKeyboardButton(
                                            text=str(genre.name),
                                            callback_data='genre_id_book_page_'
                                                          + str(genre.id)
                                                          + '/0')
        genre_keyboard.insert(genre_button)
    add_pagination(genre_keyboard, current_page,
                   count_page, 'genre_page_')
    return genre_keyboard
