import sqlite3
import contact_details as info

sqlite_file = "C:\\Users\\Lenovo\\Desktop\\GeekBrains\\Python_Learning\\Phyton_Seminars\\Seminars\\Seminar_7\\phonebook.db"
con = sqlite3.connect(sqlite_file)
cur = con.cursor()

def create_phonebook():
    '''Создает базу данных с телефонными номерами'''
    cur.execute("""CREATE TABLE phones(
                    surname TEXT,
                    name TEXT,
                    phone INTEGER,
                    description TEXT)
                    """)
    con.commit()
    cur.close()

def insert_new_phone():
    '''Записывает новый контакт в телефонную книгу'''
    surname: str = info.surname_of_contact()
    name: str = info.name_of_contact()
    phone: int = info.phone_number()
    description: str = info.description()
    cur.execute(f'''INSERT INTO 'phones' 
                VALUES ('{surname}', '{name}',
                '{phone}', '{description}')
                ''')
    print('Contact information sucesfully saved')
    con.commit()
    cur.close()
