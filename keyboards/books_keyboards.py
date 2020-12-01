"""this is book's keyboards creator."""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.menu_keyboards import add_menu_button
from keyboards.paginations.pagination_authors_keyboards import add_pagination_for_books_by_author
from keyboards.paginations.pagination_genres_keyboards import add_pagination_for_books_by_genre
from keyboards.paginations.pagination_readers_keyboards import add_pagination_for_books_by_reader


def create_books_keyboard_by_author(
                                    books: list,
                                    current_page: int,
                                    count_page: int,
                                    catch_item_id: int):
    """Keyboard in response to a specific author's button."""
    book_keyboard = InlineKeyboardMarkup(row_width=2)
    for book in books:
        book_button = InlineKeyboardButton(
                                           text=str(book.name),
                                           callback_data='book_id_'
                                                         + str(book.id))
        book_keyboard.insert(book_button)
    add_pagination_for_books_by_author(book_keyboard, current_page,
                                       count_page, catch_item_id)
    return book_keyboard


def create_books_keyboard_by_genre(
                                   books: list,
                                   current_page: int,
                                   count_page: int,
                                   catch_item_id: int):
    """Keyboard in response to a specific genre's button."""
    book_keyboard = InlineKeyboardMarkup(row_width=2)
    for book in books:
        book_button = InlineKeyboardButton(
                                           text=str(book.name),
                                           callback_data='book_id_'
                                                         + str(book.id))
        book_keyboard.insert(book_button)
    add_pagination_for_books_by_genre(book_keyboard, current_page,
                                      count_page, catch_item_id)
    return book_keyboard


def create_books_keyboard_by_reader(
                                    books: list,
                                    current_page: int,
                                    count_page: int,
                                    catch_item_id: int):
    """Keyboard in response to a specific reader's button."""
    book_keyboard = InlineKeyboardMarkup(row_width=2)
    for book in books:
        book_button = InlineKeyboardButton(
                                           text=str(book.name),
                                           callback_data='book_id_'
                                                         + str(book.id))
        book_keyboard.insert(book_button)
    add_pagination_for_books_by_reader(book_keyboard, current_page,
                                       count_page, catch_item_id)
    return book_keyboard


def create_book_keyboard_by_list(books: list):
    """Keyboard with selected audiobook."""
    selected_book_keyboard = InlineKeyboardMarkup(row_width=1)
    for book in books:
        selected_book_button = InlineKeyboardButton(
                                                    text=str(book.name),
                                                    url=book.book_url)
        selected_book_keyboard.insert(selected_book_button)
    add_menu_button(selected_book_keyboard)
    return selected_book_keyboard
