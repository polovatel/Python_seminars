import sqlite3
import contact_details as info
import program_checks as check

con = sqlite3.connect('phonebook.db')
cur = con.cursor()

def create_phonebook():
    '''Создает базу данных с телефонными номерами'''
    cur.execute("""CREATE TABLE phones(
                    surname TEXT,
                    name TEXT,
                    phone INTEGER,
                    description TEXT)
                    """)
    print('PhoneBook succesfully created!')

def insert_new_phone():
    '''Записывает новый контакт в телефонную книгу'''
    check.is_table_exist()
    surname: str = info.surname_of_contact()
    name: str = info.name_of_contact()
    phone: int = info.phone_number()
    description: str = info.description()
    cur.execute(f'''INSERT INTO 'phones' 
                VALUES ('{surname}', '{name}',
                '{phone}', '{description}')
                ''')
    print('Contact information sucesfully saved!')

    con.commit()
    cur.close()
