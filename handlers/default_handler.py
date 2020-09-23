from aiogram import types
from bot import dp


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def echo(message: types.Message):
    await message.answer(message.text)

