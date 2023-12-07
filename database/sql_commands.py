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
