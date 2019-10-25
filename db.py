import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('TestDB.db')
        self.conn.row_factory = sqlite3.Row

        self.c = self.conn.cursor()


    def create_table(self):
        self.c.execute('''CREATE TABLE if not exists messages
                     (text text)''')

    def add_message(self, message):
        self.c.execute("INSERT INTO messages VALUES (?)", [message])

    def get_all_messages(self):
        self.c.execute("SELECT * FROM messages")
        return self.c.fetchall()


if __name__ == '__main__':
    data_base = Database()
    data_base.create_table()
