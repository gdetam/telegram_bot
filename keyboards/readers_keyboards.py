"""this is reader's keyboards creator."""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.paginations.pagination_keyboards import add_pagination


def create_readers_keyboard(
                            readers: list,
                            current_page: int,
                            count_page: int):
    """Keyboard in response to the 'readers' button."""
    reader_keyboard = InlineKeyboardMarkup(row_width=2)
    for reader in readers:
        reader_button = InlineKeyboardButton(
                                             text=str(reader.name),
                                             callback_data='reader_id_book_page_'
                                                           + str(reader.id)
                                                           + '/0')
        reader_keyboard.insert(reader_button)
    add_pagination(reader_keyboard, current_page,
                   count_page, 'reader_page_')
    return reader_keyboard
