from aiogram import executor
from config import db
from handlers import (
    start,
)
from database import sql_commands

async def on_startup(_):
    db = sql_commands.Database()
    db.sql_create_tables()

start.register_start_handlers(db=db)

if  __name__=="__main__":
    executor.start_polling(
        db,
        skip_updates=True,
        on_startup=on_startup
    )