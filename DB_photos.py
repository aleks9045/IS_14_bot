import sqlite3


class PhotosDB_top:

    def __init__(self, db_file):
        """установка соединения с БД"""
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_photo(self, week_day, subject, file_id):
        self.cursor.execute(f"""UPDATE {week_day} SET {subject} = {file_id}""")
        return self.connection.commit()

    def check_photos(self, week_day):
        photo1 = ''
        photo2 = ''
        photo3 = ''
        self.cursor.execute(f"SELECT * FROM {week_day}")
        result = self.cursor.fetchone()
        a = str(result)
        lst = a.replace('(', '').replace(')', '').replace("'", '').split(', ')
        print(lst)
        if lst[0] != 'None':
            photo1 = lst[0]
        if lst[1] != 'None':
            photo2 = lst[1]
        if lst[2] != 'None':
            photo3 = lst[2]
        return [photo1, photo2, photo3]