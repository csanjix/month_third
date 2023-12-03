import sqlite3
from database import sql_queries
class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()


    def sql_create_tables(self):
        if self.connection:
            print("Database connected successfully")
        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_BAN_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_USER_FORM_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_LIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_REFERRAL_TABLE_QUERY)

        try:
            self.connection.execute(sql_queries.ALTER_USER_TABLE)
            self.connection.execute(sql_queries.ALTER_USER_V2_TABLE)
        except sqlite3.OperationalError:
            pass

        self.connection.commit()

    def sql_insert_users(self, telegram_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, username, first_name, last_name, None, None,)
        )
        self.connection.commit()

    def sql_insert_ban_user(self, telegram_id):
        self.cursor.execute(
            sql_queries.INSERT_BAN_USER_QUERY,
            (None, telegram_id, 1)
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

    def sql_update_ban_user_count(self, telegram_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_USER_COUNT_QUERY,
            (telegram_id,)
        )
        self.connection.commit()

    def sql_insert_user_form_register(self, telegram_id, nickname, bio, geo,
                                      gender, age, photo):
        self.cursor.execute(
            sql_queries.INSERT_USER_FORM_QUERY,
            (None, telegram_id, nickname, bio, geo, gender, age, photo,)
        )
        self.connection.commit()

    def sql_select_user_form(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "geo": row[4],
            "gender": row[5],
            "age": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_FORM_QUERY,
            (telegram_id,)
        ).fetchone()

    def sql_select_all_user_form(self):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "geo": row[4],
            "gender": row[5],
            "age": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_USER_FORM_QUERY
        ).fetchall()

    def sql_insert_like(self, owner, liker):
        self.cursor.execute(
            sql_queries.INSERT_LIKE_QUERY,
            (None, owner, liker,)
        )
        self.connection.commit()

    def sql_select_filter_user_form(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "geo": row[4],
            "gender": row[5],
            "age": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.FILTER_LEFT_JOIN_USER_FORM_LIKE_QUERY,
            (tg_id, tg_id,)
        ).fetchall()

    def sql_select_balance_count_referral(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "balance": row[0],
            "count": row[1],
        }
        return self.cursor.execute(
            sql_queries.DOUBLE_SELECT_REFERRAL_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_update_reference_link(self, link, owner):
        self.cursor.execute(
            sql_queries.UPDATE_REFERENCE_LINK_QUERY,
            (link, owner,)
        )
        self.connection.commit()

    def sql_select_user(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "link": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_LINK_QUERY,
            (telegram_id,)
        ).fetchone()

    def sql_select_user_by_link(self, link):
        self.cursor.row_factory = lambda cursor, row: {
            "tg_id": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_BY_LINK_QUERY,
            (link,)
        ).fetchone()

    def sql_update_balance(self, tg_id):
        print(tg_id)
        self.cursor.execute(
            sql_queries.UPDATE_USER_BALANCE_QUERY,
            (tg_id,)
        )
        self.connection.commit()

    def sql_insert_referral(self, owner, referral):
        self.cursor.execute(
            sql_queries.INSERT_REFERRAL_QUERY,
            (None, owner, referral,)
        )
        class Bot:
            def __init__(self):
                self.users = []

            def register_user(self, user_id, link):
                self.users.append({'user_id': user_id, 'link': link})

            def get_users_by_link(self, link):
                users_from_link = [user['user_id'] for user in self.users if user.get('link') == link]
                return users_from_link

        my_bot = Bot()

        my_bot.register_user(user_id='user1', link='your_link')
        my_bot.register_user(user_id='user2', link='another_link')
        my_bot.register_user(user_id='user3', link='your_link')

        your_link_users = my_bot.get_users_by_link(link='your_link')
        print(f'Пользователи, вошедшие по вашей ссылке: {your_link_users}')

        class Bot:
            def __init__(self):
                self.referral_dict = {}

            def register_userr(self, user_id, link):
                self.referral_dict.setdefault(user_id, []).append(link)

            def get_referrals_for_user(self, user_id):
                return self.referral_dict.get(user_id, [])

        my_bot = Bot()

        my_bot.register_user(user_id='user1', link='your_link')
        my_bot.register_user(user_id='user2', link='your_link')
        my_bot.register_user(user_id='user3', link='another_link')
        my_bot.register_user(user_id='user4', link='user2')

        user1_referrals = my_bot.get_referrals_for_user(user_id='user1')
        user2_referrals = my_bot.get_referrals_for_user(user_id='user2')
        user3_referrals = my_bot.get_referrals_for_user(user_id='user3')

        print(f'Рефералы пользователя user1: {user1_referrals}')
        print(f'Рефералы пользователя user2: {user2_referrals}')
        print(f'Рефералы пользователя user3: {user3_referrals}')
        self.connection.commit()