import sqlite3

conn = sqlite3.connect('name6.db')  # создаем файл базы данных
cursor = conn.cursor()  # вызываем метод cursor для объекта класса сonnect
cursor.execute('''CREATE TABLE IF NOT EXISTS
tab_1
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 TEXT
)
''')  # создаем таблицу №1 с колонками id и col_1 в базе данных
conn.commit()  # сохраняем изменения
cursor.execute('''CREATE TABLE IF NOT EXISTS
tab_2
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 INTEGER
)
''')  # создаем таблицу №2 с колонками id и col_1 в базе данных
conn.commit()  # сохраняем изменения
new_list = [1, 'red', 2, 'blue', 3, 'green', 4, 'black', 5]  # список с данными
for var in new_list:  # проходим циклом по списку
    if type(var) == str:  # если елемент списка типа str выполняем следующий блок кода
        cursor.execute('''INSERT INTO tab_1
        (col_1)
        VALUES(?)''', (var,))  # добавляем запись объекта в таблицу №1 базы данных
        cursor.execute('''INSERT INTO tab_2
            (col_1)
            VALUES(?)''', (len(var),))  # добавляем запись длинны строки в таблицу №2 базы данных
        conn.commit()  # сохраняем изменения
    elif type(var) == int:  # если елемент списка типа int выполняем следующий блок кода
        if var % 2 == 0:  # если число четное выполнить следующий длок кода
            cursor.execute('''INSERT INTO tab_2
            (col_1)
            VALUES(?)''', (var,))  # добавляем запись числа в таблицу №2 базы данных
            conn.commit()  # сохраняем изменения
        elif var % 2 != 0:  # если число нечетное выполнить следующий длок кода
            cursor.execute('''INSERT INTO tab_1    
            (col_1)
            VALUES('Нечетное')''')  # добавляем запись 'нечетное' в таблицу №1 базы данных
            conn.commit()  # сохраняем изменения
cursor.execute('''SELECT id FROM tab_2''')  # получаем все id из таблицы №2
id_ = cursor.fetchall()  # формируем список с id из таблицы №2
if len(id_) >= 5:  # если количество объектов в список id_ больше либо равно выполняем следующий блок кода
    cursor.execute('''DELETE FROM tab_1 WHERE id=1 ''')  # удалить из таблице №1 первую запись
    conn.commit()  # сохраняем изменения
elif len(id_) < 5:  # если количество объектов в кортеже id_ меньше выполняем следующий блок кода
    cursor.execute('''UPDATE tab_1 SET col_1='hello' WHERE id=1''')  # изменить в таблице №1 первую запись на 'hello'
    conn.commit()  # сохраняем изменения
