import sqlite3
import random

conn = sqlite3.connect('name5.db')  # создаем фвйл базы данных
cursor = conn.cursor()  # вызываем метод cursor для объекта класса сonnect
cursor.execute('''CREATE TABLE IF NOT EXISTS
tab_1
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 TEXT,
col_2 TEXT
)
''')  # создаем таблицу №1 с колонками id и col_1, col_2 в базе данных
conn.commit()  # сохраняем изменения
for i in range(1, 4):  # проходим циклом для заполнения баззы данных
    taple_color = ('red', 'yellow', 'blue', 'green', 'orange', 'pink')  # список с данными
    var1 = random.choice(taple_color)  # выбираем случайное значение из списка для переменной var1
    var2 = random.choice(taple_color)  # выбираем случайное значение из списка для переменной var2
    cursor.execute(f'''
    INSERT INTO 
    tab_1(col_1, col_2)
    VALUES(?, ?)
    ''', (var1, var2))  # добавляем запись в столбцы col_1, col_2 значения var1, var2
conn.commit()  # сохраняем изменения
cursor.execute('''DELETE FROM tab_1 WHERE id=2''')  # даляем вторую запись из таблицы №1 базы данных
conn.commit()  # сохраняем изменения
cursor.execute('''UPDATE tab_1 SET col_1='hellow',col_2='world' WHERE id=3''')  # изменяем в третьей записи в столбцах
# col_1, col_2 хранящиеся значения на 'hello' b 'world'
conn.commit()  # сохраняем изменения
cursor.execute('''SELECT * FROM tab_1''')  # получаем информацию из таблицы №1 базы данных
r = cursor.fetchall()  # формируем кортеж из полученной информации
with open('file.txt', 'w') as file:  # открываем текстовый файл на запись
    file.write('id  col_1  col_2 \n')  # записываем заголовки столбцов
    for taple_ in r:  # проходимся циклом по списку и извлекаем кортежи с информацией
        for str_ in taple_:  # проходимся циклом по картежу и полчаем объекты
            file.write(str(str_) + '  ')  # записываем объекты в файл
        file.write('\n')  # записываем перенос строки


