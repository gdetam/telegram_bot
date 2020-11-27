"""this is menu's keyboards creator."""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_start_menu():
    """Start keyboard."""
    menu_keyboard = InlineKeyboardMarkup(row_width=1)
    select_book = InlineKeyboardButton(
                                       text='Выбрать аудиокнигу',
                                       callback_data='select_book')
    random_book = InlineKeyboardButton(
                                       text='Случайная аудиокнига',
                                       callback_data='random_book')
    menu_keyboard.add(select_book, random_book)
    return menu_keyboard


def create_authors_and_genres_menu():
    """Keyboard in response to the 'Select Audiobook' button."""
    select_book_keyboard = InlineKeyboardMarkup(row_width=3)
    authors = InlineKeyboardButton(
                                   text='авторы',
                                   callback_data='author_page_0')
    genres = InlineKeyboardButton(
                                  text='жанры',
                                  callback_data='genre_page_0')
    readers = InlineKeyboardButton(
                                   text='исполнители',
                                   callback_data='reader_page_0')
    select_book_keyboard.add(authors, genres, readers)
    add_menu_button(select_book_keyboard)
    return select_book_keyboard


def add_menu_button(keyboard: InlineKeyboardMarkup):
    """Keyboard 'menu'."""
    button = InlineKeyboardButton(
                                  text='в меню',
                                  callback_data='menu')
    keyboard.add(button)
