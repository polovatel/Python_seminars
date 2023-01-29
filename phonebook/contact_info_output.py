import sqlite3

sqlite_file = ("C:\\Users\\Lenovo\\Desktop\\GeekBrains\\Python_Learning\\Phyton_Seminars\\Seminars\\phonebook\\phonebook.db")
con = sqlite3.connect(sqlite_file)
cur = con.cursor()
SEPARATOR = '-' * 20

def show_my_contacts_horiz():
    cur.execute('''SELECT * FROM 'phones'
                ''')
    rows = cur.fetchall()
    counter = 1
    for row in rows:
        print(f'{counter}) {row[0]}, {row[1]}, {row[2]}, {row[3]}')
        counter += 1

def show_my_contacts_vertic():
    cur.execute('''SELECT * FROM 'phones'
                ''')
    rows = cur.fetchall()

    for row in rows:
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        print(SEPARATOR)
