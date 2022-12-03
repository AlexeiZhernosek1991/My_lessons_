import sqlite3
import random

conn = sqlite3.connect('name2.db')  # создаем фвйл базы данных
cursor = conn.cursor()  # вызываем метод cursor для объекта класса сonnect
cursor.execute('''CREATE TABLE IF NOT EXISTS
 tab_1(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 col_1 INTEGER,
 col_2 INTEGER
 )
 ''')  # создаем таблицу №1 с колонками id и col_1, col_2 в базе данных
sum_var = 0  # сумма всех значений в базе данных
for i in range(4):  # проходимся циклом для заполнения базы данных
    var1 = random.randint(0, 9)  # предаем в переменную случайную цифру
    var2 = random.randint(0, 9)  # предаем в переменную случайную цифру
    cursor.execute(f'''
            INSERT INTO tab_1(col_1, col_2)
            VALUES({var1}, {var2})''')  # записываем значение на кождой итерации цикла
    sum_var += var1  # прибовляем значение 1
    sum_var += var2  # прибовляем значение 2
conn.commit()  # сохраняем изменения
if sum_var / 10 > 4:  # если среднее число переданных значений больше количества записей выполняем следующий блок кода
    cursor.execute('''DELETE FROM tab_1 WHERE id = 4''')  # удаляем из таблицы №1 четвертую запись
    conn.commit()  # сохраняем изменения
    print(sum_var / 10)  # выводим среднее число значений
else:
    print('Среднеарифметическое меньше количества записей БД')
