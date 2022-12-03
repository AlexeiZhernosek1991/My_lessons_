import sqlite3
import random

conn = sqlite3.connect('name3.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS
tab_1
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 INTEGER,
col_2 INTEGER
)
''')
for i in range(1, 11):
    var1 = random.randint(0, 9)
    var2 = random.randint(0, 9)
    cursor.execute(f'''
    INSERT INTO
    tab_1(col_1, col_2)
    VALUES({var1}, {var2})
    ''')
id_ = str(random.randint(1, 10))
cursor.execute(f'''SELECT col_1, col_2  FROM tab_1 WHERE id={id_}''')
s = cursor.fetchall()
if int(s[0][0]) != 0 and int(s[0][0]) % 2 == 0 and int(s[0][1]) != 0 and int(s[0][1]) % 2 == 0:
    cursor.execute(f'''DELETE FROM tab_1 WHERE id={id_}''')
elif int(s[0][0]) != 0 and int(s[0][0]) % 2 != 0 and int(s[0][1]) != 0 and int(s[0][1]) % 2 != 0:
    cursor.execute(f'''UPDATE tab_1 SET col_1=2, col_2=2 WHERE id={id_}''')
else:
    print('Одно из чисел равно 0')
cursor.execute('''SELECT * FROM tab_1''')
v = cursor.fetchall()
print(v)
