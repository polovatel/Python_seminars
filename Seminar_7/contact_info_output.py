import sqlite3

con = sqlite3.connect('phonebook.db')
cur = con.cursor()
SEPARATOR = '-' * 20

def show_my_contacts_horiz():
    cur.execute('''SELECT * FROM 'phones'
                ''')
    rows = cur.fetchall()
    counter = 1
    for row in rows:
        print(f'{counter}) Surname: {row[0]}, Name: {row[1]}, Tel: {row[2]}, Description: {row[3]}')
        counter += 1

def show_my_contacts_vertic():
    cur.execute('''SELECT * FROM 'phones'
                ''')
    rows = cur.fetchall()

    for row in rows:
        print(SEPARATOR)
        print(f'Surname: {row[0]}')
        print(f'Name: {row[1]}')
        print(f'Tel: {row[2]}')
        print(f'Description: {row[3]}')
        print(SEPARATOR)