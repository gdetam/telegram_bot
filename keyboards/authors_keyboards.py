"""this is author's keyboards creator."""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.paginations.pagination_keyboards import add_pagination


def create_authors_keyboard(
                            authors: list,
                            current_page: int,
                            count_page: int):
    """Keyboard in response to the 'authors' button."""
    author_keyboard = InlineKeyboardMarkup(row_width=2)
    for author in authors:
        author_button = InlineKeyboardButton(
                                             text=str(author.name),
                                             callback_data='author_id_book_page_'
                                                           + str(author.id)
                                                           + '/0')
        author_keyboard.insert(author_button)
    add_pagination(author_keyboard, current_page,
                   count_page, 'author_page_')
    return author_keyboard
