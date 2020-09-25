from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


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
