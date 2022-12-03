import sqlite3

conn = sqlite3.connect('name.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS
 tab_1(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 col_1 TEXT,
 col_2 TEXT
 )
 ''')
cursor.execute('''
    INSERT INTO tab_1(col_1, col_2)
    VALUES('hellow', 'world')
''')
conn.commit()

cursor.execute('''
CREATE TABLE IF NOT EXISTS
 tab_2(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 col_1 TEXT,
 col_2 TEXT
 )
 ''')

var1 = 'red'
var2 = 'black'

command = '''
 INSERT INTO tab_2(col_1, col_2)
    VALUES(?, ?)
 '''
cursor.execute('''
 INSERT INTO tab_2(col_1, col_2)
    VALUES(?, ?)
 ''', (var1, var2))

data_list = [('yellow', 'white') for x in range(10)]

for tuple_ in data_list:
    cursor.execute(command, tuple_)

conn.commit()

# for send_ in range(10):
#     var3 = str(input("Введите имя"))
#     var4 = str(input("Введите фамилию"))
#     cursor.execute('''
#      INSERT INTO tab_2(col_1, col_2)
#         VALUES(?, ?)''', (var3, var4))

# conn.commit()

cursor.execute('''SELECT*FROM tab_2''')
# print(cursor.fetchall())
