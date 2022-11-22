import sqlite3


def check_user_id(user_id):
    connection = sqlite3.connect('Databases/users.bd')
    cur = connection.cursor()
    cur.execute("SELECT * FROM user;")
    one_result = cur.fetchone()
    if user_id in one_result:
        return True
    else:
        return False

