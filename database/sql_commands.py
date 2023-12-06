import sqlite3
from database import sql_queries
from profanity_check import predict_prob
from database.sql_commands import BAN_USER_THRESHOLD
from aiogram import types
class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

        def sql_create_ban_table(self):
            if self.connection:
                print("Database connected successfully")

            self.connection.execute(sql_queries.CREATE_BAN_TABLE_QUERY)
            self.connection.commit()

        def sql_insert_or_update_ban_user(self, telegram_id):
            self.cursor.execute(
                sql_queries.INSERT_OR_UPDATE_BAN_USER_QUERY,
                (telegram_id,)
            )
            self.connection.commit()

        def sql_select_ban_user(self, telegram_id):
            self.cursor.row_factory = lambda cursor, row: {
                "id": row[0],
                "telegram_id": row[1],
                "count": row[2],
            }
            return self.cursor.execute(
                sql_queries.SELECT_BAN_USER_QUERY,
                (telegram_id,)
            ).fetchone()

        def sql_ban_user_threshold(self):
            return sql_queries.BAN_USER_THRESHOLD




    async def chat_messages(message: types.Message):
        db = Database()
        print(message)
        if message.chat.id == -1002128824339:
            ban_word_predict_prob = predict_prob([message.text])
            if ban_word_predict_prob > 0.1:
                await message.delete()
                user = db.sql_select_ban_user(
                    telegram_id=message.from_user.id
                )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"User: {message.from_user.id} {message.from_user.first_name}\n"
                         f"Dont curse in this chat\n"
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
        self.connection.commit()
