from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database

async def start_button(message: types.Message):
    print(message)
    db = Database()
    db.sql_insert_users(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
    )

    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'Hello {message.from_user.first_name}'
    )

def register_start_handlers(db: Dispatcher):
    db.register_message_handler(start_button, commands=['start'])