import phonebook_create as create          
import sqlite3

def database_check():
    '''Проверка наличия базы данных''' 
    phone_book_check = input('After making changes, an error '
                             'occured: "You need to create a '
                             'PhoneBook", create it? '
                             'Y/N?: ')
    
    while (phone_book_check != 'Y'
           and phone_book_check != 'N'):
           phone_book_check =  input('Please, check the '
                                     'entred information '
                                      'and try again: ')
    if phone_book_check == 'Y':
        print('Creating PhoneBook... Run again after app colsed')        
        return is_table_exist()
    if phone_book_check == 'N':
        return quit()


def is_table_exist():
    '''Проверяет наличие таблицы в БД'''
    con = sqlite3.connect('phonebook.db')
    cur = con.cursor()
    cur.execute('''SELECT count(name) FROM sqlite_master
                WHERE type = 'table' 
                AND name = 'phones'
                ''')
    
    if cur.fetchone()[0] == 1:
        create.insert_new_phone()
    else:
        create.create_phonebook()

