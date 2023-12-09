from aiogram import executor
from config import dp
from handlers import (
    start,
    callback,
    chat_actions,
    registration,
    profile,
    reference
)
from database import sql_commands
import aiogram
import logging

async def on_startup(_):
    db = sql_commands.Database()
    db.sql_create_tables()

start.register_start_handlers(dp=dp)
callback.register_callback_handlers(dp=dp)
registration.register_registration_handlers(dp=dp)
profile.register_profile_handlers(dp=dp)
reference.register_reference_handlers(dp=dp)
chat_actions.register_chat_actions_handlers(dp=dp)

if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    except aiogram.utils.exceptions.NetworkError as ne:
        print(f"Aiohttp client gives error: {ne}")
