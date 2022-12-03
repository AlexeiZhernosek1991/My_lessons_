import sqlite3
import random

conn = sqlite3.connect('name5.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS
tab_1
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 TEXT,
col_2 TEXT
)
''')
conn.commit()
for i in range(1, 4):
    taple_color = ('red', 'yellow', 'blue', 'green', 'orange', 'pink')
    var1 = random.choice(taple_color)
    var2 = random.choice(taple_color)
    cursor.execute(f'''
    INSERT INTO 
    tab_1(col_1, col_2)
    VALUES(?, ?)
    ''', (var1, var2))
conn.commit()
cursor.execute('''DELETE FROM tab_1 WHERE id=2''')
conn.commit()
cursor.execute('''UPDATE tab_1 SET col_1='hellow',col_2='world' WHERE id=3''')
conn.commit()
cursor.execute('''SELECT * FROM tab_1''')
r = cursor.fetchall()
with open('file.txt', 'w') as file:
    file.write('id  col_1  col_2 \n')
    for taple_ in r:
        for str_ in taple_:
            file.write(str(str_) + '  ')
        file.write('\n')


