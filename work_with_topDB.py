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

    def get_homework_top(self, week_day):
        """вывод домашнего задания из БД
        week_day - день недели. например monday или friday (пишем на английском)"""
        question_list = [] # список для преобразования названий предметов
        lst_homework = [] # список для вывода готовой информации о домашнем задании

        self.cursor.execute(f"PRAGMA table_info({week_day})") # извлекаем из БД строку с названием колонок
        lst_subject = [i[1] for i in self.cursor.fetchall()] # преобразование строки предметов в список для вывода (и избавление от лишнего)

        self.cursor.execute(f"SELECT * FROM friday") # обращаемся к БД
        result = self.cursor.fetchone() # берём строку с домашнимм задание
        question_list.append(result)
        for question in question_list: # в этих вложенных циклах мы преобразуем данные с БД о домашнем задании в список (также убераем лишнее)
            for i in question:
                lst_homework.append(i)
        text = f"""{lst_subject[0]}: {lst_homework[0]}

{lst_subject[1]}: {lst_homework[1]}

{lst_subject[2]}: {lst_homework[2]}"""
        return text # вывод домашнего задания с готовыми данными


    def close_db(self):
        """Разрыв соединения с БД"""
        self.connection.close()







