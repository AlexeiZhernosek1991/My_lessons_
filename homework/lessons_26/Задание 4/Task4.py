import sqlite3
import random

conn = sqlite3.connect('name4.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS
tab_1
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 INTEGER
)
''')
for i in range(1, 4):
    var1 = random.randint(0, 9)
    cursor.execute(f'''
    INSERT INTO
    tab_1(col_1)
    VALUES({var1})
    ''')
conn.commit()
cursor.execute('''SELECT * FROM tab_1''')
s = cursor.fetchall()


class Bd:
    def rem(self, a=None, b=None, c=None):
        if a is not None and b is None and c is None:
            cursor.execute('''
                INSERT INTO
                tab_1(col_1)
                VALUES(3)
                ''')
            conn.commit()
        elif a is not None and type(b) == int and c is None:
            cursor.execute('''DELETE FROM tab_1 WHERE id=1''')
            conn.commit()
        elif a is not None and b is not None and type(c) == int:
            cursor.execute('''UPDATE tab_1 SET col_1=77 WHERE id=3''')
            conn.commit()


new_bd = Bd()
new_bd.rem(a='2', b=5, c=10)
cursor.execute('''SELECT * FROM tab_1''')
v = cursor.fetchall()
print(v)
