import sqlite3

conn = sqlite3.connect('name2.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS
 tab_1(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 col_1 TEXT,
 col_2 TEXT,
 col_3 INTEGER
 )
 ''')

var1 = "Alex"
var2 = "Zhernosek"
var3 = int(input('Введите число'))
cursor.execute('''
        INSERT INTO tab_1(col_1, col_2, col_3)
           VALUES(?, ?, ?)''', (var1, var2, var3))

for i in range(1, 4):
    cursor.execute(f'''SELECT col_{i} FROM tab_1''')
    print(cursor.fetchall())
