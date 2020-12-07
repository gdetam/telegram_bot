"""this is author's pagination keyboards creator."""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def add_pagination_for_books_by_author(
                                       keyboard: InlineKeyboardMarkup,
                                       current_page: int,
                                       count_page: int,
                                       catch_item_id: int):
    """Add pagination for books."""
    keyboard.row(*add_arrow_for_books_by_author(current_page, count_page,
                                                catch_item_id))
    return InlineKeyboardMarkup(keyboard)


def add_arrow_for_books_by_author(
                                  current_page: int,
                                  count_page: int,
                                  catch_item_id: int):
    """Add buttons to switch to books."""
    row = []
    if current_page != 0:
        row.append(InlineKeyboardButton(
                                        text='<',
                                        callback_data='author_id_book_page_'
                                                      + str(catch_item_id)
                                                      + '/'
                                                      + str(current_page - 1)))

    row.append(InlineKeyboardButton(
                                    text='в меню',
                                    callback_data='menu'))

    if current_page != count_page:
        row.append(InlineKeyboardButton(
                                        text='>',
                                        callback_data='author_id_book_page_'
                                                      + str(catch_item_id)
                                                      + '/'
                                                      + str(current_page + 1)))
    return row
