from aiogram import executor
from bot import bot, dp
import handlers


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

    async def on_shutdown(dp):
        await bot.close()
        executor.start_polling(dp, on_shutdown=on_shutdown)
