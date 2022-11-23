import sqlite3

class BotDB_top:

    def __init__(self, db_file):
        """установка соединения с БД"""
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_homework_top(self, week_days, subject, homework):
        """добавляем домашнее задание в БД
        аргументы: week_days -> (например monday или friday)
        subject -> (например Математика или Иностранный_язык. Вместо пробелов в названии предметов ставится _ (нижнеее подчёркивание)
        homework -> сам текст с домашним заданием"""
        self.cursor.execute(f"""UPDATE {week_days} SET {subject} = {homework}""")
        return self.connection.commit()

#  отдельные методы на вывод верхней недели =======================================================================================================

    def monday_top(self):
        """получаем домашнее задание из БД"""
        self.cursor.execute(f"SELECT * FROM monday")
        result = self.cursor.fetchone()
        a = str(result)
        lst = a.replace('(', '').replace(')', '').replace("'", '').split(', ')
        text = f"""Математика: {lst[0]}
Информатика: {lst[1]}
Иностранный язык: {lst[2]}
Доп. занятия ИС-1"""
        return text

    def tuesday_top(self):
        """получаем домашнее задание из БД"""
        self.cursor.execute(f"SELECT * FROM tuesday")
        result = self.cursor.fetchone()
        a = str(result)
        lst = a.replace('(', '').replace(')', '').replace("'", '').split(', ')
        text = f"""Человек в современном мире: {lst[0]}
Литература: {lst[1]}
История: {lst[2]}"""
        return text

    def wednesday_top(self):
        """получаем домашнее задание из БД"""
        self.cursor.execute(f"SELECT * FROM wednesday")
        result = self.cursor.fetchone()
        a = str(result)
        lst = a.replace('(', '').replace(')', '').replace("'", '').split(', ')
        text = f"""Основы безопасности жизнедеятельности: {lst[0]}
Русский язык: {lst[1]}
Физическая культура: {lst[2]}
Доп. занятие ИС-1"""
        return text

    def thursday_top(self):
        """получаем домашнее задание из БД"""
        self.cursor.execute(f"SELECT * FROM thursday")
        result = self.cursor.fetchone()
        a = str(result)
        lst = a.replace('(', '').replace(')', '').replace("'", '').split(', ')
        text = f"""Иностранный язык: {lst[0]}
Экологические основы природопользования: {lst[1]}
Большие данные: {lst[2]}
Доп. занятие ИС-2"""
        return text

    def friday_top(self):
        """получаем домашнее задание из БД"""
        self.cursor.execute(f"SELECT * FROM friday")
        result = self.cursor.fetchone()
        a = str(result)
        lst = a.replace('(', '').replace(')', '').replace("'", '').split(', ')
        text = f"""Литература: {lst[0]}
Математика: {lst[1]}
Информатика: {lst[2]}"""
        return text

    def saturday_top(self):
        """получаем домашнее задание из БД"""
        self.cursor.execute(f"SELECT * FROM saturday")
        result = self.cursor.fetchone()
        a = str(result)
        lst = a.replace('(', '').replace(')', '').replace("'", '').split(', ')
        text = f"""Физика: {lst[0]}
Математика: {lst[1]}
Основы финансовой грамотности: {lst[2]}
Доп. занятие ИС-2"""
        return text

#===========================================================================================================

    def close_db(self):
        """Разрыв соединения с БД"""
        self.connection.close()







