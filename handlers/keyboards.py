from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from db.db import rows_author_class, counter_pagination_authors


click_callback = CallbackData('click', 'item_name')


def create_start_menu_keyboard():
    # начальная клавиатура
    menu_keyboard = InlineKeyboardMarkup(row_width=1)
    select_audiobook = InlineKeyboardButton(
        text='Выбрать аудиокнигу', callback_data=click_callback.new(item_name='select_audiobook'))
    random_audiobook = InlineKeyboardButton(
        text='Случайная аудиокнига', callback_data=click_callback.new(item_name='random_audiobook'))
    menu_keyboard.add(select_audiobook, random_audiobook)
    return menu_keyboard


def create_select_audiobook_keyboard():
    # клавиатура в ответ на кнопку 'Выбрать аудиокнигу'
    select_audiobook_keyboard = InlineKeyboardMarkup(row_width=2)
    authors = InlineKeyboardButton(text='авторы', callback_data='author_page_0')
    genres = InlineKeyboardButton(text='жанры', callback_data='genre_page_0')
    select_audiobook_keyboard.add(authors, genres)
    add_cancel_button(select_audiobook_keyboard)
    return select_audiobook_keyboard


def create_authors_keyboard(authors: list, count_page: int):
    # клавиатура в ответ на кнопку 'авторы'
    author_keyboard = InlineKeyboardMarkup(row_width=2)
    for author in authors:
        author_button = InlineKeyboardButton(
            text=str(author.first_name + ' ' + author.last_name),
            callback_data='author_id_' + str(author.author_id))
        author_keyboard.insert(author_button)
    add_pagination(author_keyboard, count_page, 'author_page_')
    # add_cancel_button(author_keyboard)
    return author_keyboard


def create_genres_keyboard(genres: list, count_page: int):
    # клавиатура в ответ на кнопку 'жанры'
    genre_keyboard = InlineKeyboardMarkup(row_width=2)
    for genre in genres:
        genre_button = InlineKeyboardButton(
            text=str(genre.name),
            callback_data='genre_id_' + str(genre.genre_id))
        genre_keyboard.insert(genre_button)
    add_pagination(genre_keyboard, count_page, 'genre_page_')
    # add_cancel_button(genre_keyboard)
    return genre_keyboard


def add_cancel_button(keyboard: InlineKeyboardMarkup):
    button = InlineKeyboardButton(text='Отмена', callback_data='cancel')
    keyboard.add(button)


def add_pagination(keyboard: InlineKeyboardMarkup, count_page: int, page_name_for_callback_data: str):
    # пагинация
    # pagination = InlineKeyboardMarkup(row_width=3)
    row = []
    for i in range(count_page):
        # pagination_page = InlineKeyboardButton(text=str(i + 1),
        # callback_data=page_name_for_callback_data + str(i))
        row.append(InlineKeyboardButton(text='<', callback_data=page_name_for_callback_data + str(i)))
        row.append(InlineKeyboardButton(text='в меню', callback_data='cancel'))
        row.append(InlineKeyboardButton(text='>', callback_data=page_name_for_callback_data + str(i + 1)))
        break
        # keyboard.insert(pagination_page)
    keyboard.row(*row)
    return InlineKeyboardMarkup(keyboard)

    # todo pagination_page = InlineKeyboardButton(text=str((int(offset) - 1) * int(limit)),
    #  callback_data='pagination_page')
    #  choice_lvl_3.insert(pagination)
    # пагинация в одну строчку

'''
row=[]
row.append(InlineKeyboardButton("<",callback_data=create_callback_data("PREV-MONTH",year,month,day)))
row.append(InlineKeyboardButton(" ",callback_data=data_ignore))
row.append(InlineKeyboardButton(">",callback_data=create_callback_data("NEXT-MONTH",year,month,day)))
keyboard.append(row)

return InlineKeyboardMarkup(keyboard)
'''
