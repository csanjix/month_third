from handlers.admin import register_admin_handlers
from aiogram import executor
from config import dp
from handlers import profile
from handlers import (
    start,
    callback,
    chat_actions
)
from database import sql_commands

async def on_startup(_):
    db = sql_commands.Database()
    db.sql_create_tables()


start.register_start_handlers(dp=dp)

if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )