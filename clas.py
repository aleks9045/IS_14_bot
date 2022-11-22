import sqlite3


class BotDB:

    def __init__(self, db_file):
        """установка соединения с БД"""
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_homework(self, week_days, subject, homework):
        """добавляем домашнее задание в БД
        аргументы: week_days -> (например monday или friday)
        subject -> (например Математика или Иностранный_язык. Вместо пробелов в названии предметов ставится _ (нижнеее подчёркивание)
        homework -> сам текст с домашним заданием"""
        self.cursor.execute(f"INSERT INTO {week_days}({subject}) VALUES('{homework}')")
        return self.connection.commit()

    def monday(self):
        """получаем домашнее задание из БД"""
        self.cursor.execute(f"SELECT * FROM monday")
        result = self.cursor.fetchone()
        a = str(result)
        lst = a.replace('(', '').replace(')', '').replace("'", '').split(', ')
        text = f"""Математика -> {lst[0]}
Информатика -> {lst[1]}
Иностранный язык -> {lst[2]}
Доп. занятия ИС-1"""
        return text

    def close_db(self):
        """Разрыв соединения с БД"""
        self.connection.close()




