import sqlite3

class Database:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_ban_table()
    def create_ban_table(self):
        self.connection.execute('''
            CREATE TABLE IF NOT EXISTS ban (
                ID INTEGER PRIMARY KEY,
                TELEGRAM_ID INTEGER,
                COUNT INTEGER
            )
        ''')
        self.connection.commit()

    def insert_or_update_ban_user(self, telegram_id):
        self.cursor.execute('''
            INSERT INTO ban (TELEGRAM_ID, COUNT)
            VALUES (?, 1)
            ON CONFLICT(TELEGRAM_ID) DO UPDATE SET COUNT = COUNT + 1
        ''', (telegram_id,))
        self.connection.commit()

    def get_ban_user_count(self, telegram_id):
        result = self.cursor.execute('''
            SELECT COUNT FROM ban
            WHERE TELEGRAM_ID = ?
        ''', (telegram_id,)).fetchone()
        return result[0] if result else 0