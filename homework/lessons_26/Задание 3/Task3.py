import sqlite3
import random

conn = sqlite3.connect('name3.db')  # создаем файл базы данных
cursor = conn.cursor()  # вызываем метод cursor для объекта класса сonnect
cursor.execute('''CREATE TABLE IF NOT EXISTS
tab_1
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 INTEGER,
col_2 INTEGER
)
''')  # создаем таблицу №1 с колонками id и col_1, col_2 в базе данных
for i in range(1, 11):  # проходимся циклом для заполнения базы данных
    var1 = random.randint(0, 9)  # создаем случайное значение для переменной
    var2 = random.randint(0, 9)  # создаем случайное значение для переменной
    cursor.execute(f'''
    INSERT INTO
    tab_1(col_1, col_2)
    VALUES({var1}, {var2})
    ''')  # записываем переменные в базу данных на каждой итерации
id_ = str(random.randint(1, 10))  # выбираем случайный id
cursor.execute(f'''SELECT col_1, col_2  FROM tab_1 WHERE id={id_}''')  # получаем информацию из базы данных по
# переданному id
s = cursor.fetchall()  # формируем список сполученной информацией
if int(s[0][0]) != 0 and int(s[0][0]) % 2 == 0 and int(s[0][1]) != 0 and int(s[0][1]) % 2 == 0:  # если каждое число
    # данной записи четное то выполняем следующий блок кода
    cursor.execute(f'''DELETE FROM tab_1 WHERE id={id_}''')  # удалить из таблицы №1 выбраную запись согласно id
elif int(s[0][0]) != 0 and int(s[0][0]) % 2 != 0 and int(s[0][1]) != 0 and int(s[0][1]) % 2 != 0:  # если каждое число
    # данной записи неетное то выполняем следующий блок кода
    cursor.execute(f'''UPDATE tab_1 SET col_1=2, col_2=2 WHERE id={id_}''')  # заменить значение в столбцах col_1 и
    # col_2 таблицы №1 базы данных согласно id
else:
    print('Одно из чисел равно 0')  # выводит информацию что числа равны 0
cursor.execute('''SELECT * FROM tab_1''')  # получаем всю информацию из таблицы №1 базы двнных
v = cursor.fetchall()  # формируем список с полученной информацией
print(v)  # выводим информацию
