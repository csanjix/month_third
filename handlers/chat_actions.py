import datetime
import sqlite3
from aiogram import types, Dispatcher
from config import bot, DESTINATION
from database.sql_commands import Database
from keyboard.inline_buttons import start_keyboard
from const import START_MENU
from profanity_check import predict, predict_prob

async def chat_messages(message: types.Message):
    db = Database()
    print(message)
    if message.chat.id == -1002053768:
        ban_word_predict_prob = predict_prob([message.text])
        if ban_word_predict_prob > 0.1:
            await message.delete()
            user = db.sql_select_ban_user(
                telegram_id=message.from_user.id
            )
            await bot.send_message(
                chat_id=message.chat.id,
                text=f"User: {message.from_user.id} {message.from_user.first_name}\n"
                     f"Don't curse in this chat\n"
                     f"In the third time you will be banned"
            )
            print(user)
            count = None
            try:
                count = user['count']
            except TypeError:
                pass
            if not user:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"Banned: {message.from_user.first_name}")
                db.sql_insert_or_update_ban_user(
                    telegram_id=message.from_user.id
                )
            elif count >= db.sql_ban_user_threshold():
                await bot.ban_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.from_user.id,
                )
            elif user:
                db.sql_insert_or_update_ban_user(
                    telegram_id=message.from_user.id
                )
    else:
        await message.reply(
            text="There is no such command"
        )
    db.connection.commit()
