import sqlite3
from database import sql_queries
from profanity_check import predict_prob
from database.sql_queries import BAN_USER_THRESHOLD
from aiogram import types
from database import sql_queries

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

    def sql_select_all_users(self):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4],
        }
        return self.cursor.execute(sql_queries.SELECT_ALL_USERS_QUERY).fetchall()

    def sql_select_potential_bans(self):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "count": row[2],
        }
        return self.cursor.execute(sql_queries.SELECT_POTENTIAL_BANS_QUERY).fetchall()

    def sql_insert_wallet(self, telegram_id):
        self.cursor.execute(
            sql_queries.INSERT_WALLET_QUERY,
            (None, telegram_id, 0)
        )
        self.connection.commit()

    def sql_select_wallet_balance(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "balance": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_WALLET_BALANCE_QUERY,
            (telegram_id,)
        ).fetchone()

    def sql_update_wallet_balance(self, telegram_id, amount):
        self.cursor.execute(
            sql_queries.UPDATE_WALLET_BALANCE_QUERY,
            (amount, telegram_id)
        )

    def sql_create_transactions_table(self):
        if self.connection:
            print("Transactions table connected successfully")
        self.connection.execute(sql_queries.CREATE_TRANSACTIONS_TABLE_QUERY)
        self.connection.commit()

    def sql_insert_transaction(self, sender_id, recipient_id, amount):
        self.cursor.execute(
            sql_queries.INSERT_TRANSACTION_QUERY,
            (None, sender_id, recipient_id, amount)
        )
        self.connection.commit()
