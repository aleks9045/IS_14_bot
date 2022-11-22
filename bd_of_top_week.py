import sqlite3

connection = sqlite3.connect('users.bd')
cur = connection.cursor()
cur.execute(
    """CREATE TABLE IF NOT EXISTS registration(
    login TEXT,
    password TEXT
    role TEXT);""")
connection.commit()
cur.execute(
    """CREATE TABLE IF NOT EXISTS login(
    login TEXT,
    password TEXT
    role TEXT);""")
connection.commit()