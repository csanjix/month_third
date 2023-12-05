import sqlite3

def create_table():
    connection = sqlite3.connect('scraped_data.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scraped_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT
        )
    ''')

    connection.commit()
    connection.close()

def write_to_table(data):
    connection = sqlite3.connect('scraped_data.db')
    cursor = connection.cursor()

    data_to_write = data[:5]

    for item in data_to_write:
        cursor.execute('INSERT INTO scraped_data (data) VALUES (?)', (item,))

    connection.commit()
    connection.close()
