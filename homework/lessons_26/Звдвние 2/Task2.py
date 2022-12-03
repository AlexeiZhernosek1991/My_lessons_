import sqlite3
import random

conn = sqlite3.connect('name2.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS
 tab_1(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 col_1 INTEGER,
 col_2 INTEGER
 )
 ''')
sum_var = 0
for i in range(4):
    var1 = random.randint(0, 9)
    var2 = random.randint(0, 9)
    cursor.execute(f'''
            INSERT INTO tab_1(col_1, col_2)
               VALUES({var1}, {var2})''')
    sum_var += var1
    sum_var += var2
if sum_var / 10 > 4:
    cursor.execute('''DELETE FROM tab_1 WHERE id = 4''')
    s = cursor.fetchall()
    print(sum_var / 10)
else:
    print('Среднеарифметическое меньше количества записей БД')
