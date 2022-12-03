import sqlite3

conn = sqlite3.connect('name6.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS
tab_1
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 TEXT
)
''')
conn.commit()
cursor.execute('''CREATE TABLE IF NOT EXISTS
tab_2
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 INTEGER
)
''')
conn.commit()
new_list = [1, 'red', 2, 'blue', 3, 'green']
for var in new_list:
    if type(var) == str:
        cursor.execute('''INSERT INTO tab_1
        (col_1)
        VALUES(?)''', (var,))
        cursor.execute('''INSERT INTO tab_2
            (col_1)
            VALUES(?)''', (len(var),))
        conn.commit()
    elif type(var) == int:
        if var % 2 == 0:
            cursor.execute('''INSERT INTO tab_2
            (col_1)
            VALUES(?)''', (var,))
            conn.commit()
        elif var % 2 != 0:
            cursor.execute('''INSERT INTO tab_1    
            (col_1)
            VALUES('Нечетное')''')
            conn.commit()
cursor.execute('''SELECT id FROM tab_2''')
id_ = cursor.fetchall()
if len(id_) > 5:
    cursor.execute('''DELETE FROM tab_1 WHERE id=1 ''')
    conn.commit()
elif len(id_) < 5:
    cursor.execute('''UPDATE tab_1 SET col_1='hello' WHERE id=1''')
    conn.commit()
