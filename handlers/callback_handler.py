"""this is commands and keyboards handler."""

import logging

from aiogram.types import CallbackQuery


def callback(call: CallbackQuery):
    """Callback's handler."""
    call.answer(cache_time=6)
    callback_data = call.data
    logging.info(f'{callback_data=}')
    return callback_data
