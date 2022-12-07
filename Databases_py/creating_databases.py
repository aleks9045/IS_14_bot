import sqlite3
connection = sqlite3.connect('../Databases/')
cur = connection.cursor()



cur.execute("""CREATE TABLE IF NOT EXISTS  (

 );""")



connection.commit()
