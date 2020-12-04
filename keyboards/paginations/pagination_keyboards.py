"""this is pagination keyboards creator."""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def add_pagination(
                   keyboard: InlineKeyboardMarkup,
                   current_page: int,
                   count_page: int,
                   page_name_for_callback_data: str):
    """Add pagination."""
    keyboard.row(*add_arrow(current_page, count_page,
                            page_name_for_callback_data))
    return InlineKeyboardMarkup(keyboard)


def add_arrow(
              current_page: int,
              count_page: int,
              page_name_for_callback_data: str):
    """Add switching buttons."""
    row = []
    if current_page != 0:
        row.append(InlineKeyboardButton(
                                        text='<',
                                        callback_data=page_name_for_callback_data
                                                      + str(current_page - 1)))

    row.append(InlineKeyboardButton(
                                    text='в меню',
                                    callback_data='menu'))

    if current_page != count_page:
        row.append(InlineKeyboardButton(
                                        text='>',
                                        callback_data=page_name_for_callback_data
                                                      + str(current_page + 1)))
    return row
