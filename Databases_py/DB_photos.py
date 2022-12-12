import sqlite3

lst_of_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

class PhotosDB_top:

    def __init__(self, db_file):
        """установка соединения с БД"""
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_photo(self, week_day, subject, file_id):
        self.cursor.execute(f"""UPDATE {week_day} SET {subject} = {file_id}""")
        return self.connection.commit()

    def check_photos(self, week_day):
        lst_of_photo = []
        self.cursor.execute(f"SELECT * FROM {week_day}")
        result = self.cursor.fetchone()
        a = str(result)
        lst = a.replace('(', '').replace(')', '').replace("'", '').split(', ')
        if lst[0] != 'None':
            lst_of_photo.append(lst[0])
        if lst[1] != 'None':
            lst_of_photo.append(lst[1])
        if lst[2] != 'None':
            lst_of_photo.append(lst[2])
        return lst_of_photo

    def all_photos(self):
        photos_lst = []
        for i in lst_of_days:
            self.cursor.execute(f"SELECT * FROM {i}")
            result = self.cursor.fetchone()
            a = str(result)
            lst = a.replace('(', '').replace(')', '').replace("'", '').split(', ')
            for j in lst:
                photos_lst.append(j)
        return photos_lst


class PhotosDB_lower:

    def __init__(self, db_file):
        """установка соединения с БД"""
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_photo(self, week_day, subject, file_id):
        self.cursor.execute(f"""UPDATE {week_day} SET {subject} = {file_id}""")
        return self.connection.commit()

    def check_photos(self, week_day):
        lst_of_photo = []
        self.cursor.execute(f"SELECT * FROM {week_day}")
        result = self.cursor.fetchone()
        a = str(result)
        lst = a.replace('(', '').replace(')', '').replace("'", '').split(', ')
        if lst[0] != 'None':
            lst_of_photo.append(lst[0])
        if lst[1] != 'None':
            lst_of_photo.append(lst[1])
        if lst[2] != 'None':
            lst_of_photo.append(lst[2])
        return lst_of_photo

    def all_photos(self):
        photos_lst = []
        for i in lst_of_days:
            self.cursor.execute(f"SELECT * FROM {i}")
            result = self.cursor.fetchone()
            a = str(result)
            lst = a.replace('(', '').replace(')', '').replace("'", '').split(', ')
            for j in lst:
                photos_lst.append(j)
        return photos_lst
