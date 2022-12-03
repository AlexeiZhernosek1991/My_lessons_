import sqlite3
import random

conn = sqlite3.connect('name4.db')  # создаем фвйл базы данных
cursor = conn.cursor()  # вызываем метод cursor для объекта класса сonnect
cursor.execute('''CREATE TABLE IF NOT EXISTS
tab_1
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 INTEGER
)
''')  # создаем таблицу №1 с колонками id и col_1 в базе данных
for i in range(1, 4):  # проходим циклом для заполнения базы данных
    var1 = random.randint(0, 9)  # генерируем случайное значение для переменной
    cursor.execute(f'''
    INSERT INTO
    tab_1(col_1)
    VALUES({var1})
    ''')  # добавляем запись объекта в таблицу №1 базы данных
conn.commit()  # сохраняем изменения
cursor.execute('''SELECT * FROM tab_1''')  # получаем всю информацию из таблицы №1 базы данных
s = cursor.fetchall()  # формируем список со значениями


class Bd:  # объявляем класс
    def rem(self, a=None, b=None, c=None):  # создаем метод для объектов класса принимающий три значения
        if a is not None and b is None and c is None:  # если передаем одно значение выполняем следующий блок кода
            cursor.execute('''
                INSERT INTO
                tab_1(col_1)
                VALUES(3)
                ''')  # добавляем запись со значением 3
            conn.commit()  # сохраняем изменения
        elif a is not None and type(b) == int and c is None:  # если передаем два значения и второе является числом
            # выполняем следующий блок кода
            cursor.execute('''DELETE FROM tab_1 WHERE id=1''')  # удаляем из таблице №1 первую запись
            conn.commit()  # сохраняем изменения
        elif a is not None and b is not None and type(c) == int:  # если передаем три значения и третье
            # является числом выполняем следующий длок кода
            cursor.execute('''UPDATE tab_1 SET col_1=77 WHERE id=3''')  # меняем значение в третьей записи в таблице №1
            # базы данных
            conn.commit()  # сохраняем изменения


new_bd = Bd()  # создаем объект класса
new_bd.rem(a='2', b=5, c=10)  # вызываем метод экземпляра класса и передаем три значения
cursor.execute('''SELECT * FROM tab_1''')  # получаем информацию из таблицы №1
v = cursor.fetchall()  # формируем список с информацией из таблицы №1
print(v)  # вывод информации
