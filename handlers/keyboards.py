"""this is keyboards creator."""

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
    select_book_keyboard = InlineKeyboardMarkup(row_width=2)
    authors = InlineKeyboardButton(
        text='авторы',
        callback_data='author_page_0')
    genres = InlineKeyboardButton(
        text='жанры',
        callback_data='genre_page_0')
    select_book_keyboard.add(authors, genres)
    add_menu_button(select_book_keyboard)
    return select_book_keyboard


def create_authors_keyboard(
        authors: list,
        current_page: int,
        count_page: int):
    """Keyboard in response to the 'authors' button."""
    author_keyboard = InlineKeyboardMarkup(row_width=2)
    for author in authors:
        author_button = InlineKeyboardButton(
            text=str(author.first_name + ' ' + author.last_name),
            callback_data='author_id_book_page_' + str(author.id) + '/0')
        author_keyboard.insert(author_button)
    add_pagination(author_keyboard, current_page,
                   count_page, 'author_page_')
    return author_keyboard


def create_genres_keyboard(
        genres: list,
        current_page: int,
        count_page: int):
    """Keyboard in response to the 'genres' button."""
    genre_keyboard = InlineKeyboardMarkup(row_width=2)
    for genre in genres:
        genre_button = InlineKeyboardButton(
            text=str(genre.name),
            callback_data='genre_id_book_page_' + str(genre.id) + '/0')
        genre_keyboard.insert(genre_button)
    add_pagination(genre_keyboard, current_page,
                   count_page, 'genre_page_')
    return genre_keyboard


def create_books_keyboard(
        books: list,
        current_page: int,
        count_page: int,
        catch_item_id: int):
    """Keyboard in response to a specific author's button."""
    book_keyboard = InlineKeyboardMarkup(row_width=2)
    for book in books:
        book_button = InlineKeyboardButton(
            text=str(book.name),
            callback_data='book_id_' + str(book.id))
        book_keyboard.insert(book_button)
    add_pagination_for_books(book_keyboard, current_page,
                             count_page, catch_item_id)
    return book_keyboard


def create_book_keyboard_by_list(books: list):
    """Keyboard with selected audiobook."""
    selected_book_keyboard = InlineKeyboardMarkup(row_width=1)
    for book in books:
        selected_book_button = InlineKeyboardButton(
            text=str(book.name),
            url='https://' + str(book.url) + '/')
        selected_book_keyboard.insert(selected_book_button)
        add_menu_button(selected_book_keyboard)
    return selected_book_keyboard


def add_menu_button(keyboard: InlineKeyboardMarkup):
    """Keyboard 'menu'."""
    button = InlineKeyboardButton(
        text='в меню',
        callback_data='menu')
    keyboard.add(button)


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
            callback_data=page_name_for_callback_data + str(current_page - 1)))

    row.append(InlineKeyboardButton(
        text='в меню',
        callback_data='menu'))

    if current_page != count_page:
        row.append(InlineKeyboardButton(
            text='>',
            callback_data=page_name_for_callback_data + str(current_page + 1)))
    return row


def add_pagination_for_books(
        keyboard: InlineKeyboardMarkup,
        current_page: int,
        count_page: int,
        author_id: int):
    """Add pagination for books."""
    keyboard.row(*add_arrow_for_books(current_page, count_page,
                                      author_id))
    return InlineKeyboardMarkup(keyboard)


def add_arrow_for_books(
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
