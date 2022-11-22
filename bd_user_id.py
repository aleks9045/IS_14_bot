import sqlite3


def check_user_id(user_id):
    connection = sqlite3.connect('users.bd')
    cur = connection.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS user(
        user_id1 INT, user_id2 INT, user_id3 INT, user_id4 INT);""")
    connection.commit()
    cur.execute("""INSERT INTO user VALUES(1205630682, 785663533, 1030737087, 1275232971)""")
    connection.commit()
    cur.execute("SELECT * FROM user;")
    one_result = cur.fetchone()
    if user_id in one_result:
        return True
    else:
        return False

